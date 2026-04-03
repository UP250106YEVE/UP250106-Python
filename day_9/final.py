# =============================================================================
#  SIMULACION 3D DE AGUJERO NEGRO  —  Detalle maximo
#  Pygame + PyOpenGL + NumPy
#
#  CARACTERISTICAS:
#    - Horizonte de sucesos con efecto de singularidad
#    - Fotosfera (esfera de fotones) pulsante
#    - Disco de acrecion con temperatura fisica (cuerpo negro)
#      colores van de rojo oscuro (exterior) a blanco-azulado (interior)
#    - Grid de Schwarzschild mostrando curvatura del espacio-tiempo
#    - Jets relativistas bipolares con particulas animadas
#    - Flujo de acrecion en espiral (gas cayendo)
#    - Estrellas orbitando que eventualmente son destruidas (tidal disruption)
#    - Particulas de polvo y gas magnetizado
#    - Halo de Einstein / lente gravitacional
#    - Efecto Doppler en el disco (lado acercandose mas brillante)
#    - Fondo estelar con galaxia distante
#    - Camara orbital con inercia y suavizado
#    - Panel HUD con datos fisicos en tiempo real
#    - Multiples modos de camara (orbital, cenital, ecuador)
#    - Controles completos
#
#  INSTALACION:
#    pip install pygame PyOpenGL PyOpenGL_accelerate numpy
#
#  CONTROLES:
#    Arrastrar raton      -> rotar camara
#    Rueda del raton      -> zoom
#    R                    -> resetear camara
#    V                    -> cambiar modo de camara
#    P / Espacio          -> pausar / reanudar
#    +  /  -              -> aumentar / disminuir velocidad
#    G                    -> mostrar/ocultar grid espaciotemporal
#    J                    -> mostrar/ocultar jets
#    D                    -> mostrar/ocultar disco de acrecion
#    S                    -> mostrar/ocultar estrellas
#    ESC / Q              -> salir
# =============================================================================

import sys, math, random, time
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluSphere, gluNewQuadric, gluQuadricNormals, GLU_OUTSIDE

try:
    from OpenGL.GLUT import glutInit
except Exception:
    def glutInit(): pass

# ─────────────────────────────────────────────────────────────────────────────
#  CONFIGURACION
# ─────────────────────────────────────────────────────────────────────────────

W, H           = 1280, 720
FPS            = 60
TITLE          = "Agujero Negro — Simulacion 3D"

RS             = 2.2          # radio de Schwarzschild (unidades de escena)
R_ISCO         = RS * 3.0     # ultima orbita circular estable
R_DISK_IN      = RS * 1.5
R_DISK_OUT     = RS * 11.0
R_PHOTON       = RS * 1.5     # esfera de fotones

N_DISK         = 2200         # particulas del disco
N_STREAM       = 500          # flujo espiral de gas
N_JET          = 350          # particulas por jet (x2)
N_STARS_ORB    = 90           # estrellas orbitando
N_BG           = 3500         # estrellas de fondo
N_GRID_R       = 28           # lineas radiales del grid
N_GRID_RINGS   = 20           # anillos del grid

# ─────────────────────────────────────────────────────────────────────────────
#  UTILES
# ─────────────────────────────────────────────────────────────────────────────

def clamp(v, lo, hi):   return max(lo, min(hi, v))
def deg2rad(d):         return d * math.pi / 180.0
def lerp(a, b, t):      return a + (b - a) * t

def blackbody_color(T):
    """Color fisico de cuerpo negro. T en Kelvin (1000..50000)."""
    T = clamp(T, 1000, 50000)
    if T <= 6600:
        r = 1.0
        g = clamp(0.39 + 0.685 * math.log(T / 100.0) - 0.40, 0.0, 1.0) if T > 1000 else 0.0
        b = 0.0 if T <= 1900 else clamp((T - 1900) / 4700.0, 0.0, 1.0)
    else:
        r = clamp(1.292 * ((T - 6000) / 6600.0) ** -0.133, 0.0, 1.0)
        g = clamp(0.900 * ((T - 6000) / 6600.0) ** -0.076, 0.0, 1.0)
        b = 1.0
    return (r, g, b)

def disk_temperature(r):
    """Perfil de temperatura del disco de acrecion (modelo simplificado)."""
    r_in = R_DISK_IN
    if r <= r_in:
        return 50000.0
    # T cae como r^(-3/4) hacia afuera
    return 50000.0 * (r_in / r) ** 0.75

def gravitational_redshift(r):
    """Factor de corrimiento al rojo gravitacional (Schwarzschild)."""
    if r <= RS:
        return 0.0
    return math.sqrt(1.0 - RS / r)

def doppler_factor(r, phi, inclination_rad):
    """
    Factor Doppler: el lado del disco acercandose al observador
    aparece mas brillante (efecto relativista beaming).
    """
    v = math.sqrt(0.5 * RS / max(r, RS * 1.01))   # velocidad kepleriana ~v/c
    cos_phi = math.cos(phi) * math.sin(inclination_rad)
    # Beaming doppler relativista simplificado
    return (1.0 + v * cos_phi) ** 3

# ─────────────────────────────────────────────────────────────────────────────
#  DISCO DE ACRECION
# ─────────────────────────────────────────────────────────────────────────────

class AccretionDisk:
    def __init__(self):
        self.particles = []
        self._spawn_all()

    def _spawn_all(self):
        self.particles = []
        for _ in range(N_DISK):
            r     = random.uniform(R_DISK_IN, R_DISK_OUT)
            phi   = random.uniform(0, 2 * math.pi)
            # Altura: disco delgado con flare hacia afuera
            h_max = RS * 0.04 * (r / R_DISK_IN) ** 1.1
            y     = random.gauss(0, h_max * 0.4)
            # Velocidad kepleriana
            omega = math.sqrt(RS / (2.0 * r ** 3))
            # Tamano y brillo
            size  = random.uniform(0.015, 0.055)
            T     = disk_temperature(r)
            color = blackbody_color(T)
            self.particles.append({
                'r': r, 'phi': phi, 'y': y,
                'omega': omega, 'size': size,
                'color': color, 'T': T,
                'alpha': random.uniform(0.55, 1.0),
            })

    def update(self, dt):
        for p in self.particles:
            p['phi'] = (p['phi'] + p['omega'] * dt * 60.0) % (2 * math.pi)
            # Deriva radial lenta hacia el interior (acrecion)
            p['r'] -= dt * 0.004 * (RS / p['r']) ** 0.5
            if p['r'] < R_DISK_IN * 0.92:
                # Resurge en el borde exterior
                p['r']   = random.uniform(R_DISK_OUT * 0.8, R_DISK_OUT)
                p['phi'] = random.uniform(0, 2 * math.pi)
                p['T']   = disk_temperature(p['r'])
                p['color'] = blackbody_color(p['T'])

    def draw(self, inclination=0.0):
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glEnable(GL_POINT_SMOOTH)

        INCL = inclination  # inclinacion del disco respecto al observador

        for p in self.particles:
            r, phi, y = p['r'], p['phi'], p['y']
            x = r * math.cos(phi)
            z = r * math.sin(phi)

            # Factor Doppler y redshift
            dop  = doppler_factor(r, phi, INCL)
            red  = gravitational_redshift(r)
            bright = dop * red * p['alpha']
            bright = clamp(bright, 0.0, 2.5)

            cr, cg, cb = p['color']
            a = clamp(bright * 0.75, 0.0, 1.0)

            glPointSize(p['size'] * 22.0 * clamp(bright, 0.3, 2.0))
            glBegin(GL_POINTS)
            glColor4f(min(cr * bright, 1.0),
                      min(cg * bright * 0.9, 1.0),
                      min(cb * bright * 0.8, 1.0), a)
            glVertex3f(x, y, z)
            glEnd()

        glDisable(GL_BLEND)
        glDisable(GL_POINT_SMOOTH)
        glEnable(GL_LIGHTING)


# ─────────────────────────────────────────────────────────────────────────────
#  FLUJO ESPIRAL DE GAS (material cayendo al agujero)
# ─────────────────────────────────────────────────────────────────────────────

class AccretionStream:
    """Gas en espiral logaritmica cayendo desde el exterior."""

    def __init__(self):
        self.streams = []
        for i in range(N_STREAM):
            t      = i / N_STREAM
            r      = lerp(R_DISK_OUT * 1.3, R_DISK_IN * 1.1, t)
            phi    = t * 6.0 * math.pi + random.uniform(-0.15, 0.15)
            speed  = random.uniform(0.008, 0.018)
            y_off  = random.gauss(0, RS * 0.08)
            T      = lerp(3000, 45000, t)
            color  = blackbody_color(T)
            self.streams.append({
                'r': r, 'phi': phi, 'y': y_off,
                'speed': speed, 'color': color,
                't_life': t,
            })

    def update(self, dt):
        for p in self.streams:
            p['t_life'] = (p['t_life'] + dt * p['speed']) % 1.0
            t      = p['t_life']
            p['r'] = lerp(R_DISK_OUT * 1.3, R_DISK_IN * 1.05, t)
            p['phi'] = (p['phi'] + dt * 0.35 * (R_DISK_IN / max(p['r'], 0.1))) % (2 * math.pi)
            p['T']   = lerp(3000, 45000, t)
            p['color'] = blackbody_color(p['T'])

    def draw(self):
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glEnable(GL_POINT_SMOOTH)

        for p in self.streams:
            t   = p['t_life']
            r   = p['r']
            x   = r * math.cos(p['phi'])
            z   = r * math.sin(p['phi'])
            y   = p['y'] * (1.0 - t * 0.5)
            cr, cg, cb = p['color']
            alpha = clamp(0.25 + t * 0.55, 0.0, 0.85)
            sz    = lerp(1.2, 3.5, t)
            glPointSize(sz)
            glBegin(GL_POINTS)
            glColor4f(cr, cg * 0.85, cb * 0.7, alpha)
            glVertex3f(x, y, z)
            glEnd()

        glDisable(GL_BLEND)
        glDisable(GL_POINT_SMOOTH)
        glEnable(GL_LIGHTING)


# ─────────────────────────────────────────────────────────────────────────────
#  JETS RELATIVISTAS
# ─────────────────────────────────────────────────────────────────────────────

class RelJet:
    """Par de jets bipolares perpendiculares al disco."""

    def __init__(self):
        self.particles = []
        self._init_particles()
        self.pulse = 0.0

    def _init_particles(self):
        self.particles = []
        for sign in (+1, -1):   # jet norte y sur
            for _ in range(N_JET):
                speed  = random.uniform(0.40, 1.20)
                spread = random.uniform(0.0, 0.18)
                phase  = random.uniform(0, 2 * math.pi)
                y0     = random.uniform(0, RS * 22.0)
                # Ancho del jet crece con la altura
                width  = spread * (1.0 + y0 / (RS * 4.0))
                T_jet  = random.uniform(8000, 25000)
                color  = blackbody_color(T_jet)
                # Color ademas teñido de azul/blanco (plasma relativista)
                cr, cg, cb = color
                cb = min(cb + 0.4, 1.0)
                cg = min(cg + 0.15, 1.0)
                self.particles.append({
                    'sign': sign,
                    'y': y0,
                    'speed': speed,
                    'spread': spread,
                    'phase': phase,
                    'color': (cr, cg, cb),
                    'alpha': random.uniform(0.3, 0.85),
                    'size': random.uniform(0.8, 2.2),
                })

    def update(self, dt):
        self.pulse = (self.pulse + dt * 3.5) % (2 * math.pi)
        for p in self.particles:
            p['y'] += p['speed'] * dt * 18.0 * p['sign']
            p['phase'] = (p['phase'] + dt * 2.0) % (2 * math.pi)
            # Si sale del rango, reiniciar cerca del centro
            if abs(p['y']) > RS * 25.0:
                p['y'] = random.uniform(0, RS * 1.5) * p['sign']

    def draw(self):
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glEnable(GL_POINT_SMOOTH)

        pulse_w = 1.0 + 0.12 * math.sin(self.pulse)

        for p in self.particles:
            y      = p['y']
            dist   = abs(y)
            # El jet se ensancha con la distancia
            width  = p['spread'] * (1.0 + dist / (RS * 3.0)) * pulse_w
            angle  = p['phase']
            x      = width * RS * math.cos(angle)
            z      = width * RS * math.sin(angle)
            cr, cg, cb = p['color']
            # Se desvanece con la distancia
            fade   = clamp(1.0 - dist / (RS * 25.0), 0.0, 1.0) ** 0.6
            a      = p['alpha'] * fade
            glPointSize(p['size'] * pulse_w)
            glBegin(GL_POINTS)
            glColor4f(cr, cg, cb, a)
            glVertex3f(x, y, z)
            glEnd()

        # Linea central del jet (eje)
        glLineWidth(0.8)
        glBegin(GL_LINES)
        glColor4f(0.6, 0.8, 1.0, 0.18)
        glVertex3f(0, -RS * 24.0, 0)
        glColor4f(0.6, 0.8, 1.0, 0.18)
        glVertex3f(0,  RS * 24.0, 0)
        glEnd()

        glDisable(GL_BLEND)
        glDisable(GL_POINT_SMOOTH)
        glEnable(GL_LIGHTING)


# ─────────────────────────────────────────────────────────────────────────────
#  GRID DEL ESPACIO-TIEMPO (curvatura de Schwarzschild)
# ─────────────────────────────────────────────────────────────────────────────

class SpacetimeGrid:
    """
    Grid en el plano y=0 con curvatura radial:
    las lineas se hunden hacia el centro simulando la curvatura.
    """

    def __init__(self):
        self._build()

    def _warp(self, x, z):
        """Desplazamiento vertical por curvatura gravitacional."""
        r = math.sqrt(x*x + z*z)
        if r < RS * 0.5:
            return -RS * 3.5
        # Hundimiento basado en metrica de Schwarzschild
        factor = -RS * 1.8 / (r + RS * 0.3)
        return factor

    def _build(self):
        extent = R_DISK_OUT * 1.6
        step   = extent / 18.0
        self.h_lines = []   # lineas horizontales (en z fijo)
        self.v_lines = []   # lineas verticales   (en x fijo)

        coords = [i * step - extent for i in range(int(2 * extent / step) + 1)]

        for z_val in coords:
            line = []
            for x_val in coords:
                y_val = self._warp(x_val, z_val)
                line.append((x_val, y_val, z_val))
            self.h_lines.append(line)

        for x_val in coords:
            line = []
            for z_val in coords:
                y_val = self._warp(x_val, z_val)
                line.append((x_val, y_val, z_val))
            self.v_lines.append(line)

    def draw(self):
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glLineWidth(0.6)

        for lines in (self.h_lines, self.v_lines):
            for line in lines:
                glBegin(GL_LINE_STRIP)
                for (x, y, z) in line:
                    r    = math.sqrt(x*x + z*z)
                    # Color: verde/cian cerca, se desvanece lejos
                    t    = clamp(1.0 - r / (R_DISK_OUT * 1.5), 0.0, 1.0)
                    near = r < RS * 2.5
                    if near:
                        glColor4f(0.10, 0.80, 0.65, t * 0.45)
                    else:
                        glColor4f(0.08, 0.45, 0.55, t * 0.22)
                    glVertex3f(x, y, z)
                glEnd()

        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING)


# ─────────────────────────────────────────────────────────────────────────────
#  ESTRELLAS ORBITANDO (con disruption tidal)
# ─────────────────────────────────────────────────────────────────────────────

class OrbitalStar:
    def __init__(self, idx):
        self.r         = random.uniform(R_DISK_OUT * 1.2, R_DISK_OUT * 3.5)
        self.phi       = random.uniform(0, 2 * math.pi)
        self.inc       = random.uniform(-0.4, 0.4)     # inclinacion orbital
        self.omega     = math.sqrt(RS / (2 * self.r**3)) * random.uniform(0.6, 1.4)
        self.ecc       = random.uniform(0.0, 0.55)
        self.color     = random.choice([
            (1.0, 0.9, 0.7),   # amarillo
            (0.7, 0.85, 1.0),  # azul
            (1.0, 0.7, 0.6),   # naranja
            (1.0, 1.0, 1.0),   # blanco
            (0.9, 0.6, 0.9),   # purpura
        ])
        self.size      = random.uniform(0.06, 0.18)
        self.trail     = []
        self.disrupted = False
        self.disruption_t = 0.0
        self.quadric   = gluNewQuadric()
        gluQuadricNormals(self.quadric, GLU_OUTSIDE)

    def update(self, dt):
        self.phi = (self.phi + self.omega * dt * 55.0) % (2 * math.pi)
        # Orbita eliptica simple
        r_eff = self.r * (1 - self.ecc * math.cos(self.phi))
        x = r_eff * math.cos(self.phi)
        y = r_eff * math.sin(self.inc) * math.sin(self.phi)
        z = r_eff * math.sin(self.phi) * math.cos(self.inc)
        self.pos = (x, y, z)
        self.trail.append((x, y, z))
        if len(self.trail) > 180:
            self.trail.pop(0)

        # Disruption tidal si se acerca demasiado
        if r_eff < RS * 4.5 and not self.disrupted:
            self.disrupted    = True
            self.disruption_t = 0.0

        if self.disrupted:
            self.disruption_t += dt
            # La estrella se "evapora" en el disco
            self.size = max(self.size - dt * 0.015, 0.0)

    def draw(self):
        if self.size <= 0.005:
            return

        # Estela
        n = len(self.trail)
        if n > 2:
            glDisable(GL_LIGHTING)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glLineWidth(0.9)
            glBegin(GL_LINE_STRIP)
            for i, pt in enumerate(self.trail):
                a = (i / n) * 0.50
                glColor4f(*self.color, a)
                glVertex3f(*pt)
            glEnd()
            glDisable(GL_BLEND)
            glEnable(GL_LIGHTING)

        # Esfera
        if hasattr(self, 'pos'):
            glPushMatrix()
            glTranslatef(*self.pos)
            cr, cg, cb = self.color
            # Halo de disruption
            if self.disrupted:
                glDisable(GL_LIGHTING)
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE)
                t = clamp(self.disruption_t, 0, 1)
                glColor4f(1.0, 0.5, 0.2, 0.3 * (1 - t))
                gluSphere(self.quadric, self.size * 2.5, 8, 8)
                glDisable(GL_BLEND)
                glEnable(GL_LIGHTING)

            glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION,
                         [cr * 0.8, cg * 0.8, cb * 0.8, 1.0])
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE,
                         [cr, cg, cb, 1.0])
            gluSphere(self.quadric, self.size, 12, 12)
            glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION,
                         [0.0, 0.0, 0.0, 1.0])
            glPopMatrix()


# ─────────────────────────────────────────────────────────────────────────────
#  HORIZONTE DE SUCESOS + FOTOSFERA
# ─────────────────────────────────────────────────────────────────────────────

class BlackHoleCore:
    def __init__(self):
        self.pulse     = 0.0
        self.rot       = 0.0
        self.quadric   = gluNewQuadric()
        gluQuadricNormals(self.quadric, GLU_OUTSIDE)
        self._gen_photosphere()

    def _gen_photosphere(self):
        """Chispas de luz atrapadas en la esfera de fotones."""
        self.photo_pts = []
        r = R_PHOTON
        for _ in range(800):
            theta = random.uniform(0, math.pi)
            phi   = random.uniform(0, 2 * math.pi)
            bri   = random.uniform(0.2, 1.0)
            sz    = random.uniform(0.5, 2.0)
            drift = random.uniform(-0.003, 0.003)
            self.photo_pts.append({
                'theta': theta, 'phi': phi,
                'bri': bri, 'sz': sz, 'drift': drift,
            })

    def update(self, dt):
        self.pulse = (self.pulse + dt * 2.2) % (2 * math.pi)
        self.rot   = (self.rot + dt * 28.0) % 360.0
        for p in self.photo_pts:
            p['phi'] = (p['phi'] + p['drift']) % (2 * math.pi)

    def draw(self):
        glPushMatrix()
        glRotatef(self.rot, 0, 1, 0.15)

        # ── Halos externos (lente gravitacional) ──────────────────────────────
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)

        pulse_f = 1.0 + 0.05 * math.sin(self.pulse)
        halo_layers = [
            (RS * 4.2 * pulse_f, 0.04, 3.5, (1.00, 0.92, 0.60)),
            (RS * 3.5 * pulse_f, 0.08, 2.5, (1.00, 0.85, 0.45)),
            (RS * 2.8 * pulse_f, 0.14, 2.0, (1.00, 0.75, 0.30)),
            (RS * 2.2 * pulse_f, 0.22, 1.8, (1.00, 0.65, 0.20)),
            (RS * 1.9 * pulse_f, 0.30, 1.5, (1.00, 0.55, 0.15)),
        ]
        for r_h, alpha, lw, col in halo_layers:
            glLineWidth(lw)
            glBegin(GL_LINE_LOOP)
            for i in range(160):
                a = 2 * math.pi * i / 160
                glColor4f(col[0], col[1], col[2], alpha)
                glVertex3f(r_h * math.cos(a), 0.0, r_h * math.sin(a))
            glEnd()

        # ── Fotosfera ──────────────────────────────────────────────────────────
        glEnable(GL_POINT_SMOOTH)
        r = R_PHOTON
        for p in self.photo_pts:
            theta, phi = p['theta'], p['phi']
            x = r * math.sin(theta) * math.cos(phi)
            y = r * math.cos(theta)
            z = r * math.sin(theta) * math.sin(phi)
            bri  = p['bri'] * (0.7 + 0.3 * math.sin(self.pulse + phi))
            bri  = clamp(bri, 0, 1)
            glPointSize(p['sz'])
            glBegin(GL_POINTS)
            glColor4f(1.0, 0.85 * bri, 0.4 * bri, bri * 0.70)
            glVertex3f(x, y, z)
            glEnd()
        glDisable(GL_POINT_SMOOTH)

        # ── Horizonte de sucesos (esfera negra perfecta) ──────────────────────
        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING)
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0.0, 0.0, 0.0, 1.0])
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION,            [0.0, 0.0, 0.0, 1.0])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR,            [0.0, 0.0, 0.0, 1.0])
        gluSphere(self.quadric, RS * 0.98, 64, 64)

        # ── Resplandor de acrecion interno ────────────────────────────────────
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glow_r = RS * 1.15 * (1 + 0.03 * math.sin(self.pulse * 2))
        glColor4f(1.0, 0.45, 0.10, 0.18)
        gluSphere(self.quadric, glow_r, 32, 32)
        glColor4f(1.0, 0.60, 0.20, 0.08)
        gluSphere(self.quadric, RS * 1.35, 32, 32)
        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING)

        glPopMatrix()


# ─────────────────────────────────────────────────────────────────────────────
#  FONDO ESTELAR CON GALAXIA DISTANTE
# ─────────────────────────────────────────────────────────────────────────────

class Background:
    def __init__(self):
        self.stars = []
        for _ in range(N_BG):
            theta = random.uniform(0, math.pi)
            phi   = random.uniform(0, 2 * math.pi)
            dist  = random.uniform(800, 1600)
            x = dist * math.sin(theta) * math.cos(phi)
            y = dist * math.cos(theta)
            z = dist * math.sin(theta) * math.sin(phi)
            bri  = random.uniform(0.4, 1.0)
            sz   = random.uniform(0.5, 2.5)
            # Tinte espectral
            kind = random.random()
            if kind < 0.25:
                col = (bri * 0.75, bri * 0.82, bri)        # azul
            elif kind < 0.50:
                col = (bri, bri * 0.90, bri * 0.70)        # amarillo
            elif kind < 0.70:
                col = (bri, bri * 0.70, bri * 0.55)        # naranja
            else:
                col = (bri, bri, bri)                       # blanco
            self.stars.append((x, y, z, col, sz))

        # Galaxia espiral en el fondo (nube de puntos)
        self.galaxy = []
        for _ in range(1200):
            arm   = random.randint(0, 1)
            t_g   = random.uniform(0, 1)
            angle = t_g * 4 * math.pi + arm * math.pi
            r_g   = lerp(20, 350, t_g)
            spread = random.gauss(0, r_g * 0.12)
            x_g   = (r_g + spread) * math.cos(angle)
            z_g   = (r_g + spread) * math.sin(angle)
            y_g   = random.gauss(0, r_g * 0.06)
            bri_g = random.uniform(0.1, 0.5) * (1 - t_g * 0.6)
            col_g = (bri_g * 0.8, bri_g * 0.7, bri_g)
            # Posicionar la galaxia lejos y arriba/lateral
            self.galaxy.append((x_g + 400, y_g + 300, z_g + 900, col_g))

    def draw(self):
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glEnable(GL_POINT_SMOOTH)

        # Galaxia
        glPointSize(1.2)
        glBegin(GL_POINTS)
        for (x, y, z, col) in self.galaxy:
            glColor4f(col[0], col[1], col[2], 0.55)
            glVertex3f(x, y, z)
        glEnd()

        # Estrellas
        for (x, y, z, col, sz) in self.stars:
            glPointSize(sz)
            glBegin(GL_POINTS)
            glColor4f(col[0], col[1], col[2], 0.88)
            glVertex3f(x, y, z)
            glEnd()

        glDisable(GL_BLEND)
        glDisable(GL_POINT_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)


# ─────────────────────────────────────────────────────────────────────────────
#  CAMARA ORBITAL CON INERCIA
# ─────────────────────────────────────────────────────────────────────────────

class Camera:
    MODES = ['orbital', 'cenital', 'ecuador']

    def __init__(self):
        self.yaw       = 25.0
        self.pitch     = 28.0
        self.dist      = 52.0
        self.target    = [0.0, 0.0, 0.0]
        self._drag     = None
        self._yaw0     = 0.0
        self._pitch0   = 0.0
        # Inercia
        self.vel_yaw   = 0.0
        self.vel_pitch = 0.0
        self._prev_mx  = 0
        self._prev_my  = 0
        self.mode_idx  = 0
        self._mode_t   = 0.0   # transicion entre modos
        # Angulos objetivo
        self._ty       = self.yaw
        self._tp       = self.pitch
        self._td       = self.dist

    def apply(self):
        # Suavizado hacia target
        self.yaw   = lerp(self.yaw,   self._ty, 0.10)
        self.pitch = lerp(self.pitch, self._tp, 0.10)
        self.dist  = lerp(self.dist,  self._td, 0.08)

        glTranslatef(0.0, 0.0, -self.dist)
        glRotatef(self.pitch, 1.0, 0.0, 0.0)
        glRotatef(self.yaw,   0.0, 1.0, 0.0)
        glTranslatef(-self.target[0], -self.target[1], -self.target[2])

    def start_drag(self, mx, my):
        self._drag   = (mx, my)
        self._yaw0   = self._ty
        self._pitch0 = self._tp
        self._prev_mx = mx
        self._prev_my = my

    def drag(self, mx, my):
        if self._drag is None:
            return
        dx = mx - self._drag[0]
        dy = my - self._drag[1]
        self.vel_yaw   = (mx - self._prev_mx) * 0.35
        self.vel_pitch = (my - self._prev_my) * 0.25
        self._prev_mx  = mx
        self._prev_my  = my
        self._ty = self._yaw0   + dx * 0.38
        self._tp = clamp(self._pitch0 + dy * 0.28, -89, 89)

    def stop_drag(self):
        self._drag = None

    def update_inertia(self):
        if self._drag is None:
            self._ty += self.vel_yaw
            self._tp  = clamp(self._tp + self.vel_pitch, -89, 89)
            self.vel_yaw   *= 0.88
            self.vel_pitch *= 0.88

    def zoom(self, delta):
        self._td = clamp(self._td - delta * 3.5, 6.0, 300.0)

    def next_mode(self):
        self.mode_idx = (self.mode_idx + 1) % len(self.MODES)
        mode = self.MODES[self.mode_idx]
        if mode == 'cenital':
            self._tp = 88.0
            self._ty = 0.0
            self._td = 65.0
        elif mode == 'ecuador':
            self._tp = 2.0
            self._ty = 0.0
            self._td = 55.0
        else:
            self._tp = 28.0
            self._ty = 25.0
            self._td = 52.0

    def reset(self):
        self._ty, self._tp, self._td = 25.0, 28.0, 52.0
        self.vel_yaw = self.vel_pitch = 0.0


# ─────────────────────────────────────────────────────────────────────────────
#  HUD
# ─────────────────────────────────────────────────────────────────────────────

class HUD:
    def __init__(self):
        self.font_title = pygame.font.SysFont("consolas", 17, bold=True)
        self.font_data  = pygame.font.SysFont("consolas", 13)
        self.font_small = pygame.font.SysFont("consolas", 11)
        self.surface    = pygame.Surface((W, H), pygame.SRCALPHA)

    def draw(self, sim_t, speed, paused, fps, cam_mode,
             show_grid, show_jets, show_disk, show_stars):

        self.surface.fill((0, 0, 0, 0))
        s = self.surface

        # Panel izquierdo
        panel = pygame.Surface((270, 260), pygame.SRCALPHA)
        panel.fill((0, 0, 0, 155))
        s.blit(panel, (8, 8))

        title = self.font_title.render("AGUJERO NEGRO — SIM 3D", True, (255, 170, 40))
        s.blit(title, (14, 13))

        # Datos fisicos
        M_solar = 10e6   # masa nominal en masas solares (10 millones)
        r_s_km  = 2.95 * M_solar / 1e6  # RS en km (aprox)
        rows = [
            ("Masa",            f"{M_solar:.1e} M☉"),
            ("Radio Schwarz.",  f"{r_s_km:.1f} km"),
            ("Spin (Kerr)",     "0.85 a/M"),
            ("Temp. disco int.","~50 000 K"),
            ("Temp. disco ext.","~3 000 K"),
            ("Jets",            "~0.99 c"),
            ("",                ""),
            ("Tiempo sim.",     f"{sim_t:.1f} s"),
            ("Velocidad",       f"x{speed:.2f}"),
            ("Modo cam.",       cam_mode),
            ("FPS",             f"{fps:.0f}"),
        ]
        for i, (label, value) in enumerate(rows):
            if not label:
                continue
            lbl  = self.font_data.render(f"{label}:", True, (130, 175, 220))
            val  = self.font_data.render(value,        True, (230, 230, 230))
            y_   = 38 + i * 18
            s.blit(lbl, (14, y_))
            s.blit(val, (160, y_))

        # Estado
        estado_col = (255, 60, 60) if paused else (60, 230, 100)
        estado_txt = "■ PAUSA" if paused else "▶ EN CURSO"
        st = self.font_data.render(estado_txt, True, estado_col)
        s.blit(st, (14, 240))

        # Indicadores de capa
        y_ind = H - 95
        capas = [
            (show_grid,  "G: Grid espacio-tiempo"),
            (show_jets,  "J: Jets relativistas"),
            (show_disk,  "D: Disco de acrecion"),
            (show_stars, "S: Estrellas orbitales"),
        ]
        ind_panel = pygame.Surface((230, 80), pygame.SRCALPHA)
        ind_panel.fill((0, 0, 0, 130))
        s.blit(ind_panel, (8, y_ind - 4))
        for i, (active, label) in enumerate(capas):
            col = (90, 220, 130) if active else (120, 120, 120)
            txt = self.font_small.render(("✔ " if active else "✘ ") + label, True, col)
            s.blit(txt, (14, y_ind + i * 17))

        # Controles (panel derecho)
        ctrl_panel = pygame.Surface((220, 160), pygame.SRCALPHA)
        ctrl_panel.fill((0, 0, 0, 130))
        s.blit(ctrl_panel, (W - 228, H - 168))
        ctrl_lines = [
            "CONTROLES:",
            "Arrastrar → rotar",
            "Rueda     → zoom",
            "R         → reset cam",
            "V         → cambiar vista",
            "P/Espacio → pausa",
            "+/-       → velocidad",
            "ESC/Q     → salir",
        ]
        for i, line in enumerate(ctrl_lines):
            col = (200, 180, 80) if i == 0 else (150, 150, 150)
            t   = self.font_small.render(line, True, col)
            s.blit(t, (W - 222, H - 162 + i * 18))

    def blit_to_gl(self):
        raw = pygame.image.tostring(self.surface, "RGBA", True)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glWindowPos2i(0, 0)
        glDrawPixels(W, H, GL_RGBA, GL_UNSIGNED_BYTE, raw)
        glDisable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)


# ─────────────────────────────────────────────────────────────────────────────
#  ILUMINACION
# ─────────────────────────────────────────────────────────────────────────────

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glShadeModel(GL_SMOOTH)

    # Luz desde el interior del disco (posicion central, difusa naranja-calida)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.5, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  [1.0, 0.75, 0.45, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 0.80, 0.50, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT,  [0.02, 0.02, 0.05, 1.0])

    # Luz ambiental fria (galaxia)
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0.0, 300.0, 0.0, 1.0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE,  [0.04, 0.04, 0.09, 1.0])
    glLightfv(GL_LIGHT1, GL_AMBIENT,  [0.03, 0.03, 0.07, 1.0])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.0,  0.0,  0.0,  1.0])


def setup_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    near, far = 0.3, 3000.0
    fov = 50.0
    aspect = W / H
    f = 1.0 / math.tan(deg2rad(fov / 2))
    glFrustum(-near/f*aspect, near/f*aspect, -near/f, near/f, near, far)
    glMatrixMode(GL_MODELVIEW)


# ─────────────────────────────────────────────────────────────────────────────
#  BUCLE PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────

def main():
    pygame.init()
    try:
        glutInit()
    except Exception:
        pass

    screen = pygame.display.set_mode((W, H), DOUBLEBUF | OPENGL)
    pygame.display.set_caption(TITLE)
    clock  = pygame.time.Clock()

    setup_projection()
    setup_lighting()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glClearColor(0.0, 0.0, 0.01, 1.0)

    # ── Crear objetos de escena ───────────────────────────────────────────────
    bh     = BlackHoleCore()
    disk   = AccretionDisk()
    stream = AccretionStream()
    jets   = RelJet()
    grid   = SpacetimeGrid()
    bg     = Background()
    stars  = [OrbitalStar(i) for i in range(N_STARS_ORB)]
    camera = Camera()
    hud    = HUD()

    # ── Estado ────────────────────────────────────────────────────────────────
    sim_t      = 0.0
    sim_speed  = 1.0
    paused     = False
    show_grid  = True
    show_jets  = True
    show_disk  = True
    show_stars = True
    fps_smooth = 60.0
    prev_t     = time.perf_counter()

    running = True
    while running:
        now    = time.perf_counter()
        rdt    = min(now - prev_t, 0.05)
        prev_t = now
        fps_smooth = fps_smooth * 0.93 + (1.0 / max(rdt, 1e-6)) * 0.07

        dt = 0.0 if paused else rdt * sim_speed

        # ── Eventos ───────────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                k = event.key
                if k in (K_ESCAPE, K_q):
                    running = False
                elif k == K_r:
                    camera.reset()
                elif k in (K_p, K_SPACE):
                    paused = not paused
                elif k in (K_PLUS, K_EQUALS, K_KP_PLUS):
                    sim_speed = min(sim_speed * 1.4, 20.0)
                elif k in (K_MINUS, K_KP_MINUS):
                    sim_speed = max(sim_speed / 1.4, 0.05)
                elif k == K_g:
                    show_grid  = not show_grid
                elif k == K_j:
                    show_jets  = not show_jets
                elif k == K_v:
                    camera.next_mode()
                elif k == pygame.K_d:
                    show_disk  = not show_disk
                elif k == pygame.K_s:
                    show_stars = not show_stars

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                camera.start_drag(*event.pos)
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                camera.stop_drag()
            elif event.type == MOUSEMOTION:
                if event.buttons[0]:
                    camera.drag(*event.pos)
            elif event.type == MOUSEWHEEL:
                camera.zoom(event.y)

        # ── Actualizar ────────────────────────────────────────────────────────
        camera.update_inertia()
        if dt > 0:
            sim_t += dt
            bh.update(dt)
            disk.update(dt)
            stream.update(dt)
            jets.update(dt)
            for st in stars:
                st.update(dt)

        # ── Render 3D ─────────────────────────────────────────────────────────
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        camera.apply()

        # Fondo (sin depth test)
        bg.draw()

        # Grid espacio-tiempo
        if show_grid:
            grid.draw()

        # Flujo espiral
        if show_disk:
            stream.draw()

        # Disco de acrecion
        if show_disk:
            disk.draw(inclination=deg2rad(15.0))

        # Jets
        if show_jets:
            jets.draw()

        # Estrellas orbitando
        if show_stars:
            for st in stars:
                st.draw()

        # Agujero negro (al final para que tape todo)
        bh.draw()

        # ── HUD ───────────────────────────────────────────────────────────────
        hud.draw(sim_t, sim_speed, paused, fps_smooth,
                Camera.MODES[camera.mode_idx],
                show_grid, show_jets, show_disk, show_stars)
        hud.blit_to_gl()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
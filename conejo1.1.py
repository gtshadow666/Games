import pygame
import random
import time
# Inicializar Pygame
pygame.init()
#hacer el raton invisble
pygame.mouse.set_visible(False)
# Dimensiones de la pantalla
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Títulos y colores
pygame.display.set_caption("Cazar al Conejo")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Cargar las imágenes
conejo_img = pygame.image.load("conejo.png")  # Asegúrate de tener esta imagen en tu carpeta
fondo_madera_img = pygame.image.load("pradera.jpg")  # Asegúrate de tener esta imagen en tu carpeta
mira_img = pygame.image.load("mira.png")
# Redimensionar la imagen del conejo si es necesario
conejo_width,conejo_height = 32,32
mira_width,mira_height = 200,164
conejo_img = pygame.transform.scale(conejo_img, (conejo_width, conejo_height))
mira_img = pygame.transform.scale(mira_img,(mira_width, mira_height))
# Posición inicial del conejo
conejo_x, conejo_y = random.randint(50, screen_width-80), random.randint(50, screen_height-80)

# Velocidad del movimiento del conejo
conejo_dx, conejo_dy = random.choice([-20, 20]), random.choice([-20, 20])  # Movimiento aleatorio en x e y

# Variables del juego
puntos = 0
tiros=0
# Fuentes para mostrar texto
font = pygame.font.SysFont('Arial', 40)

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, color, x, y):
    label = font.render(texto, True, color)
    screen.blit(label, (x, y))

# Bucle principal del juego
running = True
while running:

    # Mostrar fondo de madera
    screen.blit(fondo_madera_img, (0, 0))
    
    # Comprobamos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Obtener la posición del ratón
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Movimiento del conejo (rebote en las paredes)
    conejo_x += conejo_dx
    conejo_y += conejo_dy

    # Rebote contra las paredes
    if conejo_x <= 0 or conejo_x + conejo_width >= screen_width-10:  # Si toca el borde izquierdo o derecho
        conejo_dx = -conejo_dx  # Cambia la dirección horizontal
    
    if conejo_y <= 0 or conejo_y + conejo_height >= screen_height-10:  # Si toca el borde superior o inferior
        conejo_dy = -conejo_dy  # Cambia la dirección vertical

    # Disparar
    if pygame.mouse.get_pressed()[0]:  # Si se presiona el botón izquierdo del ratón
        distancia = ((mouse_x - (conejo_x + conejo_width // 2)) ** 2 + (mouse_y - (conejo_y + conejo_height // 2)) ** 2) ** 0.5
        tiros += 1
        if distancia < 20:  # Si el tiro está cerca del conejo
            conejo_x, conejo_y = random.randint(50, screen_width-80), random.randint(50, screen_height-80)  # Nueva posición aleatoria
            puntos += 1  # Aumenta el contador de puntos
            time.sleep(0.3)

    # Mostrar los puntos
    mostrar_texto(f'Puntos: {puntos}', BLACK, 10, 10)
    punteria= 100 if tiros ==0 else puntos/tiros *100
    mostrar_texto(f'punteria:{round(punteria)}%', BLACK ,10, 50)
    # Dibujar el conejo en la pantalla Y la mira la calibramos
    screen.blit(conejo_img, (conejo_x, conejo_y))
    screen.blit(mira_img,(mouse_x-100,mouse_y-86))
    # Actualizar la pantalla
    pygame.display.update()
    
    # Controlar FPS (24 frames por segundo)
    clock.tick(24)

pygame.quit()

import pygame

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Création de la fenêtre
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Définition des couleurs
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

# Définition des variables du joystick
joystick_pos = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
joystick_radius = 50
# Définition des variables de bouton
button_width = 100
button_height = 50
button_margin = 20

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 25)
        text = font.render(self.text, 1, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

# Création des boutons de direction
up_button = Button(WINDOW_WIDTH // 2 - button_width // 2, button_margin, button_width, button_height, GRAY, "Avant")
down_button = Button(WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT - button_height - button_margin, button_width, button_height, GRAY, "Arrière")
left_button = Button(button_margin, WINDOW_HEIGHT // 2 - button_height // 2, button_width, button_height, GRAY, "Gauche")
right_button = Button(WINDOW_WIDTH - button_width - button_margin, WINDOW_HEIGHT // 2 - button_height // 2, button_width, button_height, GRAY, "Droite")

# Définition de la taille de la fenêtre
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Définition de la police d'écriture
font = pygame.font.SysFont('Calibri', 25, True, False)

# Définition de l'affichage du texte sur les boutons
button_text = font.render('Click me!', True, BLACK)

# Création de la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Boutons de direction")

# Définition des boutons
button_width = 80
button_height = 80
button_spacing = 20

button_up = pygame.Rect(WINDOW_SIZE[0]/2 - button_width/2, button_spacing, button_width, button_height)
button_down = pygame.Rect(WINDOW_SIZE[0]/2 - button_width/2, WINDOW_SIZE[1] - button_height - button_spacing, button_width, button_height)
button_left = pygame.Rect(button_spacing, WINDOW_SIZE[1]/2 - button_height/2, button_width, button_height)
button_right = pygame.Rect(WINDOW_SIZE[0] - button_width - button_spacing, WINDOW_SIZE[1]/2 - button_height/2, button_width, button_height)
button_main = pygame.Rect(WINDOW_SIZE[0]/2 - button_width/2, WINDOW_SIZE[1]/2 - button_height/2, button_width, button_height)

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_up.collidepoint(mouse_pos):
                print("Bouton haut appuyé")
            if button_down.collidepoint(mouse_pos):
                print("Bouton bas appuyé")
            if button_left.collidepoint(mouse_pos):
                print("Bouton gauche appuyé")
            if button_right.collidepoint(mouse_pos):
                print("Bouton droite appuyé")
            if button_main.collidepoint(mouse_pos):
                print("Bouton principal appuyé")
    
    # Affichage des boutons
    pygame.draw.rect(screen, GRAY, button_up)
    pygame.draw.rect(screen, GRAY, button_down)
    pygame.draw.rect(screen, GRAY, button_left)
    pygame.draw.rect(screen, GRAY, button_right)
    pygame.draw.rect(screen, WHITE, button_main)
    screen.blit(button_text, (WINDOW_SIZE[0]/2 - button_text.get_width()/2, WINDOW_SIZE[1]/2 - button_text.get_height()/2))
    
    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()

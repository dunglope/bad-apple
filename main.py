import cv2
import pygame
import time
import threading

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

# Load font
font = pygame.font.Font(None, 22)

# Load sound
pygame.mixer.init()
sound = pygame.mixer.Sound('bad apple.mp3')  # Replace with your audio file

def print_gray(path):
    chars = ['|', " "]
    img = cv2.imread(path, 0)
    img = cv2.resize(img, (100, 50))
    f = []
    for i in img:
        line = [chars[int(s >= (225 / 2))] for s in i]
        f.append(''.join(line))
    return '\n'.join(f)

def write(text, location, color=(0, 0, 0)):
    global font
    screen.blit(font.render(text, True, color), location)

def play_sound():
    while True:
        sound.play()
        time.sleep(sound.get_length())  # Wait for the sound to finish

# Create and start the sound thread
sound_thread = threading.Thread(target=play_sound)
sound_thread.daemon = True  # The thread will exit when the main program ends
sound_thread.start()

for i in range(0, 6572):    # load frames by frames
    p = 0
    q = print_gray(f'frame{i}.jpg')
    for s in q.split('\n'):
        write(s, (10, 10 + 10 * p))
        p += 1
    
    # Calculate total video duration
    total_duration = 6576 /1000 * 19  # in seconds, 219 targeted
    
    text_surface = font.render(f'Video Length: {total_duration:.2f} seconds', True, (0, 0, 0))
    text_rect = text_surface.get_rect(bottomright=(screen_width - 10, screen_height - 10))
    screen.blit(text_surface, text_rect)
    
    pygame.display.update()
    
    pygame.time.delay(19)
    screen.fill((255, 255, 255))

pygame.quit()

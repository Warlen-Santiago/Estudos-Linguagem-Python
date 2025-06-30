import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('C:/Users/warle/Documents/MeusProjetos/Estudos-Linguagem-Python/Curso Python - Curso em vídeo(Guanabara)/PythonExercicios/keep.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
        time.sleep(1)

print("Reprodução finalizada.")
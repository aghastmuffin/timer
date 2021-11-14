import pygame
print("make sure the file is in the same folder as this program, then follow the instructions below")
musicfile = input('Add the name of the file (case specific) then the ending (.wav, .mp3, .ogg): ')
pygame.mixer.init()
pygame.mixer.music.load(musicfile)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
  pygame.time.Clock().tick()
print('Music finished')

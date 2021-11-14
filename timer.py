from time import sleep
import os
os.system("cls")
print("All rights reserved")
print("Music by derivakat")
print("© 2021")
ogtime = input("set timer: ")
os.system("cls")
time1 = int(ogtime)
while time1 > 0:
    os.system("cls")
    print(time1)
    time1 = (time1 - 1)
    sleep(1)
while time1 == (0):
    print("done")
    import pygame
    from pygame import mixer
    os.system("cls")
    pygame.mixer.init()
    pygame.mixer.music.load("REVIVED_butimlosingit - Copy (2).wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()
    print('Music finished')

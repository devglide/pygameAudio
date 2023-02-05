# import pygame
# from tkinter import *



# root = Tk()
# root.geometry = ('400x400')


# pygame.mixer.init()

# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
# pygame.init() #turn all of pygame on.


# def play():
#     pygame.mixer.music.load('sm.mp3')



# butt = Button(root, text='click me', command=play)
# butt.pack()




# root.mainloop()


import pygame


pygame.mixer.init()  # Initialize the mixer module.
sound1 = pygame.mixer.Sound('sm.mp3')  # Load a sound.

while True:
    inpt = input('Press enter to play the sound: ')
    sound1.play()  # Play the sound.
    print('Playing sound')
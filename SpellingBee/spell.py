from gtts import gTTS
import time
import os
import pygame
import keyboard
import random

print(os.getcwd())  # print the current directory
print(os.listdir())  # print a list of files in the current directory
# Define the list of words to spell out
words = []
with open('dictionary.txt', 'r') as file:
    for line in file:
        word = line.strip()  # remove the newline character
        words.append(word)  # add the word to the list

random.shuffle(words)
pygame.init()

print("\n\n\n\n\n-------NEXT WORD---------")
#playSound Function
def playSound():
    # Load audio file
    sound = pygame.mixer.Sound('sound.mp3')
    # Play audio file
    sound.play()
    # Wait for audio to finish
    while pygame.mixer.get_busy():
        if keyboard.is_pressed('enter'):
            break
        pass

# Loop through the words in the list and spell them out letter by letter
for word in words:
    tts = gTTS(word, lang='en')
    tts.save('sound.mp3')
    print(word)
    playSound()
    #print("Press enter to spell word")
    input() # Wait for user input before next word
    
    #print("Press enter for next word")
    """
    for letter in word:
        tts = gTTS(letter, lang='en')
        tts.save('sound.mp3')
        playSound()
        if keyboard.is_pressed('enter'):
            break
    input() # Wait for user input before next word
    """
    print("-------NEXT WORD---------")


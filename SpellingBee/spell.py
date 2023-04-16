from gtts import gTTS
import time
import os
import pygame
import keyboard
import random
import requests

print(os.getcwd())  # print the current directory
print(os.listdir())  # print a list of files in the current directory
# Define the list of words to spell out
words = []
with open('dictionary7-9.txt', 'r') as file:
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

def getDefinition(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)

    if response.status_code == 200:
        # The request was successful
        data = response.json()
        print(data[0]["meanings"][0]["definitions"][0]["definition"])
        return data[0]["meanings"][0]["definitions"][0]["definition"]
    else:   
        # The request was not successful
        print("Error: {}".format(response.status_code))

# Loop through the words in the list and spell them out letter by letter
for word in words:
    tts = gTTS(word, lang='en')
    tts.save('sound.mp3')
    print(word)
    playSound()
    #print("Press enter to spell word")
    recvInput = input() # Wait for user input before next word
    if (recvInput == "d"):
        definition = getDefinition(word)
        tts = gTTS(definition, lang='en')
        tts.save('sound.mp3')
        playSound()
        input()
    
    #print("Press enter for next word")
    print("-------NEXT WORD---------")


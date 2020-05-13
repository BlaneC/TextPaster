from pynput.keyboard import Key, Controller
import time

file = open("lyrics.txt", "r")
lyrics = file.read()
keyboard = Controller()
lyrics = lyrics.replace('\n', ' ')
lyrics = lyrics.split(" ")
time.sleep(2)
for words in lyrics:
    for letters in words:
        keyboard.press(letters)
        keyboard.release(letters)
    keyboard.press(Ketalking
    about
    His
    y.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)





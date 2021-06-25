import selenium
from selenium import webdriver
from pynput.keyboard import Key, Controller

import time

name = input("What is the Name: ")

keyboard = Controller()

numberOfPeople = input("How many people: ")

convertedNumberOfPeople = int(numberOfPeople)

gameCodeInput = input("Game Code: ")

x = 0

if(len(gameCodeInput) == 6):
    for x in range(0, convertedNumberOfPeople):
        browser = webdriver.Chrome("/Users/sakshamgupta/Desktop/Quizlet Bot/chromedriver")
        browser.get("https://quizlet.com/live")

        gameCode = browser.find_elements_by_class_name('UIInput-input')
        continueButton = browser.find_elements_by_class_name("UIButton.UIButton--hero")

        gameCode[0].send_keys(gameCodeInput)
        continueButton[0].click()

        convertedX = str(x)
        time.sleep(1)
        keyboard.type(name + convertedX)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
    browser.quit()



else:
    print("nope")
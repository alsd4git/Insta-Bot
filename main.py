import time
from PIL import Image
import requests
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import instabot
import random
import os


def get_random_image():
    res = random.randint(32, 108)
    res *= 10
    print(res)
    link = f'https://source.unsplash.com/random/{res}x{res}'
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    img.save('post.jpg')
    print("Image Fatched !")


def get_random_caption():

    chrome_options = Options()
    # removes webdrive start from logging
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--window-size=340,860")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://randomtextgenerator.com/")
    caption = driver.find_element_by_id('generatedtext')
    captions = caption.text.split('.')
    print("Caption Fatched !")
    return captions[0] + '. ' + f'#{captions[1].split()[0]} ' + f'#{captions[1].split()[1]} ' + f'#{captions[1].split()[2]}'


def post(caption, username="", password=""):
    caption += " #bot #random"
    bot = instabot.Bot()
    bot.login(username=username, password=password)
    bot.upload_photo('post.jpg', caption=caption)


if __name__ == "__main__":
    get_random_image()
    caption = get_random_caption()
    post(caption, username="", password="")

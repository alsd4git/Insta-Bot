import time
from PIL import Image
from io import BytesIO

import requests
from bs4 import BeautifulSoup

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

    url = "https://randomtextgenerator.com/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    caption = soup.find(id="generatedtext")

    captions = caption.text.split('.')
    print("Caption Fatched !")
    return captions[0] + '. ' + f'#{captions[1].split()[0]} ' + f'#{captions[1].split()[1]} ' + f'#{captions[1].split()[2]}'


def post(caption, username="", password=""):
    caption += " #bot #random"
    bot = instabot.Bot()
    bot.login(username=username, password=password)
    # cleanup before posting
    os.remove('post.jpg.REMOVE_ME')
    bot.upload_photo('post.jpg', caption=caption)
    # after upload this file is renamed as 'post.jpg.REMOVE_ME' for some reason


if __name__ == "__main__":
    get_random_image()
    caption = get_random_caption()
    # remeber to use username and not email, with emails only first login works somehow, this is instabot fault
    post(caption, username="", password="")

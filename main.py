
from PIL import Image
from instabot import Bot
#from dotenv import  DotEnv

import time
from dotenv import load_dotenv
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import get_colection_from_Hubble

import requests
import os, errno
from os import listdir
from os.path import isfile
from os.path import join as joinpath


def create_dir_image(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def image_to_square_size(file, cur_file):
    image = Image.open(file)
    width = image.width
    height = image.height
    square_size = width
    if height < width :
        square_size = height
    image.thumbnail((square_size, square_size))
    image.save(cur_file)
    image.close()

def image_to_unload_instagram(file, cur_file):
    time.sleep(7)
    bot.upload_photo(cur_file, caption="1")
    if bot.api.last_response.status_code != 200:
        print("Не удалось выгрузить файл")
        print(bot.api.last_response)
        print(" ")


def file_unload_instagramm(cur_path):
    mypath = cur_path
    cur_path_and_slesh = os.path.join(cur_path, "")
    for cur_file in listdir(mypath):
        if isfile(joinpath(mypath, cur_file)):
            full_name_file = "{0}{1}".format(cur_path_and_slesh,cur_file)
            image_to_square_size(full_name_file, cur_file)
            image_to_unload_instagram(full_name_file, cur_file)

def main()^
    load_dotenv()
    dir_name = os.path.join("images", "")
    create_dir_image(dir_name)

    fetch_spacex_last_launch()
    get_colection_from_Hubble("spacecraft")
    inst_login = os.getenv("INTGR_LOGIN")
    inst_passwd = os.getenv("INTGR_PASSWD")
    bot = Bot()
    bot.login(username=inst_login, password=inst_passwd)
    file_unload_instagramm("images")


if __name__ == '__main__':
    main()

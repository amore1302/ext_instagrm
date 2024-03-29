import requests
from load_image   import load_image_from_url_to_file
import os




def get_last_image_from_Hubble(id_image):
    url_image = "http://hubblesite.org/api/v3/image/{0}".format(id_image)
    response = requests.get(url_image)
    if not response.ok:
        raise requests.exceptions.HTTPError(response=response)
    images = response.json()["image_files"]
    last_image = images[-1]
    url_image = last_image["file_url"]

    _, file_extension = os.path.splitext(url_image)
    dir_name = os.path.join("images", "")
    url_file = "{0}{1}{2}".format(dir_name , id_image,    file_extension )

    first_symbols = url_image[0:4]
    if first_symbols != "http":
        url_image = "https:{0}".format(url_image)
    load_image_from_url_to_file(url_image, url_file)

def get_colection_from_Hubble(name_colection):
    url_colection = "http://hubblesite.org/api/v3/images/{0}".format(name_colection)
    response = requests.get(url_colection)
    if not response.ok:
        raise requests.exceptions.HTTPError(response=response)
    images = response.json()
    for curent_image in images:
        curent_id = curent_image["id"]
        get_last_image_from_Hubble(curent_id)


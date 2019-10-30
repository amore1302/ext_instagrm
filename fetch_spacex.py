import requests
from load_image   import load_image_from_url_to_file
import os

def fetch_spacex_last_launch():
    directory = os.path.join("images", "")
    payload = {
        "latest": "",
        "launch_date_utc": "2019-08-06T22:52:00.000Z"
    }
    url_image = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url_image, params=payload)
    if not response.ok:
        raise requests.exceptions.HTTPError(response=reponse)

    image_latest = response.json()[0]
    images  = image_latest["links"]["flickr_images"]
    for image_number, image in enumerate(images):
        full_file_name = "{0}spacex{1}.jpg".format(directory, image_number)
        load_image_from_url_to_file(image, full_file_name)

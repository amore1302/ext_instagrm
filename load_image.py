
import requests
def load_image_from_url_to_file(url_internet, url_file):
    response = requests.get(url_internet , verify=False)
    response.raise_for_status()

    with open(url_file, 'wb') as file:
        file.write(response.content)

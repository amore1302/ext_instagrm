
import requests
def load_image_from_url_to_file(url_internet, full_file_name):
    response = requests.get(url_internet , verify=False)
    response.raise_for_status()

    with open(full_file_name, 'wb') as file:
        file.write(response.content)

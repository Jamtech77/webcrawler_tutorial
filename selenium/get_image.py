import os
import random
from time import sleep

import requests
import pandas as pd

IMAGE_DIR = './image/'

# Read csv file
df = pd.read_csv('image_urls.csv')

if os.path.isdir(IMAGE_DIR):
    print('Directory already exists')
else:
    os.makedirs(IMAGE_DIR)

# Save image
for file_name, yahoo_image_url in zip(df.filename[:5], df.yahoo_image_url):
    image = requests.get(yahoo_image_url)
    with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f: # wb : write, binary
        f.write(image.content)
    
    sleep(random.randint(1, 5))

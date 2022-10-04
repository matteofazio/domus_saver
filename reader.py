import argparse
from enum import Enum
import io
import os

from google.cloud import vision
from PIL import Image, ImageDraw

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\FAZIO\\Desktop\\QUESTURE\\text-detection-362511-c9a57db7685c.json"

mypath = 'C:\\FAZIO\\Desktop\\QUESTURE'

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

f.sort(key=os.path.getmtime)
print(f)


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    result = []
    for text in texts:
        print('\n"{}"'.format(text.description))
        result.append(text.description)
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        print('bounds: {}'.format(','.join(vertices)))
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


length = len(f)
k = 1
while k < len(f):
    if f[-k][-4:] == '.jpg':
        image = f[-k]
        break
    k += 1

detect_text(mypath + '\\' + image)





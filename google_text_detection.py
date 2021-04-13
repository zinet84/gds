import io
import cv2
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()


'''
detect_text 

- Input : Image file path
- Output : List containing all detected text on the image

Google Vision API detects text from upper-left to lower-right.
Basically, Return type is JSON. 
It has text box coordinate of upper left corner with height and width.
But this function only returns the text in turn.
'''
def detect_text(img):
    """Detects text in the file."""
    response = client.text_detection(image=img)
    # Extract detected text from response
    texts = response.text_annotations

    # Concatenate all detected text to a string
    # Last text is useless. Accordingly, exclude it.
    string = ''
    for text in texts:
        string +=' ' + text.description

    # Split the result string into list
    ret = string.split()

    return ret

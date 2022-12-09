import numpy as np
import cv2
from PIL import Image

def get_list_pixel_rgb(inputs):
    if type(inputs) == str:
        '''Input is path to image'''
        image = cv2.imread(inputs)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif type(inputs) == np.ndarray:
        '''Input read with cv2.imread('''
        image = cv2.cvtColor(inputs, cv2.COLOR_BGR2RGB)
    elif type(inputs) == Image:
        '''Input is PIL image'''
        image = np.asarray(inputs)

    h, w, c = image.shape
    
    assert c == 3, f'This function does not support image with {c} channel(s) invalid'

    list_pixel = []
    for pix_h in range(h):
        for pix_w in range(w):
            list_pixel.append(image[pix_h][pix_w])

    return list_pixel


def make_color_image(pixel, image_size = (256, 256), mode = 'RGB'):
    r, g, b = pixel
    height = image_size[0]
    width = image_size[1]
    color_image = np.zeros((height, width ,3), np.uint8)
    if mode == 'BGR':
        color_image[:, :] = (b, g, r)
    else:
        color_image[:, :] = (r, g, b)
    return color_image


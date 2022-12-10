import numpy as np
import cv2

def get_list_pixel_rgb(inputs):
    if type(inputs) == str:
        '''Input is path to image'''
        image = cv2.imread(inputs)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        raise f'"{type(inputs)}" isn\'t supported'

    h, w, c = image.shape
    
    assert c == 3, f'This function does not support image with {c} channel(s), 3 channels only'

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


def save_color_txt(dominant_colors_list, savename: str = ""):
    assert savename.endswith(".txt"), f'Save name must end with ".txt"'
    write_string = ""
    if type(dominant_colors_list) == np.ndarray:
        for rgb_colors in dominant_colors_list:
            r, g, b = rgb_colors
            write_string += f"{r}, {g}, {b}\n"
    else:
        raise f'"{type(dominant_colors_list)}" isn\'t supported'

    with open(savename, mode="w") as savefile:
        savefile.write(write_string)


from sklearn.cluster import KMeans
import numpy as np
import cv2
from utils import get_list_pixel_rgb, make_color_image

def kmeans(X, n_clusters):
    if type(X) == list:
        X = np.array(X)
    
    kmeans = KMeans(n_clusters=n_clusters).fit(X)
    return kmeans.cluster_centers_.astype(int)


def get_dominant_color(inputs, n_clusters):
    list_color = get_list_pixel_rgb(inputs)
    results = kmeans(list_color, n_clusters)
    color = [cv2.imread(img_link), ]
    for result in results:
        color.append(make_color_image(result))
    Horizontal_img = np.concatenate(color, axis=1)
    return Horizontal_img, color[1:]


if __name__ == '__main__':
    img_link = './dataset/006897.jpg'
    Horizontal_img, color = get_dominant_color(img_link, 5)
    cv2.imwrite('image.jpg', Horizontal_img)
    
    
    
    
    
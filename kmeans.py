from sklearn.cluster import KMeans
import numpy as np
import cv2
from PIL import Image
from utils import get_list_pixel_rgb, make_color_image



def kmeans(X, n_clusters):
    if type(X) == list:
        X = np.array(X)
    
    kmeans = KMeans(n_clusters=n_clusters, n_init=10).fit(X)
    mydict = {i: len(np.where(kmeans.labels_ == i)[0]) for i in range(kmeans.n_clusters)}
    value = np.fromiter(mydict.values(), dtype=int)
    return kmeans.cluster_centers_.astype(int)[np.argsort(value)[::-1]]


def get_dominant_color(inputs, n_clusters):
    if type(inputs) == str:
        '''Input is path to image'''
        image = cv2.imread(inputs)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif type(inputs) == np.ndarray:
        '''Input read with cv2.imread'''
        image = cv2.cvtColor(inputs, cv2.COLOR_BGR2RGB)
    elif type(inputs) == Image:
        '''Input is PIL image'''
        image = np.asarray(inputs)


    list_color = get_list_pixel_rgb(inputs)         # RGB
    results = kmeans(list_color, n_clusters)        # RGB
    color = [image, ]                               # BGR
    for result in results:
        color.append(make_color_image(result, mode = 'RGB'))      # RGB
    Horizontal_img = np.concatenate(color, axis=1)  # RGB
    return Horizontal_img, color[1:]                # RGB
    
    
if __name__ == "__main__":
    image_path = './data/images/000004.jpg'
    number_cluster = 5
    img, color = get_dominant_color(image_path, number_cluster)
    
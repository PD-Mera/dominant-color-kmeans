from sklearn.cluster import KMeans
import numpy as np
import cv2
from color_utils import get_list_pixel_rgb, make_color_image, save_color_txt


def color_kmeans(X, n_clusters):
    if type(X) == list:
        X = np.array(X)
    
    kmeans = KMeans(n_clusters=n_clusters, n_init=10).fit(X)
    mydict = {i: len(np.where(kmeans.labels_ == i)[0]) for i in range(kmeans.n_clusters)}
    value = np.fromiter(mydict.values(), dtype=int)
    return kmeans.cluster_centers_.astype(int)[np.argsort(value)[::-1]]


def demo_dominant_color(inputs, n_clusters, save = False):
    if type(inputs) == str:
        '''Input is path to image'''
        image = cv2.imread(inputs)


    list_color = get_list_pixel_rgb(inputs)
    results = color_kmeans(list_color, n_clusters)  
    color = [image, ]                           
    for result in results:
        color.append(make_color_image(result, mode = 'BGR'))
    horizontal_img = np.concatenate(color, axis=1)
    if save:
        cv2.imwrite("test.jpg", horizontal_img) 
    return horizontal_img                           
    
    
if __name__ == "__main__":
    image_path = './data/images/000000.jpg'
    number_cluster = 5
    colors_list = get_list_pixel_rgb(image_path)  
    results = color_kmeans(colors_list, number_cluster)
    save_color_txt(results, savename = 'test.txt')
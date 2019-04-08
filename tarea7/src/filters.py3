import sys
import uuid
import argparse
import random
from enum import Enum

import cv2
import numpy as np


class Filter(Enum):
    RANDOM_DITHERING = 0
    ORDERED_DITHERING = 1
    DISPERSO_DITHERING = 2
    FLOYD_STEINBERG_DITHERING = 3


class Image_Processor(object):

    def __init__(self, image_path, filter_id):
        self.__cv_image = cv2.imread(image_path)
        self.filter_id = filter_id
        self.height, self.width, _ = self.__cv_image.shape

        self.__apply_filter(filter_id)

    def __apply_filter(self, filter_id):
        img = None
        if filter_id == Filter.RANDOM_DITHERING:
            img = self.__random_dithering_filter(self.__cv_image)
        elif filter_id == Filter.ORDERED_DITHERING:
            img = self.__ordered_dithering_filter(self.__cv_image)
        elif filter_id == Filter.DISPERSO_DITHERING:
            img = self.__disperso_dithering_filter(self.__cv_image)
        elif filter_id == Filter.FLOYD_STEINBERG_DITHERING:
            img = self.__floyd_steinberg_dithering_filter(self.__cv_image)
        self.__save_filtered_image(img)

    def __gray_scale_filter(self, cv_image):
        height, width, _ = cv_image.shape

        for x in range(height):
            for y in range(width):
                b, g, r = cv_image[x, y]
                gray = (r * 0.29) + (g * 0.59) + (b * 0.12)
                cv_image[x, y] = gray

    def __random_dithering_filter(self, cv_image):
        self.__gray_scale_filter(cv_image)
        height, width, _ = cv_image.shape

        for x in range(height):
            for y in range(width):
                random_int = random.randint(-127, 127)
                if cv_image[x][y][0] + random_int > 127:
                    cv_image[x][y] = 255
                else:
                    cv_image[x][y] = 0

        return cv_image

    def __ordered_dithering_filter(self, cv_image):
        self.__gray_scale_filter(cv_image)
        height, width, _ = cv_image.shape
        dithering_matrix = np.array([[8, 3, 4], [6, 1, 2], [7, 5, 9]])

        for x in range(height):
            for y in range(width):
                aux_1 = cv_image[x][y][0] / 255
                aux_2 = (dithering_matrix[x % 3][y % 3]) / 9
                if aux_1 > aux_2:
                    cv_image[x][y] = 255
                else:
                    cv_image[x][y] = 0

        return cv_image

    def __disperso_dithering_filter(self, cv_image):
        self.__gray_scale_filter(cv_image)
        height, width, _ = cv_image.shape
        dithering_matrix = np.array([[1, 7, 4], [5, 8, 3], [6, 2, 9]])

        for x in range(height):
            for y in range(width):
                aux_1 = cv_image[x][y][0] / 255
                aux_2 = (dithering_matrix[x % 3][y % 3]) / 9
                if aux_1 > aux_2:
                    cv_image[x][y] = 255
                else:
                    cv_image[x][y] = 0

        return cv_image

    def __floyd_steinberg_dithering_filter(self, cv_image):
        self.__gray_scale_filter(cv_image)
        cv_image = np.float32(cv_image)
        height, width, _ = cv_image.shape

        for x in range(height):
            for y in range(width):
                aux = cv_image[x][y][0]

                if cv_image[x][y][0] > 127:
                    cv_image[x][y] = 255
                else:
                    cv_image[x][y] = 0

                error = aux - cv_image[x][y][0]
                if x + 1 < height:
                    cv_image[x + 1, y] = cv_image[x + 1, y] + error * 7.0 / 16
                if x + 1 < height and y + 1 < width:
                    cv_image[x + 1, y + 1] = cv_image[x +
                                                      1, y + 1] + error * 1.0 / 16
                if y + 1 < width:
                    cv_image[x, y + 1] = cv_image[x, y + 1] + error * 5.0 / 16
                if x - 1 > 0 and y + 1 < width:
                    cv_image[x - 1, y + 1] = cv_image[x -
                                                      1, y + 1] + error * 3.0 / 16

        return np.uint8(cv_image)

    def __save_filtered_image(self, cv_image):
        name = self.filter_id.name + '_' + str(uuid.uuid4())[:8]
        cv2.imwrite('../output/{}.jpg'.format(name), cv_image)
        print('Imagen procesada exitosamente')
        print('Guardada en ../output/{}.jpg'.format(name))


def parse_filter_id(id):
    return {
        '0': Filter.RANDOM_DITHERING,
        '1': Filter.ORDERED_DITHERING,
        '2': Filter.DISPERSO_DITHERING,
        '3': Filter.FLOYD_STEINBERG_DITHERING,
    }[id]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, help='Tipo del filtro')
    parser.add_argument('--img', type=str, help='Ruta de la foto')
    args = parser.parse_args()
    filter_id = args.filter
    image_path = args.img

    print('Procesando...')
    image_processor = Image_Processor(image_path, parse_filter_id(filter_id))

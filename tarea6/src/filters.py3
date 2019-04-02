import sys
import uuid
import argparse
from enum import Enum

import cv2
import numpy as np


class Filter(Enum):
    RECURSIVE_GRAY = 0
    RECURSIVE_COLOR = 1


class Image_Processor(object):

    def __init__(self, image_path, filter_id):
        self.__cv_image = cv2.imread(image_path)
        self.height, self.width, _ = self.__cv_image.shape

        assert self.height == 500 and self.width, 'Debe de ser una imagen de 500x500'

        self.SIZE = 50

        self.__apply_filter(filter_id)

    def __apply_filter(self, filter_id):
        img = None
        if filter_id == Filter.RECURSIVE_GRAY:
            img = self.__recursive_gray_filter()
        elif filter_id == Filter.RECURSIVE_COLOR:
            img = self.__recursive_color_filter()
        self.__save_filtered_image(img)

    def __normalize(self, n):
        return 0 if (n < 0) else (n if (n < 256) else 255)

    def __gray_scale_filter(self, cv_image):
        height, width, _ = cv_image.shape

        for x in range(height):
            for y in range(width):
                b, g, r = cv_image[x, y]
                gray = (r * 0.29) + (g * 0.59) + (b * 0.12)

                cv_image.itemset((x, y, 2,), gray)
                cv_image.itemset((x, y, 1,), gray)
                cv_image.itemset((x, y, 0,), gray)

    def __brightness_filter(self, cv_image, brightness):
        height, width, _ = cv_image.shape

        for x in range(height):
            for y in range(width):
                b, g, r = cv_image[x, y]

                cv_image.itemset((x, y, 2,), self.__normalize(r + brightness))
                cv_image.itemset((x, y, 1,), self.__normalize(g + brightness))
                cv_image.itemset((x, y, 0,), self.__normalize(b + brightness))

    def __warhol_filter(self, cv_image, red, green, blue):
        height, width, _ = cv_image.shape

        for x in range(height):
            for y in range(width):
                b, g, r = cv_image[x, y]

                cv_image.itemset((x, y, 2,), red & r)
                cv_image.itemset((x, y, 1,), green & g)
                cv_image.itemset((x, y, 0,), blue & b)

    def __recursive_gray_filter(self):
        cv_image_aux = self.__cv_image.copy()
        self.__gray_scale_filter(cv_image_aux)

        new_height = self.height // self.SIZE
        new_width = self.width // self.SIZE

        new_cv_image = np.zeros((self.height, self.width, 3,), np.uint8)

        cv_image_aux_resized = cv2.resize(
            cv_image_aux, (new_width, new_height,))
        brigthness_cv_images = self.__imgs_ranging_brightness(
            cv_image_aux_resized)

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                avg_gray_region = sum(self.__region_avg_rgb(self.__cv_image,
                                                            j * new_width,
                                                            (j * new_width) +
                                                            new_width,
                                                            i * new_height,
                                                            (i * new_height) +
                                                            new_height,
                                                            new_height,
                                                            new_width)) // 3
                region = avg_gray_region // 8

                x1, x2 = j * new_width, (j * new_width) + new_width
                y1, y2 = i * new_height, (i * new_height) + new_height

                tmp = brigthness_cv_images[region]
                tmp = cv2.resize(tmp, (new_width, new_height,))

                new_cv_image[x1:x2, y1:y2] = tmp

        return new_cv_image

    def __recursive_color_filter(self):
        new_height = self.height // self.SIZE
        new_width = self.width // self.SIZE

        new_cv_image = np.zeros((self.height, self.width, 3,), np.uint8)
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                r, g, b = self.__region_avg_rgb(self.__cv_image,
                                                j * new_width,
                                                (j * new_width) + new_width,
                                                i * new_height,
                                                (i * new_height) + new_height,
                                                new_height,
                                                new_width)

                x1, x2 = j * new_width, (j * new_width) + new_width
                y1, y2 = i * new_height, (i * new_height) + new_height

                tmp = self.__cv_image.copy()
                tmp = cv2.resize(tmp, (new_width, new_height,))
                self.__warhol_filter(tmp, r, g, b)

                new_cv_image[x1:x2, y1:y2] = tmp

        return new_cv_image

    def __region_avg_rgb(self, cv_image, start_h, end_h, start_w, end_w, new_height, new_width):
        height, width, _ = cv_image.shape
        r, g, b = 0, 0, 0
        tot = new_height * new_width
        for h in range(start_h, end_h):
            for w in range(start_w, end_w):
                if h < width:
                    if w < height:
                        _b, _g, _r = cv_image[h, w]
                        r += _r
                        g += _g
                        b += _b
        r //= tot
        g //= tot
        b //= tot
        return (r, g, b,)

    def __imgs_ranging_brightness(self, cv_image):
        l_cv_images = []

        lower_bound = -128
        upper_bound = 128

        i = 0
        while lower_bound < upper_bound:
            tmp = cv_image.copy()
            self.__brightness_filter(tmp, lower_bound)

            l_cv_images.append(tmp)

            lower_bound += 8
            i += 1

        return l_cv_images

    def __save_filtered_image(self, cv_image):
        name = str(uuid.uuid4())[:8]
        cv2.imwrite('../output/{}.jpg'.format(name), cv_image)
        print('Imagen procesada exitosamente')
        print('Guardada en ../output/{}.jpg'.format(name))


def parse_filter_id(id):
    return {
        '0': Filter.RECURSIVE_GRAY,
        '1': Filter.RECURSIVE_COLOR,
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

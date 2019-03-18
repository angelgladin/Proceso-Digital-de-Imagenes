import sys
import argparse
from enum import Enum

import cv2


def show_image_with_filter(cv_image):
    cv2.imshow('Practica 5', cv_image)
    print('Imagen procesada exitosamente')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class Filter(Enum):
    SEPIA = 0
    COLOR_OIL = 1
    GRAY_TONE_OIL = 2


class Image_Processor(object):

    def __init__(self, image_path, filter_id, input_parser):
        self.__cv_image = cv2.imread(image_path)
        self.height, self.width, _ = self.__cv_image.shape
        self.parsed_input = input_parser

        self.__apply_filter(filter_id)

        show_image_with_filter(self.__cv_image)

    def __apply_filter(self, filter_id):
        if filter_id == Filter.SEPIA:
            depth = self.parsed_input.sepia_arg
            self.__sepia_filter(depth)
        elif filter_id == Filter.COLOR_OIL:
            self.__color_oil_filter()
        elif filter_id == Filter.GRAY_TONE_OIL:
            self.__gray_oil_filter()

    def __normalize(self, n):
        return 0 if (n < 0) else (n if (n < 256) else 255)

    def __sepia_filter(self, depth):
        for x in range(self.height):
            for y in range(self.width):
                b, g, r = self.__cv_image[x, y]

                rr = self.__normalize(r + (depth * 2))
                gg = self.__normalize(g + depth)
                if rr <= ((depth * 2) - 1):
                    rr = 255
                if gg <= depth - 1:
                    gg = 255

                self.__cv_image.itemset((x, y, 2,), rr)
                self.__cv_image.itemset((x, y, 1,), gg)
                self.__cv_image.itemset((x, y, 0,), b)

    def __color_oil_filter(self):
        radius = 7

        dic_freq_r, dic_freq_g, dic_freq_b = dict(), dict(), dict()

        for x in range(self.height):
            aux_x = x + radius
            for y in range(self.width):
                aux_y = y + radius

                max_r, max_g, max_b = float('inf'), float('inf'), float('inf')

                for k in range(x, aux_x):
                    if k >= self.height:
                        break
                    for l in range(y, aux_y):
                        if l >= self.width:
                            break
                        b, g, r = self.__cv_image[k, l]

                        if max_r == float('inf'):
                            max_r, max_g, max_b = r, g, b

                        if r in dic_freq_r:
                            dic_freq_r[r] += 1
                            max_r = max_r if dic_freq_r[
                                max_r] > dic_freq_r[r] else r
                        else:
                            dic_freq_r[r] = 1

                        if g in dic_freq_g:
                            dic_freq_g[g] += 1
                            max_g = max_g if dic_freq_g[
                                max_g] > dic_freq_g[g] else g
                        else:
                            dic_freq_g[g] = 1

                        if b in dic_freq_b:
                            dic_freq_r[b] += 1
                            max_b = max_b if dic_freq_b[
                                max_b] > dic_freq_b[b] else b
                        else:
                            dic_freq_r[b] = 1

                dic_freq_r.clear()
                dic_freq_g.clear()
                dic_freq_b.clear()

                self.__cv_image.itemset((x, y, 2,), max_r)
                self.__cv_image.itemset((x, y, 1,), max_g)
                self.__cv_image.itemset((x, y, 0,), max_b)

    def __gray_scale(self):
        for x in range(self.height):
            for y in range(self.width):
                b, g, r = self.__cv_image[x, y]
                gray = (r * 0.29) + (g * 0.59) + (b * 0.12)

                self.__cv_image.itemset((x, y, 2,), gray)
                self.__cv_image.itemset((x, y, 1,), gray)
                self.__cv_image.itemset((x, y, 0,), gray)

    def __gray_oil_filter(self):
        self.__color_oil_filter()
        self.__gray_scale()


class Input_Parser(object):

    def __init__(self, filter_):
        self.filter_ = filter_
        self.sepia_arg = -1
        self.__parse_input()

    def __parse_input(self):
        if self.filter_ == Filter.SEPIA:
            message = 'Ingresa la la profundidad para el sepia: [0, 255]\n'
            opt = int(input(message))
            self.sepia_arg = opt


def parse_filter_id(id):
    return {
        '0': Filter.SEPIA,
        '1': Filter.COLOR_OIL,
        '2': Filter.GRAY_TONE_OIL,
    }[id]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, help='Tipo del filtro')
    parser.add_argument('--img', type=str, help='Ruta de la foto')
    args = parser.parse_args()
    filter_id = args.filter
    image_path = args.img

    input_parser = Input_Parser(parse_filter_id(filter_id))
    image_processor = Image_Processor(
        image_path, parse_filter_id(filter_id), input_parser)

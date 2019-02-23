import sys
import argparse
from enum import Enum

import cv2


def show_image_with_filter(image):
    cv2.imshow('Practica 2', image)
    print('Imagen procesada exitosamente')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class Filter(Enum):
    BLUR = 0
    MOTION_BLUR = 1
    FIND_EDGES = 2
    SHARPEN = 3
    EMBOSS = 4
    MEDIAN = 5


class Image_Processor(object):

    def __init__(self, image_path, filter_id, input_parser):
        self.__image = cv2.imread(image_path)
        self.width, self.height, _ = self.__image.shape
        self.parsed_input = input_parser
        self.__apply_filter(filter_id)

        show_image_with_filter(self.__image)

    def __apply_filter(self, filter_id):
        if filter_id == Filter.BLUR:
            self.__blur_filter()
        elif filter_id == Filter.MOTION_BLUR:
            self.__motion_blur_filter()
        elif filter_id == Filter.FIND_EDGES:
            self.__find_edges_filter()
        elif filter_id == Filter.SHARPEN:
            self.__sharpen_filter()
        elif filter_id == Filter.EMBOSS:
            opt = self.parsed_input.emboss__option
            self.__emboss_filter(-1 if opt == 0 else (0 if opt == 1 else 1))
        elif filter_id == Filter.MEDIAN:
            self.__median_filter()

    def __normalize(self, n):
        return 0 if (n < 0) else (n if (n < 256) else 255)

    def __convolution(self, matriz, factor, bias):
        w, h, tam = self.width, self.height, len(matriz)
        rad = tam // 2
        r, g, b = 0, 0, 0

        original = [[None] * (h) for _ in range(w)]
        for x in range(w):
            for y in range(h):
                original[x][y] = self.__image[x, y]

        for x in range(w):
            xi = rad - x if (x < rad) else 0
            xf = rad + w - x if ((w - x) <= rad) else tam
            for y in range(h):
                r, g, b = 0, 0, 0

                yi = rad - y if (y < rad) else 0
                yf = rad + h - y if ((h - y) <= rad) else tam

                i = int(xi)
                px = int(x - rad)
                while i < xf:
                    j = int(yi)
                    py = int(y - rad)

                    while j < yf:
                        val = matriz[i][j]
                        r += original[px + i][py + j][2] * val
                        g += original[px + i][py + j][1] * val
                        b += original[px + i][py + j][0] * val

                        j += 1
                    i += 1

                r = r * factor + bias
                g = g * factor + bias
                b = b * factor + bias

                self.__image.itemset((x, y, 2,), self.__normalize(int(r)))
                self.__image.itemset((x, y, 1,), self.__normalize(int(g)))
                self.__image.itemset((x, y, 0,), self.__normalize(int(b)))

    def __blur_filter(self):
        m = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ]
        return self.__convolution(m, 1.0 / 13.0, 0)

    def __motion_blur_filter(self):
        m = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1]
        ]
        return self.__convolution(m, 1.0 / 7.0, 0)

    def __find_edges_filter(self):
        m = [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ]
        return self.__convolution(m, 1, 0)

    def __sharpen_filter(self):
        b = [
            [-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]
        ]
        return self.__convolution(b, 1, 0)

    def __emboss_filter(self, mode):
        eH = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
        if mode < 0:
            return self.__convolution(eH, 1, 128)
        eV = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        if mode > 0:
            return self.__convolution(eV, 1, 128)
        e45 = [[-1, -1, 0], [-1, 0, 1], [0, 1, 1]]
        return self.__convolution(e45, 1, 128)

    def __median_filter(self):
        w = self.width
        h = self.height
        tam = 3
        rad = tam // 2
        r, g, b = [], [], []

        original = [[None] * (h) for _ in range(w)]
        for x in range(w):
            for y in range(h):
                original[x][y] = self.__image[x, y]

        for x in range(w):
            xi = rad - x if (x < rad) else 0
            xf = rad + w - x if ((w - x) <= rad) else tam
            for y in range(h):
                yi = rad - y if (y < rad) else 0
                yf = rad + h - y if ((h - y) <= rad) else tam

                r = [None for _ in range((xf - xi) * (yf - yi))]
                g = [None for _ in range(len(r))]
                b = [None for _ in range(len(r))]

                px = x - rad
                i = 0
                while (i + xi) < xf:
                    j = 0
                    py = y - rad
                    while (j + yi) < yf:
                        val = matriz[i][j]
                        r[j + (yf - yi) * i] = original[px +
                                                        i + xi][py + j + yi][2]
                        g[j + (yf - yi) * i] = original[px +
                                                        i + xi][py + j + yi][1]
                        b[j + (yf - yi) * i] = original[px +
                                                        i + xi][py + j + yi][0]

                        j += 1
                    i += 1

                self.__image.itemset((x, y, 2,), self.__mediana(r))
                self.__image.itemset((x, y, 1,), self.__mediana(g))
                self.__image.itemset((x, y, 0,), self.__mediana(b))

    def __median(self, x):
        xn = len(x)
        m = -1

        i = 0
        j = 0
        while i <= xn // 2:
            for k in range(i + 1, xn):
                if x[j] > x[k]:
                    j = k
            m = x[j]
            x[j] = x[i]
            x[i] = m

            i += 1
            j = 1

        if xn % 2 == 0:
            return m + x[xn // 2 - 1] // 2
        return m


class Input_Parser(object):

    def __init__(self, filter_):
        self.filter_ = filter_
        self.emboss__option = -1
        self.__parse_input()

    def __parse_input(self):
        if self.filter_ == Filter.EMBOSS:
            message = 'Ingresa la opción para el filtro emboss\n'
            message += '0 : horizontal\n1 : es a 45 grados \n2 : vertical\n'
            opt = int(input(message))
            self.emboss__option = opt


def parse_filter_id(id):
    return {
        '0': Filter.BLUR,
        '1': Filter.MOTION_BLUR,
        '2': Filter.FIND_EDGES,
        '3': Filter.SHARPEN,
        '4': Filter.EMBOSS,
        '5': Filter.MEDIAN
    }[id]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, help='Tipo del filtro')
    parser.add_argument('--img', type=str, help='Ruta de la foto')
    args = parser.parse_args()
    filter_id = args.filter
    image_path = args.img

    if filter_id and image_path:
        input_parser = Input_Parser(parse_filter_id(filter_id))
        image_processor = Image_Processor(
            image_path, parse_filter_id(filter_id), input_parser)
    else:
        print('Argumentos inválidos')
        sys.exit(-1)

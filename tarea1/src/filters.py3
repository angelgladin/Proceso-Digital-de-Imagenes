import sys
import argparse

import cv2


def show_image_with_filter(image):
    cv2.imshow('Practica 1', image)
    print('Imagen procesada exitosamente')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

class Image_Processor(object):

    def __init__(self, image_path, filter_id, input_parser):
        self.__image = cv2.imread(image_path)
        self.width, self.height, _ = self.__image.shape
        self.parsed_input = input_parser
        self.__apply_filter(filter_id)

        show_image_with_filter(self.__image)

    def __apply_filter(self, filter_id):
        if filter_id == 0:
            self.__rgb_filter(self.parsed_input.three_args)
        elif filter_id == 1:
            self.__rgb_filter_one_color('r')
        elif filter_id == 2:
            self.__rgb_filter_one_color('g')
        elif filter_id == 3:
            self.__rgb_filter_one_color('b')
        elif filter_id == 4:
            self.__brightness_filter(self.parsed_input.one_arg)
        elif filter_id == 5:
            invert = self.parsed_input.bool_one_arg
            self.__high_contrast_filter(invert)
        elif filter_id == 6:
            self.__negative_filter()
        elif filter_id == 7:
            self.__mosaic_filter(self.parsed_input.one_arg)
        elif filter_id == 8:
            self.__gray_scale()

    def __threshold_helper(self, x, delta):
        if x + delta >= 255:
            return 255
        elif x + delta <= 0:
            return 0
        else:
            return x

    def __rgb_filter(self, rgb_input):
        for x in range(self.width):
            for y in range(self.height):
                b, g, r = self.__image[x, y]

                self.__image.itemset((x, y, 2,), self.__threshold_helper(r, rgb_input[2]))
                self.__image.itemset((x, y, 1,), self.__threshold_helper(g, rgb_input[1]))
                self.__image.itemset((x, y, 0,), self.__threshold_helper(b, rgb_input[0]))

    def __rgb_filter_one_color(self, color):
        if color == 'r':
            for x in range(self.width):
                for y in range(self.height):
                    _, _, r = self.__image[x, y]

                    self.__image.itemset((x, y, 2,), r)
                    self.__image.itemset((x, y, 1,), 0)
                    self.__image.itemset((x, y, 0,), 0)

        elif color == 'g':
            for x in range(self.width):
                for y in range(self.height):
                    _, g, _ = self.__image[x, y]

                    self.__image.itemset((x, y, 2,), 0)
                    self.__image.itemset((x, y, 1,), g)
                    self.__image.itemset((x, y, 0,), 0)

        elif color == 'b':
            for x in range(self.width):
                for y in range(self.height):
                    b, _, _ = self.__image[x, y]

                    self.__image.itemset((x, y, 2,), 0)
                    self.__image.itemset((x, y, 1,), 0)
                    self.__image.itemset((x, y, 0,), b)

    def __brightness_filter(self, brightness):
        for x in range(self.width):
            for y in range(self.height):
                b, g, r = self.__image[x, y]

                self.__image.itemset((x, y, 2,), self.__threshold_helper(r, brightness))
                self.__image.itemset((x, y, 1,), self.__threshold_helper(g, brightness))
                self.__image.itemset((x, y, 0,), self.__threshold_helper(b, brightness))

    def __high_contrast_filter(self, invert):
        for x in range(self.width):
            for y in range(self.height):
                b, g, r = map(int, self.__image[x, y])
                n = int(b+g+r)/3

                if n < 128:
                    n = 255 if invert else 0
                else:
                    n = 0 if invert else 255

                self.__image.itemset((x, y, 2,), n)
                self.__image.itemset((x, y, 1,), n)
                self.__image.itemset((x, y, 0,), n)

    def __negative_filter(self):
        for x in range(self.width):
            for y in range(self.height):
                b, g, r = self.__image[x, y]

                self.__image.itemset((x, y, 2,), 255-r)
                self.__image.itemset((x, y, 1,), 255-g)
                self.__image.itemset((x, y, 0,), 255-b)

    def __mosaic_filter(self, size):
        w = self.width
        h = self.height
        x, y, r, g, b, m, n = 0, 0, 0, 0, 0, 0, 0
        while x < w:
            m = size if (x + size) < w else w-x
            while y < h:
                n = size if (y + size) < h else h-y
                for i in range(m):
                    for j in range(n):
                        b, g, r = self.__image[i+x, j+y]
                r /= (m*n)
                g /= (m*n)
                b /= (m*n)
                for i in range(m):
                    for j in range(n):
                        self.__image.itemset((i+x, j+y, 2,), r)
                        self.__image.itemset((i+x, j+y, 1,), g)
                        self.__image.itemset((i+x, j+y, 0,), b)
                y += n
                r, g, b = 0, 0, 0
            x += m
            y = 0

    def __gray_scale(self):
        for x in range(self.width):
            for y in range(self.height):
                b, g, r = self.__image[x, y]
                gray = (r*0.29)+(g*0.59)+(b*0.12)

                self.__image.itemset((x, y, 2,), gray)
                self.__image.itemset((x, y, 1,), gray)
                self.__image.itemset((x, y, 0,), gray)


class Input_Parser(object):

    def __init__(self, filter_id):
        self.filter_id = filter_id
        self.one_arg = None
        self.three_args = None
        self.bool_one_arg = None

        if filter_id == 0:
            r = self.__parse_input('color_r')
            g = self.__parse_input('color_b')
            b = self.__parse_input('color_g')
            self.three_args = [r, g, b]
        elif filter_id == 4:
            self.one_arg = self.__parse_input('brightness')
        elif filter_id == 5:
            ans = input("¿Deseas el modo inverso del alto contraste? (y/n): ")
            self.bool_one_arg = True if "y" == ans else False
        elif filter_id == 7:
            ans = int(input("Indica la cantidad de pixeles por cada mosaico: "))
            self.one_arg = ans

    def __parse_input(self, content='nil'):
        message = 'Ingresa un valor contenido entre [-255, 255]'
        if content == 'brightness':
            message += ' para el brillo'
        elif content == 'color_r':
            message += ' para el color rojo'
        elif content == 'color_b':
            message += ' para el color azul'
        elif content == 'color_g':
            message += ' para el color verde'
        message += ': '

        n = int(input(message))
        if n >= 255:
            return 255
        elif n <= 0:
            return 0
        else:
            return n


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, help='Tipo del filtro')
    parser.add_argument('--img', type=str, help='Ruta de la foto')
    args = parser.parse_args()
    filter_id = args.filter
    image_path = args.img

    if filter_id and image_path:
        input_parser = Input_Parser(int(filter_id))
        image_processor = Image_Processor(image_path, int(filter_id), input_parser)
    else:
        print('Argumentos inválidos')
        sys.exit(-1)
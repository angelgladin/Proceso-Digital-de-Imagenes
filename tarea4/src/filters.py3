import sys
import argparse

import cv2


def show_image_with_filter(image):
    cv2.imshow('Practica 4', image)
    print('Imagen procesada exitosamente')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class Image_Processor(object):

    def __init__(self, image_path):
        self.__image = cv2.imread(image_path)
        self.height, self.width, _ = self.__image.shape
        self.__remove_watermark()

        show_image_with_filter(self.__image)

    def __remove_watermark(self):
        rgb_watermark = (235, 175, 185,)
        for x in range(self.height):
            for y in range(self.width):
                b, g, r = self.__image[x, y]
                if r>g+15 and r>b+15:
                    diff_r, diff_g, diff_b = rgb_watermark[0]-r, rgb_watermark[1]-g, rgb_watermark[2]-b
                    avg = self.__normalize((diff_r+diff_g+diff_b)//3)
                    if avg<25:
                        r=g=b=255
                    elif avg >103:
                        r=g=b=0
                    else:
                        r=g=b=((r+g+b)//3)
                self.__image.itemset((x, y, 2,), r)
                self.__image.itemset((x, y, 1,), g)
                self.__image.itemset((x, y, 0,), b)

    def __normalize(self, n):
        return 0 if (n < 0) else (n if (n < 256) else 255)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type=str, help='Ruta de la foto')
    args = parser.parse_args()
    image_path = args.img

    if image_path:
        image_processor = Image_Processor(image_path)
    else:
        print('Argumentos inválidos')
        sys.exit(-1)

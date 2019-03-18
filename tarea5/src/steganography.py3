import sys
import argparse
from enum import Enum

import cv2


class Steganography(Enum):
    HIDE_TEXT = 1
    REVEAL_TEXT = 2


class Image_Processor(object):

    def __init__(self, image_path, mode_id, txt_path):
        self.__cv_image = cv2.imread(image_path)
        self.height, self.width, _ = self.__cv_image.shape
        self.txt_path = txt_path

        self.__apply_steganography(mode_id)

    def __txt_file_to_str(self, txt_path):
        f = open(txt_path, 'r')
        return f.read()

    def __str_to_binary_str(self, x):
        return ''.join(map(lambda i: bin(ord(i))[2:].zfill(8), x))

    def __apply_steganography(self, mode_id):
        if mode_id == Steganography.HIDE_TEXT:
            msg = self.__txt_file_to_str(self.txt_path)
            msg_bin_str = self.__str_to_binary_str(msg)

            self.__cipher_hiding_text(msg_bin_str)

            print('Texto cifrado en imagen satisfactoriamente')
        elif mode_id == Steganography.REVEAL_TEXT:
            msg = self.__reveal_text()

            print('Mensaje revelado satisfactoriamente')
            print(msg)

    def __cipher_hiding_text(self, bin_msg):
        c = 0
        l = len(bin_msg)
        for x in range(self.height):
            for y in range(self.width):
                b, g, r = self.__cv_image[x, y]

                r_bin_l = list('{0:b}'.format(r))
                g_bin_l = list('{0:b}'.format(g))
                b_bin_l = list('{0:b}'.format(b))

                if c < l:
                    if c < l:
                        r_bin_l[-1] = bin_msg[c]
                        c += 1
                    if c < l:
                        g_bin_l[-1] = bin_msg[c]
                        c += 1
                    if c < l:
                        b_bin_l[-1] = bin_msg[c]
                        c += 1
                else:
                    r_bin_l[-1], g_bin_l[-1], b_bin_l[-1] = '1', '1', '1'

                new_r = int(''.join(r_bin_l), 2)
                new_g = int(''.join(g_bin_l), 2)
                new_b = int(''.join(b_bin_l), 2)

                self.__cv_image.itemset((x, y, 2,), new_r)
                self.__cv_image.itemset((x, y, 1,), new_g)
                self.__cv_image.itemset((x, y, 0,), new_b)

        cv2.imwrite('../output/{}.png'.format('secret'),
                    self.__cv_image, [cv2.IMWRITE_PNG_COMPRESSION, 9])

    def __reveal_text(self):
        bin_msg = ''
        for x in range(self.height):
            for y in range(self.width):
                b, g, r = self.__cv_image[x, y]

                r_bin_l = list('{0:b}'.format(r))
                g_bin_l = list('{0:b}'.format(g))
                b_bin_l = list('{0:b}'.format(b))

                bin_msg += r_bin_l[-1] + g_bin_l[-1] + b_bin_l[-1]

        msg = ''
        delimiter = str(bin((1 << 8) - 1))[2:]
        for i in range(0, len(bin_msg), 8):
            aux = bin_msg[i:i + 8]
            if aux == delimiter:
                break
            else:
                msg += chr(int(aux, 2))

        return msg


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, help='Modo de ejecución')
    parser.add_argument('--img', type=str, help='Ruta de la foto')
    parser.add_argument('--txt', type=str, help='Ruta del texto')
    args = parser.parse_args()
    mode_arg = args.mode
    image_path_arg = args.img
    txt_path_arg = args.txt

    mode_id = Steganography.REVEAL_TEXT
    if mode_arg == '1':
        mode_id = Steganography.HIDE_TEXT

    image_processor = Image_Processor(image_path_arg, mode_id, txt_path_arg)

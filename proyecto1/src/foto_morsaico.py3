import argparse
import math
import uuid
import cv2

DELIMITER = '###'


class PhotoMorsaic:

    def __init__(self, img_path, idx_path):
        self.__cv_img = cv2.imread(img_path)
        self.__img_width, self.__img_height, _ = self.__cv_img.shape

        self.__idx_file_path = idx_path

        self.__html_file_name = str(uuid.uuid4())[:8]

        self.mosaic_size = 15

    def __look_up_img(self, rgb_tuple):
        r_file_path = ''
        r, g, b = rgb_tuple
        min_dif = math.inf

        with open(self.__idx_file_path, 'r') as idx_file:
            for line in idx_file:
                #r_avg, g_avg, b_avg, img_path = line.split(f'{DELIMITER}')
                line = line.split(f'{DELIMITER}')
                img_path = line[-1]
                r_avg, g_avg, b_avg = [int(x) for x in line[:-1]]

                delta = math.sqrt(pow(r - r_avg, 2)
                                  + pow(g - g_avg, 2)
                                  + pow(b - b_avg, 2))

                if delta < min_dif:
                    min_dif = delta
                    r_file_path = img_path

        return r_file_path

    def generate_html(self):
        output_html_file = open(f'../output/{self.__html_file_name}.html', 'w')

        style_html = '''<style>table {transform: rotate(90deg);}</style>'''
        start_html_tags = '<table id=\"table\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">\n<tr>'

        output_html_file.write(style_html)
        output_html_file.write(start_html_tags)

        imgs_list = list()
        r, g, b, avg, r_avg, g_avg, b_avg = 0, 0, 0, 0, 0, 0, 0

        for i in range(0, self.__img_width, self.mosaic_size):
            end_x = i + self.mosaic_size
            imgs_list_tmp = list()

            for j in range(0, self.__img_height, self.mosaic_size):
                end_y = j + self.mosaic_size

                for k in range(i, end_x):
                    if k >= self.__img_width:
                        break
                    for l in range(j, end_y):
                        if l >= self.__img_height:
                            break
                        b, g, r = self.__cv_img[k, l]
                        r_avg += r
                        g_avg += g
                        b_avg += b

                        avg += 1

                r = r_avg // avg
                g = g_avg // avg
                b = b_avg // avg

                r_avg, g_avg, b_avg, avg = 0, 0, 0, 0

                img_looked_up = self.__look_up_img((r, b, g,))
                line = f'<td><img src=\"{img_looked_up}\" width=\"10\", height=\"10\"></td>\n'
                imgs_list_tmp.append(line)

            imgs_list.append(imgs_list_tmp)

        for i in range(len(imgs_list[0])):
            for x in imgs_list:
                if i >= len(x):
                    break
                output_html_file.write(x[i])
            line = '</tr><tr>\n'
            output_html_file.write(line)

        line = '</tr>\n</table></center>'
        output_html_file.write(line)

        output_html_file.close()

        print(
            f'Se creo el HTML satifactoriamente en ../output/{self.__html_file_name}.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type=str,
                        help='Ruta de la imagen que se le aplicará el filtro')
    parser.add_argument('--idx', type=str,
                        help='Ruta de el archivo con las fotos indexadas')
    args = parser.parse_args()

    img_path_arg = args.img
    idx_path_arg = args.idx

    photo_morsaic = PhotoMorsaic(img_path_arg, idx_path_arg)
    photo_morsaic.generate_html()

import os
import argparse
import cv2

IDX_FILE_NAME = 'img_averages'
DELIMITER = '###'


def average_rgb_from_image(dir_path, photo_path):
    cv_image = cv2.imread(dir_path + '/' + photo_path)
    img_height, img_width, _ = cv_image.shape

    r_avg, g_avg, b_avg = 0, 0, 0
    for x in range(img_height):
        for y in range(img_width):
            b, g, r = cv_image[x, y]
            r_avg += r
            g_avg += g
            b_avg += b

    t = img_height * img_width
    return (r_avg // t, g_avg // t, b_avg // t)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str,
                        help='Ruta de la galería de imágenes')
    args = parser.parse_args()

    dir_path = args.dir
    tmp_path = '../tmp'

    image_exts = set(['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG'])

    avegares_file = open(f'{tmp_path}/{IDX_FILE_NAME}.idx', 'w')

    for image in os.listdir(dir_path):
        img_ext = os.path.splitext(image)[-1][1:]
        if img_ext in image_exts:
            (r_avg, g_avg, b_avg) = average_rgb_from_image(dir_path, image)
            img_path = '../tmp/imgs/' + image
            s = f'{r_avg}{DELIMITER}{g_avg}{DELIMITER}{b_avg}{DELIMITER}{img_path}\n'
            avegares_file.write(s)

    print('Se creo satisfactoriamente el archivo que indexa la imágenes :D')

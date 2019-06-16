import os
import argparse
import cv2

DEFAULT_THUMBNAIL_IMG_SIZE = (100, 100,)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str,
                        help='Ruta de la galería de imágenes')
    args = parser.parse_args()

    dir_path = args.dir
    tmp_path = '../tmp/imgs/'

    image_exts = set(['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG'])
    i = 0
    for image in os.listdir(dir_path):
        img_ext = os.path.splitext(image)[-1][1:]
        if img_ext in image_exts:
            cv_img = cv2.imread(f'{dir_path}/{image}')
            aux = cv2.resize(cv_img, DEFAULT_THUMBNAIL_IMG_SIZE,
                             interpolation=cv2.INTER_AREA)
            cv2.imwrite(f'{tmp_path}/tmp_{str(i)}.{img_ext}', aux)
            i += 1

    print('Imágenes comprimidas satisfactoriamente :D')

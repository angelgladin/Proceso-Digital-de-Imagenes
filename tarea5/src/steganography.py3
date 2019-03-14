import sys
import argparse
from enum import Enum

import cv2

class Steganography(Enum):
    HIDE_TEXT = 0
    REVEAL_TEXT = 1

if __name__ == '__main__':
    print('foo')
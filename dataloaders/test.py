
import random

from PIL import Image
from scipy import ndimage
import numpy as np
import torch
import torchvision.transforms.functional as tr_F

class TestCall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("self.name: %s. " % self.name, end='   ')
        print('__call__()  is  running ')

class RandomMirror(object):
    """
    Randomly filp the images/masks horizontally
    """
    def __call__(self, sample):
        img, label = sample['image'], sample['label']
        inst, scribble = sample['inst'], sample['scribble']

        if random.random() < 0.5:

            '''
            # transpose：矩阵的转置，行和列换位置
            # 1.transpose有这么几种模式
            FLIP_LEFT_RIGHT ，FLIP_TOP_BOTTOM ，ROTATE_90 ，ROTATE_180 ，ROTATE_270，TRANSPOSE ，TRANSVERSE
            使用FLIP_LEFT_RIGHT相当于左右镜像图像;FLIP_TOP_BOTTOM相当于上下镜像图像;ROTATE_90逆时针旋转90度TRANSPOSE像素矩阵转置
            '''
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            '''
            isinstance() 与 type() 区别：   
            type() 不会认为子类是一种父类类型，不考虑继承关系。
            isinstance() 会认为子类是一种父类类型，考虑继承关系。
            '''
            if isinstance(label, dict):
                label = {catId: x.transpose(Image.FLIP_LEFT_RIGHT)
                         for catId, x in label.items()}
            else:
                label = label.transpose(Image.FLIP_LEFT_RIGHT)

            inst = inst.transpose(Image.FLIP_LEFT_RIGHT)
            scribble = scribble.transpose(Image.FLIP_LEFT_RIGHT)

        sample['image'] = img
        sample['label'] = label
        sample['inst'] = inst
        sample['scribble'] = scribble
        return sample


if __name__ == '__main__':
    call = TestCall(name='xiaoming')
    call()  # call.__call__()
    # call.__call__()

    # RandomMirror()
import torch
import sys
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torch.utils.data as data
from PIL import Image
import numpy as np
import json
import random
from xml.dom.minidom import parse 
import xml.dom.minidom
import os
category_info = {'aeroplane':0, 'bicycle':1, 'bird':2, 'boat':3, 'bottle':4,
                 'bus':5, 'car':6, 'cat':7, 'chair':8, 'cow':9,
                 'diningtable':10, 'dog':11, 'horse':12, 'motorbike':13, 'person':14,
                 'pottedplant':15, 'sheep':16, 'sofa':17, 'train':18, 'tvmonitor':19}

class Voc12Dataset(data.Dataset):
    def __init__(self, img_dir='./data/VOCdevkit/VOC2012/JPEGImages', anno_path='./data/VOCdevkit/VOC2012/Main/trainval.txt', input_transform=None, labels_path='./data/VOCdevkit/VOC2012/Annotations'):
        self.img_names  = []
        with open(anno_path, 'r') as f:
             self.img_names = f.readlines()
        self.img_dir = img_dir
        # no ground truth of voc12, just a placeholder
        self.labels = np.ones((len(self.img_names),20))
        self.input_transform = input_transform
    def __getitem__(self, index):
        name = self.img_names[index][:-1]+'.jpg'
        input = Image.open(os.path.join(self.img_dir, name)).convert('RGB')
          
        if self.input_transform:
            input = self.input_transform(input)
        return input, self.labels[index]

    def __len__(self):
        return len(self.img_names)

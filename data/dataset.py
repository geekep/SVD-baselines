# -*- coding: UTF-8 -*-
# !/user/bin/python3

import torchvision.transforms as transforms

from PIL import Image
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader


class ImageLoader(Dataset):
    def __init__(self, images_paths, transform):
        self.images_paths = images_paths
        self.transform = transform

    def __getitem__(self, index):
        img = Image.open(self.images_paths[index])
        img = img.convert('RGB')
        img = self.transform(img)
        return img, index

    def __len__(self):
        return len(self.images_paths)


def create_loader(images_paths: object, batch_size: object) -> object:
    normalize = transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
    transformation = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        normalize
    ])

    dataset = ImageLoader(images_paths, transformation)
    dataloader = DataLoader(dataset,
                            batch_size=batch_size,
                            shuffle=False,
                            num_workers=10)
    return dataloader



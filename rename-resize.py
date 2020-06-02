import cv2
import glob
import os
import PIL
from PIL import Image
import shutil


def rename(imgs, outpath):
    fnames = []
    for i, img in enumerate(imgs):
        fmt = img.split('.')[-1]
        fname = f"{outpath}/{i}.{fmt}"
        shutil.copyfile(img, fname)
        fnames.append(fname)
    return fnames


def square(img, size, fill_color=(0, 0, 0, 0)):
    x, y = img.size
    maxdim = max(x, y)
    newsize = (int(x/maxdim*size), int(y/maxdim*size))
    img = img.resize(newsize, Image.ANTIALIAS)
    new_img = Image.new('RGB', (size, size), fill_color)
    new_img.paste(img, (int((size-newsize[0])/2), int((size-newsize[1])/2)))
    return new_img


def resize(imgs):
    # Size of ImageNet input
    size = 256
    for img in imgs:
        i = Image.open(img)
        new = square(i, size)
        new.save(img)

# Settings
inpath = './images/raw'
outpath = './images/processed'

if not os.path.exists(outpath):
    os.mkdir(outpath)

if not os.path.exists(inpath):
    os.mkdir(inpath)

imgs = glob.glob(inpath + '/*')
fnames = rename(imgs, outpath)
resize(fnames)

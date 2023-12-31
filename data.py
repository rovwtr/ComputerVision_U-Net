"""data.ipynb

Automatically generated by Colaboratory.


"""

import numpy as np
import cv2
import os
from PIL import Image

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/MyDrive/Computer Vision/images'

!unzip '/content/drive/MyDrive/Computer Vision/images/data_augmented_full.zip' -d ./data_augmented_full
!unzip '/content/drive/MyDrive/Computer Vision/images/data_augmentedm_full.zip' -d ./data_augmentedm_full

#size - tuple of desired image size
# suffix 1 - rotated by 90 degrees counterclockwise
# suffix 2 - rotated by 90 degrees clockwise
# suffix 0 - not rotated

def rotate_mask(dir, size):
  for p in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, p)):
          path = os.path.join(dir, p)
          img = cv2.imread(path)
          img = cv2.resize(img, (size, size), interpolation = cv2.INTER_AREA)
          # rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

          data = np.asarray(img)
          r, g, b = data[:,:,0], data[:,:,1], data[:,:,2]
          gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
          m = np.where(gray > 128.0, 255, 0)
          new = Image.fromarray(m.astype(np.float32))
          new_path = p[:-4] + '0' + '.gif'
          _ = new.save(new_path)
          # os.remove(p)

# Commented out IPython magic to ensure Python compatibility.
dir = '/content/drive/MyDrive/Computer Vision/images/data_augmentedm_full/data_augmentedm'
# %cd /content/drive/MyDrive/Computer Vision/images/data_augmentedm_full/data_augmentedm_str
rotate_mask(dir, 256)

#rotate input image

def rotate(dir, size):
  for p in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, p)):
          path = os.path.join(dir, p)
          img = cv2.imread(path)
          img = cv2.resize(img, (size, size), interpolation = cv2.INTER_AREA)
          # rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
          filename = p[:-4] + '0' + '.jpg'
          cv2.imwrite(filename, img)

          # data = np.asarray(rotated)
          # new = Image.fromarray(data.astype(np.uint8), "RGB")
          # new_path = p[:-4] + '2' + '.jpg'
          # _ = new.save(new_path)

# Commented out IPython magic to ensure Python compatibility.
dir = '/content/drive/MyDrive/Computer Vision/images/data_augmented_full/data_augmented'
# %cd /content/drive/MyDrive/Computer Vision/images/data_augmented_full/data_augmented_str
rotate(dir, 256)

masks = []
for p in os.listdir('/content/drive/MyDrive/Computer Vision/images/data_augmentedm'):
        if os.path.isfile(os.path.join('/content/drive/MyDrive/Computer Vision/images/data_augmentedm', p)):
          path = os.path.join('/content/drive/MyDrive/Computer Vision/images/data_augmentedm', p)
          img = cv2.imread(path)
          print(p[:4])
          masks.append(np.asarray(img))


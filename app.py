import os
import cv2
import pyautogui
import matplotlib.pyplot as plt
from PIL import Image
import PIL
# model.add(layers.Dense(64, activation=opt))

image = pyautogui.screenshot()
image.save(f'{os.getcwd()}/image.jpg')








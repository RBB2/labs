#!/usr/bin/env python3

import cv2
import os
import math
import find_ball
import numpy as np


opencv_image = cv2.imread("./imgs/test01.bmp", cv2.COLOR_GRAY2RGB)
ball = find_ball.find_ball(opencv_image)
print("test01.bmp", ball)
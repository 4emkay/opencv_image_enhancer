import asyncio
import pandas as pd
import asyncio
import cv2
import json
import io
from imageio import imread
from base64 import decodebytes,b64decode
import numpy as np
import random,string
import base64
from upload import upload_file_to_bucket,upload_file_to_bucket_origninal
from PIL import Image
from PIL import Image
from io import BytesIO
from config import S3_BUCKET,SECRET_KEY
import logging
logging.getLogger('PIL').setLevel(logging.CRITICAL)

def clean_img(image_str):
        imgIn = imread(io.BytesIO(base64.b64decode(image_str)))
        N = 22
        # using random.choices()
        # generating random strings 
        res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = N))
        cv2.imwrite('image_original'+res+'.jpg',imgIn)
        original_image = upload_file_to_bucket_origninal('folder','image_original'+res+'.jpg')
        #print(imgIn)
        imgIn = cv2.cvtColor(imgIn, cv2.COLOR_BGR2GRAY)    # input()
        # imgIn = cv2.imread("oscar.jpg", cv2.IMREAD_GRAYSCALE)
        # cv2.imshow("Original", imgIn)
        # Create the identity filter, but with the 1 shifted to the right!
        kernel = np.zeros((10, 10), np.float32)
        kernel[4, 4] = 2  # Identity, times two!
        # Create a box filter:
        boxFilter = np.ones((10, 10), np.float32) / 100.0
        # Subtract the two:
        kernel = kernel - boxFilter
        custom = cv2.filter2D(imgIn, -1, kernel)
        # print(custom)
        cv2.imwrite('image'+res+'.jpg',custom)
        # image_result = open('image'+res+'.jpg', 'wb') # create a writable image and write the decoding result
        filtered_image = upload_file_to_bucket('folder','image'+res+'.jpg')
        return {'original_input':original_image,"filtered_output":filtered_image}


async def get_image(image_str):
        await asyncio.sleep(0)
        '''
        :param data:input data
        :return: score and decile
        '''

        output_list = list(map(clean_img, image_str))
        print(output_list)
        return json.dumps(output_list)
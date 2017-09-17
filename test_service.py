import numpy as np
import requests
import sys
import cv2
import json
import os

IMAGE_SIZE = 224
CHANNEL_SIZE = 3

BACKEND_URL ="http://172.19.61.250:8601/"

if len(sys.argv) < 2:
  print "usage: python readimg.py image_filename"
  exit(1)

filename = sys.argv[1] 

# Imagenet IMAGE_SIZE 228 x 228
img = cv2.imread(filename)
img.resize((IMAGE_SIZE, IMAGE_SIZE, CHANNEL_SIZE))
# mean = np.array([104, 117, 124], dtype='float32')[:, np.newaxis, np.newaxis]
img = np.swapaxes(img, 1, 2)
img = np.swapaxes(img, 1, 0)
img = img.flatten()
# img = (img - mean).flatten()
req = {"image": img.tolist()}
req = requests.request("POST", url=BACKEND_URL, json=req)

# print "response: ", json.dumps(req.json())
labelfile = "imagenet1000_clsid_to_human.txt"
label =  req.json()["data"][0]
label = np.array(label).argmax()
print label
ground_truth = {}
with open(labelfile) as f:
  for line in f:
    parts = line.rstrip("\n").split(":")
    ground_truth[int(parts[0])] = parts[1]
print ground_truth[label]

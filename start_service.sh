#!/bin/bash
wget https://s3.us-east-2.amazonaws.com/models.paddlepaddle/03.image_classification_resnet50/param.tar
wget https://s3.us-east-2.amazonaws.com/models.paddlepaddle/03.image_classification_resnet50/inference_topology.pkl
nvidia-docker run --name=my_svr -v `pwd`:/data -d -p 8000:80 -e WITH_GPU=1 paddlepaddle/book:serve-gpu

import argparse
import os
import sys
import time
import re

import torch
from torchvision import transforms
import cv2
import PIL

from custom_model import CustomModel
from vgg16 import VGG16
import utils
import base64

import numpy as np
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms

# import style_transfer.utils as utils
# from style_transfer.transformer_net import TransformerNet
# from style_transfer.vgg import Vgg16
PRESERVE_COLOR = True
def stylize(image, model_path):
    
    _, image_content = image.split(',')
    
    device = torch.device("cpu")

    # if architecture == 'VGG16':
    #     style_model = VGG16()
    #     model_path = vgg16_model_mapper[f"{make_snake_case(trained_on)}_{make_snake_case(style)}"]
        
    # else:
    #     style_model = CustomModel()
    #     model_path = custom_model_mapper[f"{make_snake_case(trained_on)}_{make_snake_case(style)}"]
    
    # content_transform = transforms.Compose([
    #     transforms.ToTensor(),
    #     transforms.Lambda(lambda x: x.mul(255))
    # ])
    if "vgg" in model_path:
        style_model = VGG16()
    else:
        style_model = CustomModel()
    
    # content_image = content_transform(content_image).unsqueeze(0).to(device)

    with torch.no_grad():
        torch.cuda.empty_cache()
        content_image = utils.load_image(image_content)
        content_tensor = utils.itot(content_image).to(device)
        # state_dict = torch.load(model_path)
                
        style_model.load_state_dict(torch.load(model_path))
        style_model.to(device)
        
        output_tensor = style_model(content_tensor).cpu()
        output_image = utils.ttoi(output_tensor.detach())

        if PRESERVE_COLOR:
            output_image = utils.transfer_color(content_image, output_image)

        # convert output_image to base64
        output_image = base64.b64encode(output_image)
        
        # image = saveimg(output)
        image = utils.saveimg(output_image, "output.jpg")
        image = utils.load_image_base64("output.jpg")
        image_tensor = utils.itot(image)
        # convert image to base64
        image_b64 = utils.save_image_base64(image_tensor[0])
    
    return image_b64


# def stylize(image_content, model, content_scale=None, cuda=False, ):
#     device = torch.device("cuda" if cuda else "cpu")

#     content_image = utils.load_image_base64(image_content, scale=content_scale)
#     content_transform = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Lambda(lambda x: x.mul(255))
#     ])
#     content_image = content_transform(content_image)
#     content_image = content_image.unsqueeze(0).to(device)

#     if model.endswith(".onnx"):
#         output = stylize_onnx_caffe2(content_image, args)
#     else:
#         with torch.no_grad():
#             style_model = TransformerNet()
#             state_dict = torch.load(model)
#             # remove saved deprecated running_* keys in InstanceNorm from the checkpoint
#             for k in list(state_dict.keys()):
#                 if re.search(r'in\d+\.running_(mean|var)$', k):
#                     del state_dict[k]
#             style_model.load_state_dict(state_dict)
#             style_model.to(device)
# #             if args.export_onnx:
# #                 assert args.export_onnx.endswith(".onnx"), "Export model file should end with .onnx"
# #                 output = torch.onnx._export(style_model, content_image, args.export_onnx).cpu()
# #             else:
#             output = style_model(content_image).cpu()
    
#     return utils.save_image(output[0])

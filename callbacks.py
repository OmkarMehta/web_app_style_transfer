import neural_style

# # dictionary to save (Name of the style, Path of the model that does style transfer)
# map_style_model_path = {'Candy':'saved_models/candy.pth',
#                         'Mosaic':'saved_models/mosaic.pth',
#                         'Rain Princess':'saved_models/rain_princess.pth',
#                         'Udnie': 'saved_models/udnie.pth'}
#### Define inference function
## VGG16 mapper
map_style_model_path = {'vgg16_coco_rain_princess': 'models/VGG16/COCO/rain_princess.pth',
                         'vgg16_coco_the_scream':  'models/VGG16/COCO/the_scream.pth',
                         'vgg16_coco_the_shipwreck':  'models/VGG16/COCO/the_shipwreck.pth',
                         'vgg16_coco_udnie':  'models/VGG16/COCO/udnie.pth',
                         'vgg16_coco_wave':  'models/VGG16/COCO/wave.pth',
                         'vgg16_tiny_imagenet_rain_princess': 'models/VGG16/TinyImagenet/rain_princess.pth',
                         'vgg16_tiny_imagenet_the_scream':  'models/VGG16/TinyImagenet/the_scream.pth',
                         'vgg16_tiny_imagenet_the_shipwreck':  'models/VGG16/TinyImagenet/the_shipwreck.pth',
                         'vgg16_tiny_imagenet_udnie':  'models/VGG16/TinyImagenet/udnie.pth',
                         'vgg16_tiny_imagenet_wave':  'models/VGG16/TinyImagenet/wave.pth',
                         'custom_coco_rain_princess': 'models/Custom/COCO/rain_princess.pth',
                         'custom_coco_the_scream':  'models/Custom/COCO/the_scream.pth',
                         'custom_coco_the_shipwreck':  'models/Custom/COCO/the_shipwreck.pth',
                         'custom_coco_udnie':  'models/Custom/COCO/udnie.pth',
                         'custom_coco_wave':  'models/Custom/COCO/wave.pth',
                         'custom_tiny_imagenet_rain_princess': 'models/Custom/TinyImagenet/rain_princess.pth',
                         'custom_tiny_imagenet_the_scream':  'models/Custom/TinyImagenet/the_scream.pth',
                         'custom_tiny_imagenet_the_shipwreck':  'models/Custom/TinyImagenet/the_shipwreck.pth',
                         'custom_tiny_imagenet_udnie':  'models/Custom/TinyImagenet/udnie.pth',
                         'custom_tiny_imagenet_wave':  'models/Custom/TinyImagenet/wave.pth'
                         }
def stylize_image(input_image_b64_str, architecture="custom", dataset="coco", style="udnie"):
    model_string = architecture + "_" + dataset + "_" + style
    model_path=map_style_model_path.get(model_string)
    image_str = neural_style.stylize(input_image_b64_str, model=model_path)
    return image_str
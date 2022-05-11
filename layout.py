import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64

from callbacks import *

theme_color_code = "#ffffff" #Indigo

image_filename = 'assets/icon.png' # Icon omage
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")

image_filename = 'assets/defaultimage.jpeg' # default image
encoded_image_default = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")

rain_princess_filename = 'assets/rain_princess.jpg' # rain princess image
encoded_rain_princess = base64.b64encode(open(rain_princess_filename, 'rb').read()).decode("utf-8")

the_scream_filename = 'assets/the_scream.jpg' # the scream image
encoded_the_scream = base64.b64encode(open(the_scream_filename, 'rb').read()).decode("utf-8")

the_shipwreck_filename = 'assets/the_shipwreck.jpg' # the shipwreck image
encoded_the_shipwreck = base64.b64encode(open(the_shipwreck_filename, 'rb').read()).decode("utf-8")

udnie_filename = 'assets/udnie.jpg' # udnie image
encoded_udnie = base64.b64encode(open(udnie_filename, 'rb').read()).decode("utf-8")

wave_filename = 'assets/wave.jpg' # wave image
encoded_wave = base64.b64encode(open(wave_filename, 'rb').read()).decode("utf-8")


# 1. Navbar placeholder (currently black row)
navbar = dbc.Row()

# 2. Mosaic icon image
icon_image = dbc.Row(
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image),
                    style={'width':'178px', 'margin-top': "5%"}),
                    justify='center'
)

meme_filename = 'assets/meme.jpeg' # meme image
encoded_meme = base64.b64encode(open(meme_filename, 'rb').read()).decode("utf-8")


### 3. Body title
body_paragraph = dbc.Row(
    [
        dbc.Col(
                [
                    html.H1(
                        "Neural Style Transfer",
                        style={'text-align':'center', "color":"black", "font-family": "Verdana; Gill Sans"}
                            ),
                    
                    html.H3(
                        "Authors: Omkar Mehta and Anurag Anand",
                        style={'text-align':'center', "color":"gray", "font-family": "Verdana; Gill Sans"}
                            ),

                    html.Br(),
                    html.H5(
                        "Apply styles from well-known pieces of art to your own photos",
                        style={'text-align':'center', "color":"darkgray", "font-family": "Verdana; Gill Sans"}
                            )
                ],
                style ={"padding":"1% 1% 3% 0%", "background-color":theme_color_code}
               )
    ],
    style = {'text-align':'center', "padding":"1% 1% 1% 0%", "background-color":theme_color_code}
)

### 3.1. dbc row for rain princess image, the scream image, the shipwreck image, udnie image, wave image in one row
body_images = dbc.Row(
    [dbc.Col(
        [html.Img(src='data:image/png;base64,{}'.format(encoded_rain_princess),
                style={'width':'100%', 'margin-top': "1%"}),]),
    dbc.Col(
        [html.Img(src='data:image/png;base64,{}'.format(encoded_the_scream),
                style={'width':'100%', 'margin-top': "1%"}),]),
    dbc.Col(
        [html.Img(src='data:image/png;base64,{}'.format(encoded_the_shipwreck),
                style={'width':'100%', 'margin-top': "1%"}),]),
    dbc.Col(
        [html.Img(src='data:image/png;base64,{}'.format(encoded_udnie),             
                style={'width':'100%', 'margin-top': "1%"}),]),
    dbc.Col(
        [html.Img(src='data:image/png;base64,{}'.format(encoded_wave),
                style={'width':'100%', 'margin-top': "1%"}),]),]
    ,style ={"padding":"1% 1% 1% 0%", "background-color":theme_color_code}
)


### 3.2. Meme image placeholder
meme_image = dbc.Row(
    html.Img(src='data:image/png;base64,{}'.format(encoded_meme),
    style={'width':'50%', 'margin-top': "10%"}),
    justify='center'
)

### 4. Github logo
github_logo = dbc.Row(
            html.A(
                html.I(className = "fa-2x fab fa-github", style={'color':'#000000'}),
                href = "https://github.com/OmkarMehta/web_app_style_transfer", target="_blank",
                className="mr-3"
        ),
        justify='center'
)

### 5. Upload button
upload_button = dbc.Col(
    [
        dcc.Upload(id='upload-image',
                   children = dbc.Col(
                       [
                           'Click to upload an image'
                       ]
                   ),
                   style={
                       'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                   }
            ),
        ]
)
        
### 6. Dropdown for selecting style
style_dropdown = dbc.Row(
    [
        dbc.Col(
            [
                html.P(html.B("Select an architecture")),
                dcc.Dropdown(
                    id='passage_dropdown_architecture',
                    options=[{'label':key, 'value' : value} for key, value in ({"Custom": "custom", "VGG16": "vgg16"}).items()],
                    placeholder = 'Architecture',
                    value='custom'
            ), 
            html.P(html.B("Select a dataset")),
            dcc.Dropdown(
                    id='passage_dropdown_dataset',
                    options=[{'label':key, 'value' : value} for key, value in ({"COCO": "coco", "Tiny ImageNet": "tiny_imagenet"}).items()],
                    placeholder = 'Dataset',
                    value='coco'
            ),
            html.P(html.B("Select a style")),
            dcc.Dropdown(
                    id='passage_dropdown_style',
                    options=[{'label':key, 'value' : value} for key, value in ({"Rain Princess": "rain_princess", "The Scream": "the_scream", "The Shipwreck": "the_shipwreck", "Udnie": "udnie", "Wave": "wave"}).items()],
                    placeholder = 'Style',
                    value='udnie'
            )
            ]
        )
    ]
)


### 7. Display original and processed images
images = dbc.Row(
    [
        dbc.Col(dbc.CardImg(id='original-image', src='data:image/png;base64,{}'.format(encoded_image_default)), 
                                                    style = {"padding" : "2% 1% 1% 2%", 
                                                            'lineHeight': '60px',
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'margin': '10px'}),
        dbc.Col(dbc.CardImg(id='processed-image'), style = {"padding" : "2% 1% 1% 2%", 
                                                            'lineHeight': '60px',   
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'margin': '10px'})
    ]
)

### 8. Footer
footer = dbc.Row(
    dbc.Col(
        html.Div(
        [
            'Transferring styles from one image to another is a powerful way to create new artworks.',
        'This work is higly inspired by the work of ',
        html.A("Gatys et al.", 
                href = "https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf",
                target = "_blank"),
        'and this web application is built using ',
        html.A("Fast Dash",
                href = "https://pypi.org/project/fast-dash/",
                target = "_blank")
        ],
    ),
    width={"size": 10}
), 
    justify='center',
    align='center',
    style={'margin-bottom': "10%"}
)

### Bring it together
top = dbc.Container(
    [
        dcc.Store(id='memory-output', storage_type='memory'),
        navbar,
        icon_image,
        body_paragraph,
        body_images,
        meme_image,
        github_logo
    ],
    fluid = False
)

middle = dbc.Container(
    [
        upload_button,
        style_dropdown,
        images
    ],
    fluid = False
)

bottom = dbc.Container(
    [   
        footer
    ],
    fluid = False
)

layout = dbc.Container(
    [
        top, 
        middle,
        bottom
    ]
)
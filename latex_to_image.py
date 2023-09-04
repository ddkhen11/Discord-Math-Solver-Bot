import requests
from PIL import Image
from io import BytesIO
from add_white_background import add_white_background

def latex_to_image(latex_code):
    latex_code = latex_code.replace(" ", "")
    payload = {
        'formula': latex_code,
        'fsize': 30,
        'fcolor': '000000',
        'mode': 0,
        'out': 1,
        'preamble': r'\usepackage{amsmath}\usepackage{amsfonts}\usepackage{amssymb}',
        'remhost': 'quicklatex.com',
        'rnd': 50
    }
    api_url = 'https://quicklatex.com/latex3.f'
    response = requests.post(api_url, data=payload)
    response.raise_for_status()

    api_output = response.text.split('\n')
    image_url = api_output[-1].split()[0]

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    img_with_background = add_white_background(img)

    buffer = BytesIO()
    img_with_background.save(buffer, format="PNG")

    return buffer.getvalue()
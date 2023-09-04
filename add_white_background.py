from PIL import Image

def add_white_background(img):
    img_w, img_h = img.size
    background = Image.new("RGBA", (img_w, img_h), "white")
    img = Image.alpha_composite(background, img)
    return img
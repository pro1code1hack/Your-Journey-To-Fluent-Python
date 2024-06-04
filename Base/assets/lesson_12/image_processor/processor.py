from PIL import Image

def open_image(path):
    """Open and return an image."""
    return Image.open(path)

def show_image(image):
    """Display the image."""
    image.show()

def rotate_image(image, degrees):
    """Rotate the image by a certain number of degrees."""
    return image.rotate(degrees)

def crop_image(image, box):
    """Crop the image to a specific box and return the cropped image."""
    return image.crop(box)
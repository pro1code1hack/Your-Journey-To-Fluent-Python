from processor import open_image, show_image, rotate_image, crop_image

def main():
    image_path = input("Enter the path to the image: ")
    image = open_image(image_path)
    show_image(image)

    rotated = rotate_image(image, 90)
    show_image(rotated)

    cropped = crop_image(image, (100, 100, 400, 400))
    show_image(cropped)

if __name__ == "__main__":
    main()
from PIL import Image


def resize_img(size1, size2):
    image = Image.open('img.jpeg')

    print(f"Image Size : {image.size}")

    new_img_size = image.resize((size1, size2))

    new_img_size.save('img.jpeg')

size1 = int(input("Width: "))
size2 = int(input("Length: "))
resize_img(size1, size2)
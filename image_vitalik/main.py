from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


with Image.open('Images/11.jpg') as pic_original:
    print(f"Розмір: {pic_original.size}\nФормат: {pic_original.format}")

    # Зображення gray
    pic_gray = pic_original.convert('L')
    pic_gray.save('Images/grey.jpg')

    # Зображення blur
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('Images/blur.jpg')

    # Зображення поворот на 90 градусів
    pic_90 = pic_original.transpose(Image.ROTATE_90)
    pic_90.save('Images/rotate90.jpg')

    # Зображення відзеркалене
    pic_mirror = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirror.save('Images/mirror.jpg')
    
    # Зображення контраст
    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('Images/contr.jpg')
    pic_contrast.show()
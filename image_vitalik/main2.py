from PIL import ImageFilter
from PIL import Image

class ImageEditor():
    # Конструктор
    def __init__(self, filename):
        self.filename = filename # Ім'я файлу зображення
        self.original = None # Оригінальний файл зображення
        self.changed = [] # Список для збереження змінених зображень

    # Функція відкриття файлу зображення

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Файл не знайдено")
        
        self.original.show()
    
    def do_left(self):

        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        rotated.save('Images/left.jpg')
        rotated.show()
    
    def do_cropped(self):
        box = (250, 100, 600, 400)

        cropped = self.original.crop(box)
        self.changed.append(cropped)
        cropped.save('Images/crop.jpg')

        cropped.show()

MyImage = ImageEditor('Images/11.jpg')

MyImage.open()
MyImage.do_left()
MyImage.do_cropped()
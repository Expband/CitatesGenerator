from PIL import Image, ImageDraw, ImageFont


class Text_operator:

    def __init__(self):
        self.__font_path: str = 'Comfortaa.ttf'
        self.__font_size = None

    def get_text_size(self, text: str):
        try:
            image = Image.new("RGB", (1, 1))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(self.__font_path, self.__font_size)
            _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
            return width, height
        except Exception as ex:
            return ex

    def set_font_path(self, font_path):
        self.__font_path = font_path


    def set_font_size(self, font_size):
        self.__font_size = font_size

    def return_font_path(self):
        return self.__font_path

    def return_font_size(self):
        return self.__font_size

from PIL import Image, ImageFont, ImageDraw


class Image_operator:

    def __init__(self, text_operator):
        self.__image_path = None
        self.__save_path = None
        self.__image = None
        self.__x, self.__y, self.__interval = None, None, None
        self.text_operator = text_operator

    def image_open(self) -> Image:
        self.__image = Image.open(self.__image_path)

    def save_image(self) -> None:
        self.__image.save('output.jpg')

    def add_text_to_image(self, text_to_add: list) -> None:
        font = ImageFont.truetype(self.text_operator.return_font_path(), self.text_operator.return_font_size())
        draw = ImageDraw.Draw(self.__image)
        for element in text_to_add:
            width, height = self.text_operator.get_text_size(text=element)
            self.__y += self.__interval
            image_center = self.get_image_center(self.__image)
            self.__x = image_center - width / 2
            text_position = (self.__x, self.__y)  # text position
            draw.text(text_position, element, font=font, fill=(233, 202, 28))  # adding text
        self.__image = self.__image

    def set_image_path(self, image_path) -> None:
        self.__image_path = image_path

    def set_text_location(self, x: int = 0, y: int = 0, interval: int = 0):
        self.__x, self.__y, self.__interval = x, y, interval

    def return_image_path(self) -> str:
        return self.__image_path

    @staticmethod
    def get_image_center(image) -> int:
        """
        :param image: type image. Image object
        :return: midl of image
        """
        width = image.width
        return width // 2

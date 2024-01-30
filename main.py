from ImageOperator import Image_operator
from Wrapper import Text_wrapper as wrapper
from TextOperator import Text_operator

text_operator = Text_operator()
image_operator = Image_operator(text_operator=text_operator)



if __name__ == "__main__":
    image_operator.set_image_path('1.jpg')
    image_operator.image_open()
    text_operator.set_font_path('Comfortaa.ttf')
    text_operator.set_font_size(45)
    image_operator.set_text_location(y=200, interval=65)
    text_to_add = 'Я не дам тебя забрать. Теперь ты моя заложница. Подопытная для моих экспериментов.'
    text_to_add = wrapper.text_wrapper(raw_string=text_to_add, max_length=30)
    image_operator.add_text_to_image(text_to_add)
    text_operator.set_font_size(60)
    image_operator.set_text_location(y=675)
    text_to_add = '© '+'Врата Штейна'
    text_to_add = wrapper.text_wrapper(raw_string=text_to_add, max_length=20)
    image_operator.add_text_to_image(text_to_add)
    image_operator.save_image()

import textwrap


class Text_wrapper:
    @staticmethod
    def text_wrapper(raw_string: str, max_length: int) -> list:
        """
        :param raw_string: type str. Wraps text in string format into wrapped text list
        :param max_length: type int. Max length for every wrap
        :return: list of wrapped text
        """
        text_wrap_list = textwrap.wrap(text=raw_string, width=max_length)
        return text_wrap_list

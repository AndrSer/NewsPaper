from django import template
import re

register = template.Library()

stop_list_words = ['редиска', 'дурак', 'идиот', 'Редиска', 'редиски', 'Редиски']


@register.filter()
def censor(input_value: str):
    for stop_word in stop_list_words:
        while stop_word in input_value:
            finder = re.search(stop_word, input_value)
            future_stars_string = input_value[finder.start():finder.end()]
            stars_string = '*' * len(future_stars_string[1:len(future_stars_string) - 1])
            replace_string = future_stars_string.replace(future_stars_string[1:len(future_stars_string) - 1],
                                                         stars_string)
            input_value = input_value.replace(future_stars_string, replace_string)
    return input_value

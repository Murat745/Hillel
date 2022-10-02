"""
Lesson 8, homework 6, task 6 solution
Creating a func to permute letters in the text words.
"""

import random


def permuted(texts):
    text_final = []
    texts = texts.split()

    for text in texts:
        text_list = []
        for sign in text:
            text_list.append(sign)

        first_sign = text_list[0]
        last_sign = text_list[len(text_list) - 1]

        del text_list[0]
        del text_list[len(text_list) - 1]

        random.shuffle(text_list)
        text_list = ''.join(text_list)
        ok_text = first_sign + text_list + last_sign
        text_final.append(ok_text)
    return ' '.join(text_final)


print(permuted('ivan muratov learns python'))  # iavn maruotv lneras poythn

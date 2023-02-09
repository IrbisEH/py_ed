import random
from tkinter import *
import string
import tkinter

# # creating a window
# window = Tk()
# window.title('PasswordGenerator')
# window.geometry('500x500')
#
# Label(window, font=('bold', 10), text='PASSWORD GENERATOR').pack()
#
# ALPHABET = ''


ASCII_UP_CHARS = [66, 91]
ASCII_LOW_CHARS = [97, 123]
ASCII_SPEC_CHARS = [33, 48]

ASCII_SEGMENTS_DIC = {
    1: ASCII_UP_CHARS,
    2: ASCII_LOW_CHARS,
    3: ASCII_SPEC_CHARS
}


APP_CONFIG = {
    'password_length': None,
    'valid_chars_seg': None
}


# User input
def get_password_length():
    print('Введите количество символов в пароле.')
    password_length = input('> ')
    if not password_length.isdigit():
        print('Невалидный ввод! Укажите число!')
        exit()
    return int(password_length)


def get_valid_ascii_num_segment():
    print('Укажите номера наборов из символов которых будет создан пароль?')
    print(f'1: {[chr(i) for i in range(*ASCII_UP_CHARS)]}')
    print(f'2: {[chr(i) for i in range(*ASCII_LOW_CHARS)]}')
    print(f'3: {[chr(i) for i in range(*ASCII_SPEC_CHARS)]}')
    input_segments = input('> ')

    valid_num_segments = []
    for char in input_segments:
        if char.isdigit() and 0 < int(char) < 4:
            valid_num_segments.append(char)
        else:
            print('Невалидный ввод!')
            exit()
    return list(map(int, list(set(valid_num_segments))))


def get_random_password(length, segments):
    available_chars = []
    for segment in segments:
        available_chars += [chr(i) for i in range(*ASCII_SEGMENTS_DIC[segment])]

    password = ''.join(random.sample(available_chars, length))

    return password


if __name__ == '__main__':
    password_length = get_password_length()
    valid_num_segments = get_valid_ascii_num_segment()
    password = get_random_password(password_length, valid_num_segments)
    print(password)
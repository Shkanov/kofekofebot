
# -*- coding: utf-8 -*-
# Этот токен невалидный, можете даже не пробовать :)
import telebot


from enum import Enum

token = '481157255:AAGM3_W6cLZaTWNXqQ3f15URKmeRzRzCM0s'
db_file = "database.vdb"



class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_KOFE = "2"
    S_SET_PAYMENT = "3"
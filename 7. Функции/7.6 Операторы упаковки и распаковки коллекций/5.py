import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

menu = {**menu, **dict([i.split("=") for i in lst_in])}

from random import randint
from PIL import Image, ImageDraw, ImageFont

from dnd_class import CLASES
from background import TRASFONDOS
from species import RAZAS

import random

def _get_stats():
    setStats = []
    while len(setStats) <= 5:
        list_amount = []
        while len(list_amount) <= 3:
            list_amount.append(randint(1,6))
        list_amount.sort(reverse=True)
        list_amount.pop()
        setStats.append(sum(list_amount))
    return setStats

def _get_3_setStats():
    list_stats = []
    while len(list_stats) <= 2:
        list_stats.append(_get_stats())
    return list_stats

def _get_clases():
    main_class = random.choice(list(CLASES.keys()))
    sub_class = random.choice(CLASES[main_class])
    return main_class, sub_class

def _get_tranfondos():
    return random.choice(TRASFONDOS)

def _get_raza():
    return random.choice(RAZAS)

def main():
    main_class, sub_class = _get_clases()
    list_stast = _get_3_setStats()
    text = f"Estadisticas: \n{list_stast[0]} \n{list_stast[1]} \n{list_stast[2]} \n" + \
    f"Clase: {main_class}\n" + \
    f"Sub Clase: {sub_class}\n" + \
    f"Trasfondos: {_get_tranfondos()}\n" + \
    f"Raza: {_get_raza()}"

    print(text)

if __name__ == '__main__':
    main()
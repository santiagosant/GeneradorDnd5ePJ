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
    return random.choice(CLASES)

def _get_tranfondos():
    return random.choice(TRASFONDOS)

def _get_raza():
    return random.choice(RAZAS)

def main():
    list_stast = _get_3_setStats()
    text = f"Estadisticas: \n{list_stast[0]} \n{list_stast[1]} \n{list_stast[2]} \n" + \
    f"Clase: {_get_clases()}\n" + \
    f"Trasfondos: {_get_tranfondos()}\n" + \
    f"Raza: {_get_raza()}"

    print(text)

    # TODO Generar imagen
    # # Create a new image with white background
    # image = Image.new(mode='RGB', size=(300, 200), color=(255, 255, 255))
    # # Create a draw object
    # draw = ImageDraw.Draw(image)
    # # Define the font and font size
    # font = ImageFont.load_default()
    # # Get the size of the text
    # text_width, text_height = draw.textsize(text, font=font)
    # # Calculate the position of the text
    # x = (image.width - text_width) // 2
    # y = (image.height - text_height) // 2
    # # Draw the text on the image
    # draw.text((x, y), text, fill=(0, 0, 0), font=font)
    # # Save the image as a file
    # image.save('output.png')

if __name__ == '__main__':
    main()
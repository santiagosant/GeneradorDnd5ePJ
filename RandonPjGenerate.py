from random import randint
from PIL import Image, ImageDraw, ImageFont

CLASES = [
    'Artifice',
    'Bárbaro',
    'Bardo',
    'Brujo',
    'Clérigo',
    'Druida',
    'Explorador',
    'Guerrero',
    'Hechicero',
    'Mago',
    'Monje',
    'Paladín',
    'Pícaro',
]

TRASFONDOS = [
    'Acolyte',
    'Anthropologist',
    'Archaeologist',
    'Astral Drifter',
    'Athlete',
    'Baldur s Gate Acolyte',
    'Baldur s Gate Charlatan',
    'Baldur s Gate Criminal',
    'Baldur s Gate Entertainer',
    'Baldur s Gate Folk Hero',
    'Baldur s Gate Guild Artisan',
    'Baldur s Gate Hermit',
    'Baldur s Gate Noble',
    'Baldur s Gate Outlander',
    'Baldur s Gate Sage',
    'Baldur s Gate Sailor',
    'Baldur s Gate Soldier',
    'Baldur s Gate Urchin',
    'Charlatan',
    'City Watch',
    'City Watch (Investigator)',
    'Clan Crafter',
    'Cloistered Scholar',
    'Courtier',
    'Criminal',
    'Criminal (Spy)',
    'Entertainer',
    'Entertainer (Gladiator)',
    'Faceless',
    'Faction Agent',
    'Far Traveler',
    'Feylost',
    'Fisher',
    'Folk Hero',
    'Gate Warden',
    'Giant Foundling',
    'Guild Artisan',
    'Guild Artisan (Guild Merchant)',
    'Haunted',
    'Hermit',
    'House Agent',
    'Inheritor',
    'Investigator',
    'Knight of the Order',
    'Marine',
    'Mercenary Veteran',
    'Noble',
    'Noble (Knight)',
    'Noble (Retainers)',
    'Outlander',
    'Planar Philosopher',
    'Rune Carver',
    'Sage',
    'Sailor',
    'Sailor (Pirate)',
    'Shipwright',
    'Smuggler',
    'Soldier',
    'Urban Bounty Hunter',
    'Urchin',
    'Uthgardt Tribe Member',
    'Waterdhavian Noble',
    'Wildspacer',
    'Witchlight Hand',
]

RAZAS = [
     'Aarakocra Lineage (choose)',
    'Aasimar',
    'Aasimar Lineage (choose)',
    'Aasimar',
    'Aasimar (Fallen)',
    'Aasimar (Protector)',
    'Aasimar (Scourge)',
    'Astral Elf Lineage (choose)',
    'Autognome Lineage (choose)',
    'Bugbear Lineage (choose)',
    'Bugbear',
    'Centaur',
    'Centaur Lineage (choose)',
    'Changeling',
    'Changeling Lineage (choose)',
    'Deep Gnome Lineage (choose)',
    'Dhampir Lineage (choose)',
    'Dragonborn',
    'Dragonborn (Base)',
    'Dragonborn (Chromatic)',
    'Dragonborn (Draconblood)',
    'Dragonborn (Gem) Lineage (choose)',
    'Dragonborn (Metallic) Lineage (choose)',
    'Dragonborn (Ravenite)',
    'Duergar Lineage (choose)',
    'Dwarf',
    'Dwarf (Duergar)',
    'Dwarf (Hill)',
    'Dwarf (Mark of Warding)',
    'Dwarf (Mountain)',
    'Eladrin Lineage (choose)',
    'Elf',
    'Elf (Drow)',
    'Elf (Eladrin)',
    'Elf (High)',
    'Elf (Mark of Shadow)',
    'Elf (Pallid)',
    'Elf (Sea)',
    'Elf (Shadar-kai)',
    'Elf (Wood)',
    'Fairy Lineage (choose)',
    'Firbolg Lineage (choose)',
    'Firbolg' ,
    'Genasi Lineage (choose)',
    'Genasi (Air) Lineage (choose)',
    'Genasi (Earth) Lineage (choose)',
    'Genasi (Fire) Lineage (choose)',
    'Genasi (Water) Lineage (choose)',
    'Giff Lineage (choose)',
    'Gith',
    'Gith (Githyanki)',
    'Gith (Githzerai)',
    'Githyanki Lineage (choose)',
    'Githzerai Lineage (choose)',
    'Gnome',
    'Gnome (Deep)',
    'Gnome (Deep/Svirfneblin)',
    'Gnome (Forest)',
    'Gnome (Mark of Scribing)',
    'Gnome (Rock)',
    'Goblin',
    'Goblin Lineage (choose)',
    'Goblin',
    'Goliath Lineage (choose)',
    'Goliath',
    'Hadozee Lineage (choose)',
    'Half-Elf',
    'Half-Elf (Variant; Aquatic Elf Descent)',
    'Half-Elf (Variant; Drow Descent)',
    'Half-Elf (Variant; Mark of Detection)',
    'Half-Elf (Variant; Mark of Storm)',
    'Half-Elf (Variant; Moon Elf or Sun Elf Descent)',
    'Half-Elf (Variant; Wood Elf Descent)',
    'Half-Orc',
    'Half-Orc (Variant; Mark of Finding)',
    'Halfling',
    'Halfling (Ghostwise)',
    'Halfling (Lightfoot)',
    'Halfling (Lotusden)',
    'Halfling (Mark of Healing)',
    'Halfling (Mark of Hospitality)',
    'Halfling (Stout)',
    'Harengon Lineage (choose)',
    'Hexblood Lineage (choose)',
    'Hobgoblin',
    'Hobgoblin Lineage (choose)',
    'Human',
    'Human (Mark of Handling)',
    'Human (Mark of Making)',
    'Human (Mark of Passage)',
    'Human (Mark of Sentinel)',
    'Human (Variant)',
    'Human (Variant; Mark of Finding)',
    'Kalashtar',
    'Kender Lineage (choose)',
    'Kenku Lineage (choose)',
    'Kenku',
    'Kobold Lineage (choose)',
    'Kobold',
    'Leonin',
    'Lizardfolk Lineage (choose)',
    'Lizardfolk',
    'Loxodon',
    'Minotaur',
    'Minotaur Lineage (choose)',
    'Orc',
    'Orc Lineage (choose)',
    'Owlin Lineage (choose)',
    'Plasmoid Lineage (choose)',
    'Reborn Lineage (choose)',
    'Satyr',
    'Satyr Lineage (choose)',
    'Sea Elf Lineage (choose)',
    'Shadar-Kai Lineage (choose)',
    'Shifter',
    'Shifter Lineage (choose)',
    'Shifter (Beasthide)',
    'Shifter (Longtooth)',
    'Shifter (Swiftstride)',
    'Shifter (Wildhunt)',
    'Simic Hybrid',
    'Tabaxi Lineage (choose)',
    'Tabaxi',
    'Thri-kreen Lineage (choose)',
    'Tiefling',
    'Tiefling (Asmodeus)',
    'Tiefling (Baalzebul)',
    'Tiefling (Base)',
    'Tiefling (Dispater)',
    'Tiefling (Fierna)',
    'Tiefling (Glasya)',
    'Tiefling (Levistus)',
    'Tiefling (Mammon)',
    'Tiefling (Mephistopheles)',
    'Tiefling (Variant; Devils Tongue)',
    'Tiefling (Variant; Hellfire)',
    'Tiefling (Variant; Infernal Legacy)',
    'Tiefling (Variant; Winged)',
    'Tiefling (Zariel)',
    'Tortle Lineage (choose)',
    'Triton',
    'Triton Lineage (choose)',
    'Triton',
    'Vedalken',
    'Verdan',
    'Warforged',
    'Yuan-Ti Lineage (choose)',
    'Yuan-ti Pureblood',
]

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
    number = randint(1,len(CLASES))
    return CLASES[number-1]

def _get_tranfondos():
    number = randint(1,len(TRASFONDOS))
    return TRASFONDOS[number-1]

def _get_raza():
    number = randint(1,len(RAZAS))
    return RAZAS[number-1]

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
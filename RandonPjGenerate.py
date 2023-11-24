from random import randint

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

def main():
    # setStats = _get_3_setStats()
    print(f'{_get_tranfondos()}')

if __name__ == '__main__':
    main()
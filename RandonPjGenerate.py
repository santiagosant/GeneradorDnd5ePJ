from random import randint

def _get_stats():
    setStats = {}
    while len(setStats) <= 5:
        list_amount = []
        while len(list_amount) <= 3:
            list_amount.append(randint(1,6))
        list_amount.sort(reverse=True)
        list_amount.pop()
        setStats[len(setStats)] = sum(list_amount)
    return setStats

def _get_3_setStats():
    list_stats = []
    while len(list_stats) <= 2:
        list_stats.append(_get_stats())
    return list_stats

def main():
    setStats = _get_3_setStats()
    print(f'{setStats}')

if __name__ == '__main__':
    main()
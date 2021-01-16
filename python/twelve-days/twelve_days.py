# f'On the {day.number} of Christmas my true love gave to me: {day.day} {day.phrase} **others'
from collections import namedtuple

Day = namedtuple("Day", ['digit', 'number', 'phrase'])
days=[
    ['first', 'a', 'Partridge in a Pear Tree'],
    ['second', 'two', 'Turtle Doves'],
    ['third', 'three', 'French Hens'],
    ['fourth', 'four', 'Calling Birds'],
    ['fifth', 'five', 'Gold Rings'],
    ['sixth', 'six', 'Geese-a-Laying'],
    ['seventh', 'seven', 'Swans-a-Swimming'],
    ['eighth', 'eight', 'Maids-a-Milking'],
    ['ninth', 'nine', 'Ladies Dancing'],
    ['tenth', 'ten', 'Lords-a-Leaping'],
    ['eleventh', 'eleven', 'Pipers Piping'],
    ['twelfth', 'twelve', 'Drummers Drumming']
]

def recite(start_verse, end_verse):

    lyrics = []
    
    for i in range(start_verse, end_verse+1):
        day = Day(*days[i-1])
        x = lambda x: f'On the {x.digit} day of Christmas my true love gave to me: {x.number} {x.phrase}' 
        temp = str(x(day))

        if i > 0:
            for _ in range(i-1,0,-1):
                day = Day(*days[_-1])
                temp += f", {day.number} {day.phrase}"
        temp = temp[::-1].replace(',', 'dna ,', 1)[::-1]
        lyrics.append(temp+'.')

    return lyrics

def make_song2(verses = 99, beverage = "soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."            
        elif num == 1:
            yield f"Only {num} bottle of {beverage} left."
        else:
            yield f"No more {beverage}!"


def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)

for i in make_song2(5, 'kombucha'):
    print(i)



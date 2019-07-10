def make_song(num, word):
    for i in range(num+1):
        if num > 1:
            yield f"{num} bottles of {word} on the wall"
            num -= 1
        elif num == 1:
            yield f"Only {num} bottle of {word} left"
            num -= 1
        else:
            yield f"No more {word}"



for i in make_song(9, "Ursus"):
    print(i)


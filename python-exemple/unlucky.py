for i in range(1, 21):
    if i == 4 or i == 13:
        print(f"{i} este nenorocos")
        continue
    if i % 2 != 0:
        print(f"{i} este impar")
    else:
        print(f"{i} este par")

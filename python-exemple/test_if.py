from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================

print(f"Random food is {food}")
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food is 'apple' or food is 'grape':
    print("fruit")
elif food is 'bacon' or food is 'steak':
    print("meat")
else:
    print("yuck")
import itertools, random
deck =list(itertools.product(range(1,14),['spade','heart','diamond','club']))
random.shuffle(deck)
print("Ahmed Shaikh 323")
print("You got :")
for i in range(4):
    print(deck[i][0], "of",deck[i][1])

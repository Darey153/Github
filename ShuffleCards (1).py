import random
dCardNames = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
dCardValues = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
dSuits = ["\u2663","\u2660","\u2666","\u2665"]
# Build a two dimensional deck with Cards suits and values.
aCards =  [['' for i in range(52)] for j in range(3)]
i = 0
n = 0
while i < 13:
	aCards[0][i] = dCardNames[i]
	aCards[0][i + 13] = dCardNames[i]
	aCards[0][i + 26] = dCardNames[i]
	aCards[0][i + 39] = dCardNames[i]

	aCards[1][i] = dSuits[0]
	aCards[1][i + 13] = dSuits[1]
	aCards[1][i + 26] = dSuits[2]
	aCards[1][i + 39] = dSuits[3]
	aCards[2][i] = dCardValues[i]
	aCards[2][i + 13] = dCardValues[i]
	aCards[2][i + 26] = dCardValues[i]
	aCards[2][i + 39] = dCardValues[i]
	
	i = i + 1 
	
i = 0
y = []
while i < 52:
	print (aCards[0][i], " ", aCards[1][i], " ", aCards[2][i])
	x = [aCards[0][i], aCards[1][i], aCards[2][i]]
	y.append(x)
	i = i + 1
random.shuffle(y)

hand1 = []
for count in range (5):
        num = 1
        while num == 1:
                x = y.pop(5)
                if x in hand1:
                        num = 1
                else:
                        num = 0
                        hand1.append(x)
print(hand1)
hand2 = []
for count in range (5):
        num = 1
        while num == 1:
                x = y.pop(5)
                if x in hand2:
                        num = 1
                else:
                        num = 0
                        hand2.append(x)
print(hand2)

	

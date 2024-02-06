numberOfPeppers = int(input())

peppers = []

pepperList = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

spiciness = 0

for i in range(numberOfPeppers):
    peppers.append(input())

for i in peppers:
    spiciness += pepperList[i]

print(spiciness)
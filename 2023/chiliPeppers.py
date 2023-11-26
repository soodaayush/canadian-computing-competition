def chiliPeppers(n, list):
    peppers = {
        "poblano": 1500,
        "mirasol": 6000,
        "serrano": 15500,
        "cayenne": 40000,
        "thai": 75000,
        "habanero": 125000
    }

    spice = 0

    for i in list:
        spice += peppers[i.lower()]

    return spice


print(chiliPeppers(4, ["Poblano", "Cayenne", "Thai", "Poblano"]))
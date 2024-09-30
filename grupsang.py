pacients = [
{"edat": 34, "gsang": "A", "rh": "+", "genere": "Femení"},
{"edat": 29, "gsang": "B", "rh": "-", "genere": "Masculí"},
{"edat": 45, "gsang": "AB", "rh": "+", "genere": "Femení"},
{"edat": 52, "gsang": "A", "rh": "+", "genere": "Femení"},
{"edat": 38, "gsang": "A", "rh": "-", "genere": "Masculí"},
{"edat": 60, "gsang": "B", "rh": "+", "genere": "Masculí"},
{"edat": 25, "gsang": "O", "rh": "+", "genere": "Femení"},
{"edat": 48, "gsang": "AB", "rh": "+", "genere": "Masculí"},
]


filtrats = [pacient for pacient in pacients if pacient["edat"] < 35 and pacient["gsang"] in ["A", "O"]]

for pacient in filtrats:
    print(pacient)

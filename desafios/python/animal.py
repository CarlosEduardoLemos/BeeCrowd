# Dicionário para identificar os animais com base nas três características
animais = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

# Entrada de três palavras
caracteristica1 = input()
caracteristica2 = input()
caracteristica3 = input()

# Localiza o animal correspondente
resultado = animais[caracteristica1][caracteristica2][caracteristica3]

# Exibe o resultado
print(resultado)

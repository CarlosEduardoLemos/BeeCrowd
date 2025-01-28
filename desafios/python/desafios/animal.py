def identificar_animal(caracteristica1, caracteristica2, caracteristica3):
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

    # Localiza o animal correspondente
    return animais[caracteristica1][caracteristica2][caracteristica3]

def main():
    # Entrada de três palavras
    caracteristica1 = input("Digite a primeira característica: ")
    caracteristica2 = input("Digite a segunda característica: ")
    caracteristica3 = input("Digite a terceira característica: ")

    # Identifica o animal correspondente
    resultado = identificar_animal(caracteristica1, caracteristica2, caracteristica3)

    # Exibe o resultado
    print(resultado)

if __name__ == "__main__":
    main()
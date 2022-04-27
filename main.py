import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_str = input(f"Calculez : {a} + {b} = ")
    reponse_int = int(reponse_str)
    if reponse_int == a + b:
        return True

    return False


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur 4:")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()


print(f"Votre note est : {nb_points} / {NB_QUESTIONS}")

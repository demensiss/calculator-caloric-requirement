
def show_activity():
    print()
    print("1. Praca siedząca, brak dodatkowej aktywności fizycznej.")
    print("2. Praca niefizyczna, mało aktywny tryb życia")
    print("3. Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu")
    print("4. Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu")
    print("5. Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu")
    print()

def check_activity(activity):
    if activity == 1:
        factor_a = 1.2
    if activity == 2:
        factor_a = 1.4
    if activity == 3:
        factor_a = 1.6
    if activity == 4:
        factor_a = 1.8
    if activity == 5:
        factor_a = 2.0
    return factor_a

def check_sex(sex):
    if sex == "K" or sex == "k":
        factor_s = -161
    if sex == "M" or sex == "m":
        factor_s = 5
    return factor_s

def base_calculation(weight, height, age, factor_s, factor_a):
    return ((10 * weight) + (6.25 * height) - (5 * age) + factor_s) * factor_a

sex = input("Podaj swoją płeć wpisując K jeśli kobieta lub M jeśli mężczyzna: ")
age = int(input("Podaj swój wiek: "))
weight = int(input("Podaj swoją wagę w kilogramach: "))
height = int(input("Podaj swój wzrost w centymetrach: "))
show_activity()
activity = int(input("Patrząc na powyższą listę określ swoją aktywność i podaj jej numer: "))

print("Twoje dzienne zapotrzebowanie kaloryczne wynosi:")
print(base_calculation(weight, height, age, check_sex(sex), check_activity(activity)))




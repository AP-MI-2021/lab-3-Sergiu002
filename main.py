#problema 6
def get_all_num_div_k(List, k):
    """
    Determina daca toate nr. dintr-o lista sunt divizibile cu k
    :param List: lista de nr. intregi
    :param k: paramatrul cu care trebuie sa fie divizibile numerele (tip intreg)
    :return: True, daca toate nr. sunt divizibile cu k si False in caz contrar
    """
    for number in List:
        if number % k != 0:
            return False
    return True
def get_longest_div_k(List, k):
    """
    Determina cea mai lunga subsecventa de nr. divizibile cu k
    :param List: lista de nr. intregi
    :param k: paramatrul cu care trebuie sa fie divizibile numerele (tip intreg)
    :return: Cea mai lunga subsecventa de nr. divizibile cu k
    """
    subsecventaMax = []
    for first in range(len(List)):
        for second in range(first, len(List)):
            if get_all_num_div_k(List[first:second + 1], k) and len(List[first:second + 1]) > len(subsecventaMax):
                subsecventaMax = List[first:second + 1]
    return subsecventaMax

def test_get_longest_div_k():
    """
    Functia de test pentru functia get_longest_div_k
    """
    assert get_longest_div_k([2, 3, 4, 6, 8, 7], 3) == [3]
    assert get_longest_div_k([1, 2, 3, 4, 8], 2) == [4, 8]
    assert get_longest_div_k([7, 14, 28, 3, 5, 6, 21], 7) == [7, 14, 28]

#problema 13
def get_prime(number):
    """
    Verifica daca un numar este prim
    :param number: tip intreg
    :return: True, daca numar este prim si False in caz contrar
    """
    if number < 2:
        return False
    for index in range(2, number // 2 + 1):
        if number % index == 0:
            return False
    return True
def get_all_digits_prime(number):
    """
    Verifica daca toate cifrele unui numar sunt prime
    :param number: tip intreg
    :return: True daca toate cifrele sunt prime si False in caz contrar
    """
    contor = 0
    contor_cif = 0
    while number:
        cif = number % 10
        contor_cif += 1
        if get_prime(cif):
            contor += 1
        number //= 10
    if contor == contor_cif:
        return True
    else:
        return False
def get_all_number_prime_digits(List):
    """
    Verifica daca toate numere din lista au toate cifrele numere prime
    :param List:lista de nr. intregi
    :return: True daca toate numerele din lista au toate cifrele prime si False in caz contrar
    """
    contor = 0
    for number in List:
        if get_all_digits_prime(number):
            contor = contor + 1
    if contor == len(List):
        return True
    else:
        return False
def get_longest_prime_digits(List):
    """
    Determina cea mai lunga subsecventa care are numerele formate din cifre prime
    :param List: lista de nr. intregi
    :return: Cea mai lunga subsecventa care are numerele formate din cifre prime
    """
    subsecventaMax = []
    for first in range(len(List)):
        for second in range(first, len(List)):
            if get_all_number_prime_digits(List[first: second + 1]) and len(List[first: second + 1]) > len(subsecventaMax):
                subsecventaMax = List[first: second + 1]
    return subsecventaMax

def test_get_longest_prime_digits():
    """
    Functia de test pentru functia get_longest_prime_digits
    """
    assert get_longest_prime_digits([234, 25, 235, 257]) == [25, 235, 257]
    assert get_longest_prime_digits([24, 25, 2, 3, 8, 12]) == [25, 2, 3]
    assert get_longest_prime_digits([24, 21, 256, 4]) == []
def print_menu_5():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de nr. divizibile cu k")
    print("3. Alta problema")
    print("4. Iesire")
def print_menu_13():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de nr. formate din cifre prime")
    print("3. Alta problema")
    print("4. Iesire")
def main():
    """
    Meniul utilizatorului
    """
    test_get_longest_prime_digits()
    test_get_longest_div_k()
    problema = int(input("Alegeti una dintre problemele 6 sau 13: "))
    if problema == 6:
        while True:
            print_menu_5()
            optiunea = int(input("Dati optiunea: "))
            if optiunea == 1:
                List = []
                k = int(input("Introduceti numarul cu care elementele din lista trebuie sa fie divizibile: "))
                given_string = input("Introduceti lista: ")
                numbers_as_string = given_string.split(" ")
                for index in numbers_as_string:
                    List.append(int(index))
            elif optiunea == 2:
                print(get_longest_div_k(List, k))
            elif optiunea == 4:
                break
            elif optiunea == 3:
                main()
            else:
                print("Optiune gresita! Reincercati!")
    elif problema == 13:
        while True:
            print_menu_13()
            optiunea = int(input("Dati optiunea: "))
            if optiunea == 1:
                List = []
                given_string = input("Introduceti lista: ")
                numbers_as_string = given_string.split(" ")
                for index in numbers_as_string:
                    List.append(int(index))
            elif optiunea == 2:
                print(get_longest_prime_digits(List))
            elif optiunea == 4:
                break
            elif optiunea == 3:
                main()
            else:
                print("Optiune gresita! Reincercati!")
if __name__ == '__main__':
    main()


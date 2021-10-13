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
#problema 8
def get_sum_is_prime(List):
    """
    Verifica daca suma listei este un numar prim sau nu
    :param List: lista de nr. intregi
    :return: True daca suma listei este un numar prim si False in caz contrar
    """
    suma = 0
    for number in List:
        suma += number
    if get_prime(suma):
        return True
    else:
        return False
def get_longest_sum_is_prime(List):
    """
    Determina cea mai lunga subsecventa de numere care au suma un numar prim
    :param List: lista de nr. intregi
    :return: Cea mai lunga subsecventa care are suma un numar prim
    """
    subsecventaMax = []
    for first in range(len(List)):
        for second in range(first, len(List)):
            if get_sum_is_prime(List[first: second + 1]) and len(List[first: second + 1]) > len(subsecventaMax):
                subsecventaMax = List[first: second + 1]
    return subsecventaMax
def test_get_longest_sum_is_prime():
    """
    Funtia de test pentru functia get_longest_sum_is_prime
    """
    assert get_longest_sum_is_prime([11, 12, 3, 4]) == [12, 3, 4]
    assert get_longest_sum_is_prime([1, 2, 3, 4]) == [1, 2]
    assert get_longest_sum_is_prime([4, 4, 6]) == []
def print_menu():
    print("0. Citire lista")
    print("1. Citire parametru k pentru problema 6")
    print("2. Afisare cea mai lunga subsecventa de nr. in care suma numerelor sa fie prima")
    print("3. Afisare cea mai lunga subsecventa de nr. formate din cifre prime")
    print("4. Afisare cea mai lunga subsecventa de nr. divizibile cu k")
    print("5. Iesire")

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
def main():
    """
    Meniul utilizatorului
    """
    test_get_longest_prime_digits()
    test_get_longest_sum_is_prime()
    test_get_longest_div_k()
    while True:
        print_menu()
        optiunea = int(input("Dati optiunea: "))
        if optiunea == 0:
            List = []
            given_string = input("Introduceti lista: ")
            numbers_as_string = given_string.split(" ")
            for index in numbers_as_string:
                List.append(int(index))
        elif optiunea == 1:
            param_k = int(input("Introduceti un numar: "))
        elif optiunea == 2:
            print(get_longest_sum_is_prime(List))
        elif optiunea == 3:
            print(get_longest_prime_digits(List))
        elif optiunea == 4:
            print(get_longest_div_k(List, param_k))
        elif optiunea == 5:
            break
        else:
            print("Optiune gresita! Reincercati!")
if __name__ == '__main__':
    main()


import LCS as lcs, naiveMethod as nm
from random import choice
from random import seed
from string import ascii_uppercase
def generate_List(random_seed, size1, size2):
    """
    Generate a pair of random character lists with given length
    :param random_seed: int
    :param size1: int, length of the first list
    :param size2: int, length of the second list
    :return: tuple, (list_1, list_2)
    """
    seed(random_seed)
    new_list1 = []
    new_list2 = []
    for i in range(size1):
        new_list1.append(choice(ascii_uppercase))
    for j in range(size2):
        new_list2.append(choice(ascii_uppercase))
    return new_list1, new_list2

if __name__ == "__main__":
    new_lists = generate_List(10, 20, 20)

    nm = nm.naiveMethod()
    lcs = lcs.LCS(new_lists[0], new_lists[1], nm)
    nm_result, nm_time = lcs.run()
    print("The result: " + str(nm_result) + "\nThe time: " + str(nm_time))
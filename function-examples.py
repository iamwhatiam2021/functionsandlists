def check_odd_even(number, odd=True):
    """
    This function checks whether a number if odd or even
    :param number: the number to check
    :param odd: True for ODD, False for even
    :return: None, just prints
    """
    if odd:
        if number % 2 == 1:
            print(f"Correct, number {number} is odd")
        else:
            print(f"wrong, number {number} is not odd")
    else:
        if number % 2 == 1:
            print(f"Correct, number {number} is even")
        else:
            print(f"wrong, number {number} is not even")

def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    roman_numbers = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I" }

    output = []
    
    for number, letters in roman_numbers.items():
        while num >= number:
            output.append(letters)
            num = num - number

    out_str = ''.join(output)

    return out_str              
            

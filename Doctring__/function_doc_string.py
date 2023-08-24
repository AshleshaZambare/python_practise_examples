def sum_two_numbers(a, b):
    """
    return the sum of two decimal numbers.

        parameters:
            a (int): a decimal integer
            b (int): a decimal integer

        returns:
            sum(int): decimal sum of a nad b
    """
    sum = a+b
    return sum

print(sum_two_numbers(2, 3))
print(sum_two_numbers.__doc__)
help(sum_two_numbers)
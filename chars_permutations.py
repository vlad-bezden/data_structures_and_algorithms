"""
Creates all posible string permutations with n as a lenght of the string

['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc',
'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc',
'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']
"""


def permutations(n, s):
    if n == 1:
        return s
    return [digit + bits for digit in permutations(1, s) for bits in permutations(n - 1, s)]


print(permutations(3, "abc"))

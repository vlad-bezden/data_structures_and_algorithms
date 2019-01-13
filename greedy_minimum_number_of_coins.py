"""Greedy algorithm to find minimum number of coins"""
import random

COINS_VALUES = [1, 5, 10, 25, 50, 100]


def number_of_coins(value):
    result = {}

    for coin_value in reversed(COINS_VALUES):
        coins, value = divmod(value, coin_value)
        if coins:
            result[coin_value] = coins

    return result


value = random.randint(0, 1000)
result = number_of_coins(value)
print(value, result)

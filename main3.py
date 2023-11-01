def checker(s):
    if type(s) != str:
        raise TypeError("no.")

    else:
        return s


print(checker('lll'))
print(checker(10))

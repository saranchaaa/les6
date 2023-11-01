class BE(Exception):
    def __str__(self):
        return f"You cannot build a house with this amount of materials."

def cm(amount, limit):
    if amount >= limit:
        return "That's enough."
    else:
        raise BE(amount)


print(cm(1000, 500))
print(cm(1000, 1000))
print(cm(500, 1000))
def attack(ele, pos):
    data = [1,5,6,2,4]
    try:
        data[pos] = ele
        return True
    except IndexError:
        return "Don't try buffer overflow attacks in python"

print(attack(3,4))
print(attack(1,6))

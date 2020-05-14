import pymorphy2

morph = pymorphy2.MorphAnalyzer()

word = morph.parse('проекта')[0]

print(morph.parse('сошедшиеся')[0].normal_form)
print(morph.parse('сошедшиеся')[0])


def multiply(a, b):
    if int == type(a) and int == type(b):
        return a * b
    else:
        return None


def first_non_consecutive(arr):
    not_cons_elem = 0
    for i in range(0, arr, 1):
        temp = arr[i+1] - arr[i]
        if abs(temp) != 1:
            not_cons_elem = arr[i+1]
        else:
            not_cons_elem = None
    return not_cons_elem



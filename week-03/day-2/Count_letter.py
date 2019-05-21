def count_letter(str):
    str = str.replace(' ', '')
    letterdic = {}
    for letter in str:
        if letter in letterdic:
            letterdic[letter] += 1
        else:
            letterdic[letter] = 1
    return letterdic

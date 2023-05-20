def swap_case(s):
    characters = []
    result = ''
    for character in s:
        characters.append(character)

    for c in characters:
        if c == c.lower():
            c = c.upper()
            result += c
        elif c == c.upper():
            c = c.lower()
            result += c
    return result


if __name__ == '__main__':
    s = input("Enter string:")
    result = swap_case(s)
    print(result)

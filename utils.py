def write_to_file(name):
    with open("names.txt", "a") as f:
        f.write(f"{name}\n")
        
def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result

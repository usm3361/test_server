def write_to_file(name):
    with open("names.txt", "a") as f:
        f.write(f"{name}\n")
        
def encrypt_caesar(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt_caesar(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


def encrypt_fance(text):
    new_text = ""
    for i in text.split():
        new_text += i    
    

def decrypt_fance(text):
    return
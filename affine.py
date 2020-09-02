import re

LIST_OF_POSSIBLE_M_KEY = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
NUMBER_OF_ALPHABET = 26  #[a..z]

def convertStringToInt(text):
    list_number = []
    for item in text :
        list_number.append(ord(item) - 97)
    return list_number

def convertIntToString(text):
    list_char = []
    for item in text :
        list_char.append(chr(item + 97))
    return list_char

def modInverse(a, m): 
    a = a % m; 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1

def affineEncrypt(text, m, b):
    for i in range(len(text)):
        text[i] = (text[i] * m + b) % NUMBER_OF_ALPHABET
    return text

def affineDecrypt(text, m , b):
    m_inverse = modInverse(m, NUMBER_OF_ALPHABET)
    for i in range(len(text)):
        text[i] =  (m_inverse * (text[i] - b)) % NUMBER_OF_ALPHABET
    return text

if __name__ == "__main__":
    flag_text = False
    while(not flag_text):
        try:
            text = input("Input text : ")
            text = re.sub("[^a-zA-Z]", "", text)    #remove non-alphabetic characters
            if(len(text)!=0):
                flag_text = True
            else:
                print("Text must not be empty!")
        except ValueError:
            print("Text must not be empty!")
            pass
    

    flag_M = False
    while(not flag_M):
        try:
            m_key = int(input ("Value of M : "))
            if(m_key in LIST_OF_POSSIBLE_M_KEY):
                flag_M = True
            else:
                print("M must be an integer prime relative to N")
        except ValueError:
            print("M must be an integer prime relative to N")
            pass

    flag_B = False
    while(not flag_B):
        try:
            b_key = int(input ("Value of B : "))
            flag_B = True
        except ValueError:
            print("B must be an integer!")
            pass

    flag_opt = False
    while(not flag_opt):
        try:
            print("\nCHOOSE OPERATION")
            print("1. Encrypt")
            print("2. Decrypt")
            opt = int(input ("OPERATION : "))
            if(opt in [1,2]):
                flag_opt = True
            else:
                print("Input must be an integer 1 or 2!")
        except ValueError:
            print("Input must be an integer 1 or 2!")
            pass

    print("\nINPUT TEXT =", text.upper())
    print("VALUE OF M =", m_key)
    print("VALUE OF B =", b_key)
    inputtext = convertStringToInt(text.lower())

    if opt == 1:
        print("ENCRYPTING")
        result = affineEncrypt(inputtext, m_key, b_key)
    else:
        print("DECRYPTING")
        result = affineDecrypt(inputtext, m_key, b_key)

    print("RESULT TEXT =", (''.join(convertIntToString(result))).upper())
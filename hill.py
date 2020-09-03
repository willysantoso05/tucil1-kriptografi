import numpy as np
import re
import random
import string

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

def gcd(a, b): 
    while a != 0:
        a, b = b, a % b
    return a

# Function to check and print if  
# two numbers are co-prime or not  
def isCoprime(x): 
    return (gcd(NUMBER_OF_ALPHABET, x) == 1) 

def hillEncrypt(text,k,m):
    result = []
    for item in text:
        multiple = np.dot(k, item)
        for number in multiple:
            result.append(number % NUMBER_OF_ALPHABET)
    return result

def hillDecrypt(text,k,m):
    result = []
    key_inverse =  (np.round_((np.linalg.inv(k) * np.linalg.det(k)) * modInverse(determinant, NUMBER_OF_ALPHABET))).astype(int) % 26

    for item in text:
        multiple = np.dot(key_inverse, item)
        for number in multiple:
            result.append(number % NUMBER_OF_ALPHABET)
    return result

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

    flag_m = False
    while(not flag_m):
        try:
            m_linear = int(input ("Value of M : "))
            flag_m = True
        except ValueError:
            print("M must be an integer!")
            pass

    flag_key = False
    while(not flag_key):
        try:
            key = input("Input key : ")
            key = re.sub("[^a-zA-Z]", "", key)    #remove non-alphabetic characters
            if(len(key)!=0):
                if(len(key) > m_linear * m_linear):
                    key = key[0:m_linear * m_linear]
                elif(len(key) < m_linear * m_linear):
                    key += str(''.join(random.choices(string.ascii_uppercase, k=m_linear * m_linear-len(key)))) 
                flag_key = True
            else:
                print("Key must not be empty!")
        except ValueError:
            print("Key must not be empty!")
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
    print("VALUE OF M =", m_linear)
    print("KEY TEXT =", key.upper())
    inputText = convertStringToInt(text.lower())
    key = convertStringToInt(key.lower())

    #Devide list into matrix of m elements
    list_of_chars = [inputText[i:i+m_linear] for i in range (0, len(inputText), m_linear)]
    while(len(list_of_chars[-1])!=m_linear):
        list_of_chars[-1].append(25)    #add Z character if text mod m != 0
    numpy_key = np.array([key[i:i+m_linear] for i in range (0, len(key), m_linear)])

    if opt == 1:
        print("\nENCRYPTING...")
        result = hillEncrypt(list_of_chars, numpy_key, m_linear)
    else:
        print("\nDECRYPTING...")
        determinant = np.linalg.det(numpy_key)
        if(determinant == 0 or not isCoprime(determinant) ):
            result = []
            print("Text can't be decrypt with input key, try another key.")
        else:
            result = hillDecrypt(list_of_chars, numpy_key, m_linear)
            print("RES =", result)
    
    if(len(result)!=0):
        print("RESULT TEXT =", (''.join(convertIntToString(result))).upper())

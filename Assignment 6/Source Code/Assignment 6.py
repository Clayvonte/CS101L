import string 
def Encrypt(string_text, int_key):     
    result = ""
    for i in range(len(string_text)):
        char = string_text[i]
        result += chr((ord(char) + int_key-65) % 26 + 65)
    return result
    
def Decrypt(string_text, int_key):   
    result = ""
    for i in range(len(string_text)):
        char = string_text[i]
        result += chr((ord(char) - int_key-65) % 26 + 65)
    return result
    
def Get_input(): 
    print("Do you want to 1) Encode a string, 2) Decode a string, or Q) Quit?")  
    get=input("Enter 1, 2, or Q: ")
    return get
    
def main():   
    Again = True   
    while Again:    
        Choice = Get_input()     
        if Choice == '1':       
            Plaintext = input("Enter (brief) text to encrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Ciphertext = Encrypt(Plaintext, Key)      
            print("Encrypted:", Ciphertext)     
        elif Choice == '2':       
            Ciphertext = input("Enter (brief) text to decrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Plaintext = Decrypt(Ciphertext, Key)      
            print("Decrypted:", Plaintext)     
        else:       
            print("Have an ordinary day.")       
            Again = False 
    
main() 

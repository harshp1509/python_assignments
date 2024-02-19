import os
def encrypt(text,shift):
    res=""
    for char in text:
        if char.isalpha():
            b=ord('a') if char.islower() else ord('A')
            res+=chr((ord(char)-b +shift)%26 +b)
        else:
            res+=char
    return res

def decrypt(text,shift):
    return encrypt(text,-shift)



print("File Encryption")
filename="temp.txt"
if not os.path.exists(filename):
    print("file not found")
    
operation=input("Choose operation (e for encrypt/d for decrypt): ").lower()

if operation not in ['e','d']:
    print("Invalid operation.")

shift=int(input("enter the shift value:--"))

try:
    file=open(filename,'r')
    content=file.read()

    if(operation=='e'):
        result=encrypt(content,shift)
    elif(operation=='d'):
        result=decrypt(content,shift)

    output_file=open(filename,'w')
    output_file.write(result)
    print("file oeration performed sucessfully.")
except FileNotFoundError:
    print("file not found")
except IOError:
    print("unable to open or write to file.")

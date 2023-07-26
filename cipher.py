plaintext=input("Please enter a plaintext: ")
plaintext=plaintext.lower()
encryptedText=""
cipher ={
    "a" : "f","b":"g","c" : "h","d":"i","e":"j","f":"k","g":"l","h":"m","i":"n","j":"o",
    "k":"p","l":"q","m":"r","n":"s","o":"t","p":"u","q":"v","r":"w","s":"x","t":"y","u":"z",
    "v":"a","w":"b","x":"c","y":"d","z":"e"
}
for i in plaintext:
    if i in cipher :
        encryptedText=encryptedText + cipher[i]
    else :
        encryptedText=encryptedText + i
      
print("The Encrypted Text is : ",encryptedText)

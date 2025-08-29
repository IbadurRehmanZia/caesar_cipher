lowercase_alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def encoder(msg,shift):
   
    e_msg=""
    for a in msg:
        e_msg+=lowercase_alphabets[lowercase_alphabets.index(a)+shift]
    
    return e_msg
def decoder(msg,shift):
   
    d_msg=""
    for a in msg:
        d_msg+=lowercase_alphabets[lowercase_alphabets.index(a)-shift]
    
    return d_msg

def main():
    
    tr=True
    while tr==True:
        method=input("Type 'decode' for decoding OR 'encode' for encoding : ")
        msg=input("Type the messege:\n")
        shift=int(input("Enter shift number:\n"))



        if method=="encode":
            
            print("encoded messege: ",encoder(msg,shift))
        else:
            print("decoded messege: ",decoder(msg,shift))
        cont=input("Do you want to continue ? (Y / N)").lower()
        if cont=="n":
            tr=False
        

main()
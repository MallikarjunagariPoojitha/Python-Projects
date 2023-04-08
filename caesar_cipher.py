alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e',
           'f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z']
def caesar_cipher(st,shift,direction):
    a=""
    pos=0
    for i in range(len(st)):
        letter=st[i]
        if letter in alphabets:    
            pos=alphabets.index(letter)
            if direction=="decode":
                newpos=pos-shift
            elif direction=="encode":
                newpos=pos+shift
            a+=alphabets[newpos]
        else:
            a+=letter
    print("The {} text is {}".format(direction,a))
user="yes"
while user=="yes":
    direction=input("enter the string to encode or decode:").lower()
    st=input("Type Your Message:").lower()
    shift=int(input("Type the shift  number:"))
    shift=shift%26
    caesar_cipher(st,shift,direction)
    user=input("if you want to encode/decode more messages yes/no:").lower()
print("Good Bye!")
        

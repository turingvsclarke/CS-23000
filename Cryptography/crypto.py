keepGoing=False;
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
key = "";

def generateKey(s):
        global key;
        ## Reset the key
        key="";
        ## Shift the alphabet by s letters. The sth letter now corresponds to a
        for i in range(0,26):
                ## Find the s+ith letter and add it to the key
                key+=alphabet[(s+i-1)%26];
        ## end for

## end generateKey

def encrypt(input):
        cipher = "";
        input=input.upper();
        for x in range(len(input)):
                if input[x]!=" ":
                        index=alphabet.index(input[x]);
                        cipher+=key[index];
                else:
                        cipher+=" ";
        ## end for
        return cipher;

def decrypt(cipher):
        plaintext = "";
        cipher=cipher.upper();
        for x in range(len(cipher)):
                if cipher[x]!=" ":
                        index=key.index(cipher[x]);
                        plaintext+=alphabet[index];
                else:
                        plaintext+=" ";
        ##end for
        return plaintext;

def genKeyPhrase(phrase):
        global key;
        # Reset the key
        key="";
        # Remove any whitespace
        phrase=phrase.replace(" ","");
        phrase=phrase.upper();
        alphabet1=alphabet;
        size=len(phrase);
        for x in range(size):
                if x<len(phrase):
                        char=phrase[x];
                        count=phrase.count(char);
                        if count>1:
                                phrase=phrase.replace(char,"");
                                phrase=phrase[:x]+char+phrase[x:];
                        else:
                                alphabet1=alphabet1.replace(char,"");
        # end for
        print(phrase);
        # Add the alphabet to the phrase, giving your new key
        key=phrase+alphabet1;   
# end genKeyPhrase


def menu():
        choice="";
        global keepGoing;
        print("(1) Add key");
        print("(2) Encrypt phrase");
        print("(3) Decrypt phrase");
        print("(4) Exit");
        choice=input();
        if choice=="1":
                print("(1) Shift alphabet by integral amount")
                print("(2) Transform alphabet using a passphrase")
                print("(3) Return to main menu");
                choice=input();

                if choice=="1":
                        print("Enter number. Entering n means A maps to the nth letter");
                        generateKey(int(input()));
                elif choice=="2":
                        print("Enter phrase");
                        genKeyPhrase(input());
        
        elif choice=="2" and key!="":
                print("encrypt");
                print(encrypt(input()));
        
        elif choice=="3" and key!="":
                print("decrypt");
                print(decrypt(input()));
        
        elif choice=="4":
                keepGoing=False;
                print("Goodbye!");
        ## 
        #print("Enter a number");
        #print("Enter a phrase");

"""
for j in range(26):
        generateKey(j);
        guess=decrypt("gk qmppw zsr jcrrcpq gq hsqr lmr clmsef rm bm ylw iglb md ylyjwqgq zcwmlb aycqyp ylb kywzc yddglc agnfcpq njcyqc qclb y jmlecp kcqqyec ugrf rfc qykc icw");      
        print(guess+"\n");
        key="";
## end for
"""

keepGoing=True;
while keepGoing:
        menu();
# end while




import random
from bs4 import BeautifulSoup
import urllib.request
import requests
from random_word import RandomWords



def hangman(tally):

    r = RandomWords()
    words = r.get_random_words()
    x=random.randint(0,1000)
    a=random.choice(words)
    #a=a.decode('utf-8')
    a=a.lower()
    b=str()
    print('Your word is: ', end= ' ')
    for i in range (0, len(a)):
        b= b+'_'
        print(b[i] ,end= ' ')
    
    guess=[]
    count=tally[0]
    points=tally[1]
    while(count>0):
        print('\n\nYou have ' +str(count)+' chances to guess the word')
        x=input("Enter an alphabet: ")[0]
        if(x.isalpha()==False):
            print("Enter a valid alphabet")
            break
        x= x.lower()
        buffer=0
        buffer1=0
        found=0
        for i in range (0,len(a)):
            if(a[i]==x):
                found=1
                buffer=1
                b=list(b)
                b[i]=x
                b="".join(b)
                points=points+1
        if(buffer==1):
            print("Correct guess :)")
            for j in range (0, len(b)):
                print(b[j] ,end= ' ')
        if(found==0):
            print("Inorrect guess, try harder!!")
            for j in range (0, len(b)):
                print(b[j] ,end= ' ')
        if(buffer==0):
            for i in range (0,len(guess)):
                if(guess[i]==x):
                    buffer1=1
            if(buffer1==0):
                count=count-1
                guess.append(x)
        buf=0
        for i in range(0, len(b)):
            if(b[i]=='_'):
                buf=1
        if(buf==0):
            print('\nYou have guessed the word with ' + str(count) +' chances left \n'+ str(points)+' points\n\n')
            tally[0]=count
            tally[1]=points
            return tally
    if(count==0):
        print('You lost. Better luck next time! \n Your word was: '+a+'\nYour points are: '+str(points))
        print(a)
        tally[0]=0
        tally[1]=points
        return tally

print('HANGMAN')
tally=[7,0]
print(type(tally[0]))
while(1):
    x=input('Press:\n 1.To play a new game \n 2. Continue existing game \n 3. Exit\n')
    x=int(x)
    if(x==1):
        tally=[7,0]
        tally= hangman(tally)
    if(x==2):
        if(tally[0]==0):
            tally[0]=7
            tally[1]=0
        tally=hangman(tally)
        
    if(x==3):
        exit()
    else:
        print("Enter a valid response ")

import random

def main():
    guess=0
    number = random.randint(0,10)
    answer = int(input("Guess the number? "))
    while(answer != number):
        if(answer < number):
            guess+=1
            print("A little bit more")
        elif(answer > number):
            guess+=1
            print("A little bit less")
        answer = int(input("Guess the number? "))
    guess+=1
    print("correct it took", guess,"tries")   
main()

#method to determine if question is right or not
def main():
    point = 0
    q1 = "the earth is flat?"
    q2 = "black is abscene of all color?"
    q3 = "frogs are green?"
    q4 = "it is August?"
    q5 = "volleyball has 6 players on one side?"
    print(q1)
    answer = str(input("True or False? "))
    if(answer == "True" or answer=="true"):
        point+=1
        print("Correct")
    else:
        print("Incorrect")

    print(q2)
    answer = str(input("True or False "))
    if(answer == "True" or answer == "true"):
        point+=1
        print("Correct")
    else:
        print("Incorrect")

    print(q3)
    answer = str(input("True or False "))

    if(answer == "True" or answer == "true"):
        point+=1
        print("Correct")
    else:
        print("Incorrect")


    print(q4)
    answer = str(input("True or False "))

    if(answer == "True" or answer == "true"):
        point+=1
        print("Correct")
    else:
        print("Incorrect")  

    print(q5)
    answer = str(input("True or False "))

    if(answer == "True" or answer == "true"):
        point+=1
        print("Correct")
    else:
        print("Incorrect")

    percent = (point / 5) * 100
    print("You got", point,"out of 5,", percent)     
#input true or false only

#print out number of questions gotten right and the percentage
main()
import random
import time

def getNums(diff):
    nums = [0] * 2
    nums[0] = random.randint(1,diff)
    nums[1] = random.randint(1,diff)
    if nums[1] > nums[0]:
        temp = nums[0]
        nums[0] = nums[1]
        nums[1] = temp
    return nums

def getDifficulty():
    print("First select your level of difficulty:\n")
    while True:
        print("type '1' for easy\ntype '2' for medium\ntype '3' for hard")
        inp = input()
        if inp.isdigit() == True:
            diff = int(inp)
            if diff == 1:
                return 10
            elif diff == 2:
                return 100
            elif diff == 3:
                return 1000
        print("\nInvalid Selection, please try again.")


def results(answer, expected, duration):
    if answer == expected:
        print("\nContratulations! You answered correctly!\nYou got the correct answer of "+str(answer)+" in "+str(duration)+" seconds!\n")
    else:
        print("\nSorry, that isn't the correct answer. The correct answer was: "+str(answer)+"\n")
    return

def readyUp():
    i = 0
    ready = input()
    while ready is not "r":
        print("Invalid input. Please type 'r' when ready.")
        ready = input()
        i += 1
        if i == 10:
            print("OK so it looks like you're just fucking with me and don't actually wanna play. Fine. Goodbye.")
            exit()

def getAnswer():
    answer = input()
    while answer.isdigit() == False:
        print("Invalid Input: Input is not an integer. Please try again.")
        answer = input()
    return answer

def addition():
    print("\nWelcome to the addition test! ")
    diff = getDifficulty()
    print("\nFor this test you will be given 2 integers in the range of 1 to " + str(diff) + " and will need to add them together.")
    print("There is no time limit but you will be timed. Enter 'r' when ready.")
    readyUp()

    nums = getNums(diff)
    print("\nAlright, the two numbers you will be adding are:\n" + str(nums[0]) + "\n" + str(nums[1]) + "\nEnter your response as an integer. You only have one chance to enter a number so make sure you're ready when you submit:")
    start = time.time()
    answer = getAnswer()
    end = time.time()

    expected = nums[0] + nums[1]
    results(int(answer), expected, round(end-start, 2))
    return

def subtraction():
    print("\nWelcome to the subtraction test! ")
    diff = getDifficulty()
    print("\nFor this test you will be given 2 integers in the range of 1 to "+str(diff)+" and will need to subtract the second from the first.\nThere is no time limit but you will be timed. Enter 'r' when ready.")
    readyUp()

    nums = getNums(diff)
    print("\nAlright, the two numbers you will be subtracting are:\n"+str(nums[0])+"\n"+str(nums[1])+"\nEnter your response as an integer. You only have one chance to enter a number so make sure you're ready when you submit:")
    start = time.time()
    answer = getAnswer()
    end = time.time()

    expected = nums[0] - nums[1]
    results(int(answer), expected, round(end-start, 2))
    return

def multiplication():
    print("\nWelcome to the multiplication test! ")
    diff = getDifficulty()
    print("\nFor this test you will be given 2 integers in the range of 1 to "+str(diff)+" and will need to multiply them together.\nThere is no time limit but you will be timed. Enter 'r' when ready.")
    readyUp()

    nums = getNums(diff)
    print("\nAlright, the two numbers you will be multiplying are:\n"+str(nums[0])+"\n"+str(nums[1])+"\nEnter your response as an integer. You only have one chance to enter a number so make sure you're ready when you submit:")
    start = time.time()
    answer = getAnswer()
    end = time.time()

    expected = nums[0] * nums[1]
    results(int(answer), expected, round(end-start, 2))
    return

def division():
    print("\nWelcome to the division test! ")
    diff = getDifficulty()
    print("\nFor this test you will be given 2 integers in the range of 1 to "+str(diff)+" and will need to divide the first by the second together.")
    print("You will need to enter your response with the following format:\n\n[x]R[y]\n\nwhere '[x]' is the quotient and '[y]' is the remainder. If there is no remainder, simply put R0.\nThere is no time limit but you will be timed. Enter 'r' when ready.")
    readyUp()

    nums = [0] * 2
    nums = getNums(diff)
    print("\nAlright, the two numbers you will be adding are:\n"+str(nums[0])+"\n"+str(nums[1])+"\nYou only have one chance to enter a number so make sure you're ready when you submit:")
    start = time.time()
    # Custome getAnswer() for division
    answer = input()
    split = answer.split("R")
    q = split[0]
    r = split[1]
    while (q.isdigit() == False) or (r.isdigit() == False):
        print("Invalid input. Please try again.")
        answer = input().split("R")
        q = answer[0]
        r = answer[1]
    end = time.time()

    quotient = int(nums[0] / nums[1])
    remainder = nums[0] % nums[1]
    expected = str(quotient) + "R" + str(remainder)

    print("Expected: " + expected + "\nAnswer: " + answer)

    if answer == expected:
        print("\nContratulations! You answered correctly!\nYou got the correct answer of "+str(q)+"R"+str(r)+" in "+str(round((end-start),2))+" seconds")
    else:
        print("\nSorry, that isn't the correct answer. The correct answer was: "+str(q)+"R"+str(r))
    return

def main():
    print("\nWelcome to the Mental Math Minigame™\nIn this game you will choose an operation and a level of difficulty, and then will be supplied with 2 numbers to perform said operation with. \nEverything is done through the console, please format your responses as indicated.")

    done = False
    while done == False:
        print("OK, what operation would you like to perform? Type the letter corresponding to the operation as provided below")
        print("'A' for addition\n'S' for subtraction\n'M' for multiplication\n'D' for division")

        op = input().upper()
        match op:
            case 'A':
                addition()
            case 'S':
                subtraction()
            case 'M':
                multiplication()
            case 'D':
                division()
            case default:
                print("\nInvalid Selection")
        
        print("Would you like to continue? Type 'y' for yes or 'n' for no.")
        answered = False
        while answered == False:
            answer = input().lower()
            if answer == 'y':
                print("\nYou have answered yes! Good Luck!\n")
                answered = True
            elif answer == 'n':
                print("\nYou have answered no. Goodbye, hope you enjoyed!")
                done = True
                answered = True
            else:
                print("Invalid input, please try again")




main()
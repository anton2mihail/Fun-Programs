def digits(n) :
    if abs(n) < 10 :
        return 1
    else :
        num = 1
        while abs(n) >= 10:
            num = num + 1
            n = n / 10
        return num


def main() :
    sg = ""
    while sg != "Q" :
        try :
            sg = input("Enter an integer (to terminate, enter Q: ")
            if sg != "" :
                num = int(sg)
                ndig = digits(num)
                print("The number of digits in "+str(num)+" is "+str(ndig))
        except ValueError :
            print("Input error - retry.")


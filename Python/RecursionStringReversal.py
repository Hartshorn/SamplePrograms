def reverse(string):
    print("Got as an argument: ", string)

    if(len(string) == 1):
        print("Bad Case")
        return string
    else:
        newString = reverse(string[1:]) + string[0]
        print("Reassembling {} and {} int {}".format(string[1:], string[0], newString))
        return newString

string = input("What String: ")
print()
resultString = reverse(string)
print("The reverse of {} is {}".format(string, resultString))
              

#write a program to determine the character entered by the user
char=input("Press any key to check:")
if(char.isalpha()):
    print("The user entered a character")
    if(char.isdigit()):
        print("The user entered a number")
        if(char.isspace()):
            print("The user entered a white space character")
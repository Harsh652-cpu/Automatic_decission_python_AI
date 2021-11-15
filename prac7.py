#Write a prorgam to enter any character.If the entered character is in lowercase then convert it into uppercase and if it is an uppercase character,then convert it into lowercase character
ch=input("Enter the character:")
if(ch>="A" and ch<="Z"):
    ch=ch.lower()
    print("The entered character is in uppercase.In lowercase it is: "+str(ch))
else:
    ch=ch.upper()
    print("The entered character is in lowercase.In uppercase it is: "+str(ch))
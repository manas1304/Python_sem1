username=input("Enter the username:")
lst=list(map(str,input("Enter the last three passwords:").split()))
def passwordcheck(password,username,passlst):
    for i in passlst:
        if i==password:
            return "Password same as one of the last three passwords"
    if len(password)<10:
        return "Password must be at least 10 characters long!!"
    countupper=0
    countlower=0
    countdigit=0
    countspecial=0
    for j in password:
        if j.isupper():
            countupper+=1
        elif j.islower():
            countlower+=1
        elif j >= "0" and j <= "9":
            countdigit+=1
        else:
            countspecial+=1
    if countupper<2 :
        return "Password must contain at least 2 uppercase letters"
    if countlower<2:
        return "Password must contain at least 2 lowercase letters"
    if countdigit<2:
        return "Password must contain at least 2 digits"
    if countspecial<2:
        return "Password must contain at least 2 special characters"
    for k in range(len(password) - 3):
        if password[k] == password[k + 1] == password[k + 2] == password[k + 3]:
            return "No character should repeat more than three times in a row"
    for i in range(0,len(username)-2):
        if username[i:i+3] in password:
            return "The password should not contain any sequence of three or more consecutive characters from the username"
    return "True"
while True:
    password=input("Enter a password:")
    ans=passwordcheck(password,username,lst)
    if ans=="True" :
        print("Password accepted")
        break
    else:
        print(ans)
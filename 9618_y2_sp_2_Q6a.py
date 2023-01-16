#Members of a family use the same laptop computer. Each family member has their own password.
# To be valid, a password must comply with the following rules:
# 1 At least two lower-case alphabetic characters
# 2 At least two upper-case alphabetic characters
# 3 At least three numeric characters
# 4 Alpha-numeric characters only
# A function, ValidatePassword, is needed to check that a given password follows these rules.
# This function takes a string, Pass, as a parameter and returns a boolean value:
# • TRUE if it is a valid password
# • FALSE otherwise
# (a) Write pseudocode to implement the function ValidatePassword.




def ValidatePassword(Pass):
    valid = False
    sc = 0
    lc = 0
    uc = 0
    num = 0
    sc = 0
    # counts each number, capital, small and special charachter in string Pass
    for ch in Pass:
        if ch >= 'a' and ch <= 'z':
            lc += 1
        elif ch >= 'A' and ch <= 'Z':
            uc += 1
        elif ch >= '0' and ch <= '9':
            num += 1
        else:
            sc += 1
    # password validity rules
    # sc(special charachters) must be equal to zero as no special ch allowed
    if lc >= 2 and uc >= 2 and num >= 3 and sc == 0:
        valid = True
    else:
        valid = False
    return valid
        

password = input('Enter Password: ')
print(ValidatePassword(password))


#%%
print("Rules for making the password are: ")
print("    1. Password length should be in between 6-16(min 6 or max 16)")
print("    2. Password should compulsory have 1 digit")
print("    3. Password should contain any special characters from (@ ! # $ % & ^)")
print("")
print("")

special = ["@", "!", "#", "$", "%", "^"]
digit = False
special_character = False

user_password = input("Enter a password that you would remember and is valid by the above rules: ")

#%%

if len(user_password) >= 6 and len(user_password) <= 16:
    for letter in user_password:
        if letter.isdigit():
            digit = True
            break
    for letter2 in user_password:
        if letter in special:
            special_character = True
            break
else:
    if len(user_password) > 16:
        print("The password contains more than 16 characters.")
        for letter in user_password:
            if letter.isdigit():
                digit = True
                break
        for letter2 in user_password:
            if letter in special:
                special_character = True
                break
    else:
        print("The password contains less than 6 characters.")
        for letter in user_password:
            if letter.isdigit():
                digit = True
                break
        for letter2 in user_password:
            if letter in special:
                special_character = True
                break

#%%


if digit and special_character:
    print("Your password is valid.")
elif not digit and not special_character:
    print("The password contain neither a digit nor a special character.")
elif not digit:
    print("The password does not contain a digit.")
elif not special:
    print("The password does not contain a special character from (@ ! # $ % & ^).")

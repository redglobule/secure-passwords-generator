import secrets

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpha_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", "<", ">", ",", ".", "/", "?", "|", "\\", "`", "~"]

caracter_type = [num, alpha_lower, alpha_upper, special_characters]

while True:
    try:
        len_password = int(input("\nChoose the length of the password (minimum 14): "))
        
        if len_password >= 14:
            break
        else:
            print("You must choose a number greater than or equal to 14.\n")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")



def secure_password_generator(len_password):
    password = []
    
    for i in range(len_password):
        random_list = secrets.choice(caracter_type)
        random_caracter = secrets.choice(random_list)
        password.append(random_caracter)
        
    password = ''.join(str(c) for c in password)
    return password


def verification_password(password):
    verif_num = False
    verif_alpha_lower = False
    verif_alpha_upper = False
    verif_special_caracters = False
    for c in range(len(password)):
        if password[c] in num:
            verif_num = True
        elif password[c] in alpha_lower:
            verif_alpha_lower = True
        elif password[c] in alpha_upper:
            verif_alpha_upper = True
        elif password[c] in special_characters:
            verif_special_caracters = True
        else:
            return
    
    if verif_num == True and verif_alpha_lower == True and verif_alpha_upper == True and verif_special_caracters == True:
        return
    else:
        password = secure_password_generator(len_password)
        verification_password(password)
    

password = secure_password_generator(len_password)
verification_password(password)

print("Your", len_password, "secure characters password is :", password, "\n")
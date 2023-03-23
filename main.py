def encode(password):
    string_password = str(password)
    password_numbers = []
    encoded_password = ""

    for i in range(len(string_password)):
        password_numbers.append(string_password[i])
#appends password
    for i, digit in enumerate(password_numbers):
        password_numbers[i] = int(digit)

    for digit in password_numbers:
        if digit in range(0, 7):
            digit += 3
            encoded_password += str(digit)
        elif digit == 7:
            encoded_password += "0"
        elif digit == 8:
            encoded_password += "1"
        elif digit == 9:
            encoded_password += "2"
        elif digit == 0:
            encoded_password += "3"
#encodes password based on the digits range
    return encoded_password

def decode(encoded_password):
    arsenal = ''
    for i in secret:
        receiver = int(i)
        receiver -= 3
        if receiver < 0:
            receiver += 10
        ta_da += str(receiver)
    print(f"The encoded password is {encoded_password}, and the original password is {arsenal}")
    print("")

if __name__ == "__main__":
    stop_menu = False
    user_passcode = 0
    user_encoded_password = ""

    while stop_menu is False: # menu loop
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode \n3. Quit\n")
        user_choice = int(input("Please enter an option: "))
#prints menu options
        if user_choice == 1:
            user_passcode = str(input("Please enter your password to encode: "))
            user_encoded_password = encode(user_code)
            print("Your password has been encoded and stored!")

        elif user_choice == 2:
            decode(user_encoded_password)
        elif user_choice == 3:
            stop_menu = True
            break
        print()
#options of what happens based on user input

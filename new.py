#Lab-06 Version Control by Timothy Kareng
def encode(user_password):
    new_user_password = ""
    for i in range(len(user_password)):
        new_user_password = new_user_password + (str(int(user_password[i]) + 3))[-1]
    return new_user_password


def decode(encoded_password):
    pass


encoded_pass = ""
decoded_pass = ""


def main():
    menu = True
    while menu == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!\n")
        if menu_option == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass} \n")
        if menu_option == 3:
            menu = False


if __name__ == "main":
    main()
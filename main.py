# Soraya Sardine
def menu():
    print('\nMenu\n-------------\n')
    print('1. Encode\n2. Decode\n3. Quit\n')


def encode_password(password):
    password = password[:8]
    encode_res = [int(item) for item in password]
    encode_res = [(element + 3) % 10 for element in encode_res]
    return ''.join(str(num) for num in encode_res)


# def decode_password(password):
#     password = password[:8]
#     decode_res = [int(item) for item in password]
#     decode_res = [(element - 3) % 10 for element in decode_res]
#     return ''.join(str(num) for num in decode_res)




#My code
def decode_password(encoded_password):
    password = ""
    for digit in encoded_password:
        shifted_digit = str((int(digit) - 3) % 10)  # shift each digit down by 3 numbers
        password += shifted_digit
    return password




def main():
    encode = None
    while True:
        menu()
        user_option = int(input('Please enter an option: '))
        if user_option == 1:
            user_password_encode = input('Please enter your password has been encoded: ')
            encode = encode_password(user_password_encode)
            print('Your password has been encoded and stored!')
        elif user_option == 2:
            decode = decode_password(encode)
            print(f'The encoded password is {encode}, and the original password is {decode}.')
        elif user_option == 3:
            break
        else:
            print('Option not valid. Please try Again!')
            continue


if __name__ == '__main__':
    main()

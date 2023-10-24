def menu():
    print('\nMenu\n-------------\n')
    print('1. Encode\n2. Decode\n3. Quit\n')


def encode_password(password):
    password = password[:8]
    encode_res = [int(item) for item in password]
    encode_res = [(element + 3) % 10 for element in encode_res]
    return ''.join(str(num) for num in encode_res)


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
            print(f'The encoded password is {encode}, and the original password is .')
        else:
            break


if __name__ == '__main__':
    main()

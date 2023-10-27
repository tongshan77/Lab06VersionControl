def encode(password):
    password = list(password)
    psw = []
    for i in password:
        i = int(i)
        i += 3
        i = str(i)
        psw.append(i)
        encode_psw = "".join(psw)
    return encode_psw


# Hemanshu version of decode function
def decode(pwd):
    pwd = list(pwd)
    decoded_pwd_list = []
    for num in pwd:
        # first convert to int to add and the convert to str to append and then join together
        # everything the same except now num -= 3
        num = int(num)
        num -= 3
        num = str(num)
        decoded_pwd_list.append(num)
    
    decoded_pwd = "".join(decoded_pwd_list)

    return decoded_pwd


def main():
    print('Menu')
    print('')
    print('-------------')
    print('')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    while True:
        user_option = int(input('Please enter an option: '))
        if user_option == 1:
            password_num = input('Please enter your password to encode: ')
            encode_password_num = encode(password_num)
            print('Your password has been encoded and stored!')

        elif user_option == 2:
            print(f'The encoded password is {encode_password_num}, and the original password is {decode(encode_password_num)}')

        elif user_option == 3:
            print('Quit')
            break


if __name__ == '__main__':
    main()

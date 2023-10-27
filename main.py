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



def decode(password):
    password = list(password)
    psw = []
    for i in password:
        i = int(i)
        i = i - 3
        i = str(i)
        psw.append(i)
        decode_psw = "".join(psw)
    return decode_psw


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

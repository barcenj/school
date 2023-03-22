# menu prompt
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

# encrypts password
def encode(password):
    password = f'{password}'
    encode_pass = []
    for i in range(len(password)):
        string = int(password[i]) + 3
        string = f'{string}'
        encode_pass.append(string)
    encode_pass = ''.join(encode_pass)
    return encode_pass

if __name__ == '__main__':
    password = None
    while True:
        menu()
        op = input('Please enter an option: ')

        if op == '1':
            encode(password)
            print('Your password has been encoded and stored!')
            print()

        elif op == '2':
            print(f'The encoded password is {encode(password)}, and the original password is {password}')


        elif op == '3':
            break

        else:
            pass
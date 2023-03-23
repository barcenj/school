# menu prompt
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

# encrypts password
def encode(password):
    # convert int to string (assuming I made the input an int LOL I changed that)
    password = f'{password}'
    encode_pass = []
    for i in range(len(password)):
        # encryption operation is + 3 to each dig
        string = int(password[i]) + 3

        # Fix instances out of range (0,9)
        if string == 10:
            string = 0
        elif string == 11:
            string = 1
        elif string == 12:
            string = 2

        # convert back to string
        string = f'{string}'
        encode_pass.append(string)

    encode_pass = ''.join(encode_pass)
    return encode_pass

def decode(encode_pass):        # added decode function (caitlin guiang)
    list(encode_pass)
    orig_pass = ''
    for element in encode_pass:
        element = int(element)
        if element > 2:
            element -= 3
        elif element <= 2:
            element += 7
        orig_pass += str(element)
    return orig_pass

if __name__ == '__main__':
    password = None
    while True:
        menu()
        op = input('Please enter an option: ')

        # encoding tool
        if op == '1':
            password = input('Please enter your password to encode: ')
            encode(password)
            print('Your password has been encoded and stored!')
            print()

        # decoding tool
        elif op == '2':
            orig_pass = decode(encode(password))        # implementing decode function into main
            print(f'The encoded password is {encode(password)}, and the original password is {orig_pass}')

        elif op == '3':
            break

        # screw error messages ig idk
        else:
            pass
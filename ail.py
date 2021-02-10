# try to simulate the encryption algorithm used in modern comuters

import sys

private_key          = {'a':65,'b':66,'c':67,'d':68,'e':69,'f':70,'g':71,
                        'h':72,'i':73,'j':74,'k':75,'l':76,'m':77,'n':78,
                        'o':79,'p':80,'q':81,'r':82,'s':82,'t':83,'u':84,
                        'v':85,'w':86,'x':87,'y':88,'z':89,'0':90,'1':91,
                        '2':92,'3':93,'4':94,'5':95,'6':96,'7':97,'8':98,
                        '9':99}

password = '130142130154'


def encryption_algorithm(password_list):
    pass2 = ''
    for i in password_list:
        j = private_key[i]
        pass2 = pass2 + str(j*2)
    return pass2


def main():
    user_input = input('Enter the password: ')
    pass1 = list(user_input.lower())

    if encryption_algorithm(pass1) == password:
        print("ACCESS GRANTED")

    else:
        print("The password you have entered is incorrect\n")
        choice = input("Would you like to try again (y/n)")

        if choice == 'y':
            pass1 = ''
            pass2 = ''
            main()
        else:
            sys.exit()

main()

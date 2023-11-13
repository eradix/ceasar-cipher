from art import logo
from caesar_cipher import ceasars, get_user_choice, get_ceasar_cipher_data

if __name__ == '__main__':

    #print the logo
    print(logo)

    to_continue = True

    while to_continue:

        # get user inputs
        user_inputs = get_ceasar_cipher_data()

        # perform caesar cipher function
        ceasars(start_text=user_inputs['text_str'],
                 shift=user_inputs['shift'],
                 direction=user_inputs['direction'])

        # get user decision to continue app
        if get_user_choice() == False:
            to_continue = False

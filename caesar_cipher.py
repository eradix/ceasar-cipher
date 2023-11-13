import os

# list of alphabets
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# check if variable is valid integer
def is_valid_integer(variable):
    try:
        int_value = int(variable)
        return True
    except ValueError:
        return False

#ceasar function
def ceasars(start_text, shift, direction):
    end_text = ""
    if direction == 'decode':
        shift *= -1

    for char in start_text:
      #keep the number/symbol/space
      if not char in alphabet:
        end_text += char
      else:
        index = (alphabet.index(char) + shift) % len(alphabet)
        end_text += alphabet[index]

    print(f"The {direction}d text is '{end_text}'")
    print()

# get user decision to continue app
def get_user_choice():
    while True:
        user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# get user ceasar cipher datas
def get_ceasar_cipher_data():
   no_direction = True
   while no_direction:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      if direction in ['encode', 'decode']:
         no_direction = False
      else:
         print("Invalid input. Please enter 'encode' or 'decode'.")
      
   text = input("Type your message:\n").lower()

   not_integer = True
   while not_integer:
      shift = input("Type the shift number:\n")
      
      if is_valid_integer(shift):
         not_integer = False
      else:
         print("Invalid input. Please enter a number only")

   return {
      'direction' : direction,
      'text_str' : text,
      'shift' : int(shift)
   }


'''We define our own clean function to clear the screen'''
def clean():
    # For Windows
    if os.name == 'nt':
        os.system('cls')

    # For macOS and Linux
    else:
        os.system('clear')


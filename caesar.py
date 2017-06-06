def rotate_character(text, rot):
    text_new = ''
    num_char = 0
    char_new = ''
    lst_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lst_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in text:
        if char in lst_lower:
            num_char = alphabet_position(char)
            num_char += rot
            if num_char > 25:
                num_char = num_char % 25
            char_new = lst_lower[num_char]
            text_new += char_new
        elif char in lst_upper:
            num_char = alphabet_position(char)
            num_char += rot
            if num_char > 25:
                num_char = num_char % 25
            char_new = lst_upper[num_char]
            text_new += char_new
        else:
            text_new += char
    print(text_new)
    return text_new
        
def alphabet_position(letter):
    ascii_position = ord(letter)
        
    if ascii_position > 91:
        ascii_position -= 32
        
    position = ascii_position - 65
    return position

def encrypt(text, rot):
    text_new = rotate_character(text, rot)
    #print(text_new)
    return text_new

def main():    
    text = input("What is your string?")
    rot = int(input("How much do you want to rotate?"))
    #for char in text:
    encrypt(text, rot)

if __name__ == '__main__':
    main()
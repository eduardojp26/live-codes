def octal_string_decode(oct):
     #1. get rid of prefic '0'
    if oct[0] == '0':
        oct =oct[1:]

    bit_index = len(oct) - 1
    total=0

    for digit in oct:
     # 1st, digit ="5"
        total += int(digit) * pow(8, bit_index)
        bit_index -= 1
    return total


   
if __name__ == "__main__":
    octal_str = input()
    print(octal_string_decode(octal_str))



   # if hex[0:2] == '0x':
    #    hex = hex {}
    #starting from lab 4, in order to pass unit test, you should
    #always have if __name__ =='___main__':
    # function definions outside of it 

def dec_to_octal(decimal):
    res = ""
    while decimal != 0:
        remainder = decimal % 8
        decimal //= 8
        res = str(remainder) + res
    return res


if __name__=="__main__":
    dec = int(input())
    print(dec_to_octal(dec))

        
    
    
    
    
    
    
    
#     #1. get rid of prefic '0'
#     if oct[0] == '0':
#         oct =oct[1:]

# bit_index = len(oct)-1
# total=0

# for digit in oct:
#     # 1st, digit ="5"
#     total += int(digit) * pow(8, bit_index)
#     bit_index -= 1
#  return total


   




   # if hex[0:2] == '0x':
    #    hex = hex {}
    #starting from lab 4, in order to pass unit test, you should
    #always have if __name__ =='___main__':
    # function definions outside of it 

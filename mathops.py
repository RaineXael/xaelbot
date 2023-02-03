import math


def do_math(num1, op_char, num2):
    
    response_str = f"The answer to {num1}{op_char}{num2} is:"
    if op_char == '+':
        return response_str + str(num1+num2)
    elif op_char == '-':
        return response_str + str(num1-num2)
    elif op_char == '*':
        return response_str + str(num1*num2)
    elif op_char == '/' or op_char == "\\":
        if num2 != 0:
            return response_str + str(num1/num2)
    elif op_char == '^':
        return response_str + str(math.pow(num1, num2))
    return f"{op_char} wasn't recognized as an operation! Please enter any of the following: `-`,`+`,`*`,`\\`,`/`,`^`"

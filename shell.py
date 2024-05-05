
import basic

#the purpose of this is to have a infinite loop taht keeps taking in input and sending it to the basic
while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)

import os, sys
import random
import eel

eel.init('web')

def close_callback(arg1, arg2):
    sys.exit()

@eel.expose()
def pass_generate(pass_len, uppercase, lowercase, number, symbol):
    if not uppercase and not lowercase and not number and not symbol:
        eel.showError()
        return
    chars = []
    if uppercase:
        chars.extend(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    if lowercase:
        chars.extend(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    if number:
        chars.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if symbol:
        chars.extend(['!', '@', '$', '%', '&', '*', '(', ')', '-', '+', '?', '#'])
    password = ""
    for i in range(int(pass_len)):
        password = password +  chars[random.randint(0,len(chars) - 1)]
    eel.showPassword(password)


# start EEL App
if __name__ == '__main__':
    size = (800,720) #size of App Window
    app_options = {
      'mode' : "chrome",
      'close_callback' : close_callback,
      'port': 0
    }
    eel.start('index.html', options=app_options, size=size, suppress_error=True)


def requestData (message,validatorFunction):
    while True:
        value = input(message)

        if validatorFunction(value):

            if validatorFunction == validationInt:
                return int(value)
            return value.strip()

def validationInt(number):
    try:
        number = int(number)
        if number > 0:
            return True
        else:
            print("only values numbers bigger than 0 is accepted")
    except ValueError:
        print("Incorrect value")
        return False

def validationString(text):
    try:
        text = str(text)
        if text != "":
            return True
        else:
            print("Values cannot be empty")
    except ValueError:
        print("Incorrect value")
        return False
    
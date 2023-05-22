print("10" + 10)
try IOError:
    print('You have an input/output error')
    print('Did you check the file permissions?')
except IOError:
    print("You have an input/outpute error")
    print("Did you check the file permissions?")
except TypeError:
    print("You are using the wrong data types!")


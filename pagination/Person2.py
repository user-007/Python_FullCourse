class Person():

    def __init__(self, passcode):

        if passcode == 123:
            print("I am a secret agent!")
        else:
            self.report()


x = Person("John", "smith")
x.reveal()

class Password:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        digit = False
        upper = False

        for ch in self.password:
            if ch.isdigit():
                digit = True
            if ch.isupper():
                upper = True

        if len(self.password) >= 8 and digit and upper:
            print("Strong")
        else:
            print("Weak")


paswd = input("Enter password: ")
p = Password(paswd)
p.check_strength()
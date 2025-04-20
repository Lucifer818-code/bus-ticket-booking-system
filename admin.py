import csv

class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminRegistration(self):
        print("----------------------------------------------------------------")
        print()
        fname = "adminCredential.csv"
        with open(fname, 'a+', newline="") as f:
            w = csv.writer(f)
            self.username = input("Enter a UserName: ")
            self.password = input("Enter a Password: ")
            w.writerow([self.username, self.password])
            print("Registration Successfully!!")
        print("----------------------------------------------------------------")

    def adminlogin(self):
        actli = []
        fname = "adminCredential.csv"
        try:
            with open(fname, 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                for row in data:
                    actli.append(row)

            while True:
                print("----------------------------------------------------------------")
                print()
                self.username = input("Enter a UserName: ")
                self.password = input("Enter a Password: ")
                for cred in actli:
                    if self.username == cred[0] and self.password == cred[1]:
                        print("Login Successfully!!")
                        return True
                print("Invalid credentials, try again!")
                print("----------------------------------------------------------------")
                return False
        except FileNotFoundError:
            print("The file 'adminCredential.csv' does not exist.")
            return False

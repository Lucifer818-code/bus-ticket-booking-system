import csv

class TicketShow:
    def ticketshow(self):
        sh = []
        fname = "passenger Data.csv"
        try:
            with open(fname, 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                id = int(input("Enter Your Booking Id: "))
                for i in data:
                    if id == int(i[0]):
                        for j in i:
                            sh.append(j)
                        break
                else:
                    print("Booking Id not found!")

            if sh:
                print("------------------------------------------------------------------------------")
                print("                         Ezhil Bus Travel                               ")
                print("------------------------------------------------------------------------------")
                print()
                print("e_Ticket :", "Chennai              : Thambarm Road Kilambakkam")
                print("Phone No/Mob No             : 1234567890,0987654321")
                print()
                print(f"{sh[3]} -------------> {sh[4]}        Passenger Id: {sh[0]}")
                print()
                print(f"Passenger Name : {sh[1]}         Number of Passenger : {sh[2]}")
                print("______________________________________________________________________________")
                print()
                print(f"Date of Booking : {sh[5]}        Seat No : {sh[6]}")
                print()
                print(f"Bus Type : {sh[7]}")
                print(f"Bus Fare : {sh[8]}")
                print()
                print("------------------------------------------------------------------------------")
        except FileNotFoundError:
            print("The file 'passenger Data.csv' does not exist.")

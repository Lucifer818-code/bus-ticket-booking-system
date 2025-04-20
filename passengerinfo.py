import csv

class PassengerRegistraion:
    def __init__(self):
        self.passengerName = None
        self.nopassenger = None
        self.depraturelocation = None
        self.destinationlocation = None
        self.ddmmyy = None
        self.seatno = None
        self.bustype = None
        self.busfare = None
        self.autoinc = 1
        self.countcol = 0

    def getpassengerinfo(self):
        self.passengerName = input("Enter a Passenger Name: ")
        self.nopassenger = int(input("Enter a Number Of Passenger: "))
        print("1:Chennai")
        print("2:Pondycheery")
        print("3:Virudhachalam")
        print("4:Trichy")
        print("5:Madurai")
        print("6:Coimbatore")

        self.dl = int(input("Enter DepratureLocation: "))
        if self.dl == 1:
            self.depraturelocation = "Chennai"
        elif self.dl == 2:
            self.depraturelocation = "Pondycherry"
        elif self.dl == 3:
            self.depraturelocation = "Virudhachalam"
        elif self.dl == 4:
            self.depraturelocation = "Trichy"
        elif self.dl == 5:
            self.depraturelocation = "Madurai"
        elif self.dl == 6:
            self.depraturelocation = "Coimbatore"
        else:
            print("Choose Correct Choice!!")
        
        print("1:Chengapattu")
        print("2:Jayankondam")
        print("3:Ariyalur")
        print("4:Kumbakonam")
        print("5:Perambalur")
        print("6:Selam")

        self.dsl = int(input("Enter Destination Location: "))
        if self.dsl == 1:
            self.destinationlocation = "Chengapattu"
        elif self.dsl == 2:
            self.destinationlocation = "Jayankondam"
        elif self.dsl == 3:
            self.destinationlocation = "Ariyalur"
        elif self.dsl == 4:
            self.destinationlocation = "Kumbakonam"
        elif self.dsl == 5:
            self.destinationlocation = "Perambalur"
        elif self.dsl == 6:
            self.destinationlocation = "Selam"
        else:
            print("Choose Correct Choice!!")
        
        self.ddmmyy = input("Enter Date Of Booking Like DD-MM-YY: ")

        print("[1]_[2]_[3]_[4]_[5]_[6]_[7]_[8]_[9]_[10]_")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]_")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]_")

        seatNolist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.bookingseat = []
        while True:
            self.seatno = int(input("Enter a Seat Number & You Can Book Two Tickets: "))
            if self.seatno <= 30:
                if self.seatno in seatNolist:
                    self.bookingseat.append(self.seatno)
                    seatNolist.remove(self.seatno)
                else:
                    print("Ticket Already Booked!!")
                print("Do you want to Book another seat? Enter (yes/no)")
                y = input("Enter yes/no: ")
                if y.lower() != "yes":
                    break
            else:
                print("Don't Choose A Seat Number Which Is Not Available!!")
            
        print("1.AC BUS =500 Fare")
        print("2:NON AC BUS =300 Fare")
        self.bustype = int(input("Enter a Bus Type: "))
        if self.bustype == 1:
            self.SelectBustype = "AC BUS"
            self.busfare = self.nopassenger * 500
        elif self.bustype == 2:
            self.SelectBustype = "NON AC BUS"
            self.busfare = self.nopassenger * 300

class PassengerDataCsv(PassengerRegistraion):
    def saveinfo(self):
        try:
            fname = "passenger Data.csv"
            with open(fname, 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow([self.autoinc, self.passengerName, self.nopassenger, self.depraturelocation, 
                            self.destinationlocation, self.ddmmyy, self.bookingseat, self.SelectBustype, self.busfare])
            print("Data Saved Successfully!!")
        except Exception as e:
            print(f"Error saving data: {e}")

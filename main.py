from passengerinfo import *
from ticketshow import *
from admin import *

def run():
    print("---------------------------------------------------")
    print("           Welcome To Ezhil Bus Travel        ")
    print("---------------------------------------------------")
    print()

    adobj = Admin()
    while True:
        print("1:Admin Registration :")
        print("2:Admin Login :")
        ch = int(input("Choose Correct Option :"))

        if ch == 1:
            adobj.adminRegistration()
        elif ch == 2:
            if adobj.adminlogin():
                while True:
                    print("1:Passenger Registration :")
                    print("2:Show Ticket :")
                    ch = int(input("Choose Correct Option :"))
                    if ch == 1:
                        pd_oj = PassengerDataCsv()
                        pd_oj.getpassengerinfo()
                        pd_oj.saveinfo()
                    elif ch == 2:
                        obj = TicketShow()
                        obj.ticketshow()
                    else:
                        print("Invalid Option!")
            else:
                print("Login Failed!")
                break
        else:
            print("Invalid Option!")

run()

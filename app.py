from flat.flat import LandLord
from flat.flat_mate import Flatmate
from utils.calender import Calender


def validate_days_in_month(month, day):
    try:
        return int(day) <= Calender.get_days(month)
    except TypeError:
        raise TypeError("[-] Incorrect day for month entered")
    except ValueError:
        raise ValueError("[-] Incorrect value for the month entered")


def get_month_for_bill():

    is_month_correct = False

    while not is_month_correct:
        month = input("[+] Enter the billing month: ")

        if Calender.get_full_month_name(month):
            is_month_correct = True
        else:
            print("[-] Invalid month entered, try again...")
    return month


def get_amount_to_pay_for_month():

    while True:
        bill_amount = input("[*] Enter the amount for bill: ")
        try:
            return float(bill_amount)
        except ValueError:
            print("[-] The bill amount must a integer or float not a string..")


def get_house_mate_for_month_occuring(month):
    
    name = get_input("[*] Add the name of a housemate: ")
    running = True

    while running:
        
        days = get_input(f"[+] Add the number of days their stayed for the month of {month.title()}: ")

        if not validate_days_in_month(month, days):
            print("[-] Error, the day entered is greater the number of days in the month, try again... ")
        else:
            running = False
    return name, days
            

def get_input(question):

    while True:
        data = input(question)
        if data:
            return data
    

def main():

    month = get_month_for_bill()
    bill = get_amount_to_pay_for_month()

    flat = LandLord(float(bill), month)
    running = True

    while running:
        house_mate_name, days_stayed = get_house_mate_for_month_occuring(month)
        mate = Flatmate(house_mate_name, int(days_stayed))
        flat.add_flat_mate(mate)

        response = get_input("\n[*] Do you want to add another housemate, press (y/n):  ")
        if response.lower() == "y":
            continue
        elif response.lower() == "n":
            running = False

    print("Generating pdf income please wait...")
    flat.generate_bill_statement_pdf()


main()
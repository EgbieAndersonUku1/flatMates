from flat.flat import Flat
from flat.flat_mate import Flatmate


# create the flat mate
sam = Flatmate("sam", days_in_house=9)
peter = Flatmate("Egbie", days_in_house=30)
vicky = Flatmate("King", days_in_house=14)
# ricky = Flatmate("Ricky", days_in_house=10)
# sammy = Flatmate("Egbie", days_in_house=30)
# karen = Flatmate("Karen", days_in_house=30)


# Add the flat mate to the flat
flat = Flat(bill=1200, month_for_payment="June")

flat.add_flat_mate(sam)
flat.add_flat_mate(peter)
flat.add_flat_mate(vicky)
#flat.add_flat_mate(ricky)
#flat.add_flat_mate(sammy)
#flat.add_flat_mate(karen)


def run():
    print(f"Creating payment plan for {flat.get_number_of_flat_mate()} flatmates based on the days they stayed, please wait..")
    print("Done..")
    print("Generating bill statement in the form of a pdf, please wait..")

    flat.generate_bill_statement_pdf()
    print("Done, You bill statement has been created and is now in the root directory")


run()





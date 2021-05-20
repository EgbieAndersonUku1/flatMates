# billCalculator
A application that calculates the amount for a bill each flatmate should pay based on the number of days stayed in the house for that month


# The housemate bill problem
I was on the train a few days ago and they were two people arguing about the house bill. It seem that one of the 
housemate felt that he should not have to pay the full amount of the bill for that month because he was only staying
there for 15 days and then travelling for the rest of the month. He felt that he should only pay for the days 
he stayed and not for the full month.

After I got home I started thinking about this problem and thought what if they was a way to code this problem 
but not just for two housemates but for an unlimited number of housemates. The app will take a number of housemates 
and then calcuate the amount they have to pay based on the number of days there stayed for that month. 


## The housemate problem defined

## Assumptions
1. The bill is paid on a monthly basis
2. The full bill for the month must be paid not a penny less or not a penny above
3. They must be at least one person who stayed for the duration of the month

## The problem

Imagine if you own a house or a flat and because the bill/rent is too much you for you to handle you get 
in housemates. This act allows you to divide the bill equal among the housemates. For example, 
if the rent is £600 a month and they are two housemates plus yourself then each person will pay a 
total of £200 pound each which is perfect. But what if the housemates were been difficult and only
 wanted to pay for the number of days they stayed in the house for that month. 
 
How much will each housmate pay based on the days that stayed in that month?

For example:

    Number of housemates: 3
    Name of housemates: Sam, Egbie, King
    Month: June
    Number of days in month: 30
    Rent for that month: £1200

1. Sam   stays: 9/30 days
1. Egbie stays: 30/30  days
1. King  stays: 14/30 days

How much will each housemate pay based on the number of days their stayed?

In this above example each housemate will pay the following:

1. Sam   pays £120 for his 9 days stay
1. Egbie pays £893.33 for his 30 day stay
1. King  pays £186.67 for his 14 day stay


# The problem coded
Technology used Python



## Run the program
1. pip install -r requirements.txt to install the fpdf which a module that allows to create a pdf file.

Open the app.py page file.
    1. create a flatmate object, add name and the number of the days they stayed. You can create as many flatmate object as you want
    2. Create flat instant object and add the bill amount and the month. The month be the first three letters of the month e.g January -> jan, February -> feb
    3. Run the application and a nice formatted pdf will be generate with the amount each housemate has to pay


## The above example in code

### create the flatmate instance
    sam = Flatmate("sam", days_in_house=9)
    peter = Flatmate("Egbie", days_in_house=30)
    vicky = Flatmate("King", days_in_house=14)


## Add the flatmate instant to the flat instance
    flat = Flat(bill=1200, month_for_payment="June")

    flat.add_flat_mate(sam)
    flat.add_flat_mate(peter)
    flat.add_flat_mate(vicky)

Run the file and a new pdf fill should be generated in your root folder containing how much each house should pay

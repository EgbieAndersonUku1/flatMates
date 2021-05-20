from flat.bill import Bill
from utils.calender import Calender


class Flatmate(Bill):
    """Creates a flatmate who lives in the flat and shares the bill"""

    def __init__(self, name, days_in_house, bill_per_month=0, period=None):
        self.name = name
        self.__month_period = period
        self.days_in_house = days_in_house

        if self.__month_period:
            super().__init__(bill_per_month, self.__month_period)
            try:
                self.days_in_month = Calender.get_days(self.__month_period)
            except:
                raise "incorrect month"

        self.pay_bill_amount = bill_per_month

    def generate_bill_statement_pdf(self):
        pass

    def get_month(self):
        return self.__month_period.title() if self.__month_period else None

    def set_month_period(self, period):
        self.days_in_month = Calender.get_days(period)
        self.__month_period = period

    def get_days_not_in_flat(self):
        return self.days_in_month - self.days_in_house

    @property
    def bill_amount_to_pay(self):
        return round(self.pay_bill_amount, 2)

    def __repr__(self):
        return f"<Name: {self.name.title()}, " \
               f"Month: {self.__month_period}, " \
               f" Days stayed: {self.days_in_house} / out of {self.days_in_month}, " \
               f"Bill amount to pay: £{round(self.pay_bill_amount, 2)}>"


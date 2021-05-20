from flat.bill_statement import FlatMateBillStatementFields
from utils.calender import Calender
from utils.errors import NoHousmatesError, invalidMonthError
from utils.pdf_generator import PdfGenerator


class LandLord(Calender):

    def __init__(self, bill, month_for_payment):
        self._house_mates = []
        self.bill = bill

        if not self.get_days(month_for_payment):
            raise invalidMonthError("The month entered is incorrect")
        self.month_for_payment = month_for_payment

    def generate_bill_statement_pdf(self):

        names = ", ".join(self.get_all_flatmates_names())

        flat_bill = _FlatBillPDFGenerator(housemates=self, file_name="housemates_bill_statement.pdf")
        flat_bill.add_heading("Bill statements for housemates")
        flat_bill.add_address(FlatMateBillStatementFields.address)
        flat_bill.add_greeting(FlatMateBillStatementFields.greeting)
        flat_bill.add_subject(FlatMateBillStatementFields.subject)

        first_paragraph = FlatMateBillStatementFields.first_paragraph.format(names, self.bill,
                                                                       self.get_full_month_name(self.month_for_payment),
                                                                       self.get_number_of_flat_mate())

        flat_bill.add_body(first_paragraph)
        flat_bill.generate_pdf()

    def get_all_flatmates_names(self):
        return [house_mate.name.title() for house_mate in self._house_mates]

    def add_flat_mate(self, house_mate):
        self._house_mates.append(house_mate)

    def get_number_of_flat_mate(self):
        return len(self._house_mates)

    def bill_for_each_flat_mate(self):
        """"""
        payment_remaining = 0
        payment_for_each_house_mate = self.bill/self.get_number_of_flat_mate()
        flat_mates_who_stayed_the_full_month, house_mates = [], []

        for house_mate in self._house_mates:

            house_mate.bill = self.month_for_payment
            house_mate.set_month_period(self.month_for_payment)

            if not house_mate.get_days_not_in_flat():

                house_mate.pay_bill_amount = payment_for_each_house_mate
                flat_mates_who_stayed_the_full_month.append(house_mate)

            else:
                amount_to_pay = (house_mate.days_in_house / house_mate.days_in_month) * payment_for_each_house_mate
                payment_remaining += (payment_for_each_house_mate - amount_to_pay)
                house_mate.pay_bill_amount = amount_to_pay
                house_mates.append(house_mate)

        if payment_remaining:
            self._divide_remaining_bill_between_flat_mates_who_stayed_the_full_month(house_mates,
                                                                                     flat_mates_who_stayed_the_full_month,
                                                                                     payment_remaining)
        else:
            house_mates = flat_mates_who_stayed_the_full_month
        return house_mates

    def _divide_remaining_bill_between_flat_mates_who_stayed_the_full_month(self, house_mates,
                                                                            house_mates_who_stayed_the_full_course,
                                                                            payment_remaining):

        if house_mates_who_stayed_the_full_course:

            amount = payment_remaining / len(house_mates_who_stayed_the_full_course)

            for house_mate in house_mates_who_stayed_the_full_course:
                house_mate.pay_bill_amount = round((house_mate.pay_bill_amount + amount), 2)
                house_mates.append(house_mate)
        else:
            msg = "Could not calculate amount there must be at least one housemate who stayed for the duration of the month"
            raise NoHousmatesError(msg)


class _FlatBillPDFGenerator(object):

    def __init__(self, housemates, file_name, cell_height=17, cell_width=0, font_size=16):
        self.housemates = housemates
        self.file_name = file_name
        self.CELL_HEIGHT = cell_height
        self.CELL_WIDTH = cell_width
        self.SIZE = font_size
        self._pdf = PdfGenerator(self.file_name)

    def generate_pdf(self):
        self._pdf.generate()

    def add_address(self, address, font="Helvetica", style="B", size=18):
        self._pdf.change_font(font_family=font, style=style, size=size)
        self._pdf.insert_data_multiple_cell(self.CELL_WIDTH, self.CELL_HEIGHT + 1, data_txt=address)
        self._pdf.add_new_line()

    def add_heading(self, heading, font="Helvetica", style="BU", size=30, cell_height=30):
        self._pdf.change_font(font_family=font, style=style, size=size)
        self._pdf.insert_title(heading, cell_height=cell_height)
        self._pdf.add_new_line()

    def add_greeting(self, greeting):

        self._pdf.change_font("Arial", size=self.SIZE)
        self._pdf.change_font_color(0, 0, 0)
        self._pdf.insert_data_multiple_cell(self.CELL_WIDTH, self.CELL_HEIGHT, data_txt=greeting)

    def add_subject(self, subject, font_family="Arial"):
        self._pdf.change_font(font_family, size=self.SIZE)
        self._pdf.change_font_color(255, 0, 0)
        self._pdf.insert_data_multiple_cell(cell_width=0, cell_height=self.CELL_HEIGHT, data_txt=subject)

    def add_body(self, data):

        self._pdf.change_font_color(0, 0, 0)
        self._pdf.insert_data_multiple_cell(cell_width=0, cell_height=18, data_txt=data)
        self._pdf.add_new_line()
        self._create_table_header()
        self._create_table_data()
        self._add_second_paragraph()

    def _create_table_header(self):

        self._pdf.change_font(style="BIU")
        self._pdf.insert_data_single_cell(cell_width=100, cell_height=17, data_txt="Name")
        self._pdf.insert_data_single_cell(cell_width=160, cell_height=17, data_txt="Days stayed")

        self._pdf.insert_data_single_cell(cell_width=120, cell_height=17, data_txt="Month")
        self._pdf.insert_data_single_cell(cell_width=150, cell_height=17, data_txt="Price")
        self._pdf.add_new_line()

    def _create_table_data(self):

        house_mates = self.housemates.bill_for_each_flat_mate()
        self._pdf.change_font(style="I")
        self._pdf.add_new_line()

        for flat_mate in house_mates:

            self._pdf.insert_data_single_cell(cell_width=120, cell_height=17, data_txt=flat_mate.name.title()[:9])
            self._pdf.insert_data_single_cell(cell_width=140, cell_height=17, data_txt=str(flat_mate.days_in_house))
            self._pdf.insert_data_single_cell(cell_width=120, cell_height=17, data_txt=str(flat_mate.get_month())[:3].title())
            self._pdf.insert_data_single_cell(cell_width=150, cell_height=17, data_txt="£" + str(flat_mate.bill_amount_to_pay))

            self._pdf.add_new_line()

    def _add_second_paragraph(self):
        self._pdf.change_font("Arial", size=self.SIZE)
        self._pdf.insert_data_multiple_cell(cell_width=0, cell_height=17, data_txt=FlatMateBillStatementFields.second_paragraph)


from fpdf import FPDF


class PdfGenerator(object):
    """
    Allows a pdf file to be created. The user of class can use the various methods
    available to manually create data in a given Pdf file. For example by calling
    the title method the user can add a title to the top of the page or change
    the color by calling the color method. The class also allows the use to add
    a single line of data to a cell but to add multiple data to a cell the
    insert_data_multiple_cell must be called
    """

    def __init__(self, file_name, font_family="Arial", size=10, style="B"):
        self.file_name = file_name
        self._pdf = FPDF(unit="pt", format="A4")
        self._pdf.add_page()
        self._pdf.set_font(family=font_family, size=size, style=style)

    def generate(self):
        """when called this creates the full pdf file and stores it in the root folder."""
        self._pdf.output(self.file_name)

    def change_font_color(self, red: int, green: int, blue: int) -> None:
        """change_font_color(red:int, green: int, blue: int)"

           Uses the RGB color system to change the font color of a text.
           In order to change the text of a color this method must be
           called first then unless this is called again and new color
           system added any text added will be the color that was set
           when this method was called
        """
        self._pdf.set_text_color(r=red, g=green, b=blue)

    def change_font(self, font_family="Arial", style="", size=16):
        """change_font(font_family: str, style:str, size: int) -> returns None

           When this is called allows the font text to be set. This style
           and the size of the font can also be set.

           :parameter

                style: The style takes three options
                    B: Bold
                    I: Italic
                    U: Underline

                    The style can also be combined in the following ways

                    For example:
                        BI: This makes the text bold and italic
                        BU: This makes the text bold and then underline
                        BIU: This makes the text bold, italic and then underlines the text

        """
        self._pdf.set_font(family=font_family, style=style, size=size)

    def insert_title(self, title, cell_height, cell_width=0, border=0, align="C"):
        """insert_title(title: str, cell_height:int, cell_width: int, border: int, align: str)


        """
        self._pdf.cell(cell_width, cell_height, txt=str(title), border=border, align=align)

    def insert_data_multiple_cell(self, cell_width, cell_height, data_txt, align="L", border=0):
        self._pdf.multi_cell(w=cell_width, h=cell_height, txt=str(data_txt), border=border, align=align)

    def insert_data_single_cell(self, cell_width, cell_height, data_txt, align="L", border=0):
        self._pdf.cell(cell_width, cell_height, data_txt, align=align, border=border)

    def add_new_line(self):
        self._pdf.ln()

    def add_img(self, img, width, height):
        self._pdf.image(img, w=width, h=height)
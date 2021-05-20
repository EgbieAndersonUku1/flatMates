class Calender(object):
    months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31,
              "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31,
               "Nov": 30, "Dec": 31}

    @staticmethod
    def get_days(month):
        return Calender.months.get(month[:3].title())
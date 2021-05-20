class Calender(object):
    months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31,
              "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31,
               "Nov": 30, "Dec": 31}

    full_month = {"Jan": "January", "Feb": "February", "Mar": "March",
                  "Apr": "April", "May": "May", "Jun": "June", "Jul": "July",
                  "Aug": "August", "Sep": "September", "Oct": "October",
                  "Nov": "November", "Dec": "December"
    }

    @classmethod
    def get_days(cls, month):
        return Calender.months.get(month[:3].title())

    @classmethod
    def get_full_month_name(cls, month):
        return cls.full_month.get(month[:3].title())
import datetime

class EnterData:
    @staticmethod
    def input_int(min_variant, max_variant):
        num = 0
        try:
            num = int(input())
        except ValueError:
            raise RuntimeError("This is not a number.")
        except Exception:
            raise RuntimeError("Something went wrong.")
        
        if num < min_variant or num > max_variant:
            raise RuntimeError("You entered an invalid value.")
        
        return num

    @staticmethod
    def input_long(min_variant, max_variant):
        num = 0
        try:
            num = int(input())
        except ValueError:
            raise RuntimeError("This is not a number.")
        except Exception:
            raise RuntimeError("Something went wrong.")
        
        if num < min_variant or num > max_variant:
            raise RuntimeError("You entered an invalid value.")
        
        return num

    @staticmethod
    def input_string():
        try:
            string_input = input()
        except Exception:
            raise RuntimeError("Something went wrong.")
        
        if not string_input:
            raise RuntimeError("You must enter something.")
        
        return string_input

    @staticmethod
    def input_date():
        date_input = input()
        try:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            raise RuntimeError("You must enter a valid date (yyyy-MM-dd format).")
        except Exception:
            raise RuntimeError("Something went wrong.")
        
        return date

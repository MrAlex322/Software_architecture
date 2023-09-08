import datetime
from Core.Customer import Customer
from ClientApplication.Authentication import Authentication

class Start(EnterData):
    def __init__(self):
        self.customer = None
        self.ticketRouteNumber = 0
        self.ticketDate = None

    def run_login_register_menu(self):
        run = True
        while run:
            self.print_message_line("Application for buying bus tickets")
            self.print_message_line("This is a test version. The database is not available in full mode.")
            self.print_message_line("To login, enter 1\nTo register, enter 2\nTo exit, enter 0")
            try:
                choice = self.input_int(0, 2)
            except RuntimeError as ex:
                print(ex)
                continue
            print("=====================================================================================")
            run = self.run_login_register_menu_choice_logic(choice)

    def run_login_register_menu_choice_logic(self, choice):
        if choice == 1:
            self.login()
            if not self.customer.get_user():
                return True
            else:
                self.run_buying_menu()
                return True
        elif choice == 2:
            self.register()
            if not self.customer:
                return True
            else:
                self.run_buying_menu()
                return True
        else:
            return False

    def login(self):
        self.print_message_line("This is a test version. The database is not available in full mode.")
        self.print_message_line("Login")
        print("User name: ", end="")
        user_name = self.input_string()
        print("Password: ", end="")
        password_hash = hash(self.input_string())
        print("=====================================================================================")
        print("Enter the system... ", end="")
        self.customer = Customer()
        try:
            self.customer.set_user(Authentication.authentication(self.customer.get_user_provider(), user_name, password_hash))
        except RuntimeError as ex:
            print("FAIL")
            print(ex)
            print("=====================================================================================")
            return
        self.print_message_line("OK")

    def register(self):
        self.print_message_line("This is a test version. The database is not available in full mode.")
        self.print_message_line("Register")
        print("Enter user name: ", end="")
        user_name = self.input_string()
        print("Enter password: ", end="")
        password_hash = hash(self.input_string())
        print("Repeat password: ", end="")
        password_hash2 = hash(self.input_string())
        if password_hash != password_hash2:
            print("=====================================================================================")
            self.print_message_line("Passwords do not match. Exit register.")
            return
        print("Enter card number: ", end="")
        card_number = self.input_long(1, 9999999999999999)
        print("=====================================================================================")
        print("Register the system... ", end="")
        self.customer = Customer()
        try:
            id = self.customer.get_user_provider().create_client(user_name, password_hash, card_number)
            self.customer.set_user(Authentication.authentication(self.customer.get_user_provider(), user_name, password_hash))
        except RuntimeError as ex:
            print("FAIL")
            print(ex)
            print("=====================================================================================")
            return
        self.print_message_line(f"OK. User {self.customer.get_user().get_user_name()} with ID {id} added to the database.")

    def run_buying_menu(self):
        run = True
        while run:
            self.print_message_line(f"Application for buying bus tickets. | User {self.customer.get_user().get_user_name()} |")
            self.print_message_line("To select route number and print all tickets, enter 1\n" +
                                     "To logout, enter 0")
            try:
                choice = self.input_int(0, 1)
            except RuntimeError as ex:
                print("==============================================================================")
                self.print_message_line(ex)
                continue
            print("=====================================================================================")
            run = self.run_buying_menu_choice_logic(choice)

    def run_buying_menu_choice_logic(self, choice):
        if choice == 1:
            self.ticket_route_number = self.run_select_route_menu()
            if self.ticket_route_number > 0:
                self.ticket_date = self.run_select_date()
                if self.ticket_date:
                    try:
                        self.customer.set_selected_tickets(self.customer.search_ticket(self.ticket_date, self.ticket_route_number))
                    except RuntimeError as ex:
                        self.print_message_line(ex)
                        return True
                    self.print_all_tickets(self.customer.get_selected_tickets())
                    self.buy_ticket_menu()
                    return True
                return True
            return True
        else:
            return False

    def run_select_route_menu(self):
        self.print_message_line(f"Input route number and date. | User {self.customer.get_user().get_user_name()} |")
        print("Route number > ", end="")
        try:
            num_route = self.input_int(1, 2)
        except RuntimeError as ex:
            self.print_message_line(ex)
            return -1
        print("=====================================================================================")
        return num_route

    def run_select_date(self):
        print("Date (format: YYYY-MM-DD) > ", end="")
        try:
            date = self.input_date()
        except RuntimeError as ex:
            self.print_message_line(ex)
            return None
        print("=====================================================================================")
        return date

    def print_all_tickets(self, ticks):
        for t in ticks:
            print(t)
        print("=====================================================================================")

    def buy_ticket_menu(self):
        self.print_message_line(f"Confirm to buy. | User {self.customer.get_user().get_user_name()} |")
        print(f"To buy a ticket for bus route {self.ticket_route_number} on {self.ticket_date}, enter \"Yes\" > ", end="")
        answer = self.input_string()
        print("=====================================================================================")
        self.buy_ticket_menu_confirm_logic(answer)

    def buy_ticket_menu_confirm_logic(self, answer):
        if answer.upper() == "YES":
            for t in self.customer.get_selected_tickets():
                if t.get_date() == self.ticket_date and t.get_route_number() == self.ticket_route_number and t.get_valid():
                    try:
                        flag = self.customer.buy_ticket(t)
                    except RuntimeError as ex:
                        self.print_message_line(ex)
                        return
                    if flag:
                        self.print_message_line(t.to_print())

    def print_message_line(self, message):
        print(message)
        print("=====================================================================================")




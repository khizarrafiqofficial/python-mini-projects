class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.account = None

    def create_account(self, account_number, initial_balance=0):
        self.account = Account(account_number, self, initial_balance)
        print(f"Account created successfully for {self.name}. "
              f"\nAccount Number: {account_number}, Initial Balance: Rs. {initial_balance:.2f}")
        return self.account

    def display_customer_info(self):
        print(f"\nCustomer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Rs. {amount:.2f} deposited successfully. New Balance: Rs. {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
            return
        self.balance -= amount
        print(f"Rs. {amount:.2f} withdrawn successfully. New Balance: Rs. {self.balance:.2f}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Current Balance: Rs. {self.balance:.2f}")


customer1 = Customer(customer_id=101, name="Khizar Rafiq", email="krkhizar@gmail.com")
customer1.display_customer_info()

account1 = customer1.create_account(account_number="ACC1001", initial_balance=5000)

account1.deposit(2000)

account1.withdraw(1500)

account1.withdraw(100000)

account1.display_balance()
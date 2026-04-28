from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.branches = []
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)
        branch.set_opening_time("9:00")

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)
            customer.set_new_customer(address="NO ADDRESS", phone_number="NO PHONE NUMBER")

    def add_interest(self, account: Account):
        account.add_interest()

    def add_funds(self, account: Account, amount: float):
        account.add_funds(amount)

    def close_account(self, account: Account):
        account.close_account()
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.add_staff_member(staff)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.remove_staff_member(staff)
        to_branch.add_staff_member(staff)

    def change_opening_time(self, branch: Branch, time: str):
        branch.set_opening_time(time)

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.set_pay_date_by_staff_category(staff_category=staff_category, date=date)

class GroupExpenses:
    def __init__(self, members):
        self.members = members
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_expenses(self):
        total_amount = {}
        for member in self.members:
            total_amount[member] = 0

        for expense in self.expenses:
            for member in expense['members']:
                total_amount[member] -= expense['amount']/len(expense['members'])

            total_amount[expense['person']] += expense['amount']

        return total_amount

def main():
    n = int(input("Enter the number of groups: "))

    for i in range(n):
        print(f"\nGroup {i + 1}:")
        members = list(map(str, input("Enter the members separated by a space: ").strip().split()))
        g = GroupExpenses(members)
        
        m = int(input("Enter the number of expenses: "))
        for j in range(m):
            expense = {}
            expense['person'] = input("Enter the name of the person who paid the expense: ")
            expense['amount'] = float(input("Enter the amount of the expense: "))
            expense['members'] = list(map(str, input("Enter the names of the members for this expense separated by a space: ").strip().split()))
            g.add_expense(expense)

        expenses = g.calculate_expenses()
        for member, amount in expenses.items():
            print(f"{member} gets {amount}")

if __name__ == "__main__":
    main()

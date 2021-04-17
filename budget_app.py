#create a budget that can instantiate objects based on different categories
#the user should be able to deposit funds into each of these categories
#the user should be able to withdraw funds from the different categories
#the budget should be able to compute the categories
#the user should be able to transer funds among the categories

class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        old_balance = self.balance
        self.balance = self.balance + amount

        return f'old balance: {old_balance}, New balance: {self.balance}'

    def withdraw(self, amount):
        old_balance = self.balance
        if self.balance < amount:
            print('You do not have sufficient funds')
        else:
            self.balance = self.balance - amount
            return f'old balance: {old_balance}, New balance: {self.balance}'

    def get_balance(self):
        feedback = f'Your budget app balance is {self.balance}'
        return feedback

    def transfer(self, amount, transfer_to):
        if self.balance < amount:
            print('You do not have sufficient funds')

        elif transfer_to.name == self.name:
            print("You can not transfer to yourself.")

        else:
            self.balance = self.balance - amount
            transfer_to.balance = transfer_to.balance + amount

            feedback = f'You transferred ${amount} from {self.name} to {transfer_to.name} \n'
            feedback += f'The balance for {self.name} is now {self.balance} \n'
            feedback += f'The balance for {transfer_to.name} is now {transfer_to.balance}'
            return feedback


food_budget = Budget('food', 4000)
clothing_budget = Budget('clothing', 3000)
entertainment_budget = Budget('Entertainment', 2000)

food_budget.deposit(1500)

food_budget.withdraw(amount=500)

food_budget.transfer(200, entertainment_budget)

food_budget.get_balance()
clothing_budget.get_balance()
entertainment_budget.get_balance()

print(food_budget.transfer(300, entertainment_budget))
print("==" * 20)
print(clothing_budget.transfer(300, food_budget))
print("==" * 20)
print(entertainment_budget.transfer(300, clothing_budget))
print("==" * 20)
print(food_budget.transfer(300, food_budget))
print("==" * 20)
print(food_budget.transfer(30000, clothing_budget))


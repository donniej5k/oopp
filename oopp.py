# Task 1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes for category name and allocated budget
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Task 2: Implement Getters and Setters
    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget  # Reset remaining budget on new allocation
        else:
            raise ValueError("Allocated budget must be a positive number")

    # Task 3: Add Budget Functionality
    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be a positive number")
        if amount > self.__remaining_budget:
            raise ValueError("Insufficient budget to cover this expense")
        self.__remaining_budget -= amount

    # Task 4: Display Budget Details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

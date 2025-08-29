# Base Class
class Person:
    def __init__(self, name, email):
        self._name = name        # protected attribute (encapsulation)
        self._email = email      # protected attribute

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")


# Derived Class (Inheritance)
class Customer(Person):
    def __init__(self, customer_id, name, email):
        super().__init__(name, email)  # call parent constructor
        self.customer_id = customer_id

    # Polymorphism: overriding method
    def display_info(self):
        print("Customer Information:")
        print(f"Customer ID: {self.customer_id}")
        super().display_info()   # reuse parent method


# Another Derived Class
class Employee(Person):
    def __init__(self, employee_id, name, email, job_title):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.job_title = job_title

    # Polymorphism: same method name, different behavior
    def display_info(self):
        print("Employee Information:")
        print(f"Employee ID: {self.employee_id}")
        print(f"Job Title: {self.job_title}")
        super().display_info()


# --- Test Polymorphism ---
people = [
    Customer(101, "Alice Johnson", "alice@example.com"),
    Employee(201, "Bob Smith", "bob@example.com", "Manager")
]

# Same method call -> different behavior depending on object type
for person in people:
    person.display_info()
    print("-" * 30)

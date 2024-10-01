# Define a parent class
class Parent:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"My name is {self.name}")

    def display_message(self):
        print("This is the parent class.")

# Define a child class that inherits from the parent class
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent constructor
        self.age = age

    def show_age(self):
        print(f"My age is {self.age}")

    # Overriding the parent method
    def display_message(self):
        print("This is the child class, overriding the parent class.")

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Create an instance of the Parent class
    parent_instance = Parent("Alice")
    parent_instance.show_name()
    parent_instance.display_message()

    print("\n---\n")

    # Create an instance of the Child class
    child_instance = Child("Bob", 10)
    child_instance.show_name()
    child_instance.show_age()
    child_instance.display_message()

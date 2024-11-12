# Create user-defined funtions

# Defined a non-value returning function
def my_animal(name, sound, pound_food):
    print(f"The {name} makes a {sound} noise!")
    print(f"The {name} eats {pound_food} pounds of food a day")
    print(f"The {name} eats {(pound_food * 7):.2f} pounds of food a week")

def getName():
    name = input("Enter your name: ")
    return name + "*******"

def displayName(first):
    lastName = input("Enter your Last name: ")
    fullName = first + " " + lastName
    return fullName






# Create a main function - all logic goes here
def main():
    print("The main function is executing!")
    print()
    # Call the my_animal function
    my_animal("Lion", "rarwwwwrr", 20.5)
    print()
    my_animal("Mouse", "ekekekekkk", 0.2)

    # Call the value-returning function
    myName = getName()
    print(myName)
    print()
    print(displayName(myName))

# Call the main function
if __name__ == "__main__":
    main()
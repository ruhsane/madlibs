def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def story():
    name = user_input("Enter a name: ")
    food = user_input("Enter a food: ")
    noun = user_input("Enter a noun: ")

    anotherNmae = user_input("Enter another name: ")


    print(name+ " was eating " + food + ", and " + name + " accidently spilled the " + food + " on Joshua's face. Joshua got pissed and started throwing " +noun + " at " + name + ".")

story()

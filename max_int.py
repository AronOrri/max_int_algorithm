# 1) The user enters an inital number, and changes max to it
# 2) If the number is not negative then another should be entered otherwise go to step 5
# 3) Check which of the entered numbers are larger and change the max to the larger one
# 4) Go back to step 2
# 5) End the calcutlations

num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int 
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if max_int < num_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line

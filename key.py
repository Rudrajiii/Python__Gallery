import random

# Your list of values as strings
my_list = ["value1", "value2", "value3", "value4", "value5"]

# Specify how many values you want to select
num_values_to_select = input("Enter the num of key:")

# Use random.sample() to select num_values_to_select elements randomly
selected_values = random.sample(my_list, int(num_values_to_select))
out_put="/".join(selected_values)

# Print the selected values
print(out_put)




   

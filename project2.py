#not an user friendly
box=[]
def modu_as(n):

    for i in range(n):
        box.append(i)  # Append i to the list

    a = int((n + 1) / 2)  # Convert the result to an integer
    b = int((n / 2 + (n / 2 + 1)) / 2)  # Convert the result to an integer

    if n % 2 == 0:  # Check if n is even
        print("median is:", (box[a - 1] + box[a]) / 2)  # Calculate and print median for even length
    else:
        print("median is:", box[b])  # Print median for odd length


modu_as(10)

#user friendly
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        middle_right = n // 2
        middle_left = middle_right - 1
        median = (numbers[middle_left] + numbers[middle_right]) / 2
        
    return median

def main():
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        input_numbers = [float(x) for x in input_str.split()]
        print(input_numbers)
        
        median = calculate_median(input_numbers)
        print("The median is:", median)
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")

if __name__ == "__main__":
    main()





    
    



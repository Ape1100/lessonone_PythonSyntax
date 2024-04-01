#Question_One 
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")
    
#Question_Two
    #<span> tags and class="hljs-number" are HTML and NOT recognized by python code
Pi_value = 3.14
userAge = 25
user_location = "New York"
MAXLIMIT = 1000

#Question_Three

variable_a = "Hello, World!" #string type
variable_b = 23 #integer
variable_c = 3.14  #Float 
variable_d = True   #boolean 

print(variable_a)  # Output: Hello, World!
print(variable_b)  # Output: 23
print(variable_c)  # Output: 3.14
print(variable_d)  # Output: True

#Question 4 - Arithmatic functions 

#task_one-print out grocery list and total for all items
butter = 3.00
corn = 7.00
juice = 10.00
popcorn = 25.00
beans = 15.00
rice = 12.50 

# Define the prices of the items
butter_price = 3.00
corn_price = 7.00
juice_price = 10.00
popcorn_price = 25.00
beans_price = 15.00
rice_price = 12.50

# Calculate the total cost
total_cost = butter_price + corn_price + juice_price + popcorn_price + beans_price + rice_price

# Print the total cost
print("Total cost of butter, corn, juice, popcorn, beans, and rice:", total_cost)

#task_two calculat bank interest 

# intital amount in bank
initial_amount = 10000  #Initial amount

# yearly interest rate 
yearly_interest_rate = 0.07  # 7% interest rate

# total amount for one year
total_amount = initial_amount + (initial_amount * yearly_interest_rate)

# total amount after one year
print("Total amount of cash in bank after one year of interest:", total_amount)

#Question 5 Understanding Assignments and Comparisons 

#task one Value Swapping 
# insital values 
a = 5
b = 10

print("Initial values: a =", a, ", b =", b)
a, b = b, a
print("Values after swapping: a =", a, ", b =", b)
if a == 10 and b == 5:
    print("Values have been successfully swapped.")
else:
    print("Values have not been swapped correctly.")






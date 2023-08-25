# Q 1:
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# number = int(input("Enter a number: "))
# print("Factorial of", number, "is", factorial(number))

# Q 2:
# def sum_even_numbers(numbers):
#     sum = 0
#     for num in numbers:
#         if num % 2 == 0:
#             sum += num
#     return sum

# Q 3:
# def is_palindrome(input_string):
#     # Remove spaces and convert to lowercase
#     input_string = input_string.replace(' ', '').lower()
    
#     # Reverse the string
#     reversed_string = input_string[::-1]
    
#     # Check if the original string is the same as the reversed string
#     if input_string == reversed_string:
#         return True
#     else:
#         return False

# Accept input from the user
# user_input = input("Enter a string: ")

# # Check if the input is a palindrome
# if is_palindrome(user_input):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# Q 4:
# def find_primes(n):
#     primes = []
#     for num in range(2, n+1):
#         is_prime = True
#         for i in range(2, int(num/2)+1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes

# # Q 5:
# def calculator():
#     print("Welcome to the calculator!")
#     print("Please enter two numbers:")
#     num1 = float(input("Number 1: "))
#     num2 = float(input("Number 2: "))

#     print("Select an operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = int(input("Enter your choice (1-4): "))

#     if choice == 1:
#         result = num1 + num2
#         print("The result of addition is:", result)
#     elif choice == 2:
#         result = num1 - num2
#         print("The result of subtraction is:", result)
#     elif choice == 3:
#         result = num1 * num2
#         print("The result of multiplication is:", result)
#     elif choice == 4:
#         if num2 != 0:
#             result = num1 / num2
#             print("The result of division is:", result)
#         else:
#             print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid choice!")

# calculator()

# Q 6:
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))

# Q 7:
# import random
# import string

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# password = generate_password(10)
# print(password)

# Q 8:
# import csv

# def calculate_stats(csv_file, column_name):
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
#         column_values = []
#         for row in reader:
#             column_values.append(float(row[column_name]))
        
#         average = sum(column_values) / len(column_values)
#         maximum = max(column_values)
#         minimum = min(column_values)
        
#         return average, maximum, minimum

# csv_file = 'data.csv'
# column_name = 'column_name'

# average, maximum, minimum = calculate_stats(csv_file, column_name)
# print(f"Average: {average}")
# print(f"Maximum: {maximum}")
# print(f"Minimum: {minimum}")

# Q 9:
# questions = [
#     "What is the capital of France?",
#     "Which planet is known as the Red Planet?",
#     "Who painted the Mona Lisa?"
# ]

# options = [
#     ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
#     ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
#     ["A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo"]
# ]

# answers = ["A", "A", "A"]

# score = 0

# for i in range(len(questions)):
#     print(questions[i])
#     for option in options[i]:
#         print(option)
#     user_answer = input("Enter your answer (A, B, C, or D): ")
#     if user_answer.upper() == answers[i]:
#         score += 1

# print("Your final score is:", score)

# # Q 12:
# def find_second_largest_smallest(numbers):
#     if len(numbers) < 2:
#         return "Not enough numbers in the list"
#     sorted_numbers = sorted(numbers)
#     second_smallest = sorted_numbers[1]
#     second_largest = sorted_numbers[-2]
#     return second_smallest, second_largest

# numbers = [5, 10, 1, 8, -3, 9]
# print(find_second_largest_smallest(numbers))
# # Output: (1, 9)

# numbers = [1, 1, 1, 1, 1]
# print(find_second_largest_smallest(numbers))
# # Output: (1, 1)

# numbers = [3, 2]
# print(find_second_largest_smallest(numbers))
# # Output: Not enough numbers in the list

# Q 13:
# import random

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Generate a random list of integers
# random_list = [random.randint(1, 100) for _ in range(10)]

# print("Original list:", random_list)

# # Sort the list using Bubble Sort
# bubble_sort(random_list)

# print("Sorted list:", random_list)

# Q 14:
# import math

# def find_prime_factors(num):
#     # Check for divisibility by 2
#     while num % 2 == 0:
#         print(2)
#         num = num // 2

#     # Check for divisibility by odd numbers starting from 3
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         while num % i == 0:
#             print(i)
#             num = num // i

#     # If the remaining number is greater than 2, it is a prime factor
#     if num > 2:
#         print(num)

# # Example usage:
# find_prime_factors(56)

# Q 16:
# Set up the game board as a list
# board = ["-", "-", "-",
# 		"-", "-", "-",
# 		"-", "-", "-"]

# # Define a function to print the game board
# def print_board():
# 	print(board[0] + " | " + board[1] + " | " + board[2])
# 	print(board[3] + " | " + board[4] + " | " + board[5])
# 	print(board[6] + " | " + board[7] + " | " + board[8])

# # Define a function to handle a player's turn
# def take_turn(player):
# 	print(player + "'s turn.")
# 	position = input("Choose a position from 1-9: ")
# 	while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
# 		position = input("Invalid input. Choose a position from 1-9: ")
# 	position = int(position) - 1
# 	while board[position] != "-":
# 		position = int(input("Position already taken. Choose a different position: ")) - 1
# 	board[position] = player
# 	print_board()

# # Define a function to check if the game is over
# def check_game_over():
# 	# Check for a win
# 	if (board[0] == board[1] == board[2] != "-") or \
# 	(board[3] == board[4] == board[5] != "-") or \
# 	(board[6] == board[7] == board[8] != "-") or \
# 	(board[0] == board[3] == board[6] != "-") or \
# 	(board[1] == board[4] == board[7] != "-") or \
# 	(board[2] == board[5] == board[8] != "-") or \
# 	(board[0] == board[4] == board[8] != "-") or \
# 	(board[2] == board[4] == board[6] != "-"):
# 		return "win"
# 	# Check for a tie
# 	elif "-" not in board:
# 		return "tie"
# 	# Game is not over
# 	else:
# 		return "play"

# # Define the main game loop
# def play_game():
# 	print_board()
# 	current_player = "X"
# 	game_over = False
# 	while not game_over:
# 		take_turn(current_player)
# 		game_result = check_game_over()
# 		if game_result == "win":
# 			print(current_player + " wins!")
# 			game_over = True
# 		elif game_result == "tie":
# 			print("It's a tie!")
# 			game_over = True
# 		else:
# 			# Switch to the other player
# 			current_player = "O" if current_player == "X" else "X"

# # Start the game
# play_game()

# Q 17:
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# def main():
#     choice = input("Enter 1 to convert Celsius to Fahrenheit, or 2 to convert Fahrenheit to Celsius: ")
    
#     if choice == "1":
#         celsius = float(input("Enter the temperature in Celsius: "))
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
#     elif choice == "2":
#         fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
#         celsius = fahrenheit_to_celsius(fahrenheit)
#         print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
#     else:
#         print("Invalid choice. Please enter either 1 or 2.")

# if __name__ == "__main__":
#     main()

# Q 18:
# def is_anagram(str1, str2):
#     # Convert both strings to lowercase and remove spaces
#     str1 = str1.lower().replace(" ", "")
#     str2 = str2.lower().replace(" ", "")
    
#     # Check if the lengths of the strings are equal
#     if len(str1) != len(str2):
#         return False
    
#     # Sort the characters in both strings
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
    
#     # Compare the sorted strings
#     if sorted_str1 == sorted_str2:
#         return True
#     else:
#         return False

# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False

# Q 19:
# import random

# def roll_dice():
#     return random.randint(1, 6)

# def play_game():
#     while True:
#         input("Press Enter to roll the dice...")
#         result = roll_dice()
#         print("You rolled a", result)
#         choice = input("Do you want to roll again? (y/n): ")
#         if choice.lower() != "y":
#             break

# play_game()

# Q 20:
# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)

#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break

#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         return total


# # Example usage
# cart = ShoppingCart()

# cart.add_item("Papaya", 100)
# cart.add_item("Guava", 200)
# cart.add_item("Orange", 150)

# print("Current Items in Cart:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

# cart.remove_item("Orange")

# print("\nUpdated Items in Cart after removing Orange:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

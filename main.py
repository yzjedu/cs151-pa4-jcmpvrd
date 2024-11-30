# Programmers: Jordi
# Course:  CS151, Dr.Yalew
# Due Date: 11/21/24
# Lab Assignment: PA 5
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: User choice and filename depending on choice
# Data Out: Depends on user choice: 1. Counts words of headlines 2. Write headlines with a specific word 3. Calculate the average length of the headline 4. Find the longest and the shortest headline 5. Load a new file
# Credits: Class
# Input Files: The txt files from 2014 to 2019

# Purpose:  Reads file to list
# Parameters: file name
# #Return: lines from the file
def read_file_to_list(filename):
    try:
        with open(filename,'r') as file:
            lines = [line.strip() for line in file]
        file.close()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return []

# Purpose:  Counts the words of the headlines
# Parameters: Headlines and word
# Return: The count for the word that appears in the headlines
def count_headlines_with_word(headlines,word):
    count = 0
    for headline in headlines:
        if word.lower() in headline.lower():
            count += 1
    print(f"The word '{word}' appears in {count} headlines")

# Purpose:  Will write the headlines with the desired word
# Parameters: Headlines, word, and an output file
# Return: The headlines with a certain word to a new file
def write_headlines_with_word(headlines,word,output_file):
    try:
        file = open(filename,"w")
        for headline in headlines:
            if word.lower() in headline.lower():
                file.write(headline + "\n")
        file.close()
        print(f"Headlines containing '{word}' has been saved to '{output_file}'")
    except:
        print("Error: Could not write to the file")

# Purpose:  Calculates the average length in headline
# Parameters: Headlines
# Return: The average headline length
def calculate_average_length(headlines):
    total_length = 0
    for headline in headlines():
        total_length += len(headline)
    if len(headlines) > 0:
        average_length = total_length / len(headlines)
        print(f"The average length of the headline is {average_length} characters.")
    else:
        print("There are no headlines to calculate.")

# Purpose:  Finds the longest and shortest headline
# Parameters: Headlines
# Return: The longest and shortest headline
def find_longest_and_shortest(headlines):
    if len(headlines)== 0:
        print("There are no headlines here!!")
        return
    longest_headline = headlines[0]
    shortest_headline = headlines[0]
    for headline in headlines:
        if len(headline) > len(longest_headline):
            longest_headline = headline
        elif len(headline) < len(shortest_headline):
            shortest_headline = headline
    print(f"The longest headline is: {longest_headline}")
    print(f"The shortest headline is: {shortest_headline}")

# Purpose:  Prompt users with a list of options to choose from
# Parameters: None
# Return: None
def display_menu():
    print("This is the program's menu. Please select a number from 1 to 6:")
    print("1: Count headlines with a specific word")
    print("2: Write headlines with a specific word")
    print("3: Calculate the average length of the headline")
    print("4: Find the longest and the shortest headline")
    print("5: Load a new file")
    print("6: Quit the program")

# Purpose:  Runs the program
# Parameters: None
# Return: None
def main():
    print("Welcome to the program. This program will be able analyze headlines.")
    headlines = []
    while len(headlines) == 0:
        filename = input("Please enter the name of the file:").strip()
        headlines = read_file_to_list(filename)
        if len(headlines) == 0:
            print("Please provide a valid file to analyze")
    choice = ""
    while choice != "6":
        display_menu()
        choice = input("Please provide a valid file to analyze").strip()
        if choice == "1":
            word = input("Please enter the word you would like it to search for:").strip()
            count_headlines_with_word(headlines, word)
        elif choice == "2":
            word = input("Please enter the word you would like it to search for:").strip()
            output_file = input("Enter the name of the output file:").strip()
            write_headlines_with_word(headlines, word, output_file)
        elif choice == "3":
            calculate_average_length(headlines)
        elif choice == "4":
            find_longest_and_shortest(headlines)
        elif choice == "5":
            headlines = []
            while len(headlines) == 0:
                filename = input("Enter the new file you would like it to analyze:").strip()
                headlines = read_file_to_list(filename)
                if len(headlines) == 0:
                    print("Please provide a valid file")
        elif choice == "6":
            print("Have a good day and thanks for using the program :)")
        else:
            print("Please provide a choice from the menu (1-6):")

main()







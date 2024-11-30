* Purpose:  Reads file to list 
* Name: read_file_to_list
* Parameters: file name 
* Return: lines from the file 
* Algorithm:
  * Try:
    * With file open it and read the file 
      * Set lines equal to the list of lines split for each line in the file 
      * Return those lines 
  * Except when file is not found:
    * Output: Error that file does not exist 
    * Return an empty list of lines 

* Purpose:  Counts the words of the headlines
* Name: count_headlines_with_word
* Parameters: Headlines and word
* Return: The count for the word that appears in the headlines
* Algorithm:
  * Set count equal to 0 
  * For the headline in headlines:
    * If the lowercase word in the lowercase headline:
      * Add one to the count
  * Output: The word {word} appears in {count} headlines

* Purpose:  Will write the headlines with the desired word
* Name: write_headlines_with_word
* Parameters: Headlines, word, and an output file 
* Return: The headlines with a certain word to a new file 
* Algorithm:
  * Try:
    * Open a new file and set it to writing 
    * For the headline in headlines:
      * If the lowercase word in the lowercase headline:
        * create new file and write the headline while indenting each new headline 
    * Close the new file 
    * Output: Headlines containing the {word} has been saved to the {output_file}
  * Except:
    * Output: Error: Could not write the file 

* Purpose:  Calculates the average length in headline 
* Name: calculate_average_length
* Parameters: Headlines
* Return: The average headline length 
* Algorithm:
  * Set total_length to 0
  * For headline in headlines:
    * Add the length of the headline to total_length
  * If the length of the headline is > 0:
    * Have average_length equal to total_length divided by the length of headlines
    * Output: The average length of the headline is {average_length} characters
  * Else:
    * Output: There are no headlines to calculate 

* Purpose:  Finds the longest and shortest headline
* Name: find_longest_and_shortest
* Parameters: Headlines
* Return: The longest and shortest headline 
* Algorithm:
  * If length of headlines is equal to 0 
    * Output: There are no headlines here !!!
    * Return 
  * Have longest_headline = headlines [0]
  * Have shortest_headline = headlines [0]
  * For headline in headlines:
    * If length of headline is > len of longest_headline:
      * longest_headline = headline 
    * Otherwise if length of headline is < len of shortest_headline:
      * shortest_headline = headline 
  * Output: The longest headline is: {longest_headline}
  * Output: The shortest headline is: {shortest_headline}

* Purpose:  Prompt users with a list of options to choose from 
* Name: display_menu
* Parameters: None 
* Return: None
* Algorithm:
  * Output: This is the program's menu. Please select a number from 1 to 6:
  * Output: 1: Count headlines with a specific word
  * Output: 2: Write headlines with a specific word
  * Output: 3: Calculate the average length of the headline
  * Output: 4: Find the longest and the shortest headline
  * Output: 5: Load a new file
  * Output: 6: Quit the program

* Purpose:  Runs the program 
* Name: main
* Parameters: None
* Return: None
* Algorithm:
  * Output: Welcome to the program. This program will be able analyze headlines.
  * Set headlines as an empty list 
  * While the length of the headlines is equal to 0:
    * Set filename equal to prompting the user: Please enter the name of the file: and then strip it
    * Set headlines equal to the funtion read_file_to_list and have filename as the parameter
    * If the length of headlines is equal to 0:
      * Output: Please provide a valid file to analyze
  * Set choice to an empty string
  * While choice is not equal to 6:
    * call the display_menu function 
    * Set choice equal to the input from user and prompt the user: Please provide a valid file to analyze and then strip it 
    * If choice is equal to 1:
      * Prompt user for input: Please enter the word you would like it to search for and then strip it 
      * Call the function count_headlines_with_word with the parameters of headlines and word
    * Otherwise if choice is equal to 2:
      * Prompt the user for input: Please enter the word you would like it to search for and then strip it 
      * Prompt the user for input: Enter the name of the output file and then strip it 
      * Call the function write_headlines_with_word and have the parameters be headlines, word, and output_file
    * Otherwise if choice is equal to 3:
      * Call the function calculate_average_length with the parameter headlines
    * Otherwise if choice is equal to 4:
      * Call the function find_longest_and_shortest with the parameter headlines
    * Otherwise if choice is equal to 5:
      * Set headlines equal to an empty list 
      * While length of headlines is equal to 0:
        * Prompt the user for input: Enter the new file you would like it to analyze and then strip it 
        * Have headlines equal to the function read_file_to_list with the parameter filename
        * If length of the headlines is equal to 0:
          * Output: Please provide a valid file
    * Otherwise if choice is equal to 6:
      * Output: Have a good day and thanks for using the program :)
    * Else:
      * Output: Please provide a choice from the menu (1-6):


1. Call the main function 



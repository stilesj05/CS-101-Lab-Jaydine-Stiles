def word_count(text):
    
    #counts amount of words within the user input and returns the amount of words
    
    words_in_text = text.split() #get individual words as elements of a list
    counter = 0
    for i in words_in_text: #iterates over every word and counts amount of words
        counter += 1
    return counter


def find_longest_word(text):
    
    #finds the longest word within the user input and returns the longest word
    
    words_in_text = text.split() #get individual words as elements of a list
    lengths = [] #to append the lengths of the words
    for word in words_in_text: #gets the length of every word and appends that to the empty list
        length_word = len(word)
        lengths.append(length_word)
    longest_index = lengths.index(max(lengths)) #what is the index of the largest length?
    longest_word = words_in_text[longest_index] 
    return longest_word
    

def count_substring(text, substring):
    
    #takes a substring from user and finds how many times that substring appears in the user inputted text
    
    num_substring = text.count(substring) #finds how many times the substring is in the full string
    return num_substring

    
def extract_unique_words(text):

    #figures out if there are any repeats in the user inputted text, only appends the unique words to a list, and returns that list
    
    unique_words_list = []
    words_in_text = text.split() #get individual words as elements of a list
    for i in words_in_text: #iterates over every word and conts amount of words
        if not i in unique_words_list: #if the word is not already in the words list (this eliminates the repeats of a word)
            unique_words_list.append(i) #adds the words to the list
    return unique_words_list 

def main():
    print('Welcome to the Text Program!\n') 
    user_text = input('Enter a text: ')
    print('\nOriginal Text:')
    print(f'{user_text}')
    play = 'yes'
    while play == 'yes': #while loop so the user gets to see the menu and pick repeatedly until they choose to quit (or until they pick '5')
        print('\nText Analysis Options:')
        print('1. Word Count')
        print('2. Longest Word')
        print('3. Count of Substring')
        print('4. Unique Words')
        print('5. Exit')
        user_analysis_pick = input('Enter the number of the analysis option (1-5): ')
        if user_analysis_pick == '1':
            print(f'\nWord Count: {word_count(user_text)}') #using word_count(text) variable
            continue
        elif user_analysis_pick == '2':
            print(f'\nLongest Word: {find_longest_word(user_text)}') #using find_longest_word(text) variable
            continue
        elif user_analysis_pick == '3':
            user_substring = input('\nEnter a substring to count: ') #getting user input for their substring of choice
            print(f"Count of Substring '{user_substring}': {count_substring(user_text, user_substring)}") #using count_substring(text, substring) variable
            continue
        elif user_analysis_pick == '4':
            print(f'\nUnique Words: {extract_unique_words(user_text)}') #using extract_unique_words(text) variable
            continue
        elif user_analysis_pick == '5': #if the user chooses five, they chose to exit the program, therefore a break statement is necessary
            break
    print('\nThank you for using the Text Processing Program!') 

if __name__ == '__main__':
    main()    
        
        



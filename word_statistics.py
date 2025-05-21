def show_menu():
    print("# Text Stats Calculator")
    print("Enter a sentence, and the program will calculate statistics about the words.\n")

def get_input():
    return input("Please enter a sentence: ")

def count_frequency_of_words(sentence):
    word_dict = {}
    words = sentence.split()
    
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return word_dict, words

def calculate_total_words(words):
    return len(words)

def calculate_average_word_length(words):
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

def display_results(total_words, average_length, word_dict):
    print("\nStatistics:")
    print(f"Total number of words: {total_words}")
    print(f"Average length of words: {average_length:.2f}")
    print("Word frequency:")
    for word, count in word_dict.items():
        print(f"{word}: {count}")

def main():
    show_menu()  # Display the menu
    sentence = get_input()  # Get user input
    word_dict, words = count_frequency_of_words(sentence)  # Count frequency of words
    total_words = calculate_total_words(words)  # Calculate total words
    average_length = calculate_average_word_length(words)  # Calculate average word length
    display_results(total_words, average_length, word_dict)  # Display results

# Start the program
main()
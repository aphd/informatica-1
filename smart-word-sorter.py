def show_menu():
    print("# Word Category Analyzer")
    print("Enter a sentence, and the program will analyze word length and starting letters.\n")

def get_input():
    return input("Please enter a sentence: ")

def split_into_words(sentence):
    words = sentence.split()
    return [word.strip(".,!?").lower() for word in words]

def find_longest_and_shortest(words):
    if not words:
        return None, None
    longest = max(words, key=len)
    shortest = min(words, key=len)
    return longest, shortest

def count_starting_letters(words):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    for word in words:
        if word[0] in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count, consonant_count

def group_words_by_first_letter(words):
    word_dict = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in word_dict:
            word_dict[first_letter] = [word]
        else:
            word_dict[first_letter].append(word)
    return word_dict

def display_results(longest, shortest, vowel_count, consonant_count, grouped_words):
    print("\nResults:")
    print(f"Longest word: {longest}")
    print(f"Shortest word: {shortest}")
    print(f"Words starting with vowels: {vowel_count}")
    print(f"Words starting with consonants: {consonant_count}")
    
    print("\nWords grouped by first letter:")
    for letter in sorted(grouped_words):
        print(f"{letter}: {grouped_words[letter]}")

def main():
    show_menu()
    sentence = get_input()
    words = split_into_words(sentence)
    longest, shortest = find_longest_and_shortest(words)
    vowel_count, consonant_count = count_starting_letters(words)
    grouped_words = group_words_by_first_letter(words)
    display_results(longest, shortest, vowel_count, consonant_count, grouped_words)

# Start the program
main()

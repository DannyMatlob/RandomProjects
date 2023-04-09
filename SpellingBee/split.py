def split_words(words):
    """
    This function takes a string of words separated by commas, spaces, or newlines,
    and returns a string of words separated by newlines.
    """
    # Replace commas and spaces with newline characters
    new_words = words.replace(',', '\n').replace(' ', '\n').replace('\n', '\n')
    # Split the new string into a list of words
    word_list = new_words.split('\n')
    # Filter out any empty strings
    word_list = filter(lambda w: w != '', word_list)
    # Join the list of words into a single string, separated by newlines
    return '\n'.join(word_list)

# Example usage
# Read input words from file
with open('wordsToSplit.txt', 'r') as file:
    input_words = file.read()

# Call the function to split the words
output_words = split_words(input_words)

# Print the output words
print(output_words)

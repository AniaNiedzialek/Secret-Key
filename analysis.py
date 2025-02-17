# Homework 1
# Niedzialek Anna, 
# CS 166, 
# Spring 2025

# Part 1: Frequency analysis
# The following code analyzes the frequencies of most occurring single letters, bigrams, and trigrams in English

# ===== FILE =====
# Open the file to begin the analysis, if file not available display the message
# ================
def open_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File was not found.")
        return None
    

# ===== FREQUENCY ======
# The following function gets the frequency of: single letters, bigrams, trigarams (gram) from the provided file (message),
# and returns their occurrences as a dictionary; keys: are the grams, values: their occurrences
# ======================
def frequency(message, gram):
    occurrence = {}
    for i in range(len(message) - gram + 1):
        freq = message[i:i + gram]
        # to have all the symbols as alphanumeric
        if freq.isalnum():
            occurrence[freq] = occurrence.get(freq, 0) + 1
    return occurrence

# The following calculates the percentage of occurrences
def calculate_percentages(occurrence_dict):

    total = sum(occurrence_dict.values())
    return {k: (v / total) * 100 for k, v in occurrence_dict.items()}

# available files
file_names = ["ciphertext-o2.txt", "ciphertext2.txt"] 

# reading both files
for file_name in file_names:
    message = open_file(file_name)  
    # single letters
    print(f'\n==== Single letters for {file_name}:')
    print(f"{dict(sorted(frequency(message, 1).items(), key=lambda x: x[1], reverse=True))}") # sorting in descending order of occurrence
    # bigrams - get only top 10 occurrences
    print(f'\n==== Bigrams for {file_name}:')
    print(f"{dict(sorted(frequency(message, 2).items(), key=lambda x: x[1], reverse=True)[:10])}")  
    # trigrams - get only top 10 occurrences
    print(f'\n==== Trigrams for {file_name}:')
    print(dict(sorted(frequency(message, 3).items(), key=lambda x: x[1], reverse=True)[:10]))  

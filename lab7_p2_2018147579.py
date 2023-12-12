def count_alphabets(file_path):
    # Open the file
    file = open(file_path, 'r')
    text = file.read().lower()  # Read and convert to lower case for case-insensitivity
    file.close()  # Close the file

    # Initialize a dictionary for alphabet counts
    alphabet_count = {}

    # Count each alphabet character
    for char in text:
        if char.isalpha():
            alphabet_count[char] = alphabet_count.get(char, 0) + 1

    # Sort the dictionary by count in descending order
    sorted_alphabets = sorted(alphabet_count.items(), key=lambda x: x[1], reverse=True)

    # Extract only the characters (keys) from the sorted list
    sorted_chars = [char.upper() for char, _ in sorted_alphabets]

    return sorted_chars

def main():
    # Assuming the file 'input_7_2.txt' is in the same directory
    sorted_chars = count_alphabets("input_7_2.txt")
    
    # Output the results
    print(sorted_chars)

if __name__ == "__main__":
    main()

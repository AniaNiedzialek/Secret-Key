# Secret Key - Frequency Analysis Tool

This repository contains a Python program for performing frequency analysis on text files, used to decipher monoalphabetic substitution cipher. 
The program calculates the frequency of single letters, bigrams, and trigrams in a given text, which is useful for cryptographic analysis, such as cracking substitution ciphers or analyzing patterns in encrypted messages.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Example Output](#example-output)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

The program reads text files and analyzes the frequency of:
- **Single letters**: The occurrence of each individual letter.
- **Bigrams**: The occurrence of pairs of letters.
- **Trigrams**: The occurrence of triplets of letters.

This analysis is particularly useful for understanding patterns in encrypted text and can assist in breaking simple substitution ciphers.

---

## Features

- **File Reading**: Reads text files and processes their content.
- **Frequency Analysis**: Calculates the frequency of single letters, bigrams, and trigrams.
- **Top N Results**: Displays the top 10 most frequent bigrams and trigrams.
- **Error Handling**: Provides clear error messages if files are not found or cannot be read.

---

## Requirements

To run this program, you need:
- **Python 3.x**: The program is written in Python and requires Python 3.x to be installed.
- **Text Files**: The program expects text files (e.g., `ciphertext-o2.txt`, `ciphertext2.txt`) to be located in the same directory as the script.

---

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AniaNiedzialek/Secret-Key.git
   cd Secret-Key
2. **Prepare Input Files:**

  Place your text files (e.g., ciphertext-o2.txt, ciphertext2.txt) in the same directory as the script.
3. **Run the Program:**

  bash
  Copy
  python frequency_analysis.py
4. **View the Output:**
  The program will display the frequency of single letters, bigrams, and trigrams for each file.

---

## Secret-Key

   ├── frequency_analysis.py  # Main Python script for frequency analysis
   ├── ciphertext-o2.txt      # Example input file 1
   ├── ciphertext2.txt        # Example input file 2
   ├── README.md              # This README file

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contribution
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
  - Fork the repository.
  - Create a new branch for your feature or bugfix.
  - Commit your changes.
  - Submit a pull request.

---

## Author
Anna Niedzialek


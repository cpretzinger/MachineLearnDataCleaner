
# File Pre Train Processor!
# Clean your datasets in 4 easy steps!!

## Overview

Welcome to the **[Project Name]**! This project focuses on preparing datasets for training AI models, specifically designed to enhance coding capabilities. The repository contains scripts that preprocess raw data, clean artifacts, tokenize the content, and verify tokenization.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Scripts](#scripts)
   - [1. Pre-process](#1-pre-process)
   - [2. Artifact Cleaner](#2-artifact-cleaner)
   - [3. Tokenize](#3-tokenize)
   - [4. Check if Tokenized](#4-check-if-tokenized)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.11 or higher
- Pip (Python package installer)

Additionally, you will need to install the required libraries. You can do this by running:

```bash
pip install -r requirements.txt
```

## Scripts

### 1. Pre-process

The **pre-process** script is responsible for cleaning and formatting the raw dataset. It performs the following tasks:

- Removes unwanted characters and symbols.
- Normalizes text by converting it to lowercase.
- Strips out HTML tags and extra whitespaces.

**Usage:**

```bash
python pre_process.py <input_file> <output_file>
```

### 2. Artifact Cleaner

The **artifact_Cleaner** script cleans up any artifacts or unwanted entries from the dataset. This ensures that the data is ready for further processing.

**Usage:**

```bash
python artifact_Cleaner.py <input_file> <output_file>
```

### 3. Tokenize

The **tokenize** script converts cleaned text data into tokens. This step prepares the dataset for model training by breaking down the text into manageable units.

**Usage:**

```bash
python tokenize.py <input_file> <output_file>
```

### 4. Check if Tokenized

The **check-if-tokenized** script verifies if the dataset has been tokenized correctly. It checks the structure and contents of the tokenized file to ensure everything is in order.

**Usage:**

```bash
python check-if-tokenized.py <input_file>
```

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/yourrepository.git
```

Navigate into the project directory:

```bash
cd yourrepository
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

After installing the prerequisites and required libraries, you can run the scripts in order to preprocess your data, clean artifacts, tokenize it, and verify the tokenization. Make sure to replace `<input_file>` and `<output_file>` with your specific file paths.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the usage commands and descriptions based on how your scripts are designed to work. This README should provide a clear and professional overview of your project!
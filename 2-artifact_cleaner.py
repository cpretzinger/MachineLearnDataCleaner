import json
import re

def clean_unicode(data):
    # Load JSON content
    with open(data, 'r', encoding='utf-8') as file:
        content = json.load(file)

    # Function to replace Unicode escape sequences with the actual characters
    def replace_unicode_escapes(text):
        # Replace common Unicode issues and special characters
        replacements = {
            "â": "'",
            "â": '"',
            "â": '"',
            "â": "–",
            "â": "—",
            "â¦": "...",
            "â¢": "™",
            "Ã©": "é",
            "Ã¨": "è",
            "Ã": "à",
            "ââ": "––",
            "ð": "🚀",  # Add more emoji replacements as needed
            "ð": "🎉",
            # Add any other character conversions you encounter
        }

        for key, value in replacements.items():
            text = text.replace(key, value)

        # Remove unnecessary backslashes
        text = re.sub(r'\\+', '', text)

        return text

    # Recursively clean all strings in the JSON
    def recursive_clean(obj):
        if isinstance(obj, dict):
            return {k: recursive_clean(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [recursive_clean(item) for item in obj]
        elif isinstance(obj, str):
            return replace_unicode_escapes(obj)
        else:
            return obj

    # Clean the content
    cleaned_content = recursive_clean(content)

    # Write the cleaned content back to a file
    with open('fully_cleaned_data_v2.json', 'w', encoding='utf-8') as file:
        json.dump(cleaned_content, file, indent=4, ensure_ascii=False)

    print("File cleaned and saved as 'fully_cleaned_data_v2.json'.")

# Usage
clean_unicode('organized_data.json')
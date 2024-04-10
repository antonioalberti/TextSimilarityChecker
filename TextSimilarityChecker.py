import nltk
import re

def detect_identical_phrases(reference_text, submitted_text):
    # Split the texts into sentences using NLTK's sentence tokenizer
    reference_sentences = nltk.sent_tokenize(reference_text)
    submitted_sentences = nltk.sent_tokenize(submitted_text)

    # Remove extra whitespace
    reference_sentences = [sentence.strip() for sentence in reference_sentences if sentence.strip()]
    submitted_sentences = [sentence.strip() for sentence in submitted_sentences if sentence.strip()]

    # Split the sentences into sub-phrases using commas and periods
    reference_subphrases = []
    for sentence in reference_sentences:
        reference_subphrases.extend(re.split(r'[,.]', sentence))

    submitted_subphrases = []
    for sentence in submitted_sentences:
        submitted_subphrases.extend(re.split(r'[,.]', sentence))

    # Remove extra whitespace from sub-phrases
    reference_subphrases = [subphrase.strip() for subphrase in reference_subphrases if subphrase.strip()]
    submitted_subphrases = [subphrase.strip() for subphrase in submitted_subphrases if subphrase.strip()]

    # Filter sub-phrases with more than 100 characters
    reference_subphrases = [subphrase for subphrase in reference_subphrases if len(subphrase) > 70]
    submitted_subphrases = [subphrase for subphrase in submitted_subphrases if len(subphrase) > 70]

    # Find identical sub-phrases
    identical_subphrases = [subphrase for subphrase in submitted_subphrases if subphrase in reference_subphrases]

    # Calculate the percentage of identical sub-phrases
    total_submitted_subphrases = len(submitted_subphrases)
    total_identical_subphrases = len(identical_subphrases)
    percentage_identical = (total_identical_subphrases / total_submitted_subphrases) * 100 if total_submitted_subphrases > 0 else 0

    return identical_subphrases, percentage_identical

# Example usage
reference_text = input("Enter the reference text: ")
print()  # Blank line after entering the reference text

submitted_text = input("Enter the submitted text: ")
print()  # Blank line after entering the submitted text

identical_subphrases, percentage_identical = detect_identical_phrases(reference_text, submitted_text)

print(f"Identical sub-phrases found: {len(identical_subphrases)}")
print(f"Percentage of identical sub-phrases: {percentage_identical:.2f}%")
print()  # Blank line before outputting the identical sub-phrases

print("Identical sub-phrases:")
for subphrase in identical_subphrases:
    print(subphrase)
    print()  # Blank line after each identical sub-phrase

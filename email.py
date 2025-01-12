import re
from collections import defaultdict

# Function to extract emails from the file and save to a new file
def extract_and_save_emails(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        content = file.read()

    # Regular expression to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    # Remove duplicates
    unique_emails = sorted(set(emails))

    # Group emails by domain
    grouped_emails = defaultdict(list)
    for email in unique_emails:
        domain = email.split('@')[1]  # Get the domain part
        grouped_emails[domain].append(email)

    # Prepare formatted emails, three per line with commas
    lines = []
    for domain, emails in grouped_emails.items():
        for i in range(0, len(emails), 3):
            line_emails = emails[i:i+3]
            line = ", ".join(line_emails) + (", " if i + 3 < len(emails) else "")
            lines.append(line)

    # Save to a new file
    with open(output_filename, 'w') as output_file:
        output_file.write("\n".join(lines))

    # Print the total number of unique emails
    print(f"Extracted {len(unique_emails)} unique emails. Saved to {output_filename}.")

# Specify your input and output filenames
input_filename = 'tc.txt'
output_filename = 'tech.txt'
extract_and_save_emails(input_filename, output_filename)

#this program extracts all emails from a file

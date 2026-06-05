import re

def extract_emails():
    try:
        with open("input.txt", "r", encoding="utf-8", errors="ignore") as file:
            text = file.read()
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        with open("emails.txt", "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
        print("Emails extracted successfully!")
        print(f"Total emails found: {len(emails)}")
    except FileNotFoundError:
        print("Error: input.txt file not found.")
if __name__ == "__main__":
    extract_emails()
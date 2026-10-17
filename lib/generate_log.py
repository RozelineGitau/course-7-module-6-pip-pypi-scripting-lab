
from datetime import datetime
import os


def generate_log(data):
    # Step 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # Step 2: Generate a filename using today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Step 3: Write each entry to the file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Step 4: Print confirmation and return the filename
    print(f"Log written to {filename}")

    return filename

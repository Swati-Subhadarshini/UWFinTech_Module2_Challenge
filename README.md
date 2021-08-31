## Loan Qualifying Application

This project is designed for a FinTech start up company for loan application. Additional application feature has been added which can prompt the user to save the number of qualifying loans as a new CSV file.

---

## Technologies Used

Leveraging python version 3.9.6
Libraries used are fire, questionary, pathlib, sys, csv
CLI used GitBash
Code written with the help of VSCode application.

---

## Installation Guide

Install VSCode and Anaconda Python
Install GitBash Command Line Interface
Inside the CLI install python fire and questionary library

Code:
pip install fire
pip install questionary

Activate Conda Development Environment
In the CLI type

"conda activate dev"

Once done with coding deactivate conda by typing "conda deactivate".

Run the code by typing:

python app.py

---

CODE BLOCK

### save_qualifying_loans.py function

''' import questionary
from pathlib import Path

def save_qualifying_loans(qualifying_loans):

    if len(qualifying_loans) > 0:
        save_qualifying_loan_data = questionary.text("Would you like to save the qualifying loans?").ask()
        if save_qualifying_loan_data == "Yes" or save_qualifying_loan_data == "yes":
            csvpath = questionary.text("Enter the output file path(.csv):").ask()
            csvpath = Path(csvpath)
            if not csvpath.exists():
                sys.exit(f"Oops! Can't find this path: {csvpath}")
    return csvpath

'''

### *save_csv_file.py function

'''

import csv

def save_csv(csvpath, qualifying_loans):

    """writes the data into CSV file.

    Args:
        csvpath (Path): The csv file path.
        qualifying loan list."""

    print("Saving the qualifying loan datas into the csv file")

    header = ['Lender', 'Loan_Amount', 'LTV', 'DTI', 'Credit_Score', 'Interest_Rate']
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write our header row first!
        csvwriter.writerow(header)

        # Then we can write the data rows
        for row in qualifying_loans:
            csvwriter.writerow(row)
'''

---


## Contributors

This project is designed by Swati Subhadarshini 
Emaid id: sereneswati@gmail.com
LinkedIn link: https://www.linkedin.com/in/swati-subhadarshini-89a8a538?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BhUCLlUYCSc2jK4x4khPVUQ%3D%3D

---


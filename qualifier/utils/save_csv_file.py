

"""Helper functions to save data to CSV file.

    This contains a helper function for write data into the CSV files.

    """

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
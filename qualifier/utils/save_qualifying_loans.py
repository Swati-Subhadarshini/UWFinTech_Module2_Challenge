

import questionary
from pathlib import Path



def save_qualifying_loans(qualifying_loans):
    
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    
    return: csvpath
    """
    if len(qualifying_loans) > 0:
        save_qualifying_loan_data = questionary.text("Would you like to save the qualifying loans?").ask()
        if save_qualifying_loan_data == "Yes" or save_qualifying_loan_data == "yes":
            csvpath = questionary.text("Enter the output file path(.csv):").ask()
            csvpath = Path(csvpath)
            if not csvpath.exists():
                sys.exit(f"Oops! Can't find this path: {csvpath}")
    return csvpath

save_csv():

print("Saving the qualifying loan datas into the csv file")
    #csvpath = Path("qualifying_loans.csv")

            header = ['Lender', 'Loan_Amount', 'LTV', 'DTI', 'Credit_Score', 'Interest_Rate']
            with open(csvpath, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)

    # Write our header row first!
    
                csvwriter.writerow(header)

        # Then we can write the data rows
                for row in qualifying_loans:
                    csvwriter.writerow(row)
import csv

def add_record(date, record_type, category, amount):
    with open('finances.csv', mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([date, record_type, category, amount])

def read_records():
    total_income = 0
    total_expense = 0
    
    with open('finances.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == "Income":
                total_income += float(row[3])
            elif row[1] == "Expense":
                total_expense -= float(row[3])
            print(row)

    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Net Income:", total_income - total_expense)

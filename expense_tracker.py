import csv
import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    
    try:
        df = pd.read_csv('Expenses.csv')
        
        print(df.head())
        
        category_totals = df.groupby('Category')['Amount'].sum()
        
        category_totals.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Total Expenses per Category')
        plt.xlabel('Category')
        plt.ylabel('Total Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("No such file found. Please make sure 'Expenses.csv' exists.")

def add_expense():
    print("\n----Expenses Tracker----")
    
    category = input("\nEnter the category (food/travel/others): ")
    while True:
        try:
            amount = float(input("Enter the amount: "))  
            break  
        except ValueError:
            print("Please enter a valid number for the amount.")
    
    date = input("Enter the date (YYYY-MM-DD): ")
    
    new_expense = pd.DataFrame([[category, amount, date]], columns=["Category", "Amount", "Date"])

    try:
        
        df = pd.read_csv('Expenses.csv')
       
        df = pd.concat([df, new_expense], ignore_index=True)
    except FileNotFoundError:
        
        df = new_expense

    df.to_csv('Expenses.csv', index=False)

    print("\nData has been saved to 'Expenses.csv'.")

def analyze_data():
    try:
        df = pd.read_csv('Expenses.csv')
        print("\nExpense Summary:")
        print(f"Total expenses: ${df['Amount'].sum():.2f}")  
        print(f"Total number of entries: {len(df)}") 
    except FileNotFoundError:
        print("No expenses data found. Please add expenses first.")

while True:
    
    print("\n1.To add expense\n2.To analyze expense\n3.Visualization\n4.Exit")
    choice = input("\nSelect an option (1, 2, 3, 4): ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        analyze_data()
    elif choice == '3':
        visualize_data()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")





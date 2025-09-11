import pandas as pd
import matplotlib.pyplot as plt
from pyodbc import connect

connection_string = (
    "Driver=<sql driver>;"
    "Server=<server>;"
    "Database=<database>;"
    "UID=<username>;"
    "PWD=<password>;"
    "TrustServerCertificate=yes;"
)

try:
    con = connect(connection_string)
    print("Connected to the database successfully.")

    # Global variables
    businessId = 102
    month = 9
    year = 2025

    # ========================== 2025 WHOLE YEAR EXPENSE SUMMARY
    procedure_name = f"EXEC usp_GetMonthlyExpenseTotalPerYear2025 {businessId}, {year}"
    journals = pd.read_sql_query(procedure_name, con)

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(journals['Month'], journals['Year_2025'], color='skyblue')
    ax.bar_label(bars, fmt='%.0f', label_type='edge', padding=5, color='darkblue')

    plt.title('2025 Whole Year Expense Summary')
    plt.xlabel('Month')
    plt.ylabel('Amount Range')
    plt.show()
    # ========================== 2025 WHOLE YEAR EXPENSE SUMMARY

    # ========================== 2025 MONTHLY EXPENSE SUMMARY
    # procedure_name = f"EXEC usp_GetSubAccountMonthlyBreakdown {businessId}, {month}, {year}"
    # journals = pd.read_sql_query(procedure_name, con)
    #
    # plt.bar(journals['TransactionDate'], journals['Debit'], color='skyblue')
    #
    # if month == 1:
    #     plt.title('January 2025 Expense Summary')
    # elif month == 2:
    #     plt.title('February 2025 Expense Summary')
    # elif month == 3:
    #     plt.title('March 2025 Expense Summary')
    # elif month == 4:
    #     plt.title('April 2025 Expense Summary')
    # elif month == 5:
    #     plt.title('May 2025 Expense Summary')
    # elif month == 6:
    #     plt.title('June 2025 Expense Summary')
    # elif month == 7:
    #     plt.title('July 2025 Expense Summary')
    # elif month == 8:
    #     plt.title('August 2025 Expense Summary')
    # elif month == 9:
    #     plt.title('September 2025 Expense Summary')
    # elif month == 10:
    #     plt.title('October 2025 Expense Summary')
    # elif month == 11:
    #     plt.title('November 2025 Expense Summary')
    # elif month == 12:
    #     plt.title('December 2025 Expense Summary')
    #
    # plt.xlabel('Month')
    # plt.ylabel('Amount Range')
    # plt.show()
    # ========================== 2025 MONTHLY EXPENSE SUMMARY
except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    if con:
        con.close()
        print("Connection closed.")
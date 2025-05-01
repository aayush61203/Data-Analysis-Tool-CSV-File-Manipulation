import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    fn = input("Enter File Name : ")
    filename = fn + ".csv"
    df = pd.read_csv(filename)

    while True:
        print("\nMain Menu")
        print("1. Display DataFrame")
        print("2. Display Head")
        print("3. Display Tail")
        print("4. Display Info")
        print("5. Display Columns")
        print("6. Display Shape")
        print("7. Display Descriptive Statistics")
        print("8. Describe Transpose")
        print("9. Sum of Particular Column")
        print("10. Count of Particular Column")
        print("11. Exit")

        print("12. Print DataFrame")
        print("13. Print specific rows")
        print("14. Print maximum value for a column")
        print("15. Print minimum value for a column")
        print("16. Describe DataFrame")
        print("17. Filter rows based on a condition")
        print("18. Print row with maximum value in a column")
        print("19. Print selected columns based on condition")
        print("20. Sort DataFrame by a column")
        print("21. Print DataFrame index")
        print("22. Set a column as index")
        print("23. Count missing values")
        print("24. Calculate total cell count")
        print("25. Calculate total missing count")
        print("26. Calculate percentage missing")
        print("27. Print DataFrame shape")
        print("28. Drop rows with missing values")
        print("29. Print DataFrame shape after dropping missing values")
        print("30. Drop columns with missing values")
        print("31. Fill missing values in a column")
        print("32. Fill missing values for all columns")
        print("33. Print value counts for a column")
        print("34. Print number of unique values in each column")
        print("35. Plot histogram of DataFrame")
        print("36. Plot histogram of a column")
        print("37. Plot scatter plot between two columns")
        print("38. Plot bar plot")
        print("39. Plot box plot")
        print("40. Plot scatter plot with regression line (lmplot)")
        print("41. Plot heatmap")
        print("42. Plot pie chart")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(df)
        elif choice == "2":
            print(df.head())
        elif choice == "3":
            print(df.tail())
        elif choice == "4":
            print(df.info())
        elif choice == "5":
            print(df.columns)
        elif choice == "6":
            print(df.shape)
        elif choice == "7":
            print(df.describe())
        elif choice == "8":
            print(df.describe().transpose())
        elif choice == "9":
            col = input("Enter Columns For Sum : ")
            print(df[col].sum())
        elif choice == "10":
            col = input("Enter Columns For Count : ")
            print(df[col].count())
        elif choice == "11":
            print("Exiting the program.")
            break
        elif choice == "12":
            print(df)
        elif choice == "13":
            start = int(input("Enter the starting row index: "))
            end = int(input("Enter the ending row index: "))
            print(df[start:end])
        elif choice == "14":
            col_name = input("Enter the column name: ")
            print(f"Maximum value in {col_name}: {df[col_name].max()}")
        elif choice == "15":
            col_name = input("Enter the column name: ")
            print(f"Minimum value in {col_name}: {df[col_name].min()}")
        elif choice == "16":
            print(df.describe())
        elif choice == "17":
            col_name = input("Enter the column name: ")
            value = float(input("Enter the filter value: "))
            print(df[df[col_name] > value])
        elif choice == "18":
            col_name = input("Enter the column name: ")
            max_row = df[df[col_name] == df[col_name].max()]
            print(max_row)
        elif choice == "19":
            col_name = input("Enter the column name: ")
            condition_col = input("Enter the condition column name: ")
            condition_value = input("Enter the condition value: ")
            print(df[df[condition_col] == condition_value][[col_name, condition_col]])
        elif choice == "20":
            sort_col = input("Enter the column name to sort by: ")
            print(df.sort_values(sort_col))
        elif choice == "21":
            print("DataFrame index:\n", df.index)
        elif choice == "22":
            index_col = input("Enter the column name to set as index: ")
            df.set_index(index_col, inplace=True)
            print(f"'{index_col}' set as index.")
        elif choice == "23":
            print("Missing value count:\n", df.isnull().sum())
        elif choice == "24":
            total_cells = df.size
            print("Total cell count:", total_cells)
        elif choice == "25":
            total_missing = df.isnull().sum().sum()
            print("Total missing count:", total_missing)
        elif choice == "26":
            total_cells = df.size
            total_missing = df.isnull().sum().sum()
            percent_missing = (total_missing / total_cells) * 100
            print("Percentage missing:", percent_missing)
        elif choice == "27":
            print("DataFrame shape:", df.shape)
        elif choice == "28":
            df = df.dropna()
            print("Rows with missing values dropped.")
        elif choice == "29":
            cd = df.dropna(axis=1)
            print("Columns with missing values dropped:\n", cd.head())
        elif choice == "30":
            drop_col = input("Enter the column name to drop: ")
            df.drop(drop_col, axis=1, inplace=True)
            print(f"'{drop_col}' column dropped.")
        elif choice == "31":
            fill_col = input("Enter the column name to fill missing values: ")
            fill_value = input(f"Enter the value to fill in '{fill_col}': ")
            df[fill_col].fillna(fill_value, inplace=True)
            print(f"Missing values in '{fill_col}' filled with '{fill_value}'.")
        elif choice == "32":
            fill_value = input("Enter the value to fill missing values: ")
            df.fillna(fill_value, inplace=True)
            print(f"All missing values filled with '{fill_value}'.")
        elif choice == "33":
            value_counts_col = input("Enter the column name to get value counts: ")
            print(df[value_counts_col].value_counts())
        elif choice == "34":
            unique_counts = df.nunique()
            print("Number of unique values in each column:\n", unique_counts)
        elif choice == "35":
            df.hist()
            plt.show()
        elif choice == "36":
            col_name = input("Enter the column name for histogram: ")
            df[col_name].hist()
            plt.show()
        elif choice == "37":
            x_col = input("Enter the column name for x-axis: ")
            y_col = input("Enter the column name for y-axis: ")
            plt.scatter(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        elif choice == "38":
            x_col = input("Enter the column name for x-axis: ")
            y_col = input("Enter the column name for y-axis: ")
            sns.barplot(x=x_col, y=y_col, data=df)
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Bar Plot")
            plt.show()
        elif choice == "39":
            x_col = input("Enter the column name for x-axis: ")
            y_col = input("Enter the column name for y-axis: ")
            sns.boxplot(x=x_col, y=y_col, data=df)
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Box Plot")
            plt.show()
        elif choice == "40":
            x_col = input("Enter the column name for x-axis: ")
            y_col = input("Enter the column name for y-axis: ")
            sns.lmplot(x=x_col, y=y_col, data=df)
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Scatter Plot with Regression Line (lmplot)")
            plt.show()
        elif choice == "41":
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
            plt.title("Correlation Heatmap")
            plt.show()
        elif choice == "42":
            col_name = input("Enter the column name for the pie chart: ")
            plt.figure(figsize=(8, 8))
            df[col_name].value_counts().plot.pie(autopct="%.1f%%", shadow=True)
            plt.title(f"Pie Chart for {col_name}")
            plt.show()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()

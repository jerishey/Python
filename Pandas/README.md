# Pandas
Pandas is a powerful and popular Python library desinged for data manipulation (cleaning, transforming, and structuring data) and data analysis (finding patterns, trends, and insights).
<br>
It simplifies working with structured datasets like tables, spreadsheets, or time-series data.
<br>
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

## Key Feature
```bash
1. Works seamlessly with structured data formats like CSV and Excel.
2. Handles missing values easily.
3. Built on NumPy for fast computation.
```

## Why use pandas
```bash
1. Performance -> Handles millions of rows efficiently.
2. Ease of use -> Beginner-friendly syntax for cleaning and transforming data.
3. Integration -> Works with libraries like Matplotlib (Visualization) and Scikit-learn (Machine Learning).
```

# Installing and Importing the Pandas Library

Installing -> Open your Command Prompt in Windows or Terminal in Mac/Linux and run the following command:
```bash
>> pip install pandas
```
Importing -> After the Pandas have been installed in the system we need to import the library. This module is imported using:
```bash
>> import pandas as pd
```
> <i>pd is just an alias for Pandas. It’s not required but using it makes the code shorter when calling methods or properties.</i>

# Data Structures in Pandas
Pandas provides two data structures for manipulating data which are as follows:
<br>
## Pandas Series
A Pandas Series is one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects etc.).
Each element in the Series has a unique label called an index. 
<br>
Series is created by loading the datasets from existing storage which can be a SQL database, a CSV file or an Excel file.
<br>
<b>Example:</b>
```bash
import pandas as pd 
import numpy as np

s = pd.Series() 
print("Pandas Series: ", s) 
data = np.array(['g', 'e', 'e', 'k', 's']) 
  
s = pd.Series(data) 
print("Pandas Series:\n", s)
```

## Pandas DataFrame
Pandas DataFrame is a two-dimensional data structure with labeled axes (rows and columns). It is created by loading the datasets from existing storage which can be a SQL database, a CSV file or an Excel file. It can be created from lists, dictionaries, a list of dictionaries etc.
<br>
<b>Example:</b>
```bash
import pandas as pd 

df = pd.DataFrame() 
print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
df = pd.DataFrame(lst) 
print(df)
```

# Operation in Pandas
Pandas provides essential operations for working with structured data efficiently.
```bash
1. Loading Data: This operation reads data from files such as CSV, Excel or JSON into a DataFrame.

2. Viewing and Exploring Data: After loading data, it is important to understand its structure and content. This methods allow you to inspect rows, summary statistics and metadata.

3. Handling Missing Data: Datasets often contain empty or missing values. Pandas provides functions to detect, remove or replace these values.

4. Selecting and Filtering Data: This operation retrieves specific columns, rows or records that match a condition. It allows precise extraction of required information.

5. Adding and Removing Columns: You can create new columns based on existing ones or delete unwanted columns from the DataFrame.

6. Grouping Data (GroupBy): Grouping allows you to organize data into categories and compute values for each group for example, sums, counts or averages.
```

# Data loading in pandas
In Pandas, data loading means importing data from different file formats (CSV, Excel, JSON, SQL, etc.) into a DataFrame for analysis.
<br>
Pandas provides many built-in functions to load data easily.

```bash
import pandas as pd

# Read data from CSV file inta a dataframe
# df = pd.read_csv("DATA/sales_data_sample.csv", encoding="latin1")

# Read data from Excel file inta a dataframe
# df = pd.read_excel("DATA/SampleSuperstore.xlsx")

# Read data from JSON file into a dataframe
# df = pd.read_json("DATA/sample_Data.json")

# print(df)
```

# Data Exploration Methods in Pandas
Data Exploration Methods are functions used to understand the structure, content, quality, and statistical properties of a dataset before performing analysis or modeling.
<br>
```bash
They help us answer questions like:
1. How many rows and columns are there?
2. What are the data types?
3. Are there missing values?
4. What is the average, minimum, or maximum value?
```
```bash
import pandas as pd

df = pd.read_json("DATA/sample_Data.json")

# head() display first five rows as default
# print(df.head())

# # tail() display last five rows as default
# print(df.tail())

# You can pass integer as agruments to search or see data

# head() display first ten rows as default
# print(df.head(10))

# tail() display last ten rows as default
# print(df.tail(10))

# info() displays dataset structure and data types.
# print(df.info())

# describe() Displays statistical summary of numerical columns.
# print(df.describe())
```
<br>

#  Handling Missing values in Pandas :
<b>What are Missing Values?</b>
<br>

Missing values mean no data is present.
<br>
Common representations:

```bash
NaN

None

empty cells

NULL (from databases)

```
<br>

<b>Check entire DataFrame by using:</b>

```bash

df.isnull()
```
<br>

isnull()  => If any Missing values in dataframe it shows True in place of missing values.
<br>
 If not any Missing values in dataframe it shows false in that place.
<br>

<b>Count missing values :</b>

```bash
df.isnull().sum()

```
<br>

<b>Percentage of missing values :</b>

```bash

(df.isnull().sum() / len(df)) * 100

```
# Fill Missing Values (Imputation) :

```bash

# Fill with a fixed value

df.fillna(0)


# Fill column-wise

df["Marks"].fillna(50, inplace=True)

# Fill with Mean (Numeric Data)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# Fill with Median (Better for Outliers)
df["Marks"].fillna(df["Marks"].median(), inplace=True)

# Fill with Mode (Categorical Data)
df["Grade"].fillna(df["Grade"].mode()[0], inplace=True)

```
## Interpolate Method
The interpolate() method in Pandas is used to fill missing values (NaN) by estimating values between existing data points.
<br>
It is commonly used in time series or numerical datasets where missing values can be approximated based on surrounding values.
```bash
import pandas as pd

data = {
    "Value": [10, None, None, 40, 50]
}

df = pd.DataFrame(data)

df["Value"] = df["Value"].interpolate()

print(df)

# Output:

   Value
0   10.0
1   20.0
2   30.0
3   40.0
4   50.0
```
### Syntax:
```bash
DataFrame.interpolate(method='linear', axis=0)

Important Parameters

method – Technique used for interpolation (default is linear)

axis – Direction of interpolation
0 → column-wise
1 → row-wise

limit – Maximum number of consecutive NaN values to fill

inplace – Modify original data if True
```
### Common Interpolation Methods
```bash
Method	                Description
linear	   ->      Default method (straight line estimation)
time	   ->      For time series data
polynomial ->      Polynomial curve interpolation
nearest	   ->      Uses nearest value
spline	   ->      Smooth curve interpolation
```
# Sorting & Aggregation
Sorting is the process of arranging data in a specific order (ascending or descending) based on one or more columns.
<br>
Aggregation is the process of calculating summary statistics from a dataset, such as total, average, minimum, and maximum values.
<br><br>
Examples: sum, mean, count, max, min
<br>

<b>Basic Aggregation on a Column :</b>

```bash
df["Marks"].sum()
df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].count()
```
## Example:
1. Sorting: Arranging data in a specific order using methods like sort_values().
```bash
import pandas as pd

data = {
    "Name": ["Rakesh", "Sourav", "Nitish", "Rohit"],
    "Age": [21, 22, 20, 23]
}

df = pd.DataFrame(data)

# Sorting by Age
sorted_df = df.sort_values(by="Age")

print(sorted_df)

# Output:
   Name    Age
2  Nitish   20
0  Rakesh   21
1  Sourav   22
3  Rohit    23
```
2. Aggregation: Calculating summary statistics from data using functions like sum(), mean(), max(), and min().
```bash
import pandas as pd

data = {
    "Salary": [50000, 45000, 52000, 49000]
}

df = pd.DataFrame(data)

print("Total Salary:", df["Salary"].sum())
print("Average Salary:", df["Salary"].mean())
print("Maximum Salary:", df["Salary"].max())
print("Minimum Salary:", df["Salary"].min())

# Output:
Total Salary: 196000
Average Salary: 49000
Maximum Salary: 52000
Minimum Salary: 45000
```

# groupby() in Pandas
groupby() is used to divide the dataset into groups based on a column and then apply operations (like sum, mean, count, etc.) on each group.
<br>
It works similar to SQL GROUP BY.
<br>
First, data is grouped by a column, then we apply aggregation functions to calculate results for each group.
<br> <br>
## Syntax:
```bash
df.groupby("column_name").aggregation_function()
```
<b>Example:</b>
```bash
import pandas as pd

data = {
    "Name": ["Rakesh", "Sourav", "Nitish", "Rohit", "Aarti"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [50000, 45000, 52000, 48000, 51000]
}

df = pd.DataFrame(data)
print(df)

df2 = df.groupby("Department")["Salary"].sum()
print(df2)

# Multiple aggregation 
df3 = df.groupby("Department")["Salary"].agg(["sum", "mean", "max", "min"])
print(df3)
```

# Merging And Joining in Pandas
In Pandas, Merging and Joining are used to combine data from multiple DataFrames into one DataFrame.
<br>
1. Merging in Pandas:
<br>
Merging is the process of combining two DataFrames based on a common column or key.
```bash
# Syntax->
pd.merge(df1, df2, on="column_name")

# Parametres
df1 → First DataFrame
df2 → Second DataFrame
on → Common column used to combine the data
```
<b>Example:</b>
```bash
import pandas as pd

data1 = {
    "ID": [1, 2, 3],
    "Name": ["Rakesh", "Sourav", "Nitish"]
}

data2 = {
    "ID": [1, 2, 3],
    "Salary": [50000, 45000, 52000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

result = pd.merge(df1, df2, on="ID")

print(result)
```
## Types of Merge:
```bash
Type	                    Description
Inner Merge	    -> Inner merge returns only the rows that have matching values in both DataFrames.
Left Merge	    -> Left merge returns all rows from the left DataFrame and matching rows from the right DataFrame.
Right Merge 	-> Right merge returns all rows from the right DataFrame and matching rows from the left DataFrame.
Outer Merge	    -> Outer merge returns all rows from both DataFrames.
```
<b>Example:</b>
```bash
import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Rakesh", "Sourav", "Nitish"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Salary": [45000, 52000, 48000]
})

print("Inner Merge")
print(pd.merge(df1, df2, on="ID", how="inner"))

print("\nLeft Merge")
print(pd.merge(df1, df2, on="ID", how="left"))

print("\nRight Merge")
print(pd.merge(df1, df2, on="ID", how="right"))

print("\nOuter Merge")
print(pd.merge(df1, df2, on="ID", how="outer"))
```
2. Joining in Pandas:
<br>
Joining is used to combine DataFrames based on their index instead of a column.
<br>
<b>Example:</b>
```bash
# Synatax -> df1.join(df2)

import pandas as pd

data1 = {
    "Name": ["Rakesh", "Sourav", "Nitish"]
}

data2 = {
    "Salary": [50000, 45000, 52000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

result = df1.join(df2)

print(result)
```

# Concatenation in Pandas
Concatenation is the process of joining multiple DataFrames together along rows or columns using the concat() function.
<br>
In Pandas, Concatenation is used to combine two or more DataFrames either vertically (row-wise) or horizontally (column-wise).
<br>
## Syntax:
```bash
pd.concat([df1, df2], axis=0)

# Parameters
df1, df2 → DataFrames to combine
axis = 0 → Combine rows (default)
axis = 1 → Combine columns
```
## Example:
```bash
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Rakesh", "Sourav"],
    "Age": [21, 22]
})

df2 = pd.DataFrame({
    "Name": ["Nitish", "Rohit"],
    "Age": [23, 20]
})

# Row-wise concatenation
print("Row Concatenation")
print(pd.concat([df1, df2], axis=0))

# Column-wise concatenation
print("\nColumn Concatenation")
print(pd.concat([df1, df2], axis=1))
```

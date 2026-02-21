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

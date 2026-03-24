# Seaborn:
Seaborn is a Python library for creating statistical visualizations. It provides clean default styles and color palettes, making plots more attractive and easier to read. Built on top of Matplotlib and integrated with pandas data structures, Seaborn makes data visualization easier and more consistent.
<br>

## Features of Seaborn
```bash
1. Attractive Default Styles –> Provides built-in themes for clean and professional-looking plots.

2. High-Level Interface –> Allows creating complex visualizations with simple and minimal code.

3. Pandas DataFrame Support –> Works directly with structured data for easy plotting.

4. Statistical Visualization –> Supports distribution, regression, and relationship analysis.

5. Variety of Plot Types –> Includes plots like scatter, bar, box, violin, and heatmaps.

6. Built on Matplotlib –> Combines ease of use with powerful customization options.
```

## How to Install Seaborn:
```bash

pip install seaborn

# If your using Python3 then use :
pip3 insatll seaborn


# if your in Anaconda / Conda:
conda insatll seaborn

# In Google Colab / Jupyter Notebook
!pip install seaborn
```
<br>

# Different Categories of plot in Seaborn
Plots are basically used for visualizing the relationship between variables. Those variables can be either completely numerical or a category like a group, class, or division.

## 1. Relational plots
Relational plots in Seaborn are used to visualize the relationship between two or more variables, helping to identify patterns, trends, or correlations in the data.
<br>
### Types of Relational Plot:
```bash
1. Scatter Plot : A scatter plot is used to display the relationship between two numerical variables by plotting data points on a graph.

- Uses:
To analyze relationship between two numerical variables
To identify correlation, clusters, and outliers

2. Line Plot : A line plot is used to show trends or changes in data over a continuous variable, usually time, by connecting data points with a line.

- Uses:
To show trends over time or continuous data
To analyze increase/decrease patterns

3. Relplot : relplot() is a figure-level function in Seaborn used to create relational plots (like scatter plots and line plots) with an easy interface and support for multiple subplots.

- Uses:
To create multiple relational plots in one figure
To easily compare data across categories using:
    . hue (color grouping)
    . col / row (multiple plots)
```
### Example:

<i>Scatter Plot:
```bash

import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000]
})

sns.scatterplot(x="Age", y="Salary", data=df)
```
Line Plot:
```bash
import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Sales": [100, 150, 200, 250, 300]
})

sns.lineplot(x="Year", y="Sales", data=df)
```
Relplot:
```bash
import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000],
    "Gender": ["M", "F", "M", "F", "M"]
})

sns.relplot(x="Age", y="Salary", data=df, hue="Gender", kind="scatter")
```
</i>

## 2. Categorical Plots
Categorical plots in Seaborn are used to analyze and visualize data that is divided into distinct groups or categories. 
<br>
These plots help in comparing values across categories, understanding distributions, and identifying patterns such as variations, central tendency, and outliers within each group.

### Types of Categorical Plots
```bash
1. Bar Plot : Shows the comparison of values across categories using rectangular bars. The height of each bar represents the value, making it easy to compare different groups visually.

-Uses:
Compare values between categories
Show average or total values

-Features:
The height or length of each bar represents the magnitude of the data.
It is one of the most commonly used plots for simple comparisons.

2. Count Plot : Displays the count (frequency) of observations in each category. It helps identify which category appears most and least frequently in the dataset.

-Uses:
Count how many times each category appears
Understand frequency distribution

-Features:
It is a special type of bar plot where only categorical data is required.
Helps quickly identify the most and least frequent categories.

3. Box Plot : Shows the distribution of data based on quartiles (min, Q1, median, Q3, max). It is useful for detecting outliers and understanding how data is spread.

-Uses:
Identify outliers
Understand spread of data

-Features:
It provides a summary of the dataset through five key values.
Useful for comparing distributions across multiple categories.

4. Violin Plot : Combines box plot + density plot, showing distribution shape. It provides deeper insight into how data is distributed beyond summary statistics.

-Uses:
Understand data distribution in detail
Compare distributions between categories

-Features:
It combines features of box plot and density plot.
The width of the shape represents the concentration of data points.

5. Strip Plot : Displays individual data points with slight randomness (jitter). It helps visualize actual data values rather than summarized information.

-Uses:
Visualize raw data
Useful for small datasets

-Features:
Points are slightly spread (jittered) to reduce overlap.
Helps in observing exact values rather than summaries.

6. Swarm Plot : Similar to strip plot but avoids overlapping points. It gives a clearer and more accurate representation of dense data.

-Uses:
Clear view of all data points
Better for dense data

-Features:
It arranges points in a way that they do not overlap.
Provides a more accurate representation of data distribution.
```
### Example:

<i>Bar Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=df)
plt.show()
```
Count Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.countplot(x="day", data=df)
plt.show()
```
Box Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", data=df)
plt.show()
```
Violin Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill", data=df)
plt.show()
```
Strip Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.stripplot(x="day", y="total_bill", data=df)
plt.show()
```
Swarm Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.swarmplot(x="day", y="total_bill", data=df)
plt.show()
```
</i>
<br>

## 3. Distribution Plots
Distribution plots are used to show how data values are spread or distributed over a range. They help us understand the shape, center, and spread of data.

### Types of Distribution Plots
```bash
1. Histogram : A histogram is a plot that divides data into intervals (bins) and shows the frequency of values in each bin using bars.

-Uses:
To understand the distribution of numerical data
To identify patterns like normal or skewed distribution

-Features:
Uses bins to group data
Shows frequency clearly
Easy to interpret

2. KDE Plot (Kernel Density Estimation) : A KDE plot is a smooth curve that represents the probability density of continuous data.

-Uses:
To visualize the probability density of data
To get a smooth view of distribution without bins

-Features:
Smooth curve (no bars)
Better visualization of pattern
Reduces noise

3. Dist Plot (Deprecated in newer Seaborn) : A dist plot combines histogram + KDE curve in a single plot.

-Uses:
To view both frequency and density together
To quickly analyze distribution in one graph

-Features:
Shows both bars and curve
Easy combined analysis
Not used in latest versions

4. Rug Plot : A rug plot shows individual data points as small vertical lines on an axis.

-Uses:
To observe exact positions of data points
To complement histogram or KDE plot 

-Features:
Shows each data point
Simple and minimal
Best with other plots
```
### Example:
<i> Histogram
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.histplot(data["total_bill"])
plt.show()
```
KDE Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.kdeplot(data["total_bill"])
plt.show()
```
Dist Plot (Deprecated)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.distplot(data["total_bill"])
plt.show()
```
Rug Plot
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.rugplot(data["total_bill"])
plt.show()
```
</i>
<br>

## 4. Regression Plots
Regression plots are used to visualize the relationship between two variables and show how one variable depends on another. They also display a best-fit line (regression line) to predict trends in data.

### Types of Regression Plots
```bash
1. Linear Regression Plot (regplot) : A regplot shows the relationship between two variables using a scatter plot along with a regression line.

-Uses:
To find correlation between variables
To predict trends

-Features:
Shows scatter points + line
Displays confidence interval
Simple and clear

2. Regression Plot with Categories (lmplot) : An lmplot is an advanced regression plot that separates data into categories and shows regression lines for each group.

-Uses:
To compare relationships across categories
To analyze grouped data

-Features:
Supports grouping (hue)
Multiple regression lines
More flexible than regplot

3. Residual Plot (residplot) : A residual plot shows the difference between actual values and predicted values (errors).

-Uses:
To check model accuracy
To detect patterns in errors

-Features:
Shows residuals (errors)
Helps validate regression model
Detects non-linearity
```
### Example:
<i>

Linear Regression Plot (regplot)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.regplot(x="total_bill", y="tip", data=data)
plt.show()
```
Regression Plot with Categories (lmplot)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex", data=data)
plt.show()
```
Residual Plot (residplot)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.residplot(x="total_bill", y="tip", data=data)
plt.show()
```
</i>
<br>

## 5. Matrix Plots
Matrix plots are used to visualize relationships between multiple variables in a dataset in a matrix (grid) format. They help in understanding patterns, correlations, and distributions across many variables at once.

### Types of Matrix Plots
```bash
1. Heatmap : A heatmap represents data in a matrix form using colors, where different colors indicate different values.

-Uses:
To visualize correlation between variables
To identify patterns and relationships

-Features:
Uses color intensity
Easy to spot high/low values
Works well with correlation data

2. Cluster Map (clustermap) : A clustermap is similar to a heatmap but also groups similar data using clustering techniques.

-Uses:
To find similar groups in data
To analyze patterns with clustering

-Features:
Includes dendrograms (tree structure)
Groups similar rows/columns
Advanced visualization

3. Pair Plot (pairplot) : A pair plot shows pairwise relationships between multiple variables using a grid of plots.

-Uses:
To analyze relationships between all variables
To detect trends and correlations

-Features:
Multiple plots in grid form
Shows scatter plots + histograms
Good for exploratory data analysis
```

### Example:
<i>

Heatmap
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

corr = data.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.show()
```
Cluster Map (clustermap)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

corr = data.corr(numeric_only=True)

sns.clustermap(corr)
plt.show()
```
Pair Plot (pairplot)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.pairplot(data)
plt.show()
```
</i>
<br>

## 6. Multi-Plot Grid
A multi-plot grid is used to display multiple plots in a structured grid format (rows and columns). It helps in comparing different subsets of data side by side.

### Types of Multi-Plot Grids
```bash
1. Facet Grid (FacetGrid) : FacetGrid is used to create a grid of plots based on rows and columns of categorical variables.

-Uses:
To visualize data for different categories separately
To compare patterns across subsets

-Features:
Supports row and column grouping
Flexible plotting
Works with multiple plot types

2. Pair Grid (PairGrid) : PairGrid is used to create a grid of plots showing pairwise relationships between variables with custom control.

-Uses:
To explore relationships between multiple variables
To customize pair plots

-Features:
More control than pairplot
Supports different plots in grid
Flexible and powerful

3. Joint Grid (JointGrid) : JointGrid is used to display the relationship between two variables along with their individual distributions.

-Uses:
To analyze two variables together
To see both joint and individual distributions

-Features:
Combines scatter + histogram/KDE
Shows detailed relationship
Compact visualization
```

### Example:
<i>

Facet Grid (FacetGrid)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

g = sns.FacetGrid(data, col="time", row="sex")
g.map(sns.scatterplot, "total_bill", "tip")

plt.show()
```

Pair Grid (PairGrid)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

g = sns.PairGrid(data)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)

plt.show()
```

Joint Grid (JointGrid)
```bash
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

g = sns.JointGrid(data=data, x="total_bill", y="tip")
g.plot(sns.scatterplot, sns.histplot)

plt.show()
```

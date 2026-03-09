# Matplotlib
Matplotlib is a used Python library used for creating static, animated and interactive data visualizations. It is built on the top of NumPy and it can easily handles large datasets for creating various types of plots such as line charts, bar charts, scatter plots, etc.

## What is Matplotlib Used For?
Matplotlib is a Python library for data visualization, primarily used to create static, animated and interactive plots. It provides a wide range of plotting functions to visualize data effectively.
```bash
Key Uses of Matplotlib:

1. Basic Plots: Line plots, bar charts, histograms, scatter plots, etc.
2. Statistical Visualization: Box plots, error bars and density plots.
3. Customization: Control over colors, labels, gridlines and styles.
4. Subplots & Layouts: Create multiple plots in a single figure.
5. 3D Plotting: Surface plots and 3D scatter plots using mpl_toolkits.mplot3d.
6. Animations & Interactive Plots: Dynamic visualizations with FuncAnimation.
7. Integration: Works well with Pandas, NumPy and Jupyter Notebooks.
```

## Key Features of Matplotlib
```bash
1. Versatile Plotting: Create a wide variety of visualizations, including line plots, scatter plots, bar charts and histograms.

2. Extensive Customization: Control every aspect of your plots, from colors and markers to labels and annotations.

3. Seamless Integration with NumPy: Effortlessly plot data arrays directly, enhancing data manipulation capabilities.

4. High-Quality Graphics: Generate publication-ready plots with precise control over aesthetics.

5. Cross-Platform Compatibility: Use Matplotlib on Windows, macOS and Linux without issues.

6. Interactive Visualizations: Engage with your data dynamically through interactive plotting features.
```

## Matplotlib Pyplot
Pyplot is a module within Matplotlib that provides a MATLAB-like interface for making plots. It simplifies the process of adding plot elements such as lines, images and text to the axes of the current figure.
```bash
Steps to Use Pyplot:

1. Import Matplotlib: Start by importing matplotlib.pyplot as plt.
2. Create Data: Prepare your data in the form of lists or arrays.
3. Plot Data: Use plt.plot() to create the plot.
4. Customize Plot: Add titles, labels and other elements using methods like plt.title(), plt.xlabel() and plt.ylabel().
5. Display Plot: Use plt.show() to display the plot.
```

## 1. Visualizing Data with Pyplot using Matplotlib
Pyplot is a module in Matplotlib that provides a simple interface for creating plots. It allows users to generate charts like line graphs, bar charts and histograms with minimal code. Let’s explore some examples with simple code to understand how to use it effectively.

### 1. Line Chart
Line chart is one of the basic plots and can be created using plot() function. It is used to represent a relationship between two data X and Y on a different axis.
```bash
# Syntax -> matplotlib.pyplot.plot(x, y)

# Parameter: x, y Coordinates for data points.
```
<b>Example:</b>
<br>
This code plots a simple line chart with labeled axes and a title using Matplotlib.
```bash
import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y)
plt.title("Line Chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()
```
### 2. Bar Chart
Bar chart displays categorical data using rectangular bars whose lengths are proportional to the values they represent. It can be plotted vertically or horizontally to compare different categories.

```bash
# Syntax -> matplotlib.pyplot.bar(x, height)

# Parameter:

# x: Categories or positions on x-axis.
# height: Heights of the bars (y-axis values).
```
<b>Example:</b>
<br>
This code creates a simple bar chart to show total bills for different days. X-axis represents the days and Y-axis shows total bill amount.
```bash
import matplotlib.pyplot as plt

x = ['Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190]

plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
```

### 3. Histogram
Histogram shows the distribution of data by grouping values into bins. The hist() function is used to create it, with X-axis showing bins and Y-axis showing frequencies.

```bash
# Syntax -> matplotlib.pyplot.hist(x, bins=None)

# Parameter:

# x: Input data.
# bins: Number of bins (intervals) to group data.
```
<b>Example:</b>
<br>
This code plots a histogram to show frequency distribution of total bill values from the list x. It uses 10 bins and adds axis labels and a title for clarity.
```bash
import matplotlib.pyplot as plt

x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='steelblue')
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()
```

### 4. Scatter Plot
Scatter plots are used to observe relationships between variables. The scatter() method in the matplotlib library is used to draw a scatter plot.

```bash
# Syntax -> matplotlib.pyplot.scatter(x, y)

# Parameter: x, y Coordinates of the points.
```
<b>Example:</b>
<br>
This code creates a scatter plot to visualize the relationship between days and total bill amounts using scatter().
```bash
import matplotlib.pyplot as plt

x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 160, 130, 240, 200]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
```

### 5. Pie Chart
Pie chart is a circular chart used to show data as proportions or percentages. It is created using the pie(), where each slice (wedge) represents a part of the whole.
```bash
# syntax -> matplotlib.pyplot.pie(x, labels=None, autopct=None)

# Parameter:

# x: Data values for pie slices.
# labels: Names for each slice.
# autopct: Format to display percentage (e.g., '%1.1f%%').
```
<b>Example:</b>
<br>
This code creates a simple pie chart to visualize distribution of different car brands. Each slice of pie represents the proportion of cars for each brand in the dataset.
```bash
import matplotlib.pyplot as plt
import pandas as pd

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars)
plt.title(" Pie Chart")
plt.show()
```

### 6. Box Plot
Box plot is a simple graph that shows how data is spread out. It displays the minimum, maximum, median and quartiles and also helps to spot outliers easily.
```bash
# Syntax -> matplotlib.pyplot.boxplot(x, notch=False, vert=True)

# Parameter:

# x: Data for which box plot is to be drawn (usually a list or array).
# notch: If True, draws a notch to show the confidence interval around the median.
# vert: If True, boxes are vertical. If False, they are horizontal.
```
<b>Example:</b>
<br>
This code creates a box plot to show the data distribution and compare three groups using matplotlib
```bash
import matplotlib.pyplot as plt

data = [ [10, 12, 14, 15, 18, 20, 22],
         [8, 9, 11, 13, 17, 19, 21],
         [14, 16, 18, 20, 23, 25, 27] ]

plt.boxplot(data)
plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()
```

### 7. Heatmap
Heatmap is a graphical representation of data where values are shown as colors. It helps visualize patterns, correlations or intensity in a matrix-like format. It is created using imshow() method in Matplotlib.
```bash
# Syntax -> matplotlib.pyplot.imshow(X, cmap='viridis')

# Parameter:

# X: 2D array (data to display as an image or heatmap).
# cmap: Sets the color map.
```
<b>Example:</b>
<br>
This code creates a heatmap of random 10×10 data using imshow(). It uses 'viridis' color map and colorbar() adds a color scale.
```bash
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = np.random.rand(10, 10)

plt.imshow(data, cmap='viridis', interpolation='nearest')

plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Heatmap')
plt.show()

# Explanation:
# np.random.seed(0): Ensures same random values every time (reproducibility).
# np.random.rand(10, 10): Generates a 10×10 array of random numbers between 0 and 1.
```

## 2. How to Customize Matplotlib Visualizations
Customization in Matplotlib allows you to improve look and clarity of plots by adjusting elements like colors, styles, labels, titles and gridlines. It helps make visualizations more informative and visually appealing for better data communication.

### 1. Customizing Line Chart
```bash
Line charts can be customized using various properties:

1. Color: Change the color of the line
2. Linewidth: Adjust the width of the line
3. Marker: Change the style of plotted points
4. Markersize: Change the size of the markers
5. Linestyle: Define the style of the line like solid, dashed, etc.
```
<b>Example:</b>
<br>
This code creates a customized line chart with a green dashed line, thicker width, large circular markers and labeled axes and title.
```bash
import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y, color='green', linewidth=3, marker='o', markersize=15, linestyle='--')

plt.title("Customizing Line Chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()
```

### 2. Customizing Bar Chart
```bash
Bar charts can be made more informative and visually appealing by customizing:

1. Color: Fill color of the bars
2. Edgecolor: Color of the bar edges
3. Linewidth: Thickness of the edges
4. Width: Width of each bar
```
<b>Example:</b>
<br>
This code creates a customized bar chart with green bars, blue edges, thicker border lines and labeled axes and title.
```bash
import matplotlib.pyplot as plt

x = ['Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190]

plt.bar(x, y, color='green', edgecolor='black', linewidth=2)

plt.title("Customizing Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
```

### 3. Customizing Histogram Plot
```bash
To make histogram plots more effective various customizations can be applied:

1. Bins: Number of groups (bins) to divide data into
2. Color: Bar fill color
3. Edgecolor: Bar edge color
4. Linestyle: Style of the edges like solid, dashed, etc.
5. Alpha: Transparency level (0 = transparent, 1 = opaque)
```
<b>Example:</b>
<br>
This code creates a customized histogram with green bars, blue edges, dashed border lines, semi-transparent fill and labeled axes and title.
```bash
import matplotlib.pyplot as plt

x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17,
     18, 18, 19, 20, 20, 21, 22, 23, 24, 25, 25, 26, 28, 30,
     32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='green', edgecolor='blue',linestyle='--', alpha=0.5)

plt.title("Customizing Histogram Plot")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()
```

### 4. Customizing Scatter Plot
```bash
Scatter plots can be enhanced with:

1. S: Marker size (single value or array)
2. C: Color of markers or sequence of colors
3. Marker: Marker style like circle, diamond, etc.
4. Linewidths: Width of marker borders
5. Edgecolor: Color of marker borders
6. Alpha: Blending value, between 0 (transparent) and 1 (opaque)
```
<b>Example:</b>
<br>
This code creates a customized scatter plot using diamond-shaped markers, where color represents size, marker size reflects the total bill and transparency is added for better visualization. It includes labeled axes and a title.
```bash
import matplotlib.pyplot as plt

x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 180, 130, 260, 200]
size = [2, 3, 4, 2, 3, 2, 4, 3]  
bill = [170, 120, 250, 190, 180, 130, 260, 200]  

plt.scatter(x, y, c=size, s=bill, marker='D', alpha=0.5)

plt.title("Customizing Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
```

### 5. Customizing Pie Chart
```bash
To make pie charts more effective and visually appealing use:

1. Explode: Moving the wedges of the plot
2. Autopct: Label the wedge with their numerical value.
3. Color: Colors of the slices
4. Sadow: Used to create a shadow effect
```
<b>Example:</b>
<br>
This code creates a customized pie chart with colored slices, exploded segments for emphasis, percentage labels with two decimal places and a shadow effect for better visual appeal.
```bash
import matplotlib.pyplot as plt
import pandas as pd

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 13, 35, 15, 12]
explode = [0.1, 0.5, 0, 0, 0]
colors = ( "orange", "cyan", "yellow","grey", "green",)

plt.pie(data, labels=cars, explode=explode, autopct='%1.2f%%',colors=colors, shadow=True)
plt.show()
```
## 3. Saving Plots Using savefig()
When plots are created using Matplotlib, users may want to save them as image files for use in reports, presentations or sharing. Matplotlib offers savefig() function to save the current plot to a file. By changing file extension, users can store the plot in different formats such as .png, .jpg, .pdf or .svg.
<br>
<br>
<b>Example:</b>
```bash
import matplotlib.pyplot as plt

year = ['2010', '2002', '2004', '2006', '2008']
production = [25, 15, 35, 30, 10]

plt.bar(year, production)

plt.savefig("output.jpg")
plt.savefig("output1", facecolor='y', bbox_inches="tight",pad_inches=0.3, transparent=True)
```
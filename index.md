# How to Create a Bar Graph in Tableau

Welcome! This tutorial will walk you through the steps of creating a simple, effective bar graph using Tableau.

## 🛠️ Requirements

- [Tableau Public](https://public.tableau.com/en-us/s/download/) (Free download)
- A dataset (you can use one of these [sample datasets](https://public.tableau.com/app/learn/sample-data?qt-overview_resources=1) or your own)

---

## 📂 Step 0: Prepare and Understand Your Data
Before you start, it's important to check that your dataset is clean and organized. This helps Tableau interpret your data correctly and prevents issues during visualization.

You can use tools like Tableau Prep, Excel, or your favorite code editor (like Python or R) to clean your data. While Tableau Desktop offers some basic cleaning features—such as filtering, renaming fields, creating calculated columns, and handling nulls—it is not designed for full-scale data wrangling. For more advanced cleaning tasks (like reshaping, removing duplicates, or normalizing data), use Tableau Prep or an external tool before importing the dataset into Tableau.

### What to Check:
1. Ensure your file has **clear headers** and **consistent data types**.
2. Remove any unnecessary blank rows or columns.
3. Check for **null or missing values**, especially in key columns.
4. Identify which columns are **categorical** (like Region, Product, or Category) and which are **numeric** (like Sales or Profit).
5. Reflect on the data itself. Who collected it, and for what purpose? Are all groups equally represented, or are there gaps or biases we should be aware of?
   
A clean dataset will save you time and make your visualization process much smoother.

---

## 📊 Step 1: Open Tableau and Connect to Data

1. Open Tableau Public or Tableau Desktop.
2. Click **"Connect to Data"** and select your file type which will most likely be **Microsoft Excel** or **Text File (CSV)**.
3. Data sets you have worked with in Tableau will populate under **Saved Data Sources**.
4. Choose your dataset file and click **Open**.

<img src="images/open_file_edited.png" alt="Connect to Data" width="800"/>

---

## 📈 Step 2: Build a Bar Graph

1. In the **Data pane**, drag a **categorical variable** (e.g., `Department`, `Category`, or `Product Name`) to the **Columns** shelf.
2. Drag a **numeric measure** (e.g., `Sales`, `Profit`, or `Quantity`) to the **Rows** shelf.
3. Tableau will automatically generate a bar graph!

<img src="images/bar_graph_edited.png" alt="Basic Bar Graph" width="800"/>

---

## 🎨 Step 3: Customize Your Chart

- Click the **Color** shelf to change bar colors.
- Use **Labels** to show values on each bar.
- Sort the bars by value using the **Sort** button.
- Change the chart title by double-clicking it.

<img src="images/color_example.png" alt="Customize Graph" width="800"/>

### Think About: 

- Customizing your bar graph is a great opportunity to reinforce clarity in your visual.
- If you use color, make sure it’s not just decorative. Does it add insight? Are the color choices accessible to people with color vision deficiencies? This ties into Data Feminism’s focus on inclusivity in design and our class on color blindness and accessible graphs. 
- As Tufte would advise, avoid ‘chartjunk’ such as 3D effects, excessive gradients, or shadows because they can detract from the actual data. Labels should be used to enhance understanding, not clutter the chart.
- Following Cairo’s principles, be transparent about what your graph shows and what it doesn’t. If the graph might suggest a causal relationship when there’s only correlation, add a note or make that context clear.

---

## 📤 Step 4: Export 

- Click **Worksheet > Export > Image** to save your graph.

<img src="images/export_image.png" alt="Export Image" width="800"/>

Before exporting and sharing your chart, take a moment to reflect on what it communicates. Is the design honest and inclusive?

As Cairo suggests, once a visualization leaves your screen, it becomes a form of public communication — one that can persuade or mislead. We have a responsibility to ensure our charts are truthful and ethically designed.

Also, from a Data Feminism lens, consider who might be affected by this data or its interpretation. Is there anyone whose story or perspective is missing? Are there communities that may interpret the graph differently based on lived experience?

---

## ➕ Bonus: Turn Your Bar Chart into a Dashboard

Dashboards are great for presenting multiple perspectives from a dataset in a single view. Take your analysis a step further by combining multiple charts into one interactive dashboard using the following steps:

1. Click the “Dashboard” tab at the bottom of Tableau.
2. Drag your bar graph worksheet into the blank dashboard area.
3. Add additional charts (e.g., pie chart, line graph, map) if available.
4. Use the “Actions” menu to add interactivity—such as clicking on a bar to filter another chart.
5. Customize layout and design, then export or publish to Tableau Public.

---

## ⚠️ Common Mistakes

- Bars not appearing? Make sure you’ve chosen the right fields.
- Labels overlapping? Try increasing chart size or reducing font.
- Missing categories? Double-check for nulls in your data.

---

## ✅ You're Done!

You just built and customized a bar graph in Tableau! Try experimenting with different datasets and variables to gain more insight from your data. There are so many things you can do with Tableau including making dashboards to display multiple data visualizations at once!

---

## 💪 Extra Practice Exercise

Test your skills with this challenge:

Using the Superstore sample dataset, create a bar graph that shows total **Sales** by **Sub-Category**. Then, add color to the bars based on **Profit**, and sort them by total sales.

Bonus: Turn it into a dashboard by adding a line chart of **Sales over Time**, and set a filter action that highlights the bar chart when a month is selected.

---

### 🔗 Resources

- [Tableau Official Help](https://help.tableau.com/)
- [More Tableau Tutorials](https://www.tableau.com/learn/training)

---

© Mia Kunath – [GitHub](https://github.com/kunathmi)

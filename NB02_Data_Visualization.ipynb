{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Visualization Notebook for Vivino Wine Project"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Install modules \n",
    "!pip install pandas\n",
    "!pip install numpy\n",
    "!pip install matplotlib\n",
    "!pip install seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import modules\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Read data file\n",
    "If using this notebook in IBM Cloud, replace the code below with the code fragment provided by IBM Cloud for reading a file from the cloud storage.\n",
    "\n",
    "Otherwise, replace the directory path in the file name below with the one where your data file is stored"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read data from csv file\n",
    "df = pd.read_csv('vivino_data_00-4_FINAL.csv')\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.1 Set size of canvas for displaying plots + set up default geo_region sort order for plotting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set size of canvas for displaying plots\n",
    "sns.set(rc={\"figure.figsize\":(15,10)}) #width=15, height=10\n",
    "\n",
    "# Set up geo_region as the index for the dataframe\n",
    "df.index = df['geo_region']\n",
    "\n",
    "# Set up how we wish the plots to order the geographic regions during display\n",
    "order_geo_region = ['W Europe', 'S Europe', 'C/E Europe', 'Oceania', 'N America', 'S America', \n",
    "                    'Africa', 'C/W Asia', 'E Asia']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2 Set 1 -- Pie Plots\n",
    "This pie plot was eventually not used because I needed to spend too much time tweaking the chart. It's in this notebook to show how to create pie plots using the Seaborn library. How to get the text labels set up correctly, etc. is left as an item for you to explore / investigate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 1.2 Set 1 -- Pie Plots\n",
    "\n",
    "# Set pie plot colours (outer ring and inner ring)\n",
    "cmap = plt.get_cmap(\"tab20c\") \n",
    "outer_colors = cmap(np.array([11,26,7,7,1,12,14,9,0])) \n",
    "inner_colors = cmap(np.array([4,7]))\n",
    "\n",
    "count_geo_region = df['geo_region'].groupby(df.geo_region).value_counts()\n",
    "count_country = df['country'].groupby(df.geo_region).value_counts()\n",
    "\n",
    "# This plots the outer circle\n",
    "plt.pie(count_country, startangle = 270, colors = outer_colors, counterclock = False,\n",
    "        radius = 1.0, labeldistance = 1.2,\n",
    "        textprops ={ 'fontweight': 'bold','fontsize':10}, \n",
    "        wedgeprops = { 'linewidth' : 5,'edgecolor' : 'white' })\n",
    "\n",
    "# This plots the inner circle\n",
    "plt.pie(count_geo_region, startangle = 270, colors = outer_colors, counterclock = False,\n",
    "        radius = 0.8, labeldistance = 0.5, labels = order_geo_region, autopct = '%.1f%%',\n",
    "        textprops ={ 'fontweight': 'bold','fontsize':12},\n",
    "        wedgeprops = { 'linewidth' : 5,'edgecolor' : 'white' })##\n",
    "\n",
    "# This sets up the donut hole\n",
    "center_circle = plt.Circle((0,0), 0.2, color=\"white\")\n",
    "fig = plt.gcf()\n",
    "fig.gca().add_artist(center_circle)\n",
    "\n",
    "plt.axis('equal')  # equal aspect ratio\n",
    "plt.tight_layout()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2 Set 2 -- Bar Plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (1.2) Set 2 -- Bar Plots (geo_region level)\n",
    "# Hat-tip to Niithiya for the tip on declaring the Dataframe index in Step 1.1 to get this going\n",
    "\n",
    "# Set up plot layout in the canvas (2 rows, 1 column)\n",
    "fig, axes = plt.subplots(2,1)\n",
    "\n",
    "# This sets up the hue order\n",
    "hue_order=['Red', 'White']\n",
    "\n",
    "# Set up the y axis tick marks and the scale\n",
    "axes[0].set_yticks([0,1,2,3,4,5])\n",
    "axes[0].set_ylim(bottom=0, top=6)\n",
    "\n",
    "# This plots the bar plot of geo_region vs wine_rating, split by wine_type\n",
    "sns.barplot(x=df.index, y=df['wine_rating'], hue=df['wine_type'], hue_order=hue_order, ci=None, palette='OrRd_r',\n",
    "            order=order_geo_region, ax=axes[0]).set(title='Top: Wine Rating by Geographic Region\\nBelow: Price by Geographic Region')\n",
    "\n",
    "# Set up the y axis tick marks and the scale\n",
    "axes[1].set_yticks([0,20,40,60,80,100,120])\n",
    "axes[1].set_ylim(bottom=0, top=140)\n",
    "\n",
    "# This plots the bar plot of geo_region vs wine_rating, split by wine_type\n",
    "sns.barplot(x=df.index, y=df['price'], hue=df['wine_type'], hue_order=hue_order, ci=None, palette='GnBu_r',\n",
    "            order=order_geo_region, ax=axes[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2 Set 3 -- Box Plots (geo_region level)\n",
    "Notice how the geo_regions are ordered -- as per the configured default order in Step 1.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (1.2) Set 3 -- Box Plots (geo_region level)\n",
    "# Set up plot layout in the canvas (2 rows, 1 column)\n",
    "fig, axes = plt.subplots(2,1)\n",
    "\n",
    "# This sets up the hue order\n",
    "hue_order=['Red', 'White']\n",
    "\n",
    "# This plots the box plot in the first row\n",
    "graph = sns.boxplot(x=df.index, y=df['wine_rating'], hue=df['wine_type'], hue_order=hue_order, palette='OrRd_r', \n",
    "                    order=order_geo_region, ax=axes[0])\n",
    "\n",
    "# This sets the title of the box plot in the first row\n",
    "graph.set(title='Top: Wine Rating by Geographic Region\\nBelow: Price by Geographic Region')\n",
    "\n",
    "# This sets the title of the box plot in the second row\n",
    "graph = sns.boxplot(x=df.index, y=df['price'], hue=df['wine_type'], hue_order=hue_order, palette='GnBu_r', \n",
    "                    order=order_geo_region, ax=axes[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2 Set 4 -- Box Plots (country level)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (1.2) Set 4 -- Box Plots (country level)\n",
    "# Set up plot layout in the canvas (2 rows, 1 column)\n",
    "fig, axes = plt.subplots(2,1)\n",
    "\n",
    "# This sets up the hue order\n",
    "hue_order=['Red', 'White']\n",
    "\n",
    "# Set up a new dataframe that will copy rows with geo_region == S Europe or C/E Europe\n",
    "# We'll use this dataframe to plot the boxplots for the countries in these 2 geo_regions\n",
    "df1 = df[(df.geo_region == 'S Europe') | (df.geo_region == 'C/E Europe')]\n",
    "df1.index = df1['country']\n",
    "\n",
    "# Plot the boxplot for wine_ratings for each country in these two geo_regions\n",
    "graph = sns.boxplot(x=df1.index, y=df1['wine_rating'], hue=df1['wine_type'], palette='OrRd_r', ax=axes[0])\n",
    "graph.set(title='Top: Wine Rating by Country (Europe)\\nBelow: Price by Country (Europe)')\n",
    "\n",
    "# Draw horizontal lines on the boxplot to show the global mean, global Red & global White wine_rating means\n",
    "graph.axhline(df['wine_rating'].mean(), ls='--', c='g')\n",
    "graph.axhline(df['wine_rating'][(df.wine_type=='Red')].mean(), ls='--', c='r')\n",
    "graph.axhline(df['wine_rating'][(df.wine_type=='White')].mean(), ls='--', c='y')\n",
    "\n",
    "# Plot the boxplots for price for each country in these two regions\n",
    "graph = sns.boxplot(x=df1.index, y=df1['price'], hue=df1['wine_type'], palette='GnBu_r', ax=axes[1])\n",
    "\n",
    "# Draw horizontal lines on the boxplot to show the global mean, global Red & global White price means\n",
    "graph.axhline(df['price'].mean(), ls='--', c='r')\n",
    "graph.axhline(df['price'][(df.wine_type=='Red')].mean(), ls='--', c='b')\n",
    "graph.axhline(df['price'][(df.wine_type=='White')].mean(), ls='--', c='g')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise -- Draw the wine_rating and price boxplots for other countries outside Europe\n",
    "Hint: Just look at the code in Step 1.3 and adjust accordingly. For the list of other geo_regions, look at the order_geo_region list declared in Step 1.1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2 Set 5 -- Heatmap Plots (Correlation Maps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (1.2) Set 5 -- Heatmap Plots (Correlation maps)\n",
    "df.drop('year', axis=1, inplace=True)\n",
    "\n",
    "# Set up plot layout in the canvas (1 row, 2 columns)\n",
    "fig, axes = plt.subplots(1,2)\n",
    "\n",
    "# Set up dataframe to shortlist countries in the Europe geo_regions\n",
    "df1 = df[(df.geo_region == 'W Europe') | (df.geo_region == 'S Europe') | (df.geo_region == 'C/E Europe')]\n",
    "\n",
    "# Plot the heatmap\n",
    "sns.heatmap(df1.corr(), cmap=\"RdYlBu_r\", annot=True, square=True, annot_kws={'size': 10}, ax=axes[0],\n",
    "            cbar_kws={'shrink': 0.7}).set(title='Correlation Heat Map (Europe)\\n')\n",
    "\n",
    "# Set up dataframe to shortlist countries in the non-European geo_regions\n",
    "df2 = df[(df.geo_region == 'N America') | (df.geo_region == 'S America') | \\\n",
    "        (df.geo_region == 'Oceania') | (df.geo_region == 'Africa') | (df.geo_region == 'C/W Asia')]\n",
    "\n",
    "# Plot the heatmap\n",
    "sns.heatmap(df2.corr(), cmap=\"RdBu_r\", annot=True, square=True, annot_kws={'size': 10}, ax=axes[1],\n",
    "            cbar_kws={'shrink': 0.7}).set(title='Correlation Heat Map (Outside Europe)\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise -- Plot Heatmaps for the other correlations, e.g. Red wines in Europe, etc. Have fun with various permutations of filters.\n",
    "Hint: You need to learn the syntax for selecting data rows from a Pandas DataFrame, based on some selection criteria in some columns. Examples below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# EXAMPLES\n",
    "\n",
    "# Total no. of rows in DataFrame:\n",
    "print ('Total no. of rows in Dataframe df =', len(df))\n",
    "\n",
    "# Now we select those df rows with wine_type == 'Red' and copy them into df1 \n",
    "# In other words, df1 is a DataFrame of red wines only\n",
    "df1 = df[(df.wine_type == 'Red')]\n",
    "print ('Total no. of rows in Dataframe df1 (red wines only) =', len(df1))\n",
    "\n",
    "# Here is an example of compounding conditions, e.g. we want to select Red wines with price > 50\n",
    "# We do this:\n",
    "df1 = df[(df.wine_type =='Red') & (df.price > 50)]\n",
    "print ('Total no. of rows in Dataframe df1 now (red wines priced > 50) =', len(df1))\n",
    "\n",
    "# Here is an example of a more complex compounding condition, \n",
    "# e.g. we want to select White wines AND EITHER { price > 50 and price <= 110 } OR { grape == Riesling }\n",
    "# It's just a matter of understanding the structure & sequence of conditions, \n",
    "# and then using the parentheses at the right places:\n",
    "\n",
    "df1 = df[(df.wine_type =='White') & (((df.price > 50) & (df.price <= 110)) | (df.grape == 'Riesling'))]\n",
    "print ('Total no. of rows in Dataframe df1 now (White) AND ((50 < price <= 110) or (grape is Riesling)) =', len(df1))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.5 Set 5 -- Scattermap Plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (1.5) Set 5 -- Scattermap Plots\n",
    "# Set up plot layout in the canvas (1 row, 1 column)\n",
    "fig, axes = plt.subplots(1,1)\n",
    "\n",
    "# This sets up the hue order\n",
    "hue_order=['Red', 'White']\n",
    "\n",
    "# Plot the scattermap\n",
    "graph = sns.scatterplot(x=df.light_bold, y=df.price, data=df, \n",
    "                        hue=df.wine_type, hue_order=hue_order, palette='husl')\n",
    "graph.set(title='Wine Boldness - Distribution & Price')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# End of Notebook"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

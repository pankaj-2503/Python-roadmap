# Distribution Plots:

# sns.histplot(data, x=..., y=..., hue=..., ...):
# Creates histograms to visualize the distribution of single or multiple variables.
# sns.kdeplot(data, x=..., y=..., hue=..., ...):
# Creates kernel density estimate plots, showing the probability density of a variable.
# sns.displot(data, x=..., y=..., hue=..., kind=..., ...):
# A figure-level interface for drawing distribution plots, offering more flexibility and control.
# sns.rugplot(data, x=..., y=..., ...):
# Draws a rug plot, which shows the distribution of data points along a single axis.
# sns.ecdfplot(data, x=..., y=..., hue=..., ...):
# Plots empirical cumulative distribution functions.


# 2. Categorical Plots:

# sns.barplot(data, x=..., y=..., hue=..., ...):
# Creates bar plots to compare the values of categorical variables.
# sns.countplot(data, x=..., hue=..., ...):
# Creates count plots to show the number of observations in each category.
# sns.boxplot(data, x=..., y=..., hue=..., ...):
# Creates box plots to visualize the distribution of data across categories and identify outliers.
# sns.violinplot(data, x=..., y=..., hue=..., ...):
# Creates violin plots, which combine box plots and kernel density estimates.
# sns.stripplot(data, x=..., y=..., hue=..., ...):
# Creates strip plots to show the distribution of data points across categories.
# sns.swarmplot(data, x=..., y=..., hue=..., ...):
# Creates swarm plots, which are similar to strip plots but avoid overlapping points.
# sns.catplot(data, x=..., y=..., hue=..., kind=..., ...):
# A figure-level interface for categorical plots, offering more control over the plot type.


# 3. Relational Plots:

# sns.scatterplot(data, x=..., y=..., hue=..., size=..., ...):
# Creates scatter plots to visualize the relationship between two numerical variables.
# sns.lineplot(data, x=..., y=..., hue=..., ...):
# Creates line plots to visualize the relationship between two numerical variables.
# sns.relplot(data, x=..., y=..., hue=..., kind=..., ...):
# A figure-level interface for relational plots.



# 4. Matrix Plots:

# sns.heatmap(data, annot=..., cmap=..., ...):
# Creates heatmaps to visualize data as a color-encoded matrix.
# sns.clustermap(data, ...):
# Creates hierarchically clustered heatmaps.
# sns.pairplot(data, hue=..., ...):
# Creates a matrix of scatter plots for pairwise relationships in a dataset.
# sns.pairgrid(data, ...):
# A more flexible way to create pairwise plots.



# 5. Regression Plots:

# sns.regplot(data, x=..., y=..., ...):
# Creates scatter plots with a regression line.
# sns.lmplot(data, x=..., y=..., hue=..., ...):
# Creates regression plots with more flexibility for categorical variables.



# 6. Plot Aesthetics:

# sns.set_style(style):
# Sets the overall style of the plots (e.g., "whitegrid", "darkgrid", "white", "dark", "ticks").
# sns.set_context(context):
# Sets the scale of the plot elements (e.g., "paper", "notebook", "talk", "poster").
# sns.set_palette(palette):
# Sets the color palette for the plots.
# SWAA Travel Analysis

This repository contains a range of Python tools for analyzing and visualizing travel data from the [Survey of Workplace Arrangements and Attitudes](https://wfhresearch.com/). 

## Installation

There are three steps to set up this workflow on a local machine:

#### 1. Clone this repository. 

Instructions on how to clone a repository from GitHub are available [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

#### 2. Set up a virtual environment and install dependencies.

These instructions assume you have already installed Anaconda. An Anaconda distribution can be downloaded [here.]( https://www.anaconda.com/products/distribution)

Open the Anaconda Prompt command line interface. Install a virtual environment using Anaconda and activate it (replace @ENV_NAME with the name of your virtual environment):

```
conda create --name @ENV_NAME python=3.7
conda activate @ENV_NAME
```

For example:

```
conda create --name swaa python=3.7
conda activate swaa
```

Import dependencies via requirements.txt (replace @DIRECTORY with the location of your cloned repo from step 1):

```
cd @DIRECTORY
pip install -r requirements.txt
```

#### 3. Download the latest data 

Sign up for free access to the latest SWAA data at [wfhresearch.com](https://wfhresearch.com/). Once you have downloaded the latest data (e.g. `WFHdata_January23.csv`), then save it in the `Data/` folder as `data.csv`.

## Usage

Once completed, you can create your own Python script, import the helper functions and explore the data however you like. A large Jupyter notebook containing examples of how to use the helper functions to import, filter, modify and plot survey data is provided in the `Code/` folder. 

For example, this code creates four charts to explore differences in work location by attitudes towards remote work with just two lines of code for each chart:

```
fig, axs = plt.subplots(2, 2, constrained_layout=True, figsize=figsize)

# Commute
wt_stack = hf.thirdplace_split(df, 'wfh_top3benefits_commute')
axs[0,0] = hf.plot_stacked_column(wt_stack,
            xlabel='(b) Is lack of commuting a top 3 benefit of RW?', 
            ylim=[0, 40], 
            blabels =['Yes', 'No'],
            ax = axs[0,0])

# Flexibility
wt_stack = hf.thirdplace_split(df, 'wfh_top3benefits_flex')
axs[0,1] = hf.plot_stacked_column(wt_stack,
            xlabel='(b) Is schedule flexibility a top 3 benefit of RW?', 
            ylim=[0, 40],
            blabels =['Yes', 'No'],
            ax = axs[0,1])

# Socializing
wt_stack = hf.thirdplace_split(df, 'wbp_top3benefits_social')
axs[1,0] = hf.plot_stacked_column(wt_stack,
            xlabel='(c) Is socializing a top 3 benefit of in-person work?',  
            ylim=[0, 40],
            blabels =['Yes', 'No'],
            ax = axs[1,0])

# Quiet
wt_stack = hf.thirdplace_split(df, 'wbp_top3benefits_quiet')
axs[1,1] = hf.plot_stacked_column(wt_stack,
            xlabel='(d) Is quiet a top 3 benefit of in-person work?',  
            ylim=[0, 40],
            blabels =['Yes', 'No'],
            ax = axs[1,1])

fig.supylabel('Third Place % of Total Worked Hours')
fig.tight_layout();

```

![image](https://user-images.githubusercontent.com/56656229/227348555-879205c3-0a9e-4378-b5f7-807c9aba65c8.png)


The helper functions can be grouped into different categories as follows. Note that there are many more functions than those described below.

**Filtering and processing**
- `filter_df()`: Filters the entire dataset to high-quality responses only and to a specific set of questions relevant for travel. Also sets the scale column.
- `create_columns()`: Creates several new helpful columns for travel data analysis.

**Create or adjust columns**
- `bin_column()`: Assign values in a quantitative column into bins. 
- `get_primary()`: Find the primary choice for a series of proportional split questions.
- `replace_values()`: Replace categorical values with preferred values.
- `indicator_column_eq()`: Create a new indicator column based on an equality condition.
- `indicator_column_ineq()`: Create a new indicator column based on an inequality condition.

**Get column statistics**
- `weighted_avg()`: Find the weighted average of an entire column.
- `count_var()`: Count the responses within each category.
- `sum_var()`: Sum the responses within each category.
- `get_categories()`: Return the set of chosen responses for a categorical column.
- `get_dates()`: Return the months of the survey that have valid answers for a given column.
- `weighted_freq()`: Find the weighted frequency of responses in a column.
- `weighted_avg_group()`: Find the weighted average of one column, split by groups in a separate column.

**Plot data**
- `plot_timeseries()`: Plot a timeseries line chart for several months of data.
- `plot_column()`: Plot a basic column chart.
- `plot_clustered_column()`: Plot a clustered column chart.
- `plot_stacked_column()`: Plot a stacked column chart.
- `plot_pie()`: Plot a pie chart.
- `plot_area()`: Plot an area chart.

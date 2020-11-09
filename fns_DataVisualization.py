# data import and manipulation
import numpy as np
import pandas as pd

# plotting and graphing
import matplotlib.pyplot as plt
import seaborn as sns

# module dependencies
from fns_DataWrangling import clean_currency


def price_analysis_plots(dataframe, is_vertical=True):

    # Clean the pricing column for strings and integer variations
    dataframe['price'] = dataframe['price'].apply(
        clean_currency).astype('float')

    # Select all x variables in dataframe
    x_variables = dataframe.columns[dataframe.columns != 'price']

    # Ensure all x variables are of string datatype
    # Not totally robust, but provides simple compatibility with seaborn barplot() function
    dataframe[x_variables] = dataframe[x_variables].astype('str')

    # How many categorical variables are there to plot?
    x_count = len(x_variables)

    # Set up a plot based on number of categorical variables
    plt_rows = x_count // 2 + x_count % 2

    if x_count > 1:
        plt_cols = 2
    else:
        plt_cols = 1

    plt.figure(figsize=[5 * x_count, 16])

    # Loop through variables to add to figure.
    for index, variable in enumerate(x_variables):
        plt.subplot(plt_rows, plt_cols, index + 1)

        # If horizontal requested, set-up fariable to flip chart horizontal
        if is_vertical:
            bar_orientation = 'v'
            sns.barplot(x=variable, y='price', data=dataframe,
                        orient=bar_orientation)
        else:
            bar_orientation = 'h'
            sns.barplot(x='price', y=variable, data=dataframe,
                        orient=bar_orientation)

    return plt

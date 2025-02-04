# data import and manipulation
import numpy as np
import pandas as pd


def drop_na_columns(dataframe_list):
    for dataframe in dataframe_list:
        dataframe.dropna(axis=1, how='all', inplace=True)


def drop_ident_columns(dataframe_list, word_list):
    for dataframe in dataframe_list:
        for word in word_list:
            drop_columns = [
                col for col in dataframe.columns if col.endswith(word)]
            dataframe.drop(drop_columns, axis=1, inplace=True)


def drop_same_columns(dataframe_list):
    for dataframe in dataframe_list:
        nunique = dataframe.apply(pd.Series.nunique)
        drop_columns = nunique[nunique == 1].index
        dataframe.drop(drop_columns, axis=1, inplace=True)


def drop_nonoverlap_columns(df1, df2):
    # Find overlapping/instersecting columns between the two datasets
    intersecting_columns = set(df1.columns) & set(df2.columns)

    # Assign each dataset it's own drop columns based off the complete list of intersections
    for dataframe in df1, df2:
        drop_columns = set(dataframe.columns) - intersecting_columns
        dataframe.drop(drop_columns, axis=1, inplace=True)


def print_column_types(dataframe_list):
    for dataframe in dataframe_list:
        print("\nDataframe Shape:{}".format(dataframe.shape))
        for col in dataframe:
            print("{}:{}".format(col, dataframe[col].dtypes))


def cleanse_data_tf_to_boolean(dataframe_list):

    for dataframe in dataframe_list:

        column_list = []

        for col in dataframe.columns:
            if sum(dataframe[col].isin(['t', 'f'])) == len(dataframe[col]):
                column_list.append(col)

        for col in column_list:
            dataframe.loc[(dataframe[col] == 't'), col] = True
            dataframe.loc[(dataframe[col] == 'f'), col] = False


def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)

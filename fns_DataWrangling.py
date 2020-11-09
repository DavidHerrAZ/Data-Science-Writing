# data import and manipulation
import numpy as np
import pandas as pd

# Pricing must be cleaned as the column contains strings, floats, and ints.


def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)

import pandas as pd
import numpy as np

def identify_day_types(ohlc_df):
    """
    Identify whether each trading day is 'green', 'red', or 'neutral' based on Open and Close prices.
    
    A green day occurs when Close > Open, red when Close < Open, and neutral when Close = Open.
    Also calculates the percentage distribution of each day type.

    Parameters
    ----------
    ohlc_df : pd.DataFrame
        DataFrame containing Open and Close prices with columns 'Open' and 'Close'.

    Returns
    -------
    tuple
        A tuple containing:
        - pd.DataFrame: Original DataFrame with added 'DayType' column
        - dict: Dictionary with percentages for each day type (green, red, neutral)

    Examples
    --------
    >>> df_with_types, percentages = identify_day_types(ohlc_df)
    >>> print(percentages)
    {'green': 30.0, 'red': 70.0, 'neutral': 0.0}
    """

    df = ohlc_df.copy() 

    df['DayType'] = df.apply( 
        lambda row: 'green' if row['Close'] > row['Open'] else ( 
            'red' if row['Close'] < row['Open'] else 'Neutral' 
        ),
        axis=1
    )

    # Calculate percentages
    total_days = len(df)
    percentages = {
        'green': calculate_percentage((df['DayType'] == 'green').sum(), total_days),
        'red': calculate_percentage((df['DayType'] == 'red').sum(), total_days),
        'neutral': calculate_percentage((df['DayType'] == 'Neutral').sum(), total_days)
    }

    return df, percentages

def get_green_day_subset(ohlc_df):
    """
    Filter and return rows for green days (days where Close > Open).

    Parameters
    ----------
    ohlc_df : pd.DataFrame
        The full OHLC DataFrame containing price data.

    Returns
    -------
    pd.DataFrame
        DataFrame containing only the rows for green days.

    Examples
    --------
    >>> green_days = get_green_day_subset(ohlc_df)
    >>> print(green_days.head())
    """
    df_with_types, _ = identify_day_types(ohlc_df)
    green_days = df_with_types[df_with_types['DayType'] == 'green']
    return green_days


def get_red_day_subset(ohlc_df):
    """
    Filter and return rows for red days (days where Close < Open).

    Parameters
    ----------
    ohlc_df : pd.DataFrame
        The full OHLC DataFrame containing price data.
    
    Returns
    -------
    pd.DataFrame
        DataFrame containing only the rows for red days.

    Examples
    --------
    >>> red_days = get_red_day_subset(ohlc_df)
    >>> print(red_days.head())
    """
    df_with_types, _ = identify_day_types(ohlc_df)
    red_days = df_with_types[df_with_types['DayType'] == 'red']
    return red_days

# Counting and Percentage Functions




def get_green_day_count(day_types):
    """
    Count the number of 'green' days in a Series of day types.

    Parameters
    ----------
    day_types : pd.Series
        Series containing day type values ('green', 'red', 'neutral').

    Returns
    -------
    int
        The total count of green days.

    Examples
    --------
    >>> df_with_types, _ = identify_day_types(ohlc_df)
    >>> green_count = get_green_day_count(df_with_types['DayType'])
    >>> print(f"Number of green days: {green_count}")
    """
    return (day_types == 'green').sum()

def get_red_day_count(day_types):
    """
    Count the number of 'red' days in a Series of day types.

    Parameters
    ----------
    day_types : pd.Series
        Series containing day type values ('green', 'red', 'neutral').

    Returns
    -------
    int
        The total count of red days.

    Examples
    --------
    >>> df_with_types, _ = identify_day_types(ohlc_df)
    >>> red_count = get_red_day_count(df_with_types['DayType'])
    >>> print(f"Number of red days: {red_count}")
    """
    return (day_types == 'red').sum()

def calculate_percentage(specific_count, total_count):
    """
    Calculate the percentage of a specific count relative to a total count.

    Parameters
    ----------
    specific_count : int
        The count of the specific category (e.g., green or red days).
    total_count : int
        The total count of all categories.

    Returns
    -------
    float
        The percentage of the specific count relative to the total count,
        rounded to 2 decimal places. Returns 0 if total_count is 0.

    Examples
    --------
    >>> percentage = calculate_percentage(30, 100)
    >>> print(f"Percentage: {percentage}%")
    30.0%
    """
    if total_count == 0:
        return 0
    return round((specific_count / total_count) * 100, 2)

# Return calculation functions
def calculate_daily_returns(ohlc_df):
    """
    Calculate daily returns based on Open and Close prices.

    The daily return is calculated as (Close - Open) / Open.

    Parameters
    ----------
    ohlc_df : pd.DataFrame
        DataFrame containing Open and Close prices with columns 'Open' and 'Close'.

    Returns
    -------
    pd.Series
        A Series containing daily returns as decimal values (e.g., 0.02 for 2% return).

    Examples
    --------
    >>> daily_returns = calculate_daily_returns(ohlc_df)
    >>> print(daily_returns.head())
    """
    return (ohlc_df['Close'] - ohlc_df['Open']) / ohlc_df['Open']

# Statistical Analysis Functions
def get_avg_return(return_series):
    """
    Calculate the average (mean) return from a Series of daily returns.

    Parameters
    ----------
    return_series : pd.Series
        Series containing daily returns.

    Returns
    -------
    float
        The average return, rounded to 4 decimal places.

    Examples
    --------
    >>> avg_return = get_avg_return(daily_returns)
    >>> print(f"Average return: {avg_return:.4f}")
    """
    return round(return_series.mean(), 4)

def get_median_return(return_series):
    """
    Calculate the median return from a Series of daily returns.

    The median return represents the middle value when returns are sorted,
    providing a better measure of central tendency when there are outliers.

    Parameters
    ----------
    return_series : pd.Series
        Series containing daily returns.
    
    Returns
    -------
    float
        The median return, rounded to 4 decimal places.
    
    Examples
    --------
    >>> median_return = get_median_return(daily_returns)
    >>> print(f"Median return: {median_return:.4f}")
    """
    return round(return_series.median(), 4)

def get_max_return(return_series):
    """
    Calculate the maximum return from a Series of daily returns.

    Parameters
    ----------
    return_series : pd.Series
        Series containing daily returns. 

    Returns
    -------
    float
        The maximum return, rounded to 4 decimal places.

    Examples
    --------
    >>> max_return = get_max_return(daily_returns)
    >>> print(f"Maximum return: {max_return:.4f}")
    """
    return round(return_series.max(), 4)

def get_min_return(return_series):
    """
    Calculate the minimum return from a Series of daily returns.

    Parameters
    ----------
    return_series : pd.Series
        Series containing daily returns.

    Returns
    -------
    float
        The minimum return, rounded to 4 decimal places.

    Examples
    --------
    >>> min_return = get_min_return(daily_returns)
    >>> print(f"Minimum return: {min_return:.4f}")
    """
    return round(return_series.min(), 4)

def get_return_std_dev(return_series):
    """
    Calculate the standard deviation of returns from a Series of daily returns.

    The standard deviation measures the dispersion of returns around the mean,
    providing a measure of volatility.

    Parameters
    ----------
    return_series : pd.Series
        Series containing daily returns.

    Returns
    -------
    float
        The standard deviation of returns, rounded to 4 decimal places.

    Examples
    --------
    >>> std_dev = get_return_std_dev(daily_returns)
    >>> print(f"Standard deviation: {std_dev:.4f}")
    """
    return round(return_series.std(), 4)


import pandas as pd
import numpy as np
from ohlc_analysis import identify_day_types

def win_loss_ratio(df):
    """
    Calculate Win/Loss ratio from OHLC DataFrame.
    
    The Win/Loss ratio is a fundamental market strength indicator that measures
    the relationship between profitable trading periods (green days) and losing
    periods (red days). A ratio above 1.0 indicates more winning days than
    losing days, suggesting strong market momentum.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Open' and 'Close' columns.
    
    Returns:
        float: Win/Loss ratio (green_days / red_days).
               - Values > 1.0: More green days than red days
               - Values < 1.0: More red days than green days  
               - float('inf'): No red days (all gains)
               - 0: No price changes or insufficient data
    
    Example:
        >>> df = pd.DataFrame({'Open': [100, 102, 98, 105, 103], 
        ...                    'Close': [102, 98, 105, 103, 107]})
        >>> win_loss_ratio(df)
        1.5
    """
    if len(df) < 1:
        return 0
    
    # Use the identify_day_types function from ohlc_analysis
    df_with_types, _ = identify_day_types(df)
    
    green_days = (df_with_types['DayType'] == 'green').sum()
    red_days = (df_with_types['DayType'] == 'red').sum()
    
    # Calculate ratio (avoid division by zero)
    if red_days == 0:
        return float('inf') if green_days > 0 else 0
    
    return green_days / red_days


def win_rate(df):
    """
    Calculate Win Rate (percentage of winning days).
    
    The Win Rate shows the probability of a positive return on any given day
    by calculating the percentage of days where the price increased. This is
    a fundamental market strength indicator that complements the Win/Loss ratio.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Open' and 'Close' columns.
    
    Returns:
        float: Win Rate as a percentage (0-100).
               - 50%: Equal green and red days
               - >50%: More green days (bullish tendency)
               - <50%: More red days (bearish tendency)
    
    Example:
        >>> df = pd.DataFrame({'Open': [100, 102, 98, 105, 103], 
        ...                    'Close': [102, 98, 105, 103, 107]})
        >>> win_rate(df)
        60.0
    """
    if len(df) < 1:
        return 0.0
    
    # Use the identify_day_types function from ohlc_analysis
    df_with_types, percentages = identify_day_types(df)
    
    return percentages['green']


def max_streak(df, streak_type='win'):
    """
    Calculate the maximum streak (longest consecutive green or red days).
    
    This function finds the longest sequence of consecutive positive or negative returns,
    which indicates the best sustained momentum in the dataset.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Open' and 'Close' columns.
        streak_type (str): 'win' for green days or 'loss' for red days.
    
    Returns:
        int: Maximum number of consecutive days of the specified type.
    
    Example:
        >>> df = pd.DataFrame({'Open': [100, 102, 105, 108, 95, 98, 101, 104], 
        ...                    'Close': [102, 105, 108, 95, 98, 101, 104, 107]})
        >>> max_streak(df, 'win')
        4
    """
    if len(df) < 1:
        return 0
    
    # Use the identify_day_types function from ohlc_analysis
    df_with_types, _ = identify_day_types(df)
    
    # Determine which day type to look for
    target_type = 'green' if streak_type == 'win' else 'red'
    
    # Create a boolean mask for the target day type
    is_target = df_with_types['DayType'] == target_type
    
    # Use cumsum trick to identify consecutive groups (cumsum stands for cumulative sum - it calculates the cumulative sum of values in a Series or array)
    # When we encounter a non-target day, increment the group counter
    groups = (~is_target).cumsum()
    
    # Count consecutive occurrences within each group where is_target is True
    if is_target.any():
        streak_lengths = is_target.groupby(groups).sum()
        return int(streak_lengths.max())
    else:
        return 0


def avg_streak(df, streak_type='win'):
    """
    Calculate the average streak length.
    
    This function finds all streaks and calculates their average length,
    providing insight into typical sustained momentum patterns.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Open' and 'Close' columns.
        streak_type (str): 'win' for green days or 'loss' for red days.
    
    Returns:
        float: Average length of streaks.
    
    Example:
        >>> df = pd.DataFrame({'Open': [100, 102, 105, 95, 98, 101, 104, 90], 
        ...                    'Close': [102, 105, 95, 98, 101, 104, 90, 92]})
        >>> avg_streak(df, 'win')
        2.33
    """
    if len(df) < 1:
        return 0.0
    
    # Use the identify_day_types function from ohlc_analysis
    df_with_types, _ = identify_day_types(df)
    
    # Determine which day type to look for
    target_type = 'green' if streak_type == 'win' else 'red'
    
    # Create a boolean mask for the target day type
    is_target = df_with_types['DayType'] == target_type
    
    # Use cumsum trick to identify consecutive groups
    groups = (~is_target).cumsum()
    
    # Get all streak lengths (excluding zeros)
    streak_lengths = is_target.groupby(groups).sum()
    streak_lengths = streak_lengths[streak_lengths > 0]
    
    if len(streak_lengths) == 0:
        return 0.0
    
    return float(streak_lengths.mean())


def calculate_all_metrics(df):
    """
    Calculate all win/loss metrics at once for efficiency.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Open' and 'Close' columns.
    
    Returns:
        dict: Dictionary containing all calculated metrics.
    
    Example:
        >>> df = pd.DataFrame({'Open': [100, 102, 98, 105, 103], 
        ...                    'Close': [102, 98, 105, 103, 107]})
        >>> metrics = calculate_all_metrics(df)
        >>> print(metrics)
        {'win_loss_ratio': 1.5, 'win_rate': 60.0, ...}
    """
    metrics = {
        'win_loss_ratio': win_loss_ratio(df),
        'win_rate': win_rate(df),
        'max_win_streak': max_streak(df, 'win'),
        'max_loss_streak': max_streak(df, 'loss'),
        'avg_win_streak': avg_streak(df, 'win'),
        'avg_loss_streak': avg_streak(df, 'loss')
    }
    
    return metrics


# Backward compatibility wrapper functions
def max_win_streak(prices):
    """Backward compatibility wrapper. Use max_streak(df, 'win') instead."""
    if isinstance(prices, list):
        df = pd.DataFrame({'Open': prices[:-1], 'Close': prices[1:]})
    else:
        df = prices
    return max_streak(df, 'win')


def max_loss_streak(prices):
    """Backward compatibility wrapper. Use max_streak(df, 'loss') instead."""
    if isinstance(prices, list):
        df = pd.DataFrame({'Open': prices[:-1], 'Close': prices[1:]})
    else:
        df = prices
    return max_streak(df, 'loss')


def avg_win_streak(prices):
    """Backward compatibility wrapper. Use avg_streak(df, 'win') instead."""
    if isinstance(prices, list):
        df = pd.DataFrame({'Open': prices[:-1], 'Close': prices[1:]})
    else:
        df = prices
    return avg_streak(df, 'win')


def avg_loss_streak(prices):
    """Backward compatibility wrapper. Use avg_streak(df, 'loss') instead."""
    if isinstance(prices, list):
        df = pd.DataFrame({'Open': prices[:-1], 'Close': prices[1:]})
    else:
        df = prices
    return avg_streak(df, 'loss')
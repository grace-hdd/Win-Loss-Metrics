
def max_win_streak(prices):
    """
    Calculate the maximum win streak (longest consecutive green days).
    
    This function finds the longest sequence of consecutive positive returns,
    which indicates the best sustained bullish momentum in the dataset.
    
    Args:
        prices (list): List or array of price data in chronological order.
                      Must contain at least 2 data points.
    
    Returns:
        int: Maximum number of consecutive green days.
             - 0: No green days or insufficient data
             - 1+: Longest streak of consecutive up days
    
    Example:
        >>> prices = [100, 102, 105, 108, 95, 98, 101, 104, 107]
        >>> max_win_streak(prices)
        4
        # Days 1-3 had 3 consecutive green days, days 5-8 had 4 consecutive green days
    """
    if len(prices) < 2:
        return 0
    
    max_streak = 0
    current_streak = 0
    
    # Check each day for consecutive green days
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:  # Green day
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:  # Red day or flat - reset streak
            current_streak = 0
    
    return max_streak
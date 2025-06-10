def max_loss_streak(prices):
    """
    Calculate the maximum loss streak (longest consecutive red days).
    
    This function finds the longest sequence of consecutive negative returns,
    which indicates the worst sustained bearish momentum in the dataset.
    
    Args:
        prices (list): List or array of price data in chronological order.
                      Must contain at least 2 data points.
    
    Returns:
        int: Maximum number of consecutive red days.
             - 0: No red days or insufficient data
             - 1+: Longest streak of consecutive down days
    
    Example:
        >>> prices = [100, 98, 95, 92, 102, 99, 96, 93, 90]
        >>> max_loss_streak(prices)
        4
        # Days 1-3 had 3 consecutive red days, days 5-8 had 4 consecutive red days
    """
    if len(prices) < 2:
        return 0
    
    max_streak = 0
    current_streak = 0
    
    # Check each day for consecutive red days
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:  # Red day
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:  # Green day or flat - reset streak
            current_streak = 0
    
    return max_streak

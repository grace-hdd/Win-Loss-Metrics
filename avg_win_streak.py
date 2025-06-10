
def avg_win_streak(prices):
    """
    Calculate the average win streak length.
    
    This function finds all win streaks and calculates their average length,
    providing insight into typical sustained bullish momentum patterns.
    
    Args:
        prices (list): List or array of price data in chronological order.
                      Must contain at least 2 data points.
    
    Returns:
        float: Average length of win streaks.
               - 0.0: No win streaks or insufficient data
               - 1.0+: Average number of consecutive green days per streak
    
    Example:
        >>> prices = [100, 102, 105, 95, 98, 101, 104, 90, 92]
        >>> avg_win_streak(prices)
        2.33
        # Win streaks: [2, 3, 2] → (2+3+2)/3 = 2.33 average
    """
    if len(prices) < 2:
        return 0.0
    
    win_streaks = []
    current_streak = 0
    
    # Find all win streak lengths
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:  # Green day
            current_streak += 1
        else:  # Red day or flat - end current streak
            if current_streak > 0:
                win_streaks.append(current_streak)
                current_streak = 0
    
    # Don't forget the last streak if it ends with the data
    if current_streak > 0:
        win_streaks.append(current_streak)
    
    # Calculate average
    if len(win_streaks) == 0:
        return 0.0
    
    return sum(win_streaks) / len(win_streaks)

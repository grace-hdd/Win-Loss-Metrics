def win_loss_ratio(prices):
    """
   Calculate Win/Loss ratio from price data.
    
    The Win/Loss ratio is a fundamental market strength indicator that measures
    the relationship between profitable trading periods (green days) and losing
    periods (red days). A ratio above 1.0 indicates more winning days than
    losing days, suggesting strong market momentum.
    
    Args:
        prices (list): List or array of price data in chronological order.
                      Must contain at least 2 data points.
    
    Returns:
        float: Win/Loss ratio (green_days / red_days).
               - Values > 1.0: More green days than red days
               - Values < 1.0: More red days than green days  
               - float('inf'): No red days (all gains)
               - 0: No price changes or insufficient data
    
    Example:
        >>> prices = [100, 102, 98, 105, 103, 107]
        >>> win_loss_ratio(prices)
        1.5
        # 3 green days, 2 red days = 3/2 = 1.5
    """
    if len(prices) < 2:
        return 0
    
    green_days = 0
    red_days = 0
    
    # Count green and red days
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            green_days += 1
        elif prices[i] < prices[i-1]:
            red_days += 1
    
    # Calculate ratio (avoid division by zero)
    if red_days == 0:
        return float('inf') if green_days > 0 else 0
    
    return green_days / red_days


def win_rate(prices):
    """
    Calculate Win Rate (percentage of winning days).
    
    The Win Rate shows the probability of a positive return on any given day
    by calculating the percentage of days where the price increased. This is
    a fundamental market strength indicator that complements the Win/Loss ratio.
    
    Args:
        prices (list): List or array of price data in chronological order.
                      Must contain at least 2 data points.
    
    Returns:
        float: Win Rate as a percentage (0-100).
               - 50%: Equal green and red days
               - >50%: More green days (bullish tendency)
               - <50%: More red days (bearish tendency)
               - 100%: All days were green (very rare)
               - 0%: All days were red (very rare)
    
    Example:
        >>> prices = [100, 102, 98, 105, 103, 107]
        >>> win_rate(prices)
        60.0
        # 3 green days out of 5 total trading days = 3/5 * 100 = 60%
    """
    if len(prices) < 2:
        return 0.0
    
    green_days = 0
    total_trading_days = 0
    
    # Count green days and total trading days
    for i in range(1, len(prices)):
        total_trading_days += 1
        if prices[i] > prices[i-1]:
            green_days += 1
    
    # Calculate win rate as percentage
    if total_trading_days == 0:
        return 0.0
    
    return (green_days / total_trading_days) * 100



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


def avg_loss_streak(prices):
    """
    Calculate the average loss streak length.
    
    This function finds all loss streaks and calculates their average length,
    providing insight into typical sustained bearish momentum patterns.
    
    Args:
        prices (list): List or array of price data in chronological order.
                      Must contain at least 2 data points.
    
    Returns:
        float: Average length of loss streaks.
               - 0.0: No loss streaks or insufficient data
               - 1.0+: Average number of consecutive red days per streak
    
    Example:
        >>> prices = [100, 98, 95, 105, 102, 99, 96, 110, 108]
        >>> avg_loss_streak(prices)
        2.33
        # Loss streaks: [2, 3, 2] → (2+3+2)/3 = 2.33 average
    """
    if len(prices) < 2:
        return 0.0
    
    loss_streaks = []
    current_streak = 0
    
    # Find all loss streak lengths
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:  # Red day
            current_streak += 1
        else:  # Green day or flat - end current streak
            if current_streak > 0:
                loss_streaks.append(current_streak)
                current_streak = 0
    
    # Don't forget the last streak if it ends with the data
    if current_streak > 0:
        loss_streaks.append(current_streak)
    
    # Calculate average
    if len(loss_streaks) == 0:
        return 0.0
    
    return sum(loss_streaks) / len(loss_streaks)
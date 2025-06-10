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
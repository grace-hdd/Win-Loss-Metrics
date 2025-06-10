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

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

import pandas as pd
from win_loss_metrics import (
    win_loss_ratio, win_rate, max_streak, avg_streak, calculate_all_metrics
)

# Load the Bitcoin OHLC data
df = pd.read_csv('top5_daily_ohlcv_since_2018-02-09.csv')

# Rename columns to match expected format (capitalize first letter)
df.columns = df.columns.str.capitalize()

# Ensure we have the required columns
if 'Open' not in df.columns or 'Close' not in df.columns:
    print("Error: DataFrame must have 'Open' and 'Close' columns")
else:
    print("Bitcoin OHLC Data Analysis")
    print("=" * 50)
    
    # Calculate individual metrics
    print(f"\nWin/Loss Ratio: {win_loss_ratio(df):.2f}")
    print(f"Win Rate: {win_rate(df):.2f}%")
    print(f"Maximum Win Streak: {max_streak(df, 'win')} days")
    print(f"Maximum Loss Streak: {max_streak(df, 'loss')} days")
    print(f"Average Win Streak: {avg_streak(df, 'win'):.2f} days")
    print(f"Average Loss Streak: {avg_streak(df, 'loss'):.2f} days")
    
    # Calculate all metrics at once
    print("\n" + "=" * 50)
    print("All Metrics (calculated efficiently):")
    print("=" * 50)
    
    all_metrics = calculate_all_metrics(df)
    for metric, value in all_metrics.items():
        if isinstance(value, float) and value != float('inf'):
            print(f"{metric}: {value:.2f}")
        else:
            print(f"{metric}: {value}")
    
    # Demonstrate the efficiency improvement
    print("\n" + "=" * 50)
    print("Key Improvements:")
    print("=" * 50)
    print("1. ✓ Uses vectorized pandas operations (no loops)")
    print("2. ✓ Leverages identify_day_types from ohlc_analysis")
    print("3. ✓ Unified streak functions with 'win'/'loss' parameter")
    print("4. ✓ Efficient batch calculation with calculate_all_metrics()") 
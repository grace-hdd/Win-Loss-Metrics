# Win-Loss-Metrics

A comprehensive Python library for calculating win/loss trading metrics from price data. This collection provides essential market analysis functions to evaluate trading performance and momentum patterns.

## Functions Overview

### Core Metrics

#### `win_loss_ratio(prices)`
**File:** `win_loss_ratio.py`  
Calculates the Win/Loss ratio from price data - the fundamental relationship between green days and red days.
- **Returns:** Float ratio (green_days / red_days)
- **Example:** `win_loss_ratio([100, 102, 98, 105]) → 1.5` (3 green, 2 red)

#### `win_rate(prices)`
**File:** `win_rate.py`  
Calculates the Win Rate as a percentage - probability of positive returns.
- **Returns:** Percentage (0-100)
- **Example:** `win_rate([100, 102, 98, 105, 103, 107]) → 60.0` (3 of 5 days were green)

### Streak Analysis

#### `max_win_streak(prices)`
**File:** `max_win_streak.py`  
Finds the longest consecutive sequence of green days.
- **Returns:** Integer count of maximum consecutive up days
- **Example:** `max_win_streak([100, 102, 105, 108, 95]) → 3`

#### `max_loss_streak(prices)`
**File:** `max_loss_streak.py`  
Finds the longest consecutive sequence of red days.
- **Returns:** Integer count of maximum consecutive down days
- **Example:** `max_loss_streak([100, 98, 95, 92, 102]) → 3`

#### `avg_win_streak(prices)`
**File:** `avg_win_streak.py`  
Calculates the average length of all win streaks.
- **Returns:** Float average of win streak lengths
- **Calculation:** Sum of all win streak lengths ÷ number of win streaks
- **Example:** Win streaks [2, 3, 2] → `(2+3+2)/3 = 2.33`

#### `avg_loss_streak(prices)`
**File:** `avg_loss_streak.py`  
Calculates the average length of all loss streaks.
- **Returns:** Float average of loss streak lengths
- **Calculation:** Sum of all loss streak lengths ÷ number of loss streaks
- **Example:** Loss streaks [2, 3, 2] → `(2+3+2)/3 = 2.33`

## Usage

### Basic Example
```python
# Import any function
from win_loss_ratio import win_loss_ratio
from win_rate import win_rate
from max_win_streak import max_win_streak

# Sample price data
prices = [100, 102, 98, 105, 103, 107, 104, 110]

# Calculate metrics
ratio = win_loss_ratio(prices)          # 1.67 (5 green, 3 red)
rate = win_rate(prices)                 # 62.5% (5 of 8 days green)
max_streak = max_win_streak(prices)     # 2 (longest consecutive green)

print(f"Win/Loss Ratio: {ratio:.2f}")
print(f"Win Rate: {rate:.1f}%")
print(f"Max Win Streak: {max_streak} days")
```

### Input Requirements
- **prices:** List or array of numerical price data in chronological order
- **Minimum:** 2 data points required for meaningful calculations
- **Format:** `[100, 102, 98, 105, 103, ...]` (any numerical values)

## Interpretation Guide

### Win/Loss Ratio
- `> 1.0` = More green days than red (bullish)
- `< 1.0` = More red days than green (bearish)
- `= 1.0` = Equal green and red days (neutral)
- `inf` = No red days (very bullish)

### Win Rate
- `> 50%` = More green days (bullish tendency)
- `< 50%` = More red days (bearish tendency)
- `= 50%` = Equal green and red days (neutral)

### Streak Analysis
- **Max streaks** show extreme momentum periods
- **Average streaks** reveal typical momentum patterns
- Higher values indicate stronger sustained trends

## Files Structure
```
win-loss-metrics/
├── win_loss_ratio.py    # Core win/loss ratio calculation
├── win_rate.py          # Win rate percentage calculation
├── max_win_streak.py    # Maximum consecutive green days
├── max_loss_streak.py   # Maximum consecutive red days
├── avg_win_streak.py    # Average win streak length
├── avg_loss_streak.py   # Average loss streak length
└── README.md           # This documentation
```
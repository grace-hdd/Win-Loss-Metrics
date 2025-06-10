"""
Win-Loss Metrics Library
========================

A comprehensive Python library for calculating win/loss trading metrics from price data.
This collection provides essential market analysis functions to evaluate trading 
performance and momentum patterns.

Usage:
    from win_loss_metrics import win_loss_ratio, win_rate, max_win_streak
    
    prices = [100, 102, 98, 105, 103, 107]
    ratio = win_loss_ratio(prices)
    rate = win_rate(prices)
    streak = max_win_streak(prices)
"""

from .win_loss_ratio import win_loss_ratio
from .win_rate import win_rate
from .max_win_streak import max_win_streak
from .max_loss_streak import max_loss_streak
from .avg_win_streak import avg_win_streak
from .avg_loss_streak import avg_loss_streak

__version__ = "1.0.0"
__author__ = "Win-Loss Metrics Team"
__description__ = "Comprehensive win/loss trading metrics for price data analysis"

# Expose all functions
__all__ = [
    "win_loss_ratio",
    "win_rate", 
    "max_win_streak",
    "max_loss_streak",
    "avg_win_streak",
    "avg_loss_streak"
] 
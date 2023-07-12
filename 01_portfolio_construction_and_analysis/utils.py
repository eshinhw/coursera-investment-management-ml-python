import pandas as pd


def drawdown(return_series: pd.Series):
    """
    Takes a times series of asset returns
    Computes and returns a DataFrame that contains:
    the wealth index
    the previous peaks
    percentage drawdown
    """
    wealth_index = 1000 * (1 + return_series).cumprod()
    prev_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - prev_peaks) / prev_peaks
    return pd.DataFrame(
        {"Wealth": wealth_index, "Peaks": prev_peaks, "Drawdown": drawdowns}
    )

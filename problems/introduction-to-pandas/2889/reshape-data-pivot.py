import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivot_weather = weather.pivot(index='month', columns='city', values='temperature')
    return pivot_weather
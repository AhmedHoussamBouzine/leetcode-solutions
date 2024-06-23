import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products_filled = products.fillna(value={'quantity': 0})
    return products_filled
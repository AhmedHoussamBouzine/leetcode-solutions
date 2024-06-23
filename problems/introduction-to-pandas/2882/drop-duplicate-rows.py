import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    unique_customers = customers.drop_duplicates(subset=['email'])
    return unique_customers
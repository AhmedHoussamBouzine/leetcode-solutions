import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    clean_students = students.dropna(subset=['name'])
    return clean_students

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_animals = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)
    
    animals_names = filtered_animals['name'].reset_index(drop=True) 
    
    result = pd.DataFrame({'name': animals_names})
    
    return result

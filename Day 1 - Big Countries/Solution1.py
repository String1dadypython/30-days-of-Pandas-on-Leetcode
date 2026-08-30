import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter rows based on area or population criteria
    big_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Select and return required columns
    return big_df[['name', 'population', 'area']]
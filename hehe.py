import pandas as pd
from typing import List, Union

def calculate_statistics(data: List[Union[int, float]]) -> pd.DataFrame:
    """
    Converts a list of numbers into a DataFrame and returns summary statistics.
    """
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(data, columns=['Values'])
    return df.describe()

if __name__ == "__main__":
    # Example usage of the calculation utility
    sample_data = [15, 22, 34, 42, 58]
    summary = sample_data
    print(summary)
    
import pandas as pd

def sort_rows_by_location_and_price(df):
    """
    Sorts the rows of a DataFrame by 'Location' (ascending) and then by 'Price' (descending).

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be sorted.

    Returns:
    - sorted_df (pd.DataFrame): The sorted DataFrame.
    """
    # Sort by 'Location' in ascending order, then by 'Price' in descending order
    sorted_df = df.sort_values(by=['Location', 'Price'], ascending=[True, False])
    return sorted_df

import pandas as pd

def remove_rows_with_roommates(df):
    """
    Removes rows from the DataFrame where 'Roommates' is equal to 1.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
    - cleaned_df (pd.DataFrame): The DataFrame with rows removed where 'Roommates' is 1.
    """
    # Remove rows where 'Roommates' is 1
    cleaned_df = df[df['Roommates'] != 1]

    # Count how many rows were removed
    rows_removed = df.shape[0] - cleaned_df.shape[0]

    # Output the number of rows removed
    print(f"Number of 'Roommates' listings removed: {rows_removed}")

    return cleaned_df
import pandas as pd

def remove_duplicate_rows(df):
    """
    Removes duplicate rows from the DataFrame based on identical values in columns 
    except for 'Listing ID', 'Date Posted', 'Title', and 'URL'. 
    Reports the number of rows removed.

    Parameters:
    - df (pd.DataFrame): The input DataFrame from which to remove duplicates.

    Returns:
    - df (pd.DataFrame): The cleaned DataFrame with duplicates removed.
    - rows_removed (int): The number of rows removed.
    """
    # Keep a copy of the original number of rows for comparison
    original_row_count = df.shape[0]

    # List of columns to check for duplicates, excluding 'Listing ID', 'Date Posted', 'Title', and 'URL'
    columns_to_check = df.columns.difference(['Listing ID', 'Date Posted', 'Title', 'URL'])

    # Drop duplicates based on the specified columns
    df_cleaned = df.drop_duplicates(subset=columns_to_check)

    # Calculate how many rows were removed
    rows_removed = original_row_count - df_cleaned.shape[0]
    



    return df_cleaned, rows_removed
import pandas as pd

def remove_rows_with_not_available_location(df):
    """
    Removes rows from the DataFrame where 'Location' is equal to 'Not Available'.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
    - cleaned_df (pd.DataFrame): The DataFrame with rows removed where 'Location' is 'Not Available'.
    """
    # Remove rows where 'Location' is 'Not Available'
    cleaned_df = df[df['Location'] != 'Not available']

    # Count how many rows were removed
    rows_removed = df.shape[0] - cleaned_df.shape[0]

    # Output the number of rows removed
    print(f"Number of rows removed where 'Location' was 'Not available': {rows_removed}")

    return cleaned_df
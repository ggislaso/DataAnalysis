import pandas as pd

def remove_price_outliers(df):
    """
    Removes rows from the DataFrame where 'Price' is greater than 10,000.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
    - cleaned_df (pd.DataFrame): The DataFrame with rows removed where 'Price' is greater than 10,000.
    """
    # Remove rows where 'Price' is greater than 10,000
    cleaned_df = df[df['Price'] <= 10000]

    # Count how many rows were removed
    rows_removed = df.shape[0] - cleaned_df.shape[0]

    # Output the number of rows removed
    print(f"Number of rows removed where 'Price' was greater than 10,000: {rows_removed}")

    return cleaned_df
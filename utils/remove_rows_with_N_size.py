import pandas as pd

def remove_rows_with_N_size(input_file):
    """
    Removes rows from the CSV where 'Size' is equal to 'N'.

    Parameters:
    - input_file (str): The file path for the input CSV file.

    Returns:
    - df (pd.DataFrame): The DataFrame with rows removed where 'Size' is 'N'.
    """
    # Load the CSV
    df = pd.read_csv(input_file)

    # Remove rows where 'Size' is 'N'
    df_cleaned = df[df['Size'] != 'N']

    # Count how many rows were removed
    rows_removed_due_to_size = df.shape[0] - df_cleaned.shape[0]

    # Output the number of rows removed due to 'N' size
    print(f"Number of rows removed due to 'N' size: {rows_removed_due_to_size}")

    return df_cleaned
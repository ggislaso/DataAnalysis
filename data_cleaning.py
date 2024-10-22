import pandas as pd

def clean_scraped_data(input_file, output_file):
    """
    Removes rows from the CSV where 'Size' is equal to 'N'.

    Parameters:
    - input_file (str): The file path for the input CSV file.
    - output_file (str): The file path for the output cleaned CSV file.

    Returns:
    - df (pd.DataFrame): The DataFrame with rows removed where 'Size' is 'N'.
    """
    # Load the CSV
    df = pd.read_csv(input_file)

    # Remove rows where 'Size' is 'N'
    df = df[df['Size'] != 'N']

    # Save the cleaned data to a new CSV
    df.to_csv(output_file, index=False)

    return df

# Example usage:
input_file = r'C:\Users\17809\Projects\data\scraped_data.csv'
output_file = r'C:\Users\17809\Projects\data\cleaned_scraped_data.csv'
cleaned_df = clean_scraped_data(input_file, output_file)
print(cleaned_df.head())
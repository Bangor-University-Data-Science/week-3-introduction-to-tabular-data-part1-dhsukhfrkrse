import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = []
    
    for column in df.columns:
        summary_data.append({
            'Feature Name': column,
            'Data Type': str(df[column].dtype),
            'Number of Unique Values': df[column].nunique(),
            'Has Missing Values?': df[column].isnull().any()
        })
    
    summary_df = pd.DataFrame(summary_data)
    
    return summary_df

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    
    for feature in categorical_features:
        unique_values[feature] = df[feature].unique().tolist()
        
        print(f"\n{feature} unique values:")
        for value in unique_values[feature]:
            print(f"- {value}")
    
    return unique_values

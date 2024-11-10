import pandas as pd
import os

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__)) 
        project_root = os.path.dirname(current_dir)  
        
        if filepath.startswith('../'):
            filepath = filepath.replace('../../', '')
        
        absolute_path = os.path.join(project_root, filepath)
        
        print(f"Trying to load file from: {absolute_path}")  
        
        df = pd.read_csv(absolute_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath} (Absolute path: {absolute_path})")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

import pandas as pd
import os 
from src.decorators.decorators import timeit, logit  


@logit
@timeit 
def load_data(data_path):
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)
    elif data_path.endswith("xlsx"):
        df = pd.read_excel(data_path)
        
    else:
        raise ValueError("Unsupported file format")
    print("Data loaded successfully")
    
    return df

@logit
@timeit 
def clean_data(df):
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    
    print("Data cleaned Successfully")
    return df

@logit
@timeit 
def analyze_data(df): 
    print("Basic Data Analysis")
    print(df.describe())
    print("\nProducts with  highest price:")
    highestPrices = df.nlargest(3, "price")
    print(highestPrices)
    print("\nLowest price product:")
    minPrices = df.nsmallest(1, "price")
    print(minPrices)
    
    
 
@logit
@timeit    
def save_clean_data(df, output_path):
    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)
    elif output_path.endswith(".xlsx"):
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported file format")
    print(f"Clean data saved to {output_path}")         
    
if __name__ == "__main__":
    data_path = "data/raw/products.csv"   
    output_path = "data/processed/cleaned_products.csv"
    
    df = load_data(data_path)
    df = clean_data(df) 
    analyze_data(df)
    os.makedirs("data/processed", exist_ok=True)
   
    save_clean_data(df,output_path) 
    
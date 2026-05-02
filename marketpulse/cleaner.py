import pandas as pd

class DataCleaner:
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        df.drop_duplicates(inplace=True)
        
        if 'Acquisition_Cost' in df.columns:
            df['Acquisition_Cost'] = (
                df['Acquisition_Cost']
                .astype(str)
                .str.replace(r'[\,]', '', regex=True)
                .astype(float)
            )
        
        if 'Date' in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df['Date']):
                print(" Date column is already in datetime format - skipping conversion")
            else:
                try:
                    df['Date'] = pd.to_datetime(df['Date'], unit='d', origin='1899-12-30', errors='coerce')
                    print(" Converted Excel serial dates to datetime")
                except:
                    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                    print(" Converted Date column using standard parsing")
        
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        
        cat_cols = ['Campaign_Type', 'Channel_Used', 'Target_Audience', 
                   'Customer_Segment', 'Location', 'Language']
        for col in cat_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.title()
        
        print(f" Data cleaning completed: {len(df):,} rows remaining")
        return df
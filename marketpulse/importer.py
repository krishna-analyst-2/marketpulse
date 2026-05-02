import os
import pandas as pd

class CampaignImporter:
    
    def import_data(self, file_path: str) -> pd.DataFrame:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f" File not found: {file_path}")
        
        ext = file_path.lower()
        
        try:
            if ext.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
                file_type = "Excel (.xlsx)"
            elif ext.endswith('.csv'):
                df = pd.read_csv(file_path)
                file_type = "CSV"
            else:
                raise ValueError(f" Unsupported file format: {ext}\nPlease use .csv or .xlsx")
            
            print(f" Successfully imported {len(df):,} rows from {file_type}: {os.path.basename(file_path)}")
            return df
            
        except Exception as e:
            raise RuntimeError(f" Failed to import file {file_path}\nError: {str(e)}")
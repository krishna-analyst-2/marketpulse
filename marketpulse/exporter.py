import os
import pandas as pd

def export_report(df: pd.DataFrame, metrics: dict, output_path: str = "output/marketpulse_report.xlsx"):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Cleaned_Data', index=False)
        
        metrics['summary'].to_excel(writer, sheet_name='Summary_Statistics')
        
        metrics['by_channel'].to_excel(writer, sheet_name='By_Channel')
        
        metrics['by_campaign_type'].to_excel(writer, sheet_name='By_Campaign_Type')
        
        if 'daily_trend' in metrics:
            metrics['daily_trend'].head(100).to_excel(writer, sheet_name='Daily_Trend')
    
    print(f" Full Excel report successfully exported: {output_path}")
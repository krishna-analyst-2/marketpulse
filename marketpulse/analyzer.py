import pandas as pd

class CampaignAnalyzer:
    
    def analyze(self, df: pd.DataFrame) -> dict:
        metrics = {}
        
        key_metrics = ['Impressions', 'Clicks', 'Conversion_Rate', 
                      'Acquisition_Cost', 'ROI', 'Engagement_Score']
        
        metrics['summary'] = df[key_metrics].describe().round(2)
        
        metrics['by_channel'] = df.groupby('Channel_Used')[['ROI', 'Clicks', 'Impressions']].mean().round(2)
        
        metrics['by_campaign_type'] = df.groupby('Campaign_Type')[['ROI', 'Clicks']].mean().round(2)
        
        if 'Date' in df.columns:
            df_time = df.set_index('Date').sort_index()
            daily_trend = df_time.resample('D')[['Impressions', 'Clicks', 'ROI']].mean()
            metrics['daily_trend'] = daily_trend
        
        if 'Impressions' in df.columns and 'Clicks' in df.columns:
            df['CTR'] = (df['Clicks'] / df['Impressions'] * 100).round(2)
            metrics['overall_ctr'] = df['CTR'].mean().round(2)
        
        print(" Analysis completed - summary statistics and trends generated")
        return metrics
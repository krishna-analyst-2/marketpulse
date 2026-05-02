import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CampaignVisualizer:
    
    def __init__(self):
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.figsize'] = (12, 7)
    
    def visualize(self, df: pd.DataFrame, metrics: dict, output_dir: str = "output"):
        os.makedirs(output_dir, exist_ok=True)
        
        plt.figure()
        channel_data = metrics['by_channel']['ROI'].sort_values(ascending=False)
        sns.barplot(x=channel_data.index, y=channel_data.values, palette="Blues_d")
        plt.title('Average ROI by Marketing Channel', fontsize=16, pad=20)
        plt.xlabel('Channel')
        plt.ylabel('Average ROI')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{output_dir}/1_roi_by_channel.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        if 'daily_trend' in metrics and not metrics['daily_trend'].empty:
            trend = metrics['daily_trend'].tail(60)  
            plt.figure()
            ax1 = plt.gca()
            sns.lineplot(data=trend, x=trend.index, y='ROI', marker='o', label='ROI', color='blue', ax=ax1)
            ax2 = ax1.twinx()
            sns.lineplot(data=trend, x=trend.index, y='Clicks', marker='x', label='Clicks', color='orange', ax=ax2)
            plt.title('Campaign Performance Trend (Last 60 Days)', fontsize=16, pad=20)
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Average ROI', color='blue')
            ax2.set_ylabel('Average Clicks', color='orange')
            plt.legend()
            plt.tight_layout()
            plt.savefig(f"{output_dir}/2_performance_trend.png", dpi=300, bbox_inches='tight')
            plt.close()
        
        plt.figure()
        top_campaigns = df.nlargest(10, 'ROI')[['Campaign_ID', 'ROI', 'Channel_Used']]
        sns.barplot(data=top_campaigns, x='ROI', y='Campaign_ID', hue='Channel_Used', palette="viridis")
        plt.title('Top 10 Campaigns by ROI', fontsize=16, pad=20)
        plt.xlabel('ROI')
        plt.ylabel('Campaign ID')
        plt.tight_layout()
        plt.savefig(f"{output_dir}/3_top_campaigns.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        plt.figure()
        conv_by_type = df.groupby('Campaign_Type')['Conversion_Rate'].mean().sort_values(ascending=False)
        sns.barplot(x=conv_by_type.index, y=conv_by_type.values, palette="Greens_d")
        plt.title('Average Conversion Rate by Campaign Type', fontsize=16, pad=20)
        plt.xlabel('Campaign Type')
        plt.ylabel('Conversion Rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{output_dir}/4_conversion_by_type.png", dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f" 4 Professional visualizations saved to {output_dir}/ folder")
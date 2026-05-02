
import argparse
import os
from marketpulse.importer import CampaignImporter
from marketpulse.cleaner import DataCleaner
from marketpulse.analyzer import CampaignAnalyzer
from marketpulse.visualizer import CampaignVisualizer
from marketpulse.exporter import export_report

def main():
    parser = argparse.ArgumentParser(
        description=" MarketPulse - Marketing Campaign Data Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    default_file = "data/marketing_campaign_cleaned_engineered.xlsx"
    
    parser.add_argument('--input', '-i', default=default_file,
                        help=f'Path to input file (default: {default_file})')
    parser.add_argument('--output', '-o', default='output/marketpulse_report.xlsx',
                        help='Path for output Excel report')
    args = parser.parse_args()

    print("="*70)
    print(" Starting MarketPulse (Modular Version)")
    print("="*70 + "\n")

    # Initialize components
    importer = CampaignImporter()
    cleaner = DataCleaner()
    analyzer = CampaignAnalyzer()
    visualizer = CampaignVisualizer()

    try:
        df_raw = importer.import_data(args.input)
        df_clean = cleaner.clean(df_raw)
        metrics = analyzer.analyze(df_clean)
        visualizer.visualize(df_clean, metrics)
        export_report(df_clean, metrics, args.output)

        print("\n" + "="*70)
        print("MarketPulse completed successfully!")
        print(f" Report  → {args.output}")
        print(f" Charts  → output/ folder")
        print("="*70)

    except FileNotFoundError:
        print(f"\n File not found: {args.input}")
        print("Please make sure the file exists in the 'data/' folder.")
        print(f"Current file name you have: marketing_campaign_cleaned_engineered.xlsx")
    except Exception as e:
        print(f"\n Error: {str(e)}")

if __name__ == "__main__":
    main()
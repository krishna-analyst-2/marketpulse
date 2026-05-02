# MarketPulse - Real-Time Campaign Data Importer

A lightweight, modular Python tool for importing, cleaning, analyzing, and visualizing marketing campaign data from **CSV and Excel files**.

Built exactly as per your **PRD, HLD, and LLD**.

## Features
- Supports both **CSV** and **Excel** files (FR1)
- Data cleaning (duplicates, missing values, date formatting) (FR2)
- Summary statistics + trend analysis (FR3, FR4)
- Professional visualizations using seaborn & matplotlib (FR5)
- Exports full report to Excel with multiple sheets (FR6)

## Project Structure
---
marketpulse/
├── data/                          # Your raw datasets
├── notebooks/                     # Your Google Colab cleaning steps
├── output/                        # Generated reports & charts
├── marketpulse/                   # Main package
├── main.py
├── requirements.txt
└── README.md
text


## Quick Start

1. Install dependencies:
   
   pip install -r requirements.txt

## Run the tool

python main.py --input data/marketing_campaign_dataset.xlsx


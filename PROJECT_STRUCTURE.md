# Project Structure

```
amfex_uber_ride_analysis/
│
├── data/                              # Data directory
│   ├── README.md                      # Data documentation
│   ├── Uber_Data.xlsx                 # Original dataset (297 rides)
│   └── Uber_Data_Cleaned.csv          # Cleaned dataset (generated)
│
├── scripts/                           # Analysis scripts
│   ├── README.md                      # Scripts documentation
│   └── uber_data_analysis.py          # Main analysis script
│
├── Visualizations/                    # Generated charts
│   ├── README.md                      # Visualizations documentation
│   ├── 25_rides_per_time.png          # Rides by time of day
│   ├── 26_payment_method_distribution.png  # Payment methods breakdown
│   ├── 27_distance_vs_fare.png        # Distance vs fare scatter plot
│   ├── 28_fare_distribution.png       # Fare distribution histogram
│   ├── 29_avg_fare_top10_pickup.png   # Top pickup locations
│   └── 30_monthly_sales_trend.png     # Monthly revenue trend
│
├── .gitignore                         # Git ignore rules
├── ANALYSIS_RESULTS.md                # Complete analysis results
├── LICENSE                            # MIT License
├── PROJECT_STRUCTURE.md               # This file
├── QUICKSTART.md                      # Quick start guide
├── README.md                          # Main project documentation
└── requirements.txt                   # Python dependencies
```

## Directory Descriptions

### data/
Contains all datasets used in the project:
- Original Excel dataset with 297 Uber ride records
- Cleaned CSV dataset with additional calculated columns
- Data documentation and quality information

### scripts/
Contains the analysis code:
- Main Python script that performs comprehensive data analysis
- Script documentation with usage instructions
- Modular code structure with clear sections

### Visualizations/
Contains all generated charts:
- 6 professional PNG visualizations
- High-resolution images (300 DPI)
- Documentation explaining each chart

## File Descriptions

### Root Level Files

**README.md**
- Main project documentation
- Overview, key findings, and setup instructions
- Technologies used and skills demonstrated

**ANALYSIS_RESULTS.md**
- Complete detailed results from all analysis questions
- Statistical summaries and insights
- Business recommendations

**QUICKSTART.md**
- Quick setup and installation guide
- Running instructions
- Troubleshooting tips

**PROJECT_STRUCTURE.md**
- This file
- Complete project organization
- Directory and file descriptions

**requirements.txt**
- Python package dependencies
- Version specifications

**LICENSE**
- MIT License
- Open source usage terms

**.gitignore**
- Git ignore patterns
- Excludes generated files and Python artifacts

## Running the Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run analysis:
   ```bash
   python scripts/uber_data_analysis.py
   ```

3. View results:
   - Console output for detailed statistics
   - Visualizations/ folder for charts
   - data/Uber_Data_Cleaned.csv for processed data

## Generated Files

When you run the analysis script, it generates:
- `data/Uber_Data_Cleaned.csv` - Cleaned dataset
- `Visualizations/*.png` - 6 visualization charts

These files are listed in .gitignore and will be regenerated each time you run the script.

## Customization

Each directory contains its own README.md with specific information about:
- Contents and purpose
- Usage instructions
- Customization options
- Technical details

## Project Workflow

1. **Data Input**: Original data in `data/Uber_Data.xlsx`
2. **Processing**: Run `scripts/uber_data_analysis.py`
3. **Output**: 
   - Cleaned data in `data/`
   - Visualizations in `Visualizations/`
   - Console results
4. **Documentation**: Review `ANALYSIS_RESULTS.md` for insights

## Maintenance

- Keep data/ directory for datasets only
- Keep scripts/ directory for analysis code
- Visualizations/ is auto-generated
- Update documentation when adding new features

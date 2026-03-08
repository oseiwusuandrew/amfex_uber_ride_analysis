# Quick Start Guide

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/oseiwusuandrew/amfex_uber_ride_analysis.git
cd amfex_uber_ride_analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Analysis
```bash
python scripts/uber_data_analysis.py
```

## What You'll Get

### Console Output
- Complete analysis results printed to terminal
- Comprehensive statistical analysis and metrics
- Business insights and strategic recommendations

### Generated Files
- `Uber_Data_Cleaned.csv` - Cleaned dataset with new columns
- 6 visualization PNG files in `Visualizations/` folder

### Visualizations Created
1. **25_rides_per_time.png** - Bar chart of rides by time of day
2. **26_payment_method_distribution.png** - Pie chart of payment methods
3. **27_distance_vs_fare.png** - Scatter plot showing distance-fare relationship
4. **28_fare_distribution.png** - Histogram of fare amounts
5. **29_avg_fare_top10_pickup.png** - Bar chart of top pickup locations
6. **30_monthly_sales_trend.png** - Line chart of monthly revenue

## Project Files

- `scripts/uber_data_analysis.py` - Main analysis script
- `data/Uber_Data.xlsx` - Original dataset
- `data/Uber_Data_Cleaned.csv` - Cleaned dataset (generated)
- `Visualizations/` - Generated charts (6 PNG files)
- `README.md` - Project documentation
- `ANALYSIS_RESULTS.md` - Complete analysis results
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules
- `LICENSE` - MIT License

## Key Results at a Glance

- **Total Rides**: 297
- **Total Revenue**: $23,485.91
- **Average Fare**: $79.08
- **Peak Revenue Time**: Morning ($6,585.31)
- **Top Location**: Tamale ($5,076.95)
- **Busiest Day**: Tuesday (51 rides)

## Customization

### Analyze Your Own Data
Replace `data/Uber_Data.xlsx` with your dataset. Ensure it has these columns:
- RideID
- Date
- PickupLocation
- DropoffLocation
- Distance (km)
- FareAmount ($)
- TimeOfDay
- PaymentMethod

### Modify Analysis
Edit `scripts/uber_data_analysis.py` to:
- Add new metrics
- Change visualization styles
- Include additional analysis sections
- Export results in different formats

## Troubleshooting

### Import Errors
```bash
pip install --upgrade pandas openpyxl matplotlib seaborn numpy
```

### File Not Found
Ensure `Uber_Data.xlsx` is in the `data/` directory.

### Visualization Issues
If plots don't display, they're saved as PNG files in the `Visualizations/` folder.

## Next Steps

1. Review `ANALYSIS_RESULTS.md` for detailed findings
2. Check visualizations in `Visualizations/` folder
3. Explore `data/Uber_Data_Cleaned.csv` for processed data
4. Customize the analysis for your specific needs

## Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/oseiwusuandrew/amfex_uber_ride_analysis/issues).

---

Happy Analyzing!

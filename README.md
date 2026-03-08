# Uber Ride Data Analysis

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-oseiwusuandrew-181717.svg?style=flat&logo=github)](https://github.com/oseiwusuandrew)

An end-to-end data analysis project examining Uber ride patterns, revenue trends, and customer behavior to derive actionable business insights using Python.

## Project Overview

This project performs an in-depth analysis of Uber ride data to uncover insights about ride patterns, pricing strategies, and operational efficiency. Through systematic data cleaning, exploratory data analysis, statistical modeling, and visualization, the project delivers actionable recommendations for business optimization and strategic decision-making.

## Key Findings

### Revenue Insights
- **Total Revenue**: $23,485.91 across 297 rides
- **Average Fare**: $79.08 per ride
- **Peak Revenue Period**: Morning ($6,585.31)
- **Highest Revenue Location**: Tamale ($5,076.95)

### Operational Insights
- **Busiest Day**: Tuesday (51 rides)
- **Most Popular Time**: Evening (80 rides)
- **Preferred Payment**: Wallet (77 rides, $82.13 avg fare)
- **Distance-Fare Correlation**: 0.059 (weak correlation suggests pricing is influenced by factors beyond distance)

### Pricing Analysis
- **Most Expensive Period**: Afternoon ($7.99 per km)
- **Highest Earning Month**: January ($87.03 avg fare)
- **Fare Range**: $6.57 - $149.96

## Project Structure

```
amfex_uber_ride_analysis/
│
├── scripts/
│   └── uber_data_analysis.py      # Main analysis script
│
├── data/
│   ├── Uber_Data.xlsx             # Original dataset
│   └── Uber_Data_Cleaned.csv      # Cleaned dataset
│
├── Visualizations/
│   ├── 25_rides_per_time.png
│   ├── 26_payment_method_distribution.png
│   ├── 27_distance_vs_fare.png
│   ├── 28_fare_distribution.png
│   ├── 29_avg_fare_top10_pickup.png
│   └── 30_monthly_sales_trend.png
│
├── README.md                      # Project documentation
├── ANALYSIS_RESULTS.md            # Detailed analysis results
├── QUICKSTART.md                  # Setup and usage guide
├── PROJECT_STRUCTURE.md           # Complete project structure
├── requirements.txt               # Python dependencies
└── LICENSE                        # MIT License
```

For detailed information about each directory, see [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

## Analysis Sections

### 1. Data Understanding
- Dataset contains 297 rides across multiple locations
- 5 unique pickup locations and 5 drop-off locations
- Data spans from January to December 2024
- 4 time periods: Morning, Afternoon, Evening, Night
- 4 payment methods: Wallet, Card, Cash, Mobile Money

### 2. Data Cleaning
- No missing values detected
- No duplicate records found
- All distance and fare values validated as positive
- Created derived metrics: FarePerKM, Month, DayOfWeek

### 3. Descriptive Analysis
- Comprehensive statistical summaries
- Location-based performance metrics
- Time-based ride distribution
- Payment method preferences

### 4. Trend Analysis
- Revenue analysis by time of day
- Payment method profitability
- Top performing pickup locations
- Day of week and monthly patterns

### 5. Visualizations
- 6 professional charts covering:
  - Ride distribution by time
  - Payment method breakdown
  - Distance vs fare relationship
  - Fare distribution patterns
  - Location performance
  - Monthly revenue trends

### 6. Business Insights
- Identified 2 unusual pricing cases for review
- Weak distance-fare correlation suggests dynamic pricing factors
- Weekend rides (88) significantly lower than weekdays (209)
- September showed highest month-over-month growth (56.80%)

## Recommendations

### Pricing Strategy
- Implement dynamic pricing during morning peak hours
- Incentivize wallet payments (highest average fare)
- Review pricing tiers based on $7.12 average per km

### Service Efficiency
- Focus driver deployment in Tamale (top revenue location)
- Optimize routing algorithms to balance distance and fare
- Investigate and standardize the 2 unusual pricing cases

### Driver Distribution
- Increase driver availability during morning hours
- Enhance coverage in top 5 revenue-generating locations
- Balance driver supply across all time periods

## Technologies Used

- **Python 3.14**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualizations
- **openpyxl** - Excel file handling

## Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running the Analysis
```bash
python scripts/uber_data_analysis.py
```

### Output
- Console output with detailed analysis results
- 6 visualization PNG files
- Cleaned dataset (CSV format)

## Sample Visualizations

The analysis generates 6 comprehensive visualizations:
1. Rides per time of day (bar chart)
2. Payment method distribution (pie chart)
3. Distance vs fare relationship (scatter plot)
4. Fare amount distribution (histogram)
5. Average fare by top pickup locations (bar chart)
6. Monthly sales trend (line chart)

## Dataset Information

- **Total Rides**: 297
- **Date Range**: January - December 2024
- **Locations**: 5 pickup and 5 drop-off locations
- **Distance Range**: 1.20 km - 39.61 km
- **Fare Range**: $6.57 - $149.96

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Statistical analysis and correlation
- Data visualization
- Business intelligence and insights
- Python programming
- Problem-solving and critical thinking

## Analysis Coverage

This project provides comprehensive analysis including:
- Data understanding and exploration
- Data quality assessment and cleaning
- Descriptive statistics and distributions
- Trend and grouped analysis
- Visual analytics and data visualization
- Business insights and strategic recommendations
- Deep-dive analysis of key metrics

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/oseiwusuandrew/amfex_uber_ride_analysis/issues).

## Contact

**Andrew Oseiwusu**  
GitHub: [@oseiwusuandrew](https://github.com/oseiwusuandrew)

For questions or collaboration opportunities, reach out via [GitHub](https://github.com/oseiwusuandrew).

---

**Note**: This analysis is based on Uber ride data for educational and portfolio purposes.

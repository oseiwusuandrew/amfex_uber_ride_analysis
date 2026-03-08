# Visualizations Directory

This directory contains all the generated visualizations from the Uber ride data analysis.

## Generated Charts

### 25_rides_per_time.png
Bar chart showing the distribution of rides across different times of day (Morning, Afternoon, Evening, Night).

Key Insight: Evening has the most rides (80), followed by Morning (79).

### 26_payment_method_distribution.png
Pie chart displaying the percentage breakdown of rides by payment method.

Key Insight: Payment methods are well-balanced, with Wallet being slightly preferred (77 rides).

### 27_distance_vs_fare.png
Scatter plot illustrating the relationship between ride distance and fare amount.

Key Insight: Weak correlation (0.0589) suggests pricing is influenced by factors beyond just distance.

### 28_fare_distribution.png
Histogram showing the frequency distribution of fare amounts.

Key Insight: Most fares cluster around the $70-90 range, with some outliers up to $150.

### 29_avg_fare_top10_pickup.png
Bar chart displaying average fare amounts for the top 10 pickup locations.

Key Insight: Tema has the highest average fare, while location-based pricing varies significantly.

### 30_monthly_sales_trend.png
Line chart tracking total monthly revenue throughout 2024.

Key Insight: Revenue shows seasonal variation with September experiencing the highest growth (56.80%).

## Chart Specifications

- Format: PNG
- Resolution: 300 DPI
- Size: Optimized for presentations and reports
- Style: Professional with clear labels and titles

## Regenerating Charts

Charts are automatically generated when running the analysis script:
```bash
python scripts/uber_data_analysis.py
```

All existing charts will be overwritten with updated versions.

## Usage

These visualizations can be used for:
- Project presentations
- GitHub repository showcase
- Data analysis reports
- Business intelligence dashboards
- Academic papers or portfolios

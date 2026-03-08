"""
Uber Ride Data Analysis
End-to-end data analysis project examining ride patterns, revenue trends, and customer behavior.
Includes data cleaning, statistical analysis, visualizations, and business recommendations.

Author: Andrew Oseiwusu
GitHub: https://github.com/oseiwusuandrew
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================================
# SECTION 1: DATA UNDERSTANDING
# ============================================================================

def load_and_explore_data(filepath):
    """Load the dataset and perform initial exploration."""
    print("="*80)
    print("SECTION 1: DATA UNDERSTANDING")
    print("="*80)
    
    # Load data
    df = pd.read_excel(filepath)
    
    # Q1: Total records
    print(f"\n1. Total records (rides): {len(df)}")
    
    # Q2: Column names and data types
    print(f"\n2. Column names and data types:")
    print(df.dtypes)
    
    # Q3: Unique pickup and drop-off locations
    unique_pickup = df['PickupLocation'].nunique()
    unique_dropoff = df['DropoffLocation'].nunique()
    print(f"\n3. Unique pickup locations: {unique_pickup}")
    print(f"   Unique drop-off locations: {unique_dropoff}")
    
    # Q4: Earliest and latest ride date
    df['Date'] = pd.to_datetime(df['Date'])
    earliest = df['Date'].min()
    latest = df['Date'].max()
    print(f"\n4. Earliest ride date: {earliest.date()}")
    print(f"   Latest ride date: {latest.date()}")
    
    # Q5: Rides per time of day
    print(f"\n5. Rides per Time of Day:")
    print(df['TimeOfDay'].value_counts().sort_index())
    
    # Q6: Payment methods
    print(f"\n6. Payment methods used:")
    print(df['PaymentMethod'].value_counts())
    
    return df


# ============================================================================
# SECTION 2: DATA CLEANING
# ============================================================================

def clean_data(df):
    """Clean and prepare the dataset."""
    print("\n" + "="*80)
    print("SECTION 2: DATA CLEANING")
    print("="*80)
    
    # Q7: Check for missing and duplicate values
    print(f"\n7. Missing values per column:")
    print(df.isnull().sum())
    print(f"\n   Duplicate rows: {df.duplicated().sum()}")
    
    # Q8: Replace missing payment methods
    if df['PaymentMethod'].isnull().sum() > 0:
        df['PaymentMethod'].fillna('Unknown', inplace=True)
        print(f"\n8. Missing payment methods replaced with 'Unknown'")
    else:
        print(f"\n8. No missing payment methods found")
    
    # Q9: Convert Date to datetime (already done in load function)
    print(f"\n9. Date column converted to datetime format")
    
    # Q10: Ensure positive values
    negative_distance = (df['Distance (km)'] < 0).sum()
    negative_fare = (df['FareAmount ($)'] < 0).sum()
    df = df[(df['Distance (km)'] > 0) & (df['FareAmount ($)'] > 0)]
    print(f"\n10. Removed {negative_distance} negative distance values")
    print(f"    Removed {negative_fare} negative fare values")
    
    # Q11: Create FarePerKM column
    df['FarePerKM'] = (df['FareAmount ($)'] / df['Distance (km)']).round(2)
    print(f"\n11. Created FarePerKM column")
    
    # Q12: Extract Month and Day of Week
    df['Month'] = df['Date'].dt.month_name()
    df['DayOfWeek'] = df['Date'].dt.day_name()
    print(f"\n12. Added Month and DayOfWeek columns")
    
    return df


# ============================================================================
# SECTION 3: DESCRIPTIVE ANALYSIS
# ============================================================================

def descriptive_analysis(df):
    """Perform descriptive statistical analysis."""
    print("\n" + "="*80)
    print("SECTION 3: DESCRIPTIVE ANALYSIS")
    print("="*80)
    
    # Q13: Fare statistics
    print(f"\n13. Fare Amount Statistics:")
    print(f"    Average: ${df['FareAmount ($)'].mean():.2f}")
    print(f"    Minimum: ${df['FareAmount ($)'].min():.2f}")
    print(f"    Maximum: ${df['FareAmount ($)'].max():.2f}")
    
    # Q14: Distance statistics
    print(f"\n14. Distance Statistics:")
    print(f"    Average: {df['Distance (km)'].mean():.2f} km")
    print(f"    Minimum: {df['Distance (km)'].min():.2f} km")
    print(f"    Maximum: {df['Distance (km)'].max():.2f} km")
    
    # Q15: Pickup location with most rides
    top_pickup = df['PickupLocation'].value_counts().head(1)
    print(f"\n15. Pickup location with most rides:")
    print(f"    {top_pickup.index[0]}: {top_pickup.values[0]} rides")
    
    # Q16: Drop-off location with highest average fare
    avg_fare_dropoff = df.groupby('DropoffLocation')['FareAmount ($)'].mean().sort_values(ascending=False)
    print(f"\n16. Drop-off location with highest average fare:")
    print(f"    {avg_fare_dropoff.index[0]}: ${avg_fare_dropoff.values[0]:.2f}")
    
    # Q17: Time of day with most rides
    top_time = df['TimeOfDay'].value_counts().head(1)
    print(f"\n17. Time of day with most rides:")
    print(f"    {top_time.index[0]}: {top_time.values[0]} rides")
    
    # Q18: Most frequent payment method
    top_payment = df['PaymentMethod'].value_counts().head(1)
    print(f"\n18. Most frequent payment method:")
    print(f"    {top_payment.index[0]}: {top_payment.values[0]} rides")


# ============================================================================
# SECTION 4: TREND AND GROUPED ANALYSIS
# ============================================================================

def trend_analysis(df):
    """Perform trend and grouped analysis."""
    print("\n" + "="*80)
    print("SECTION 4: TREND AND GROUPED ANALYSIS")
    print("="*80)
    
    # Q19: Average fare per time of day
    print(f"\n19. Average fare per time of day:")
    avg_fare_time = df.groupby('TimeOfDay')['FareAmount ($)'].mean().sort_values(ascending=False)
    print(avg_fare_time.round(2))
    
    # Q20: Total revenue per payment method
    print(f"\n20. Total revenue per payment method:")
    revenue_payment = df.groupby('PaymentMethod')['FareAmount ($)'].sum().sort_values(ascending=False)
    print(revenue_payment.round(2))
    
    # Q21: Top 5 pickup locations by revenue
    print(f"\n21. Top 5 pickup locations by total revenue:")
    top5_pickup_revenue = df.groupby('PickupLocation')['FareAmount ($)'].sum().sort_values(ascending=False).head(5)
    print(top5_pickup_revenue.round(2))
    
    # Q22: Average FarePerKM by time of day
    print(f"\n22. Average FarePerKM by time of day:")
    avg_fare_per_km = df.groupby('TimeOfDay')['FarePerKM'].mean().sort_values(ascending=False)
    print(avg_fare_per_km.round(2))
    print(f"    Most expensive period: {avg_fare_per_km.index[0]}")
    
    # Q23: Busiest day of week
    print(f"\n23. Busiest day of week:")
    day_counts = df['DayOfWeek'].value_counts()
    print(f"    {day_counts.index[0]}: {day_counts.values[0]} rides")
    
    # Q24: Average fare per month
    print(f"\n24. Average fare per month:")
    monthly_avg = df.groupby('Month')['FareAmount ($)'].mean().sort_values(ascending=False)
    print(monthly_avg.round(2))
    print(f"    Highest earning month: {monthly_avg.index[0]}")
    
    return avg_fare_time, revenue_payment, top5_pickup_revenue, avg_fare_per_km, day_counts, monthly_avg


# ============================================================================
# SECTION 5: VISUALIZATION TASKS
# ============================================================================

def create_visualizations(df, avg_fare_time, revenue_payment, top5_pickup_revenue):
    """Create all required visualizations."""
    print("\n" + "="*80)
    print("SECTION 5: VISUALIZATION TASKS")
    print("="*80)
    print("\nGenerating visualizations...")
    
    # Q25: Bar chart - rides per time of day
    plt.figure(figsize=(10, 6))
    time_counts = df['TimeOfDay'].value_counts()
    time_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('25. Number of Rides per Time of Day', fontsize=14, fontweight='bold')
    plt.xlabel('Time of Day')
    plt.ylabel('Number of Rides')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../Visualizations/25_rides_per_time.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Q26: Pie chart - payment method distribution
    plt.figure(figsize=(10, 8))
    payment_counts = df['PaymentMethod'].value_counts()
    plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('26. Percentage of Rides by Payment Method', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('../Visualizations/26_payment_method_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Q27: Scatter plot - Distance vs Fare
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Distance (km)'], df['FareAmount ($)'], alpha=0.5, color='green')
    plt.title('27. Distance vs Fare Amount', fontsize=14, fontweight='bold')
    plt.xlabel('Distance (km)')
    plt.ylabel('Fare Amount ($)')
    plt.tight_layout()
    plt.savefig('../Visualizations/27_distance_vs_fare.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Q28: Histogram - Fare distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['FareAmount ($)'], bins=30, color='orange', edgecolor='black')
    plt.title('28. Distribution of Fare Amounts', fontsize=14, fontweight='bold')
    plt.xlabel('Fare Amount ($)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('../Visualizations/28_fare_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Q29: Bar chart - average fare by top 10 pickup locations
    plt.figure(figsize=(12, 6))
    top10_pickup_avg = df.groupby('PickupLocation')['FareAmount ($)'].mean().sort_values(ascending=False).head(10)
    top10_pickup_avg.plot(kind='bar', color='purple', edgecolor='black')
    plt.title('29. Average Fare by Top 10 Pickup Locations', fontsize=14, fontweight='bold')
    plt.xlabel('Pickup Location')
    plt.ylabel('Average Fare ($)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../Visualizations/29_avg_fare_top10_pickup.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Q30: Line chart - monthly total fares
    plt.figure(figsize=(12, 6))
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_revenue = df.groupby('YearMonth')['FareAmount ($)'].sum()
    monthly_revenue.plot(kind='line', marker='o', color='red', linewidth=2)
    plt.title('30. Monthly Total Fares (Sales Trend)', fontsize=14, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Total Fare ($)')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../Visualizations/30_monthly_sales_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("All visualizations saved successfully!")


# ============================================================================
# SECTION 6: INSIGHTS & REPORTING
# ============================================================================

def insights_and_reporting(df):
    """Generate insights and recommendations."""
    print("\n" + "="*80)
    print("SECTION 6: INSIGHTS & REPORTING")
    print("="*80)
    
    # Q31: Time of day with highest revenue
    revenue_by_time = df.groupby('TimeOfDay')['FareAmount ($)'].sum().sort_values(ascending=False)
    print(f"\n31. Time of day with highest total revenue:")
    print(f"    {revenue_by_time.index[0]}: ${revenue_by_time.values[0]:.2f}")
    
    # Q32: Payment method with highest average fare
    avg_fare_payment = df.groupby('PaymentMethod')['FareAmount ($)'].mean().sort_values(ascending=False)
    print(f"\n32. Payment method with highest average fare:")
    print(f"    {avg_fare_payment.index[0]}: ${avg_fare_payment.values[0]:.2f}")
    
    # Q33: Location earning most revenue
    pickup_revenue = df.groupby('PickupLocation')['FareAmount ($)'].sum().sort_values(ascending=False)
    dropoff_revenue = df.groupby('DropoffLocation')['FareAmount ($)'].sum().sort_values(ascending=False)
    print(f"\n33. Locations earning most revenue:")
    print(f"    Top Pickup: {pickup_revenue.index[0]} - ${pickup_revenue.values[0]:.2f}")
    print(f"    Top Drop-off: {dropoff_revenue.index[0]} - ${dropoff_revenue.values[0]:.2f}")
    
    # Q34: Correlation between distance and fare
    correlation = df['Distance (km)'].corr(df['FareAmount ($)'])
    print(f"\n34. Correlation between distance and fare: {correlation:.4f}")
    if correlation > 0.7:
        print("    Strong positive correlation - fare increases with distance")
    elif correlation > 0.4:
        print("    Moderate positive correlation")
    else:
        print("    Weak correlation")
    
    # Q35: Unusual rides
    print(f"\n35. Unusual rides (short distance but high fare):")
    unusual = df[(df['Distance (km)'] < 5) & (df['FareAmount ($)'] > df['FareAmount ($)'].quantile(0.9))]
    print(f"    Found {len(unusual)} unusual rides")
    if len(unusual) > 0:
        print(unusual[['Date', 'PickupLocation', 'DropoffLocation', 'Distance (km)', 'FareAmount ($)', 'FarePerKM']].head())
    
    # Q36: Recommendations
    print(f"\n36. RECOMMENDATIONS FOR UBER MANAGEMENT:")
    print("\n    PRICING STRATEGY:")
    print(f"    - Peak revenue time is {revenue_by_time.index[0]} - consider dynamic pricing")
    print(f"    - {avg_fare_payment.index[0]} has highest avg fare - incentivize this payment method")
    print(f"    - Average FarePerKM is ${df['FarePerKM'].mean():.2f} - review pricing tiers")
    
    print("\n    SERVICE EFFICIENCY:")
    print(f"    - Focus on {pickup_revenue.index[0]} (highest revenue pickup location)")
    print(f"    - Optimize routes to reduce distance while maintaining fare")
    print(f"    - Address {len(unusual)} unusual pricing cases")
    
    print("\n    DRIVER DISTRIBUTION:")
    print(f"    - Deploy more drivers during {revenue_by_time.index[0]}")
    print(f"    - Increase coverage in top 5 revenue locations")
    print(f"    - Balance supply across all times of day")


# ============================================================================
# BONUS QUESTIONS
# ============================================================================

def bonus_analysis(df):
    """Answer bonus questions."""
    print("\n" + "="*80)
    print("BONUS QUESTIONS")
    print("="*80)
    
    # Q37: Average fare per day of week
    print(f"\n37. Average fare per day of week:")
    avg_fare_day = df.groupby('DayOfWeek')['FareAmount ($)'].mean().sort_values(ascending=False)
    print(avg_fare_day.round(2))
    
    # Q38: Weekends vs weekdays
    df['IsWeekend'] = df['DayOfWeek'].isin(['Saturday', 'Sunday'])
    weekend_rides = df[df['IsWeekend']].shape[0]
    weekday_rides = df[~df['IsWeekend']].shape[0]
    print(f"\n38. Weekend vs Weekday rides:")
    print(f"    Weekend rides: {weekend_rides}")
    print(f"    Weekday rides: {weekday_rides}")
    print(f"    Weekends have {'MORE' if weekend_rides > weekday_rides else 'FEWER'} rides than weekdays")
    
    # Q39: Month with highest revenue growth
    print(f"\n39. Monthly revenue analysis:")
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_revenue = df.groupby('YearMonth')['FareAmount ($)'].sum()
    monthly_growth = monthly_revenue.pct_change() * 100
    if len(monthly_growth) > 1:
        max_growth_month = monthly_growth.idxmax()
        print(f"    Highest growth month: {max_growth_month} ({monthly_growth.max():.2f}% growth)")
    
    # Q40: Average fare per KM by payment method
    print(f"\n40. Average FarePerKM by payment method:")
    avg_fare_km_payment = df.groupby('PaymentMethod')['FarePerKM'].mean().sort_values(ascending=False)
    print(avg_fare_km_payment.round(2))


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("\n" + "="*80)
    print("UBER RIDE DATA ANALYSIS")
    print("="*80)
    
    # Load and explore data
    df = load_and_explore_data('../data/Uber_Data.xlsx')
    
    # Clean data
    df = clean_data(df)
    
    # Descriptive analysis
    descriptive_analysis(df)
    
    # Trend analysis
    avg_fare_time, revenue_payment, top5_pickup_revenue, avg_fare_per_km, day_counts, monthly_avg = trend_analysis(df)
    
    # Create visualizations
    create_visualizations(df, avg_fare_time, revenue_payment, top5_pickup_revenue)
    
    # Insights and reporting
    insights_and_reporting(df)
    
    # Bonus questions
    bonus_analysis(df)
    
    # Save cleaned data
    df.to_csv('../data/Uber_Data_Cleaned.csv', index=False)
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print("Cleaned data saved to: data/Uber_Data_Cleaned.csv")
    print("Visualizations saved to: Visualizations/")
    print("="*80)


if __name__ == "__main__":
    main()

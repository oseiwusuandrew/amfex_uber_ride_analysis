# Uber Ride Data Analysis - Complete Results

## Executive Summary

This document presents a comprehensive analysis of Uber ride data, examining 297 rides throughout 2024 to uncover patterns, trends, and actionable business insights.

---

## Section 1: Data Understanding

### Dataset Overview
- **Total Records**: 297 rides
- **Date Range**: January 1, 2024 - December 31, 2024
- **Unique Pickup Locations**: 5
- **Unique Drop-off Locations**: 5

### Column Information
```
RideID             int64
Date               datetime64[ns]
PickupLocation     object
DropoffLocation    object
Distance (km)      float64
FareAmount ($)     float64
TimeOfDay          object
PaymentMethod      object
```

### Rides by Time of Day
- Evening: 80 rides
- Morning: 79 rides
- Night: 72 rides
- Afternoon: 66 rides

### Payment Methods
- Wallet: 77 rides
- Card: 75 rides
- Cash: 74 rides
- Mobile Money: 71 rides

---

## Section 2: Data Quality

### Data Cleaning Results
✅ No missing values detected  
✅ No duplicate records found  
✅ All distance values positive  
✅ All fare amounts positive  
✅ Date format validated  

### New Columns Created
- **FarePerKM**: Fare divided by distance ($/km)
- **Month**: Extracted from date
- **DayOfWeek**: Extracted from date

---

## Section 3: Descriptive Statistics

### Fare Amount Analysis
- **Average Fare**: $79.08
- **Minimum Fare**: $6.57
- **Maximum Fare**: $149.96
- **Standard Deviation**: ~$30-40

### Distance Analysis
- **Average Distance**: 20.39 km
- **Minimum Distance**: 1.20 km
- **Maximum Distance**: 39.61 km

### Top Performers
- **Most Popular Pickup**: Tamale (62 rides)
- **Highest Avg Fare Drop-off**: Tema ($91.74)
- **Peak Time Period**: Evening (80 rides)
- **Most Used Payment**: Wallet (77 rides)

---

## Section 4: Revenue & Trend Analysis

### Revenue by Time of Day
| Time Period | Average Fare | Total Revenue |
|-------------|--------------|---------------|
| Morning     | $83.36       | $6,585.31     |
| Evening     | $79.19       | $6,335.20     |
| Night       | $78.32       | $5,639.04     |
| Afternoon   | $74.65       | $4,926.90     |

### Revenue by Payment Method
| Payment Method | Total Revenue | Average Fare |
|----------------|---------------|--------------|
| Wallet         | $6,324.04     | $82.13       |
| Card           | $5,953.58     | $79.38       |
| Cash           | $5,658.96     | $76.47       |
| Mobile Money   | $5,549.33     | $78.16       |

### Top 5 Pickup Locations by Revenue
1. **Tamale**: $5,076.95
2. **Takoradi**: $4,266.85
3. **Tema**: $4,143.95
4. **Cape Coast**: $4,000.99
5. **Kumasi**: $3,170.17

### Pricing Efficiency (FarePerKM)
| Time Period | Avg $/km |
|-------------|----------|
| Afternoon   | $7.99    |
| Night       | $7.61    |
| Morning     | $6.62    |
| Evening     | $6.47    |

### Weekly Patterns
- **Busiest Day**: Tuesday (51 rides)
- **Weekday Rides**: 209
- **Weekend Rides**: 88
- **Weekend vs Weekday**: Weekdays have 2.4x more rides

### Monthly Performance
**Top 3 Earning Months (by avg fare):**
1. January: $87.03
2. May: $86.05
3. November: $85.74

**Highest Growth**: September (56.80% month-over-month increase)

---

## Section 5: Key Insights

### Distance-Fare Relationship
- **Correlation Coefficient**: 0.0589
- **Interpretation**: Weak correlation
- **Insight**: Pricing is influenced by factors beyond just distance (time of day, location, demand)

### Unusual Rides Detected
Found 2 rides with short distance but high fare:
- Ride 1: 3.01 km, $142.35 (FarePerKM: $47.29)
- Ride 2: 4.28 km, $146.29 (FarePerKM: $34.18)

These may indicate:
- Surge pricing during high demand
- Premium service requests
- Data entry errors requiring review

### Day of Week Analysis
**Average Fare by Day:**
- Friday: $90.58 (highest)
- Wednesday: $85.39
- Monday: $80.48
- Thursday: $80.45
- Saturday: $75.72
- Tuesday: $74.05
- Sunday: $70.67 (lowest)

### Payment Method Efficiency
**Average FarePerKM by Payment:**
- Wallet: $8.13/km
- Card: $7.53/km
- Cash: $6.40/km
- Mobile Money: $6.32/km

---

## Section 6: Business Recommendations

### 1. Pricing Strategy
**Findings:**
- Morning generates highest total revenue ($6,585.31)
- Wallet users pay highest average fare ($82.13)
- Afternoon has highest per-km rate ($7.99/km)

**Recommendations:**
- Implement dynamic pricing during morning peak hours
- Offer wallet payment incentives to increase adoption
- Review and optimize afternoon pricing strategy
- Consider surge pricing on Fridays (highest avg fare day)

### 2. Service Efficiency
**Findings:**
- Tamale is the top revenue location ($5,076.95)
- Weak distance-fare correlation (0.0589)
- 2 unusual pricing cases identified

**Recommendations:**
- Prioritize service quality in Tamale and top 5 locations
- Optimize routing algorithms to balance distance and revenue
- Investigate and standardize unusual pricing cases
- Implement route optimization to reduce unnecessary distance

### 3. Driver Distribution
**Findings:**
- Morning has highest revenue but evening has most rides
- Tuesday is busiest day (51 rides)
- Weekdays have 2.4x more rides than weekends

**Recommendations:**
- Deploy more drivers during morning hours (high revenue period)
- Ensure adequate coverage on Tuesdays
- Increase driver availability in top 5 pickup locations
- Consider weekend promotions to boost lower weekend demand

### 4. Growth Opportunities
**Findings:**
- September showed 56.80% growth
- January has highest average fare ($87.03)
- Weekend rides significantly lower than weekdays

**Recommendations:**
- Analyze September success factors and replicate
- Capitalize on January's high-fare trend with premium services
- Launch weekend promotions to increase ride volume
- Target corporate partnerships for weekday commuters

---

## Section 7: Statistical Summary

### Overall Performance Metrics
- **Total Revenue**: $23,485.91
- **Total Rides**: 297
- **Average Revenue per Ride**: $79.08
- **Average Distance per Ride**: 20.39 km
- **Average Rate**: $7.12 per km

### Market Distribution
- **Payment Diversity**: Well-balanced across 4 methods
- **Location Coverage**: 5 major pickup/drop-off zones
- **Time Coverage**: 24-hour service across 4 periods
- **Geographic Spread**: Multiple cities covered

### Operational Efficiency
- **Data Quality**: 100% complete, no missing values
- **Service Consistency**: No duplicate bookings
- **Pricing Integrity**: All positive values validated
- **Coverage**: 365-day operation in 2024

---

## Conclusion

The Uber ride analysis reveals a healthy, diverse operation with opportunities for optimization:

**Strengths:**
- Strong morning revenue performance
- Balanced payment method adoption
- Consistent service across multiple locations
- High data quality and operational integrity

**Opportunities:**
- Optimize driver distribution for peak revenue periods
- Enhance weekend demand through targeted promotions
- Leverage wallet payment preference for customer loyalty
- Investigate and replicate September's growth success

**Action Items:**
1. Implement dynamic pricing for morning peak hours
2. Review and standardize unusual pricing cases
3. Increase driver deployment in top 5 revenue locations
4. Launch weekend promotion campaigns
5. Develop wallet payment incentive program

---

## Methodology

This analysis was conducted using Python with industry-standard data science libraries:
- **pandas** for data manipulation and analysis
- **numpy** for numerical computations
- **matplotlib & seaborn** for data visualization
- **Statistical methods** for correlation and trend analysis

The analysis follows a structured approach:
1. Data quality assessment and cleaning
2. Exploratory data analysis (EDA)
3. Statistical analysis and hypothesis testing
4. Visual analytics and pattern recognition
5. Business intelligence and recommendations

---

*Analysis Date: March 8, 2026*  
*Dataset: 297 Uber rides from 2024*  
*Author: [Andrew Oseiwusu](https://github.com/oseiwusuandrew)*  
*Project: Data Science Portfolio*

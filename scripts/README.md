# Scripts Directory

This directory contains the analysis scripts for the Uber ride data project.

## Files

### uber_data_analysis.py
Main analysis script that performs comprehensive data analysis on Uber ride data.

## Script Structure

The script is organized into the following sections:

1. **Data Understanding**
   - Load and explore dataset
   - Display basic statistics
   - Show data types and structure
   - Analyze data distribution

2. **Data Cleaning**
   - Check for missing values and duplicates
   - Validate data integrity
   - Create derived columns
   - Feature engineering

3. **Descriptive Analysis**
   - Calculate statistical summaries
   - Identify top performers
   - Analyze distributions
   - Key performance metrics

4. **Trend and Grouped Analysis**
   - Revenue analysis by various dimensions
   - Time-based patterns
   - Location-based insights
   - Comparative analysis

5. **Visualizations**
   - Generate 6 professional charts
   - Save as PNG files in Visualizations folder
   - Data storytelling through visuals

6. **Insights and Reporting**
   - Business insights
   - Correlation analysis
   - Strategic recommendations
   - Actionable findings

7. **Advanced Analysis**
   - Deep-dive analysis
   - Additional metrics
   - Pattern recognition

## Running the Script

From the project root directory:
```bash
python scripts/uber_data_analysis.py
```

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- openpyxl

Install dependencies:
```bash
pip install -r requirements.txt
```

## Output

The script generates:
- Console output with detailed analysis results
- 6 visualization PNG files in Visualizations folder
- Cleaned dataset in data folder (Uber_Data_Cleaned.csv)

## Customization

You can modify the script to:
- Add new analysis sections
- Change visualization styles
- Include additional metrics
- Export results in different formats
- Adjust file paths for different directory structures

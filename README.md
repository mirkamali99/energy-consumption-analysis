# Energy Consumption Analysis – Iranian Schools

## Overview
Analysis of natural gas consumption in educational buildings across Iran.

## Dataset
- **Source:** Norouzi, M., Labbafan, S., Farajnia, B., Torabi, M., & Norouzi, M. R. (2023). *Dataset on environmental impacts and costs of energy consumption in educational buildings in Iran.* Data in Brief, 51, 109606.
- **DOI:** 10.17632/6w6vv8n4tf.1
- **Records:** 1,700+
- **Provinces:** 14
- **Features:** Natural gas consumption, outdoor temperature, environmental impact indicators, payable amounts (IRR & USD)

## Tools Used
- Python (pandas, matplotlib)
- Power BI Desktop
- Git & GitHub

## Key Insights
1. **Winter Peak:** Gas consumption is highest during winter months (December–February).
2. **Cost Correlation:** Strong positive relationship between gas consumption and payable amount.
3. **Seasonal Pattern:** 12-month trend shows clear seasonal cycles — high in cold months, low in warm months.

## Recommendation
Optimize heating systems and improve building insulation in schools to reduce winter gas consumption and lower costs.

## Files
| File | Description |
|------|-------------|
| `energy_project.py` | Python script for data cleaning, analysis, and visualization |
| `cleaned_energy_data.csv` | Cleaned dataset ready for analysis |
| `dashboard.pdf` | Power BI dashboard export |
| `report.md` | 2-page project report |

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib openpyxl

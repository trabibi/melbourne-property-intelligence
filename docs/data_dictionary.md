# Data Dictionary 
Melbourne Property Intellignce 

This document describes the structure, definition, and assumptions of the processed datasets used in the project. 

The datasets documented here are used for: 
- Analytical notebooks 
- Summary insights 
- Streamlit dashboard visualisastions 

All metrics are derived from publicly available Victorian Government and Australian datasets and are intended for comparative analysis only. 

## Dataset Index

| Dataset | Description |
|-------|------------|
| suburb_house_rental_yield.csv | Suburb-level gross rental yield for 3-bed houses |
| suburb_yield_rate_spreads.csv | Yield vs interest rate spread scenarios |
| yield_demand_lga_2025.csv | LGA-level yield and rental demand indicators |
| yield_demand_band_summary.csv | Aggregated yield and demand band summary |
| yield_quartile_rate_spread_summary.csv | Average rate sensitivity by yield group |

## suburb_house_rental_yield.csv

**Purpose**  
Provides suburb-level gross rental yield estimates for 3-bedroom houses across Melbourne, combining median rent and median house price data.

**Grain**  
One row per suburb.

### Columns

| Column | Type | Description |
|------|------|------------|
| region | string | ABS-style regional grouping |
| suburb | string | Standardised suburb name |
| median_rent | float | Weekly median rent (AUD) for 3-bed houses |
| property_type | string | Property category (3 Bed House) |
| median_price | float | Median sale price (AUD) |
| sales_count | integer | Number of sales used to compute median |
| gross_yield | float | Annual rent ÷ median price |
| gross_yield_pct | float | Gross rental yield (%) |

### Derived Fields
- gross_yield = (median_rent x 52) / median_price
- gross_yield_pct = gross_yield × 100

## suburb_yield_rate_spreads.csv

**Purpose**  
Evaluates suburb-level income resilience by comparing gross rental yields against benchmark mortgage interest rate scenarios

**Grain**  
One row per suburb.

### Columns

| Column | Type | Description |
|------|------|------------|
| suburb | string | Standardised suburb name |
| gross_yield_pct | float | Gross rental yield (%) |
| yield_quartile | string | Yield bucket (Low, Mid-Low, Mid-High, High) |
| spread_low_rate | float | Yield minus 3.0% mortgage rate |
| spread_current_rate | float | Yield minus 5.5% mortgage rate |
| spread_high_rate | float | Yield minus 7.0% mortgage rate |

### Derived Fields
- spread = gross_yield - interest_rate

Positive values indicate rental income exceeds borrowing costs.

## yield_demand_lga_2025.csv

**Purpose**  
Combines LGA level average rental yields with active rental bond counts to jointly assess income potential and rental demand stability.

**Grain**  
One row per LGA (Local Government Area).

### Columns

| Column | Type | Description |
|------|------|------------|
| lga | string | Local Government Area name |
| avg_gross_yield_pct | float | Average gross rental yield (%) across observed suburbs |
| suburb_count | integer | Number of suburbs contributing to LGA yield |
| active_bonds | integer | Number of active rental bonds (Jun 2025) |
| coverage_flag | string | Indicates limited vs broader suburb coverage |
| demand_band | string | Rental demand tier (Low, Medium, High) |
| yield_demand_quadrant | string | Yield-demand classification |

### Derived Fields
- avg_gross_rental_yield: mean of suburb level yields within LGA 
- demand_band: terciles of active bond counts 
- yield_demand_quadrant: median_based yield/demand classification 

## yield_demand_band_summary.csv

**Purpose**  
Provides aggregated summary statistics for LGAs grouped by rental demand intensity. 

**Grain**  
One row per demand band. 

### Columns

| Column | Type | Description |
|------|------|------------|
| demand_band | string | Rental demand category |
| avg_yield_pct | float | Mean gross rental yield (%) |
| avg_active_bonds | integer | Mean number of active rental bonds |
| lga_count | integer | Number of LGAs in band |

## yield_quartile_rate_spread_summary.csv

**Purpose**  
Summarises interest rate sensitivity across yield quartiles to highlight differential cash flow risk

**Grain**  
One row per yield quartile.

### Columns

| Column | Type | Description |
|------|------|------------|
| yield_quartile | string | Yield category |
| spread_low_rate | float | Average yield-rate spread at 3.0% |
| spread_current_rate | float | Average yield-rate spread at 5.5%  |
| spread_high_rate | float | Average yield-rate spread at 7.0%  |

### Key Assumptions & Limitations
- Gross rental yields are used due to the absense of consistent suburb level operating cost data 
- Active rental bonds are used as a proxy for rental demand, not a direct vacancy measure 
- Interest rates scenarios are illustrated benchmarks 
- Some LGAs are represented by a limited number of suburbs due to data availability 
- Results are historical, does not constitue investment advice 

## Interpretation Notes 
- Higher yields often reflect lower asset prices rather than superior rental markets 
- High demand areas typically exhibit lower yields but greater rental stability 
- Yield demand trade offs should be intepreted relative relative to investor objective and financing structures
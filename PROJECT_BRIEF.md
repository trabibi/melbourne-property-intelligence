# **Melbourne Property Intelligence**

### Rental Yield, Vacancy, and Interest Rate Sensitivity Analysis

---

## 1. Background 

Residential property investment decisions in Melbourne are increasingly influenced by shifting macroeconomic conditions, particularly rising interest rates and changing rental market conditions. While median rents and property prices are widely reported, these metrics in isolation provide limited insight into the relative attractiveness and risk profile of different suburbs.

In practice, investors must simultaneously evaluate income returns, demand stability, and financing risk. A suburb with a high rental yield may face weak tenant demand, while a high-demand inner suburb may offer stability at the cost of compressed yields and higher interest rate exposure. Understanding these trade-offs at a granular level is crucial for making informed residential investment analysis. 

This project develops an integrated, suburb and LGA level analytical framework that combines rental yield, rental demand proxies, and interest rate sensitivity to support comparative investment decision making across Melbourne. 

---

## 1.1. Real World Relevance & Industry Context 

This project is motivated by prior experience in real estate investment and asset management, where quarterly market reports are commonly used to summarise rental trends, pricing movements, vacancy conditions, and macroeconomic conditions. While these reports are informative, they often present metrics in isolation and at aggregated levels that obscure meaningful cross-suburb differences. 

In practice, investment decisions are made at a much finer level of granularity. Assessing how rental income, demand, and interest rate exposure interact across specific locations is critical for understanding cash-flow resilience and vacancy risk. 

This project bridges the gap by transforming quietly published public data into a unified analytical framework. By combining yield analysis, demand proxies, and interest rate stress testing, it demonstrates how descriptive market data can be converted into actionable, risk-aware investment insights. 

---

## 2. Problem Statement

This project examines how rental income potential, demand conditions, and interest rate sensitivity vary across Melbourne suburbs and LGAs. The objective is to provide a comparative, data-driven view of income return and risk profiles under different macroeconomic conditions. 

Rather than identifying a single "best" suburb, the analysis highlights structural trade-offs between yield, demand stability, and financing risk across different parts of Melbourne. 

---

## 3. Target Users / Stakeholders

- Residential property investors
- Real estate analysts and researchers
- Advisory and asset management professionals
- Students and practitioners interested in applied property and housing analytics

---

## 4. Key Analytical Questions

- How do gross rental yields differ across Melbourne suburbs?
- How does rental demand differ across LGAs, and how does it relate to yield levels?
- How sensitive are rental yields to changes in interest rates?
- Which locations offer stronger cash flow resilience versus greater demand stability?
- Where do balanced risk-return profiles emerge across yield and demand dimensions?

---

## 5. Key Metrics & Definitions

- **Gross Rental Yield (%)**

    Annual rental income relative to property value, calculated using median renta nd median price data. Gross yield is used due to the absence of consistent suburb level expense data and serves as a comparative income metric.
    
- **Rental Demand Proxy (Active Rental Bonds)**
    
    Active rental bonds from the Victorian Residential Tenancies Bond Authority (RTBA) are used as a proxy for rental demand and market depth. Higher bond counts indicate a larger and more stable occupied rental market. 
    
- **Interest Rate Level / Change**
    
    The difference between rental yield and assumed interest rate scenarios (low/current/higher rates), used to assess cash flow resilience under changing financing conditions.
    

These metrics are selected to jointly capture the return–risk trade-off faced by property investors.

---

## 6. Data Sources & Constraints

### Data Sources 

- RTBA median rent and active bond data (Victorian Rental Report)
- Victorian median house price data (suburb-level sales data)
- RBA cash rate and scenario assumptions 
- Australian postcode and suburb-LGA mapping data (open community data on GitHub)

### Constraints & Assumptions

- Analysis focuses on gross yields due to unavailable operating expense data 
- Rental demand is measured as a proxy rather than direct vacancy rates 
- Results are descriptives and comparative and not predictive
- Findings reflect historical data and do not constitute investment advice

---

## 7. Analytical Approach 

1. **Data Cleaning & Integration**
    
    - Cleaning and aligning suburb level rent and price data 
    - Standardising suburb names and mapping suburbs to LGAs 
    - Aggregating suburb level yields to LGA level where necessary 
    
2. **Rental Yield Analaysis**
    
    - Suburb level gross rental yield calculation
    - Identification of high and low yield markets 
    
3. **Demand & Vacancy Risk Analysis**
    - Use of active rental bonds as demand proxy 
    - Demand band classification (low/medium/high demand)
    - Yield-demand quadrant framework 

4. **Interest Rate Sensitivity Analysis**
    - Yield interest rate spread calculation under multiple rate scenarios 
    - Comparison of cash flow resilience across yield quartiles 

---

## 8. Outputs

- Cleaned, reproducible suburb and LGA level datasets 
- Yield-demand quadrant classifications 
- Interest rate sensitivity summaries by yield group 
- Visualisations supporting comparaitve analysis 
- An interactive streamlit dashboard for suburb-level exploration 
- Clear, investment-oriented insights and takeaways

---

## 9. Risks & Limitations

- Data availability varies across suburbs and dwelling types 
- Demand proxies do not capture short-term vacancy fluctuations 
- Interest rate scenarios assume other market factors remain unchanged/constant 

---

## 10. Potential Extensions

- Incorporation of capital growth and price appreciation metrics
- Segmentation by property type (houses vs units)
- Longer horizon interest rate and macroeconomic conditions 
- Integration of demographic, employment, or infrastructure indicators

---

### **Project Status**

Final analysis complete; dashboard development in progress


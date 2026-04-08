# Modeling Global Market Integration and Asymmetric Shock Transmission  
## A US–India Time Series Analysis

![Cover](cover.png)

---

## Overview

Financial markets are increasingly interconnected, with movements in major economies influencing global capital flows and investor sentiment. This project analyzes the relationship between the US and Indian equity markets, focusing on how shocks propagate across markets and how global macro-financial factors shape these dynamics.

Using a rigorous time series framework, the study captures both long-run equilibrium relationships and short-run interactions, providing insights into market integration, causality, and risk transmission.

---

## Objectives

- Examine whether US and Indian markets move together in the long run  
- Analyze short-run influence of the US market on India  
- Evaluate the impact of global factors (VIX, BRENT, DXY)  
- Measure the speed of shock transmission  
- Identify asymmetric and nonlinear market responses  
- Assess changes in dynamics during geopolitical conflict periods  

---

## Methodology

The analysis follows a structured econometric pipeline:

- **Stationarity Testing** – Augmented Dickey-Fuller (ADF)  
- **Cointegration Analysis** – Johansen Test  
- **Short-Run Dynamics** – Vector Error Correction Model (VECM)  
- **Causality Analysis** – Granger Causality  
- **Multivariate Modeling** – Vector Autoregression (VAR)  
- **Shock Analysis** – Impulse Response Functions (IRF)  
- **Asymmetry & Nonlinearity** – Positive/Negative and Small/Large shock decomposition  
- **Event Analysis** – Crisis-period modeling using interaction terms  

---

## Data

Daily time series data (2007 – March'26):

- S&P 500 (US equity market)  
- NIFTY 50 (Indian equity market)  
- VIX (market volatility index)  
- BRENT (crude oil prices)  
- DXY (US Dollar Index)  
- USD/INR exchange rate  

---

## Key Findings

- US and Indian markets are **cointegrated**, indicating long-run integration  
- The US market **drives short-run movements** in India  
- Indian markets are more **sensitive to global macro factors**  
- **Negative and large shocks** have stronger transmission effects  
- Crisis periods **intensify global linkages and volatility impact**  

---

## Project Structure

global-market-shock-transmission \
├── notebooks/ \
├── src/ \
└── README.md 


---


---

## Tools & Technologies

- **Python (Pandas, NumPy)**  
- **Statsmodels (VAR, VECM, Granger Causality)**  
- **ARCH/GARCH**  
- **Matplotlib**  

---

## Conclusion

The analysis highlights the dominant role of the US market in global finance and the sensitivity of emerging markets like India to external shocks. While integration enhances connectivity, it also increases vulnerability, particularly during periods of market stress and geopolitical uncertainty.

---

## Note

This project is intended for educational and analytical purposes.
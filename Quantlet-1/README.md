# BlockchainAcrossIndustries

## Quantlet: BlockchainAcrossIndustries  
### Title  
Blockchain Transaction Analytics Across Industries

### Description  
This Quantlet analyzes a blockchain-inspired transaction dataset across multiple industries and locations.  
It performs data cleaning, feature engineering (time-based variables), one-hot encoding of categorical fields, descriptive statistics, fraud analysis, and visualization of key patterns.

The purpose is to demonstrate how blockchain-related operational data (e.g., smart contract status, fraud flags, compliance checks) can be analyzed using Python to extract insights relevant for supply chains, logistics, and digital transaction monitoring.

### Key Results  
- Identifier columns removed to improve modeling clarity  
- Time features extracted: weekday, month, year  
- Smart contract states, order statuses, and payment statuses encoded  
- Location-level averages of order amounts, shipment quantities, and mismatches computed  
- Fraudulent transactions show slightly higher average order amounts  
- Two visualizations generated and saved  
  - Distribution of order amounts  
  - Fraud vs. non-fraud order amount comparison  

### Visualizations  
The Quantlet produces the following output files in `/output/`:

- `order_amount_distribution.png`  
- `fraud_vs_nonfraud_order_amount.png`

### Author  
Haiyao Ni

### Keywords  
Blockchain, Smart Contracts, Fraud Detection, Supply Chain Analytics, Time Series Features, Data Analysis, One-Hot Encoding, Quantlet

### Input  
`bcn.csv` — blockchain transaction dataset with 10k+ rows

### Output  
- Cleaned dataset (in-memory)  
- Two PNG visualizations in `/output/`  
- Printed summary of insights  

### Requirements  
- Python 3.x  
- pandas  
- matplotlib  
- seaborn  
- numpy  

### Usage  
Run the script:

```bash
python BlockchainAcrossIndustries.py
```

Ensure folder structure:

```
BlockchainAcrossIndustries/
 ├── README.md
 ├── MetaInfo.txt
 ├── code/
 │     └── BlockchainAcrossIndustries.py
 ├── data/
 │     └── bcn.csv
 └── output/
       ├── order_amount_distribution.png
       └── fraud_vs_nonfraud_order_amount.png
```

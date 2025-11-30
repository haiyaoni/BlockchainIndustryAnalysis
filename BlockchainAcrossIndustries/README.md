# BlockchainIndustryAnalysis

## Description
This Quantlet performs an exploratory analysis of blockchain-enabled transactional data.  
It preprocesses the dataset, visualizes transaction patterns, and compares order amounts between fraudulent and non-fraudulent cases.  
The goal is to demonstrate how blockchain-based datasets can support transparency and fraud detection across industries.

## Data
The dataset `bcn.csv` contains transactional attributes, including:
- Order amounts  
- Fraud labels  
- Timestamps  
- Payment and smart contract statuses  
- Customer and supplier identifiers  

Unnecessary identifiers are removed during preprocessing.

## Requirements
To run this Quantlet, install:

```bash
pip install numpy pandas matplotlib seaborn
```

Python version ≥ 3.10 is recommended.

## Usage
Run the Quantlet from the `code/` directory:

```bash
python BlockchainAcrossIndustries.py
```

It will automatically:
1. Load `data/bcn.csv`
2. Clean and preprocess the data
3. Encode categorical features
4. Generate fraud analysis visualizations
5. Save results into the `output/` folder

## Output
The Quantlet produces the following figures:

- **fraud_vs_nonfraud_order_amount.png**  
  Comparison of order amounts between fraudulent and non-fraudulent transactions.

- **order_amount_distribution.png**  
  Distribution of order amounts across the dataset.

These outputs are located in `output/`.

## Author
Haiyao Ni  
BCN-Seminar_CL_1  
Humboldt University of Berlin

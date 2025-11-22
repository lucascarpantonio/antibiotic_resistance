# Antibiotic Resistance — A Data-Driven Exploration  
### Understanding resistance patterns before building a predictive model

This project explores a synthetic clinical microbiology dataset to understand how **bacterial resistance**, **patient demographics**, and **temporal trends** interact.  
Rather than jumping straight into machine learning, the analysis focuses on discovering *what the data can reveal on its own*; a crucial mindset in real-world data science.

This repository contains the full workflow: from cleaning and reshaping raw clinical data to constructing a first resistance baseline model and visualizing higher-order patterns such as resistance indexes and temporal dynamics.

---

## Project Objectives

- Explore **resistance patterns** across multiple antibiotics  
- Analyse how **gender**, **age**, and **sample origin** influence susceptibility  
- Examine **temporal trends** in infections and resistance  
- Build a **Resistance Index** to summarize multi-antibiotic behavior  
- Train an initial **Logistic Regression** model  
- Highlight the limitations of baseline approaches and motivate more advanced modelling

---

## Key Insights

### Resistance Index (multi-antibiotic measure)
By calculating the proportion of antibiotics for which each isolate is resistant, we uncover:
- Stable resistance profiles over time  
- Minimal gender-related differences  
- Distinct “signatures” for each bacterial strain  
- No clear upward trend in resistance within the observed years

### Temporal Dynamics
A multi-panel visualization shows how infections fluctuate year by year for each species.  
These trends often reflect:
- seasonal patterns  
- clinical practices  
- sampling variability  

### Bacterial Behaviour
Species maintain characteristic profiles:
- *E. coli* and *K. pneumoniae* show consistent mid-range resistance  
- *Morganella morganii* and *Proteus mirabilis* show slightly more variability  
- Other species exhibit stable, predictable behavior

### Correlation Structure
A heatmap reveals minimal strong correlations, meaning:
- the dataset is rich, multidimensional  
- no single feature dominates  
- models must rely on interactions rather than simple rules

### Baseline Predictive Model
A logistic regression model was used as a preliminary benchmark.

**Performance Summary:**
- ~50% accuracy  
- Good recall for the majority class  
- Demonstrates the difficulty of predicting resistance from demographics alone

This prototype sets the stage for tree-based models, SHAP interpretability, and cost-sensitive learning.

---

## Data Cleaning & Preparation

The notebook includes extensive preprocessing:
- Extracting and fixing inconsistent `collection_date` entries  
- Harmonizing gender and categorical fields  
- Removing corrupted rows  
- Identifying antibiotic result columns and creating a consolidated structure  
- Deriving temporal features  
- Computing the **Resistance Index** per isolate  

---

## Future Work

- Try **Random Forest**, **XGBoost**, and **LightGBM**  
- Introduce **cost-sensitive training** for imbalanced data  
- Perform **SHAP-based interpretability**  
- Build a small **dashboard** (Plotly or Streamlit)  
- Expand to **multi-class or multi-label modelling**  
- Add antibiotic-specific predictive models  

---

## 📖 Related Blog Post
A full narrative walkthrough of this project is available here:  
👉 https://lucascarpantonio.github.io/antibiotic_resistance/blog/

---

## 🧑‍💻 Author
Luca — Data Scientist in progress, focusing on real-world analytical pipelines.
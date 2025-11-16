# 🧬 Antibiotic Resistance Analysis  
### Exploring demographic, temporal, and bacterial patterns in a synthetic clinical dataset

## Project Overview
Antibiotic resistance is a rising global concern, driven by the ability of bacteria to rapidly adapt and overcome standard treatments.  
This project analyzes a **synthetic dataset** that simulates clinical laboratory results, patient demographics, and bacterial susceptibility profiles.

The goal is to explore:
- How infections vary across **age**, **gender**, and **geography**
- Which bacterial species are most frequently involved
- How resistance patterns differ across antibiotics
- Whether demographic or clinical variables correlate with recurrent infections
- What predictive insights can be extracted using a simple machine-learning model

The project follows a complete exploratory workflow — from cleaning to visualization, and ends with a first predictive model.

---

## Dataset Description
The dataset contains simulated clinical microbiology data, including:

- **Demographics:** Age, gender, state, unstructured patient notes  
- **Clinical history:** Infection frequency, comorbidities  
- **Bacterial species:** *E. coli*, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa*, and more  
- **Antibiotics tested:** Ciprofloxacin, Imipenem, Gentamicin, Cephalosporins, etc.  
- **Resistance results:** Binary values (0 = sensitive, 1 = resistant)  
- **Collection date:** Used for temporal trend analysis  

Although synthetic, the dataset is structured to resemble real hospital or public-health microbiology data.

---

## Data Cleaning & Preparation
Main preprocessing steps include:

- Fixing missing or inconsistent demographic fields  
- Standardizing unstructured text (gender, address, state extraction)  
- Removing corrupted or unrealistic entries  
- Extracting temporal components from the `collection_date`  
- Encoding resistance results for grouping and modeling  

---

## Exploratory Analysis Highlights

### ** Demographic Insights**
- Infections show an age-related pattern, with some bacteria more common in older patients.  
- Gender distribution varies across species.  
- Some U.S. states show notably higher infection counts.

---

### ** Bacterial Behaviour**
- *E. coli* and *K. pneumoniae* dominate the dataset.  
- Less frequent species nevertheless display consistent, biologically meaningful resistance patterns.

---

### ** Antibiotic Resistance Landscape**
A resistance heatmap reveals **three broad behavioral clusters**:

- **High resistance:** *E. coli*, *Klebsiella pneumoniae*  
- **Moderate resistance:** Citrobacter, Enterobacter, Morganella  
- **Lower resistance:** Serratia, *P. aeruginosa* (for selected antibiotics)

Some antibiotics remain broadly effective:
- **Imipenem**  
- **Ciprofloxacin**  
- **Colistin**

These serve as key therapeutic options (with colistin as a last resort).

---

### ** Temporal Trends**
Temporal grouping suggests moderate shifts in resistance across years — requiring long-term monitoring rather than static assumptions.

---

## Predictive Modeling (Prototype)
A basic **Logistic Regression** model was built to classify cases as *high-risk* vs *low-risk* based on clinical and demographic variables.

**Key results:**
- **Accuracy ≈ 50%**
- Strong recall for high-risk cases (0.85)
- Weak recall for low-risk cases (0.15)
- Indicates:  
  - complex patterns  
  - limited predictive features  
  - the need for more advanced models (Random Forest, XGBoost)

This prototype serves as an introduction to modeling rather than a clinical decision tool.

---

## Repository Structure
├── antibiotic_analysis.ipynb     → Full notebook with analysis & modeling
├── data/                         → Synthetic dataset(s)
├── images/                       → Visual assets for README/blog
├── README.md                     → Project summary (this file)
└── requirements.txt              → Dependencies


---
layout: default
title: "Exploring Antibiotic Resistance"
---

Over the last months I’ve started to explore machine learning more seriously, step by step and with a lot of curiosity.  
This article is the story of my **first real experiment**: a data-driven exploration of an antibiotic resistance dataset.

My goal here is not to build a perfect, production-ready model, but to learn how to:

- clean and structure messy data  
- explore patterns in bacteria and infections  
- visualize results in a way that is understandable and useful  
- prepare the ground for future ML models  

If you want to see more of my work and experiments, you can visit my GitHub blog here:  
[https://lucascarpantonio.github.io](https://lucascarpantonio.github.io)

---

## Dataset and Questions

The dataset contains information about:

- the **bacterial strain** that was isolated  
- some **clinical features** about patients  
- the **response to different antibiotics** (sensitive / intermediate / resistant)  
- basic contextual information such as **collection date** and **location**  

With this data, I started from a few simple questions:

1. Which bacteria appear most frequently in the dataset?  
2. Are some bacteria clearly associated with specific **types of infection**?  
3. What patterns can we see in **antibiotic resistance** across strains?  
4. Which variables might be useful later for a **predictive model**?

This is still an exploratory project, but these questions already help to shape the analysis and keep things focused.

---

## Exploring Bacteria Frequencies

Once the dataset was in a better shape, I started with **simple frequency analysis**.

- I counted how many times each bacterial species appeared.  
- I identified the most common strains in the dataset.  

A plain frequency chart is already informative: it tells us where to focus and which bacteria might be driving most of the clinical cases in this dataset.

However, raw counts only tell part of the story.

---

## Linking Bacteria to Infection Type

To go a bit deeper, I grouped the data by:

- `souche_description` (bacterial strain)  
- `infection_label` (type of infection)  

This produced a table showing how often each strain appears in each infection category.

This view is more clinically interesting, because:

- some bacteria are spread across several infection types  
- others seem to be strongly associated with one specific label  

In future iterations, this relationship between **strain** and **infection type** will probably be one of the key inputs for any ML model.

---

## Looking at Antibiotic Resistance

The most delicate part of the dataset is the response to different antibiotics.

For each antibiotic, the result is typically encoded as:

- **S** – sensitive  
- **I** – intermediate  
- **R** – resistant  

By aggregating these responses, we can start to:

- see which antibiotics tend to lose effectiveness more often  
- compare resistance patterns across different bacteria  
- identify combinations of strain + infection type where resistance is particularly frequent  

This is exactly the kind of structured information that a future classifier could try to learn and predict.

---

## Next Steps and ML Perspective

At this stage, the project is mainly **exploratory**.  
But during the analysis, a few natural next steps emerged:

- Build a simple **classification model** to predict resistance (e.g. S vs R) for a given antibiotic.  
- Explore **feature importance** to understand which variables drive resistance patterns.  
- Experiment with **clustering** to see if there are natural groups of samples sharing similar resistance profiles.  
- Evaluate how much **clinical variables** (such as comorbidities) actually add to the predictive power.

The idea is to start simple (logistic regression, decision trees, etc.) and then iterate from there.

---

## Conclusions

This project is a **first hands-on step** into applying data science and early ML concepts to a real, meaningful topic: antibiotic resistance.

What I have now is:

- a cleaned and structured dataset  
- a first set of descriptive insights about bacteria, infections and resistance  
- a clearer view of which questions could be turned into machine learning tasks  

It’s not a finished product, but it is a solid foundation.  
From here, I plan to move towards more explicit ML models and to keep sharing the journey on my GitHub blog:

👉 [https://lucascarpantonio.github.io](https://lucascarpantonio.github.io)

If you’re curious about the code or want to follow my future experiments, feel free to stop by!
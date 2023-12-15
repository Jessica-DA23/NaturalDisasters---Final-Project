# EMDAT Natural Disasters Dataset Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Project Overview

This project involves a comprehensive analysis of the EMDAT natural disasters dataset. The goal is to derive insights into the frequency, impact, and trends of natural disasters from 2000 to 2021. Includes data cleaning, visualization, and statistical analysis to understand the global patterns of natural disasters.

## Dataset Description

The `eda-natural-disasters` dataset from the Emergency Events Database (EMDAT) serves as the foundation of our analysis. It includes detailed records on the occurrence of natural disasters, their geographical and temporal distribution, casualties, financial impacts, and the number of people affected.



## Project Overview

This project analyzes the EMDAT natural-disasters dataset, focusing on the period from 2015 to 2021, to uncover insights into the occurrence and impacts of natural disasters worldwide. The analysis aims to identify trends, distributions, and the severity of these events using various machine learning models to predict outcomes such as the number of casualties or the economic cost of each disaster.


## Model Training

A suite of machine learning models were trained and evaluated, including Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Naive Bayes, and Multi-Layer Perceptron (MLP). Each model was rigorously tested, and feature importance was analyzed to understand which factors most significantly predict the impact of natural disasters.
The SMOTE technique was also applied to handle imbalanced data, but the results didn't imporve.

## Evaluation

Model performance was assessed using accuracy, precision, recall, and F1 score. The Random Forest Classifier emerged as the best performing model with the following metrics:

- Accuracy: 0.9278
- Precision: 0.8788
- Recall: 0.7945
- F1 Score: 0.8137

The evaluation provided insight into the models' capabilities to predict disaster impacts accurately and identify the most influential predictive variables.

## Results

The project's findings, underpinned by the superior performance of the Random Forest model, offer valuable perspectives on disaster impact prediction. The analysis informs on the most vulnerable regions and the types of disasters that require increased attention for mitigation and preparedness strategies. The insights gleaned can aid policymakers, disaster response teams, and researchers in understanding and managing the risks associated with natural disasters.

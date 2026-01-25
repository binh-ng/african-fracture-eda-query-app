# African Medical Multimodal Fracture Dataset - Exploratory Data Analysis

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-complete-success.svg)

## 📋 Overview

This repository contains a comprehensive exploratory data analysis (EDA) of the African Medical Multimodal Fracture Dataset, examining fracture cases across multiple African countries. The analysis explores relationships between fracture types, clinical measurements, patient demographics, cultural factors, and healthcare access patterns to provide insights into injury patterns and treatment approaches in African medical contexts.

## 🎯 Objectives

- Analyze fracture type distributions and injury mechanisms across African regions
- Examine clinical measurements (vital signs, pain assessments, anthropometric data) by fracture type
- Investigate demographic patterns including age, gender, education, and socioeconomic factors
- Assess traditional medicine usage rates and cultural beliefs about injury treatment
- Evaluate healthcare access barriers (distance, transportation, digital literacy)
- Identify correlations between clinical, demographic, and environmental variables
- Provide statistical validation of differences across fracture types

## 📊 Dataset Description

**Source**: [HuggingFace - electricsheepafrica/african-medical-multimodal-fracture](https://huggingface.co/datasets/electricsheepafrica/african-medical-multimodal-fracture)

**Size**: 100+ patient records

**Geographic Coverage**: Multiple African countries including Nigeria, Kenya, Ghana, Zimbabwe, Mali, Ethiopia, Tanzania, Uganda, and more

### Data Categories

The dataset includes comprehensive multimodal information:

#### 1. **Demographics** (12 variables)
- Age, gender, country, region type (urban/rural/peri-urban)
- Occupation, education level, income level
- Healthcare distance, transportation mode
- Insurance status, family size, primary language

#### 2. **Clinical Measurements** (11 variables)
- **Vital Signs**: Heart rate, blood pressure (systolic/diastolic), temperature, respiratory rate, oxygen saturation
- **Anthropometric**: Height, weight, BMI, arm circumference
- **Pain Assessment**: Pain scale (1-10), pain location, pain quality

#### 3. **Clinical Context** (6 variables)
- Fracture type, mechanism of injury
- Traditional medicine usage (type, timing, effectiveness)
- Cultural beliefs about injury
- Preferred treatment approach

#### 4. **Environmental Context** (5 variables)
- Season, injury time, day of week
- Weather conditions (precipitation, visibility)
- Geographic risk factors

#### 5. **Mobile Health Data** (4 variables)
- Phone ownership, phone type, internet access
- Digital literacy level

## 🔬 Analysis Components

### 1. Data Processing
- JSON data extraction and flattening from nested structures
- Data cleaning and validation
- Feature engineering (40+ variables extracted)

### 2. Descriptive Statistics
- Summary statistics for all numeric variables
- Frequency distributions for categorical variables
- Cross-tabulations and contingency tables
- Missing value analysis

### 3. Demographic Analysis
- Age and gender distributions
- Geographic coverage and regional patterns
- Socioeconomic indicators (education, income, insurance)
- Healthcare access metrics

### 4. Fracture Type Analysis
- Distribution of fracture types
- Mechanism of injury patterns
- Fracture characteristics by demographics
- Traditional medicine usage patterns

### 5. Clinical Measurements
- Vital signs analysis by fracture type
- Pain scale distributions and patterns
- Nutritional status assessment
- Anthropometric measurements

### 6. Correlation Analysis
- Pearson correlation matrix for numeric variables
- Identification of strongest relationships
- Multivariate pattern exploration

### 7. Statistical Testing
- Kruskal-Wallis H-tests for group differences
- Non-parametric testing across fracture types
- Significance testing for clinical measurements

## 📈 Visualizations

The analysis generates **5 publication-quality PNG files** (300

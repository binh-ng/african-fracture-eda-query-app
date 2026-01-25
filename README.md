# African Medical Multimodal Fracture Dataset - Exploratory Data Analysis

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-CC0-green.svg)
![Status](https://img.shields.io/badge/status-complete-success.svg)

## 📋 Overview

This repository contains a comprehensive exploratory data analysis (EDA) of the African Medical Multimodal Fracture Dataset, examining fracture cases across multiple African countries. The analysis explores relationships between fracture types, clinical measurements, patient demographics, cultural factors, and healthcare access patterns to provide insights into injury patterns and treatment approaches in African medical contexts.

## 🎯 Objectives

- Analyze fracture type distributions and injury mechanisms across African regions
- Examine clinical measurements (vital signs, pain assessments, anthropometric data) by fracture type
- Investigate demographic patterns, including age, gender, education, and socioeconomic factors
- Assess traditional medicine usage rates and cultural beliefs about injury treatment
- Evaluate healthcare access barriers (distance, transportation, digital literacy)
- Identify correlations between clinical, demographic, and environmental variables
- Provide statistical validation of differences across fracture types

## 📊 Dataset Description

**Source**: [HuggingFace - electricsheepafrica/african-medical-multimodal-fracture](https://huggingface.co/datasets/electricsheepafrica/african-medical-multimodal-fracture)

**Size**: 100+ patient records

**Geographic Coverage**: Multiple African countries, including Nigeria, Kenya, Ghana, Zimbabwe, Mali, Ethiopia, Tanzania, Uganda, and more

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

### 6. Statistical Testing
- Kruskal-Wallis H-tests for group differences
- Non-parametric testing across fracture types
- Significance testing for clinical measurements

### 7. Additional Insights
- Mechanism of injury vs fracture type cross-tabulation
- Traditional medicine usage by country
- Pain scale by region type
- Healthcare distance statistics
- Digital literacy and phone ownership patterns

## 📈 Visualizations

The analysis generates **3 publication-quality PNG files** (300 DPI):

### 1. `01_demographics.png`
9 visualizations covering:
- Fracture type distribution (bar chart)
- Gender distribution (pie chart)
- Age distribution (histogram)
- Top 10 countries (horizontal bar)
- Region type distribution
- Income level distribution
- Education level distribution
- Transportation mode distribution
- Family size distribution (histogram)

### 2. `03_clinical_boxplots.png`
Box plots for 6 key clinical metrics across fracture types:
- Heart rate (bpm)
- Systolic blood pressure (mmHg)
- Pain scale (1-10)
- Temperature (°C)
- BMI
- Oxygen saturation (%)

### 3. `fracture_summary.csv`
Summary statistics table including:
- Age (mean, std)
- Heart rate (mean, std)
- Systolic BP (mean, std)
- Pain scale (mean, std)
- BMI (mean, std)
- Patient count by fracture type

## 🔍 Key Findings

### Clinical Insights
- **Pain Scale Patterns**: Significant variation in pain levels across fracture types
- **Vital Signs**: Elevated heart rates and blood pressure observed in trauma-related fractures
- **Nutritional Status**: Distribution includes normal, overweight, and obese categories
- **BMI Correlations**: Relationships between body composition and injury patterns

### Healthcare Access
- **Geographic Barriers**: Average healthcare distance varies significantly by region
- **Transportation**: Walking and public transport most common modes
- **Digital Divide**: Variable phone ownership and digital literacy levels
- **Insurance Coverage**: Mixed coverage across government, private, community, and none

### Cultural Factors
- **Traditional Medicine**: High usage rates (60-70%) across certain regions
- **Treatment Preferences**: Mix of modern medicine, traditional first, and combined approaches
- **Cultural Beliefs**: Injury attributed to natural causes, bad luck, spiritual causes, or punishment
- **Family Involvement**: High family involvement in medical decision-making

### Demographic Patterns
- **Age Distribution**: Wide range from children to the elderly
- **Gender**: Both male and female patients represented
- **Education**: Varies from no formal education to tertiary level
- **Income**: Predominantly low to middle income levels
- **Urban vs Rural**: Majority from rural areas with limited healthcare access

## 🛠️ Technologies & Libraries

- **Python 3.8+**
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Statistical Analysis**: SciPy
- **Data Access**: Requests, JSON

## 📁 Repository Structure
```
african-fracture-eda/
│
├── african_fracture_eda.py          # Main analysis script
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
│
└── outputs/                          # Generated outputs
    ├── 01_demographics.png
    ├── 03_clinical_boxplots.png
    └── fracture_summary.csv
```

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8 or higher
pip package manager
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/binh-ng/african-fracture-eda.git
cd african-fracture-eda
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Analysis

**Option 1: Local Python**
```bash
python african_fracture_eda.py
```

**Option 2: Google Colab**
1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `african_fracture_eda.py` or copy-paste the code
3. Run all cells

### Expected Runtime
- Data fetching: ~5 seconds
- Analysis: ~10-15 seconds
- Visualization generation: ~20-30 seconds
- **Total**: ~1 minute

## 📊 Output Files

After running the analysis, you'll find:

1. **2 PNG visualization files** (300 DPI, publication-ready)
   - `01_demographics.png` - 9 demographic charts
   - `03_clinical_boxplots.png` - 6 clinical boxplots
2. **1 CSV summary table** (`fracture_summary.csv`) with statistics by fracture type
3. **Console output** with detailed statistical results and insights

## 📝 Analysis Workflow

The script follows a 10-step process:

1. **Data Loading** - Fetch from HuggingFace API and flatten JSON structure
2. **Data Overview** - Display dataset info, first records, missing values, basic statistics
3. **Demographic Analysis** - Country distribution, gender, age, region, education, income
4. **Fracture Type Analysis** - Distribution, mechanism of injury, traditional medicine usage
5. **Clinical Measurements** - Summary statistics for all vital signs and metrics
6. **Demographics Visualization** - Generate 9-panel demographic chart
7. **Clinical Boxplots** - Generate 6-panel clinical measurement boxplots
8. **Additional Analysis** - Cross-tabs, traditional medicine by country, regional patterns
9. **Statistical Tests** - Kruskal-Wallis tests for clinical measurements
10. **Summary Table** - Generate and save fracture_summary.csv

## 📈 Statistical Methods

### Tests Performed
- **Kruskal-Wallis H-test**: Non-parametric test for differences across fracture types
  - Applied to: heart rate, blood pressure (systolic), pain scale, temperature, BMI
  - Significance level: α = 0.05
  - Results indicate whether clinical measurements differ significantly across fracture types

### Descriptive Statistics
- Mean, standard deviation, min, max for all numeric variables
- Frequency counts and percentages for categorical variables
- Cross-tabulations for mechanism of injury vs fracture type
- Grouped statistics by fracture type, country, and region

## 🎓 Use Cases

This analysis is valuable for:

- **Healthcare Researchers**: Understanding fracture patterns in African populations
- **Public Health Professionals**: Identifying healthcare access barriers
- **Medical Anthropologists**: Studying traditional medicine integration
- **Data Scientists**: Learning EDA techniques for medical datasets
- **Policy Makers**: Informing healthcare infrastructure decisions
- **Medical Educators**: Teaching about diverse medical practices

## 📚 Research Applications

Potential research questions this analysis can help answer:

1. How do fracture types vary across African countries and regions?
2. What is the relationship between pain levels and fracture types?
3. How does traditional medicine usage affect treatment outcomes?
4. What are the main barriers to healthcare access in rural Africa?
5. How do socioeconomic factors influence injury patterns?
6. What role does digital literacy play in healthcare follow-up?

## 🔄 Future Enhancements

- [ ] Add predictive modeling for fracture type classification
- [ ] Include time-series analysis if temporal data available
- [ ] Develop interactive dashboards (Plotly/Dash/Streamlit)
- [ ] Add geospatial visualization for country-level patterns
- [ ] Integrate natural language processing for clinical text analysis
- [ ] Compare with global fracture datasets
- [ ] Add survival analysis for recovery patterns
- [ ] Expand correlation analysis with additional visualizations

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewAnalysis`)
3. Commit your changes (`git commit -m 'Add new analysis'`)
4. Push to the branch (`git push origin feature/NewAnalysis`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Creative Commons Zero v1.0 Universal - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset Source**: electricsheepafrica on HuggingFace
- **African Medical Community**: For data collection and curation
- **Open Source Community**: For the amazing Python data science tools

## 📧 Contact

For questions, suggestions, or collaborations:

- **Email**: bill.nguyen.analytics@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/binh-ng/

## 📖 Citation

If you use this analysis in your research, please cite:
```bibtex
@software{african_fracture_eda,
  author = {Thanh Binh Nguyen},
  title = {African Medical Multimodal Fracture Dataset - Exploratory Data Analysis},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/binh-ng/african-fracture-eda}
}
```

---

**Note**: This is an educational and research project. Medical decisions should always be made by qualified healthcare professionals.

⭐ If you find this analysis helpful, please consider giving it a star!

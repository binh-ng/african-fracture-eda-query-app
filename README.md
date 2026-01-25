# 🏥 African Medical Fracture Dataset Query System

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.53+-red.svg)
![License](https://img.shields.io/badge/license-CC0-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

An interactive web application for querying and exploring the African Medical Multimodal Fracture Dataset. Built for healthcare practitioners, researchers, and data scientists working with fracture data across African countries.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](your-app-url-here)

## 📋 Overview

This Streamlit application provides an intuitive interface for exploring patient records from the African Medical Multimodal Fracture Dataset. Unlike static analysis, this tool enables real-time querying, filtering, and visualization of individual patient records and aggregate statistics, making it ideal for clinical reference, research exploration, and educational demonstrations.

## 🎯 Key Features

### 🔍 Search & Query Capabilities
- **Patient ID Search** - Find all records associated with a specific patient
- **Record ID Search** - Look up individual medical encounters
- **Browse All Mode** - Explore the complete dataset with advanced filtering options

### 📊 Data Exploration Tools
- **Multi-Dimensional Filtering** - Filter by country, fracture type, gender, and more
- **Detailed Patient Views** - Comprehensive information organized in intuitive tabs
- **Visual Analytics** - Interactive Plotly charts comparing patient vitals to dataset averages
- **Data Export** - Download filtered results as CSV files for further analysis

### 📱 Interactive Dashboard
- **Real-time Statistics** - Live dataset overview in sidebar
- **Responsive Design** - Works on desktop, tablet, and mobile devices
- **Clean Medical UI** - Professional styling optimized for healthcare professionals
- **Quick Stats** - At-a-glance metrics for rapid assessment

## 🌟 Information Categories

The application organizes patient data into five comprehensive tabs:

### 👤 Demographics
- Personal information (age, gender, country, region)
- Socioeconomic indicators (occupation, education, income)
- Healthcare access metrics (distance, transportation, insurance)
- Family context (size, primary language)

### 🏥 Clinical Information
- Fracture type and classification
- Mechanism of injury
- Pain assessment (intensity, quality, scale 1-10)
- Cultural context (traditional medicine usage, beliefs, treatment preferences)

### 📊 Vital Signs & Measurements
- Vital signs (heart rate, blood pressure, temperature, respiratory rate, O2 saturation)
- Anthropometric data (height, weight, BMI)
- Nutritional status assessment
- Interactive comparison charts vs. dataset averages

### 🌍 Environmental Context
- Seasonal factors
- Injury timing (time of day, day of week)
- Weather conditions (precipitation, visibility)

### 📱 Digital Health Indicators
- Phone ownership and type
- Digital literacy levels
- Technology access patterns

## 📊 Dataset

**Source**: [HuggingFace - electricsheepafrica/african-medical-multimodal-fracture](https://huggingface.co/datasets/electricsheepafrica/african-medical-multimodal-fracture)

**Coverage**: 
- 100+ patient records
- Multiple African countries (Nigeria, Kenya, Ghana, Zimbabwe, Tanzania, Uganda, Ethiopia, Mali, and more)
- Comprehensive multimodal data (demographics, clinical, environmental, cultural)

**Data Categories**: Demographics (12 variables), Clinical Measurements (11 variables), Clinical Context (6 variables), Environmental Context (5 variables), Mobile Health Data (4 variables)

## 🚀 Live Demo

Visit the live application: **[your-deployment-url.streamlit.app](your-deployment-url-here)**

## 🛠️ Installation & Usage

### Prerequisites
```bash
Python 3.8 or higher
pip package manager
```

### Option 1: Run Locally

```bash
# Clone the repository
git clone https://github.com/binh-ng/african-fracture-query-app.git
cd african-fracture-query-app

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Option 2: Deploy to Streamlit Cloud

1. Fork this repository to your GitHub account
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your forked repository, branch (main), and `app.py`
6. Click "Deploy"

Your app will be live at a public URL within minutes!

### Option 3: Run in Google Colab

```python
!pip install streamlit pyngrok plotly

# Save app.py and run with ngrok for public URL
```

## 📋 Requirements

```
streamlit>=1.53.0
pandas>=2.2.0
requests>=2.32.0
plotly>=5.24.0
```

See `requirements.txt` for complete dependency list.

## 📁 Repository Structure

```
african-fracture-query-app/
│
├── app.py                    # Main Streamlit application
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── .gitignore               # Git ignore rules
```

## 📖 How to Use the Application

### Searching for Specific Patients

1. **Select Search Type**: Choose "Patient ID" or "Record ID" from the radio buttons
2. **Select ID**: Use the dropdown to select from available patient or record IDs
3. **View Results**: Patient information will display in organized tabs
4. **Explore Details**: Click through the five tabs to see comprehensive patient data
5. **Compare Metrics**: View the interactive chart comparing vital signs to dataset averages

### Browsing the Complete Dataset

1. **Select "Browse All"** from the search type options
2. **Open Filters**: Expand the "Filter Options" panel
3. **Apply Filters**: Select countries, fracture types, or genders to filter
4. **Review Table**: Browse the filtered results in the data table
5. **Export Data**: Click "Download Filtered Data as CSV" to export your selection

### Understanding the Dashboard

- **Sidebar**: View real-time dataset statistics and quick facts
- **Main Panel**: Interactive query interface and results display
- **Tabs**: Organized patient information in five categories
- **Charts**: Visual comparisons with hover-over details
- **Metrics**: Quick-reference cards for key values

## 🎯 Use Cases

### For Healthcare Professionals
- **Clinical Reference**: Quick lookup of patient histories
- **Case Review**: Comprehensive patient data for consultations
- **Pattern Recognition**: Identify common injury mechanisms

### For Researchers
- **Data Exploration**: Interactive exploration before formal analysis
- **Cohort Selection**: Filter and identify patient subgroups
- **Hypothesis Generation**: Discover patterns for further investigation

### For Medical Educators
- **Case Studies**: Real-world examples for teaching
- **Cultural Competence**: Demonstrate diverse healthcare contexts
- **Data Literacy**: Teach students to interpret medical data

### For Public Health Professionals
- **Access Assessment**: Evaluate healthcare distance and transportation barriers
- **Cultural Integration**: Understand traditional medicine usage patterns
- **Digital Health Planning**: Assess technology readiness for interventions

## 🔒 Data Privacy & Ethics

- **De-identified Data**: All patient records are de-identified and anonymized
- **Public Dataset**: Uses publicly available data from HuggingFace
- **No PHI**: No personally identifiable health information is included
- **Educational Purpose**: Designed for research and educational use only

## 💡 Technical Highlights

### Performance Optimizations
- **Data Caching**: Uses `@st.cache_data` to load dataset once
- **Efficient Filtering**: Pandas operations optimized for speed
- **Lazy Loading**: Data loaded only when needed

### User Experience
- **Responsive Layout**: Adapts to different screen sizes
- **Custom Styling**: Medical-themed CSS for professional appearance
- **Interactive Charts**: Plotly visualizations with hover details
- **Clear Navigation**: Intuitive interface requiring no training

### Code Quality
- **Modular Design**: Separated functions for maintainability
- **Error Handling**: Graceful handling of loading failures
- **Documentation**: Comprehensive inline comments
- **Best Practices**: Follows Streamlit and Python conventions

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
- Report bugs or suggest features via [Issues](https://github.com/binh-ng/african-fracture-query-app/issues)
- Improve documentation
- Add new visualizations or features
- Optimize performance
- Enhance UI/UX

### Contribution Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 🔄 Future Enhancements

- [ ] Add patient comparison feature (side-by-side view)
- [ ] Implement advanced statistical analysis tools
- [ ] Add geospatial visualization for patient locations
- [ ] Create printable patient summary reports (PDF export)
- [ ] Integrate natural language search queries
- [ ] Add user authentication for sensitive deployments
- [ ] Implement patient timeline visualization
- [ ] Add bulk data analysis tools
- [ ] Create API endpoints for programmatic access
- [ ] Add multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose, including commercial use, as long as you include the original copyright notice and license.

## 🙏 Acknowledgments

- **Dataset Source**: [electricsheepafrica](https://huggingface.co/electricsheepafrica) on HuggingFace for curating and sharing this valuable dataset
- **African Medical Community**: For data collection and contributing to global medical knowledge
- **Streamlit**: For providing an excellent framework for data applications
- **Open Source Community**: For the amazing Python data science ecosystem (Pandas, Plotly, NumPy)

## 🔗 Related Projects

- **[African Fracture EDA](https://github.com/binh-ng/african-fracture-eda)** - Comprehensive exploratory data analysis of the same dataset
- [Original Dataset on HuggingFace](https://huggingface.co/datasets/electricsheepafrica/african-medical-multimodal-fracture)

## 📧 Contact & Support

**Author**: Thanh Binh Nguyen

- **Email**: bill.nguyen.analytics@gmail.com
- **LinkedIn**: [linkedin.com/in/binh-ng](https://www.linkedin.com/in/binh-ng/)
- **GitHub**: [@binh-ng](https://github.com/binh-ng)

For questions, suggestions, or collaborations, feel free to reach out via any of the channels above or open an issue in this repository.

## 📖 Citation

If you use this application in your research or teaching, please cite:

```bibtex
@software{african_fracture_query_app,
  author = {Nguyen, Thanh Binh},
  title = {African Medical Fracture Dataset Query System},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/binh-ng/african-fracture-query-app}
}
```

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Python Graphing Library](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [African Medical Research Resources](https://huggingface.co/electricsheepafrica)

---

**⚠️ Medical Disclaimer**: This application is for research and educational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers with any questions regarding medical conditions.

⭐ **If you find this application useful, please consider giving it a star on GitHub!**

---

**Built with ❤️ for advancing healthcare research and education in Africa**

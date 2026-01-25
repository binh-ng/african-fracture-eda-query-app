import streamlit as st
import requests
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="African Medical Fracture Dataset Query",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        padding-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load data with caching
@st.cache_data(show_spinner=False)
def load_data():
    """Load and process the fracture dataset"""
    url = "https://huggingface.co/datasets/electricsheepafrica/african-medical-multimodal-fracture/raw/main/data/multimodal_records.json"
    
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        
        # Flatten nested JSON structure
        records = []
        for record in data:
            flat_record = {
                'record_id': record['record_id'],
                'patient_id': record['patient_id'],
                'fracture_type': record['fracture_type'],
                
                # Demographics
                'age': record['demographics']['age'],
                'gender': record['demographics']['gender'],
                'country': record['demographics']['country'],
                'region_type': record['demographics']['region_type'],
                'occupation': record['demographics']['occupation'],
                'education_level': record['demographics']['education_level'],
                'healthcare_distance_km': record['demographics']['healthcare_distance_km'],
                'transportation_mode': record['demographics']['transportation_mode'],
                'income_level': record['demographics']['income_level'],
                'insurance_status': record['demographics']['insurance_status'],
                'family_size': record['demographics']['family_size'],
                'primary_language': record['demographics']['primary_language'],
                
                # Clinical Text
                'mechanism_of_injury': record['clinical_text']['mechanism_of_injury'],
                'pain_intensity': record['clinical_text']['pain_description']['intensity'],
                'pain_quality': record['clinical_text']['pain_description']['quality'],
                'used_traditional_medicine': record['clinical_text']['traditional_medicine_history']['used_traditional_medicine'],
                'cultural_beliefs': record['clinical_text']['cultural_context']['cultural_beliefs_about_injury'],
                'preferred_treatment': record['clinical_text']['cultural_context']['preferred_treatment_approach'],
                
                # Clinical Measurements
                'heart_rate': record['clinical_measurements']['vital_signs']['heart_rate'],
                'bp_systolic': record['clinical_measurements']['vital_signs']['blood_pressure_systolic'],
                'bp_diastolic': record['clinical_measurements']['vital_signs']['blood_pressure_diastolic'],
                'temperature': record['clinical_measurements']['vital_signs']['temperature'],
                'respiratory_rate': record['clinical_measurements']['vital_signs']['respiratory_rate'],
                'oxygen_saturation': record['clinical_measurements']['vital_signs']['oxygen_saturation'],
                'height_cm': record['clinical_measurements']['anthropometric']['height_cm'],
                'weight_kg': record['clinical_measurements']['anthropometric']['weight_kg'],
                'bmi': record['clinical_measurements']['anthropometric']['bmi'],
                'pain_scale': record['clinical_measurements']['pain_assessment']['pain_scale_1_10'],
                'nutritional_status': record['clinical_measurements']['nutritional_status'],
                
                # Environmental Context
                'season': record['environmental_context']['season'],
                'injury_time': record['environmental_context']['injury_time'],
                'day_of_week': record['environmental_context']['day_of_week'],
                'precipitation': record['environmental_context']['weather_conditions']['precipitation'],
                'visibility': record['environmental_context']['weather_conditions']['visibility'],
                
                # Mobile Health
                'owns_phone': record['mobile_health_data']['phone_ownership']['owns_phone'],
                'phone_type': record['mobile_health_data']['phone_ownership'].get('phone_type', 'none'),
                'digital_literacy': record['mobile_health_data']['digital_literacy'],
            }
            records.append(flat_record)
        
        return pd.DataFrame(records)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Main app
def main():
    # Header
    st.markdown('<div class="main-header">🏥 African Medical Multimodal Fracture Dataset</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Patient Information Query System</div>', unsafe_allow_html=True)
    
    # Load data
    with st.spinner('📊 Loading dataset from HuggingFace...'):
        df = load_data()
    
    if df is None:
        st.error("Failed to load data. Please try again later.")
        return
    
    # Sidebar - Dataset Overview
    with st.sidebar:
        st.header("📊 Dataset Overview")
        st.metric("Total Records", f"{len(df):,}")
        st.metric("Countries", df['country'].nunique())
        st.metric("Fracture Types", df['fracture_type'].nunique())
        st.metric("Unique Patients", df['patient_id'].nunique())
        
        st.divider()
        
        st.subheader("🔍 Quick Stats")
        st.write(f"**Age Range:** {df['age'].min()}-{df['age'].max()} years")
        st.write(f"**Avg Pain Scale:** {df['pain_scale'].mean():.1f}/10")
        st.write(f"**Traditional Medicine:** {df['used_traditional_medicine'].sum()/len(df)*100:.1f}%")
        st.write(f"**Phone Ownership:** {df['owns_phone'].sum()/len(df)*100:.1f}%")
        
        st.divider()
        st.caption("💡 Tip: Use the query form above to search for specific patients")
    
    # Main query interface
    st.header("🔍 Patient Query")
    
    # Query type selection
    col1, col2 = st.columns([1, 2])
    
    with col1:
        query_type = st.radio(
            "Search by:",
            ["Patient ID", "Record ID", "Browse All"],
            horizontal=False
        )
    
    with col2:
        if query_type == "Patient ID":
            patient_ids = sorted(df['patient_id'].unique())
            selected_id = st.selectbox("Select Patient ID:", [""] + patient_ids, key="patient_select")
            search_query = selected_id
            search_field = 'patient_id'
        elif query_type == "Record ID":
            record_ids = sorted(df['record_id'].unique())
            selected_id = st.selectbox("Select Record ID:", [""] + record_ids, key="record_select")
            search_query = selected_id
            search_field = 'record_id'
        else:
            search_query = None
            search_field = None
    
    st.divider()
    
    # Display results
    if query_type == "Browse All":
        st.subheader("📋 All Patient Records")
        
        # Filters
        with st.expander("🔧 Filter Options", expanded=True):
            filter_col1, filter_col2, filter_col3 = st.columns(3)
            
            with filter_col1:
                country_filter = st.multiselect("Country:", sorted(df['country'].unique()))
            with filter_col2:
                fracture_filter = st.multiselect("Fracture Type:", sorted(df['fracture_type'].unique()))
            with filter_col3:
                gender_filter = st.multiselect("Gender:", sorted(df['gender'].unique()))
        
        # Apply filters
        filtered_df = df.copy()
        if country_filter:
            filtered_df = filtered_df[filtered_df['country'].isin(country_filter)]
        if fracture_filter:
            filtered_df = filtered_df[filtered_df['fracture_type'].isin(fracture_filter)]
        if gender_filter:
            filtered_df = filtered_df[filtered_df['gender'].isin(gender_filter)]
        
        st.info(f"📊 Showing **{len(filtered_df):,}** of **{len(df):,}** records")
        
        # Display table
        display_cols = ['record_id', 'patient_id', 'fracture_type', 'age', 'gender', 
                       'country', 'pain_scale', 'mechanism_of_injury']
        st.dataframe(
            filtered_df[display_cols].style.format({
                'age': '{:.0f}',
                'pain_scale': '{:.0f}'
            }),
            use_container_width=True, 
            height=400
        )
        
        # Download option
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name="fracture_data_filtered.csv",
            mime="text/csv"
        )
        
    elif search_query:
        # Query specific record
        result = df[df[search_field] == search_query]
        
        if len(result) == 0:
            st.warning(f"⚠️ No records found for {query_type}: **{search_query}**")
        else:
            # Display patient information
            for idx, patient in result.iterrows():
                st.success(f"✅ Record Found: **{patient['record_id']}** (Patient: **{patient['patient_id']}**)")
                
                # Patient Overview Cards
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    st.metric("Age", f"{patient['age']} yrs")
                with col2:
                    st.metric("Gender", patient['gender'])
                with col3:
                    st.metric("Fracture Type", patient['fracture_type'])
                with col4:
                    st.metric("Pain Scale", f"{patient['pain_scale']}/10")
                with col5:
                    st.metric("Country", patient['country'])
                
                st.divider()
                
                # Detailed Information Tabs
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "👤 Demographics", 
                    "🏥 Clinical Info", 
                    "📊 Vital Signs",
                    "🌍 Context",
                    "📱 Digital Health"
                ])
                
                with tab1:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Personal Information")
                        info_data = {
                            "Country": patient['country'],
                            "Region Type": patient['region_type'],
                            "Occupation": patient['occupation'],
                            "Education": patient['education_level'],
                            "Primary Language": patient['primary_language'],
                            "Family Size": f"{patient['family_size']} members"
                        }
                        for key, value in info_data.items():
                            st.text(f"{key}: {value}")
                    
                    with col2:
                        st.subheader("Socioeconomic Status")
                        socio_data = {
                            "Income Level": patient['income_level'],
                            "Insurance Status": patient['insurance_status'],
                            "Healthcare Distance": f"{patient['healthcare_distance_km']} km",
                            "Transportation Mode": patient['transportation_mode']
                        }
                        for key, value in socio_data.items():
                            st.text(f"{key}: {value}")
                
                with tab2:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Injury Details")
                        injury_data = {
                            "Fracture Type": patient['fracture_type'],
                            "Mechanism of Injury": patient['mechanism_of_injury'],
                            "Pain Intensity": patient['pain_intensity'],
                            "Pain Quality": patient['pain_quality'],
                            "Pain Scale": f"{patient['pain_scale']}/10"
                        }
                        for key, value in injury_data.items():
                            st.text(f"{key}: {value}")
                    
                    with col2:
                        st.subheader("Cultural Context")
                        trad_med = "Yes ✓" if patient['used_traditional_medicine'] else "No ✗"
                        cultural_data = {
                            "Traditional Medicine Used": trad_med,
                            "Cultural Beliefs": patient['cultural_beliefs'],
                            "Preferred Treatment": patient['preferred_treatment']
                        }
                        for key, value in cultural_data.items():
                            st.text(f"{key}: {value}")
                
                with tab3:
                    # Vital Signs
                    st.subheader("Vital Signs")
                    vital_col1, vital_col2, vital_col3 = st.columns(3)
                    
                    with vital_col1:
                        st.metric("Heart Rate", f"{patient['heart_rate']} bpm")
                        st.metric("Temperature", f"{patient['temperature']}°C")
                    
                    with vital_col2:
                        st.metric("Blood Pressure", f"{patient['bp_systolic']}/{patient['bp_diastolic']} mmHg")
                        st.metric("Respiratory Rate", f"{patient['respiratory_rate']}/min")
                    
                    with vital_col3:
                        st.metric("O2 Saturation", f"{patient['oxygen_saturation']}%")
                        st.metric("BMI", f"{patient['bmi']:.1f}")
                    
                    # Anthropometric data
                    st.divider()
                    st.subheader("Anthropometric Measurements")
                    anthro_col1, anthro_col2, anthro_col3, anthro_col4 = st.columns(4)
                    
                    with anthro_col1:
                        st.metric("Height", f"{patient['height_cm']} cm")
                    with anthro_col2:
                        st.metric("Weight", f"{patient['weight_kg']} kg")
                    with anthro_col3:
                        st.metric("BMI", f"{patient['bmi']:.1f}")
                    with anthro_col4:
                        st.metric("Nutritional Status", patient['nutritional_status'])
                    
                    # Vital signs comparison chart
                    st.divider()
                    st.subheader("📈 Vital Signs vs. Dataset Average")
                    
                    vital_metrics = {
                        'Heart Rate\n(bpm)': (patient['heart_rate'], df['heart_rate'].mean()),
                        'Systolic BP\n(mmHg)': (patient['bp_systolic'], df['bp_systolic'].mean()),
                        'Temperature\n(°C)': (patient['temperature'], df['temperature'].mean()),
                        'O2 Sat\n(%)': (patient['oxygen_saturation'], df['oxygen_saturation'].mean()),
                        'Resp Rate\n(/min)': (patient['respiratory_rate'], df['respiratory_rate'].mean())
                    }
                    
                    fig = go.Figure()
                    
                    metrics_list = list(vital_metrics.keys())
                    patient_vals = [vital_metrics[m][0] for m in metrics_list]
                    avg_vals = [vital_metrics[m][1] for m in metrics_list]
                    
                    fig.add_trace(go.Bar(
                        name='This Patient',
                        x=metrics_list,
                        y=patient_vals,
                        marker_color='#ff6b6b'
                    ))
                    fig.add_trace(go.Bar(
                        name='Dataset Average',
                        x=metrics_list,
                        y=avg_vals,
                        marker_color='#4ecdc4'
                    ))
                    
                    fig.update_layout(
                        barmode='group',
                        showlegend=True,
                        height=400,
                        margin=dict(l=20, r=20, t=30, b=20),
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1
                        )
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                with tab4:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Environmental Context")
                        env_data = {
                            "Season": patient['season'],
                            "Injury Time": patient['injury_time'],
                            "Day of Week": patient['day_of_week']
                        }
                        for key, value in env_data.items():
                            st.text(f"{key}: {value}")
                    
                    with col2:
                        st.subheader("Weather Conditions")
                        weather_data = {
                            "Precipitation": patient['precipitation'],
                            "Visibility": patient['visibility']
                        }
                        for key, value in weather_data.items():
                            st.text(f"{key}: {value}")
                
                with tab5:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Phone Ownership")
                        phone_status = "Yes ✓" if patient['owns_phone'] else "No ✗"
                        st.text(f"Owns Phone: {phone_status}")
                        if patient['owns_phone']:
                            st.text(f"Phone Type: {patient['phone_type']}")
                    
                    with col2:
                        st.subheader("Digital Literacy")
                        st.text(f"Level: {patient['digital_literacy']}")
    
    else:
        st.info("👆 Please select a Patient ID or Record ID to view detailed information, or choose 'Browse All' to explore the dataset.")
    
    # Footer
    st.divider()
    st.caption("🏥 African Medical Multimodal Fracture Dataset - Query System v1.0 | Data from HuggingFace")

if __name__ == "__main__":
    main()

---
# MN5610: Advanced Measurement Systems and Data Analysis — Term Project

[![Python Application](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)

---

<div align="center">

<img src="picture/brenel.png" height="100" alt="Brunel University London Logo"/>

## Assignment - MN5610: Advanced Measurement Systems and Data Analysis
### Brunel University London
### Department of Mechanical and Aerospace Engineering

</div>

---

## Project Title

**Metrology Strategy and Dimensional Data Analysis** Using Python and advanced statistical modeling, this project evaluates dimensional measurement data and formulates robust inspection strategies for a simulated precision engineering firm.

---

## Assignment Objectives

The project addresses four key manufacturing metrology challenges:

1. **Instrument Analysis:** A comparative evaluation of digital and Vernier micrometer measurements conducted by two different operators using Two-way ANOVA.
2. **Batch Inspection:** Evaluation of 20 bearing housing assemblies with multiple hole sizes and specific tolerance limits.
3. **Shaft Straightness Monitoring:** Dimensional trend analysis for 5 torque shafts measuring 800 mm in length, including the proposal of alternative measurement setups due to limited CMM capacity.
4. **Bespoke Component Measurement:** Comprehensive dimensional recording for high-value, low-volume pump assemblies strictly adhering to ISO 286-2 standards.

---

## Workflow and Methodology

1. **Strategic Metrology Planning:** Identifying critical-to-quality (CTQ) features and selecting appropriate measurement instruments based on production volume (e.g., Air Gauging for high-volume vs. CMM for 1-off bespoke units).
2. **Data Ingestion:** Importing raw experimental datasets for micrometer comparison and shaft straightness monitoring.
3. **Preprocessing & Statistical Modeling:** - Cleaning and transforming data using `pandas` and `numpy`.
   - Executing **Two-way ANOVA** via `statsmodels` to evaluate operator and instrument significance.
4. **Predictive Maintenance & SPC:** Developing Python-based trend analysis models to monitor process stability and detect tool wear before parts exceed tolerance limits.
5. **Standards Verification:** Validating measurement results against **ISO 286-2** (Limits and Fits) and ensuring metrological traceability.
6. **Project Management & Costing:** Formulating a 4-week implementation timeline (Gantt Chart) and a budget justification for the selected metrology equipment.
7. **Documentation:** Compiling technical findings, statistical plots, and strategic recommendations into a formal 3,500-word engineering report.
---

## Project Advisor

<div align="center">
<img src="picture/Dr_moscho.jpeg" height="160" alt="Dr. Moschos Papananias"/>
<br/>
<b>Dr.Moschos Papananias</b> 
</div>

---

## Technologies Used

- **Python 3.x** for core programming  
- **pandas** & **numpy** for data manipulation  
- **statsmodels** for Two-way ANOVA and statistical modeling  
- **matplotlib** & **seaborn** for data visualization  
- **Jupyter Notebook** / **VS Code** for development environment  

---

## File Structure

```bash

├── picture/             # Supporting figures and images
├── cylinder_measurements.xlsx  # Input experimental measurement data
├── Scripts.ipynb      # Main Jupyter notebook for analysis and plots
└── README.md            # This documentation file (Current File)
```
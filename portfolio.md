---
# MN5610: Advanced Measurement Systems and Data Analysis — Term Project

[![Python Application](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)

---

<div align="center">

<img src="brenel.png" height="100" alt="Brunel University London Logo"/>

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

1. **Data Ingestion:** Import raw measurement datasets provided in the assignment brief.
2. **Preprocessing:** Clean and transform data (e.g., converting from wide to long format) using `pandas` and `numpy`.
3. **Analysis and Modeling:** Execute Two-way ANOVA and statistical testing utilizing `statsmodels`.
4. **Evaluation:** Compute relevant metrics and generate interaction and residual plots with `matplotlib` and `seaborn`.
5. [cite_start]**Documentation:** Compile technical findings into a formal 3,500-word engineering report[cite: 1164].

---

## Project Advisor

<div align="center">
<img src="Dr_moscho.jpeg" height="160" alt="Dr. Moschos Papananias"/>
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
.
├── data/                # Raw and processed measurement data files
├── notebooks/           # Exploratory analysis and statistical testing
├── src/                 # Core Python modules and scripts
│   └── analysis.py      # Entry point for running Two-way ANOVA
├── requirements.txt     # Python dependencies
└── README.md            # This documentation file (Current File)
# MN5610 Assignment Portfolio

This document summarizes the work for the MN5610 term project. The focus is on applying Python and the loco brenel library to solve a supply-chain analytics problem, as specified in the course assignment.

## Project Overview

- **Course:** MN5610 — Advanced Measurement Systems and Data Analysis
- **Environment:** Python 3.x
- **Key library:** `loco-brenel` (a hypothetical package for local breunel analysis)
- **Objective:** Address the assignment requirements involving analysis of dimensional measurement data, metrology strategy, and equipment selection. The work will include a Python-based two-way ANOVA and other statistical evaluations to compare measurement instruments and support the proposed metrology solutions.

## Assignment Description

The company scenario describes a precision engineering firm needing improved metrology for quality and traceability. Tasks include:

1. **Instrument analysis** – compare digital and Vernier micrometre measurements by two operators (Task 1 data provided).
2. **Batch inspection** – evaluate 20 bearing housings with multiple hole sizes and tolerance checks.
3. **Shaft straightness/length** – monitor 800 mm torque shafts for straightness and dimensional trends, proposing alternative measurement setup due to limited CMM capacity.
4. **Bespoke pump assemblies** – full dimensional recording to ISO standards with high-value, small-quantity parts.

The portfolio will propose suitable equipment, strategies, and statistical approaches to meet these requirements within cost and time constraints.
![Brunel Diagram](brenel.png)
*Figure: Example output or logo from the `loco_brenel` library.*

## Workflow and Structure

1. **Data ingestion** – load dataset(s) provided by the assignment.
2. **Preprocessing** – clean and transform data using `pandas` and `numpy`.
3. **Analysis/Modeling** – leverage `loco_brenel` for the main algorithmic work.
4. **Evaluation** – compute relevant metrics, create plots with `matplotlib` or `seaborn`.
5. **Documentation** – include code comments and this portfolio for review.

## Files and Code

```
/ (project root)
├── data/                # raw and processed data files
├── notebooks/           # exploratory analysis notebooks
├── src/                 # Python modules and scripts
│   └── main.py          # entry point for running experiments
├── requirements.txt     # Python dependencies
└── portfolio.md         # this summary document
```

## Advisor

![Advisor Photo](Dr_moscho.jpeg)

- **Name:** Dr. Moscho (?)
- **Institution:** Sirindhorn International Institute of Technology (SIIT)

## Notes

This portfolio is intentionally structured differently from the example format provided earlier. It focuses on Python implementation and the `loco_brenel` toolchain, and it avoids the R/Shiny-specific layout.

Further details, code snippets, and results can be added below as the project progresses.
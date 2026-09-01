# 🩺 Medical Examination Data Visualizer (Seaborn & Matplotlib)

A data visualization project analyzing medical examination records to explore relationships between cardiac disease, body measurements, blood markers, and lifestyle choices.

## 🎯 Project Overview
This project processes medical data to normalize clinical metrics, filter physiological outliers, and build interactive visualizations:
1. **Categorical Plot (`catplot`):** Shows counts of categorical features (cholesterol, glucose, smoking, alcohol intake, physical activity, overweight) split by cardiovascular disease status.
2. **Correlation Heatmap:** Visualizes feature correlations after cleaning inaccurate blood pressure records and extreme height/weight outliers.

## 🛠️ Tech Stack & Tools
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib

## 📌 Key Data Processing & Visualization Highlights
- **Feature Engineering:** Calculated BMI to create a binary `overweight` indicator feature.
- **Data Normalization:** Transformed categorical blood markers (`cholesterol`, `gluc`) into binary representations ($0 = Normal, 1 = Above Normal$).
- **Data Cleaning:** Filtered out erroneous physiological entries (e.g., diastolic pressure higher than systolic) and extreme values outside the $2.5^{th} - 97.5^{th}$ percentiles.
- **Advanced Plotting:** Built masked triangular heatmaps and multi-facet categorical bar charts.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/medical-data-visualizer.git](https://github.com/YOUR-USERNAME/medical-data-visualizer.git)
  pip install pandas numpy seaborn matplotlib
  from medical_data_visualizer import draw_cat_plot, draw_heat_map

cat_fig = draw_cat_plot()
heat_fig = draw_heat_map()

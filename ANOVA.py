import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# --- STEP 1: การนำเข้าข้อมูล ---
# แนะนำให้จัดไฟล์ Excel ให้มี 3 คอลัมน์: Operator, Instrument, Measurement
# ตามข้อมูลใน Table 1.1 และ 1.2 [cite: 1276, 1279]
file_path = '/Users/bifook/Desktop/MN5610 Assignment/cylineder_measurements.xlsx' 
df = pd.read_excel(file_path)

# --- STEP 2: การตั้งค่า Model และรัน ANOVA ---
# สูตร 'Measurement ~ Factor1 * Factor2' จะคำนวณทั้งผลหลักและผลร่วม (Interaction)
model = ols('Measurement ~ C(Operator) * C(Instrument)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("--- ANOVA Table Results ---")
print(anova_table)

# --- STEP 3: สร้างกราฟ Interaction Plot ---
# กราฟนี้สำคัญมากในการวิเคราะห์ "Repeatability" และ "User influence" [cite: 1235, 1254]
plt.figure(figsize=(10, 6))
sns.pointplot(data=df, x='Instrument', y='Measurement', hue='Operator', capsize=.1)
plt.title('Interaction Plot: Operator vs Instrument (MN5610 Task 1)')
plt.ylabel('Diameter (mm)')
plt.grid(True, alpha=0.3)
plt.show() # หรือใช้ plt.savefig('result.png') เพื่อเซฟรูปไปใส่ในรายงาน [cite: 1166]
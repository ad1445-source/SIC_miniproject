Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
df = pd.read_csv(r"C:\Users\Lenovo\Downloads\NFHS-5-States.csv")
columns_to_keep = [
    "State",
    "Obesity_Men", "Obesity_Women",
    "Anaemia_Children", "Anaemia_Women",
    "HighBloodSugar_Men", "HighBloodSugar_Women",
    "Hypertension_Men", "Hypertension_Women"
]
df = df[columns_to_keep]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    df = df[columns_to_keep]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\frame.py", line 4384, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 6302, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 6352, in _raise_if_missing
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['State', 'Obesity_Men', 'Obesity_Women', 'Anaemia_Children',\n       'Anaemia_Women', 'HighBloodSugar_Men', 'HighBloodSugar_Women',\n       'Hypertension_Men', 'Hypertension_Women'],\n      dtype='str')] are in the [columns]"
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 4847 entries, 0 to 4846
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   state        4847 non-null   str    
 1   state_code   4716 non-null   str    
 2   indicator    4847 non-null   str    
 3   nfhs5_urban  4693 non-null   float64
 4   nfhs5_rural  4635 non-null   float64
 5   nfhs5_total  4799 non-null   float64
 6   nfhs4_total  3660 non-null   float64
dtypes: float64(4), str(3)
memory usage: 265.2 KB
df_pivot = df.pivot_table(
    index="state",
    columns="indicator",
    values="nfhs5_total"
).reset_index()
rename_map = {
    "Overweight or obesity among men (age 15-49 years)": "Obesity_Men",
    "Overweight or obesity among women (age 15-49 years)": "Obesity_Women",
    "Anaemia among children (age 6-59 months)": "Anaemia_Children",
    "Anaemia among women (age 15-49 years)": "Anaemia_Women",
    "High blood sugar among men (age 15-49 years)": "HighBloodSugar_Men",
    "High blood sugar among women (age 15-49 years)": "HighBloodSugar_Women",
    "Hypertension among men (age 15-49 years)": "Hypertension_Men",
    "Hypertension among women (age 15-49 years)": "Hypertension_Women"
}
df_pivot = df_pivot.rename(columns=rename_map)
df_pivot["Gender_Obesity_Gap"] = df_pivot["Obesity_Women"] - df_pivot["Obesity_Men"]
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Obesity_Women'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df_pivot["Gender_Obesity_Gap"] = df_pivot["Obesity_Women"] - df_pivot["Obesity_Men"]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Obesity_Women'
print(df["indicator"].unique())
<StringArray>
[                                '1. Female population age 6 years and above who ever attended school (%)',
                                                                    '2. Population below age 15 years (%)',
                                          '3. Sex ratio of the total population (females per 1,000 males)',
                '4. Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                   '5. Children under age 5 years whose birth was registered with the civil authority (%)',
                                   '6. Deaths in the last 3 years registered with the civil authority (%)',
                                                 '7. Population living in households with electricity (%)',
                          '8. Population living in households with an improved drinking-water source1 (%)',
                        '9. Population living in households that use an improved sanitation facility2 (%)',
                                                        '10. Households using clean fuel for cooking3 (%)',
 ...
                                           '123. Women having a mobile phone that they themselves use (%)',
   '124. Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)',
                '125. Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)',
 '126. Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)',
                          '127. Young women age 18-29 years who experienced sexual violence by age 18 (%)',
                                       '128. Women age 15 years and above who use any kind of tobacco (%)',
                                         '129. Men age 15 years and above who use any kind of tobacco (%)',
                                               '130. Women age 15 years and above who consume alcohol (%)',
                                                 '131. Men age 15 years and above who consume alcohol (%)',
                     '66. Children age 9-35 months who received a vitamin A dose in the last 6 months (%)']
Length: 132, dtype: str
keywords = ["obesity", "anaemia", "hypertension", "blood sugar"]
for kw in keywords:
    matches = [col for col in df["indicator"].unique() if kw.lower() in col.lower()]
    print(f"\nIndicators containing '{kw}':")
    for m in matches:
        print(" -", m)

        

Indicators containing 'obesity':

Indicators containing 'anaemia':

Indicators containing 'hypertension':

Indicators containing 'blood sugar':
 - 99. Blood sugar level - high (141-160 mg/dl)23 (%)
 - 100. Blood sugar level - very high (>160 mg/dl)23 (%)
 - 101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
 - 102. Blood sugar level - high (141-160 mg/dl)23 (%)
 - 103. Blood sugar level - very high (>160 mg/dl)23 (%)
 - 104. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
for kw in ["weight", "overweight", "anaemia", "blood sugar", "hypertension"]:
    matches = [col for col in df["indicator"].unique() if kw.lower() in col.lower()]
    print(f"\nIndicators containing '{kw}':")
    for m in matches:
        print(" -", m)

        

Indicators containing 'weight':
 - 82. Children under 5 years who are wasted (weight-for-height)18 (%)
 - 83. Children under 5 years who are severely wasted (weight-for-height)19 (%)
 - 84. Children under 5 years who are underweight (weight-for-age)18 (%)
 - 85. Children under 5 years who are overweight (weight-for-height)20 (%)
 - 88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)
 - 89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)

Indicators containing 'overweight':
 - 85. Children under 5 years who are overweight (weight-for-height)20 (%)
 - 88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)
 - 89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)

Indicators containing 'anaemia':

Indicators containing 'blood sugar':
 - 99. Blood sugar level - high (141-160 mg/dl)23 (%)
 - 100. Blood sugar level - very high (>160 mg/dl)23 (%)
 - 101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
 - 102. Blood sugar level - high (141-160 mg/dl)23 (%)
 - 103. Blood sugar level - very high (>160 mg/dl)23 (%)
 - 104. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)

Indicators containing 'hypertension':
df_pivot = df.pivot_table(index="state", columns="indicator", values="nfhs5_total")
rename_map = {
    "88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)": "Obesity_Women",
    "89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)": "Obesity_Men",
    "99. Blood sugar level - high (141-160 mg/dl)23 (%)": "BloodSugar_High",
    "100. Blood sugar level - very high (>160 mg/dl)23 (%)": "BloodSugar_VeryHigh",
    "101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)": "BloodSugar_Total"
    # Add anaemia and hypertension once you locate their exact names
}
df_pivot = df_pivot.rename(columns=rename_map)
if "Obesity_Women" in df_pivot.columns and "Obesity_Men" in df_pivot.columns:
    df_pivot["Gender_Obesity_Gap"] = df_pivot["Obesity_Women"] - df_pivot["Obesity_Men"]

    
print(df_pivot.head())
indicator                  1. Female population age 6 years and above who ever attended school (%)  ...  Gender_Obesity_Gap
state                                                                                               ...                    
Andaman & Nicobar Islands                                               83.5                        ...                -7.2
Andhra Pradesh                                                          65.6                        ...                 5.2
Arunachal Pradesh                                                       71.2                        ...                -3.7
Assam                                                                   78.2                        ...                -1.0
Bihar                                                                   61.1                        ...                 1.2

[5 rows x 133 columns]
rename_map = {
    "88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)": "Obesity_Women",
    "89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)": "Obesity_Men",
    "99. Blood sugar level - high (141-160 mg/dl)23 (%)": "BloodSugar_High",
    "100. Blood sugar level - very high (>160 mg/dl)23 (%)": "BloodSugar_VeryHigh",
    "101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)": "BloodSugar_Total",
    # Add anaemia + hypertension once you locate their exact names
}
df_pivot = df_pivot.rename(columns=rename_map)
df_pivot["Gender_Obesity_Gap"] = df_pivot["Obesity_Women"] - df_pivot["Obesity_Men"]

corr_matrix = df_pivot[["Obesity_Women","Obesity_Men","BloodSugar_Total","Gender_Obesity_Gap"]].corr()
print(corr_matrix)
indicator           Obesity_Women  ...  Gender_Obesity_Gap
indicator                          ...                    
Obesity_Women            1.000000  ...            0.391654
Obesity_Men              0.878541  ...           -0.095423
BloodSugar_Total         0.630167  ...            0.368732
Gender_Obesity_Gap       0.391654  ...            1.000000

[4 rows x 4 columns]
plt.figure(figsize=(6, 5))
<Figure size 600x500 with 0 Axes>
plt.imshow(corr_matrix, cmap="coolwarm", interpolation="nearest")
<matplotlib.image.AxesImage object at 0x0000028962643FE0>
plt.colorbar(label="Correlation")
<matplotlib.colorbar.Colorbar object at 0x000002896265D220>
labels = corr_matrix.columns
plt.xticks(np.arange(len(labels)), labels, rotation=45, ha="right")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    plt.xticks(np.arange(len(labels)), labels, rotation=45, ha="right")
NameError: name 'np' is not defined
import numpy as np
plt.xticks(np.arange(len(labels)), labels, rotation=45, ha="right")
([<matplotlib.axis.XTick object at 0x00000289623621E0>, <matplotlib.axis.XTick object at 0x00000289623DA480>, <matplotlib.axis.XTick object at 0x00000289623DA5A0>, <matplotlib.axis.XTick object at 0x000002896268FF20>], [Text(0, 0, 'Obesity_Women'), Text(1, 0, 'Obesity_Men'), Text(2, 0, 'BloodSugar_Total'), Text(3, 0, 'Gender_Obesity_Gap')])
plt.yticks(np.arange(len(labels)), labels)
([<matplotlib.axis.YTick object at 0x0000028962641E80>, <matplotlib.axis.YTick object at 0x00000289626419D0>, <matplotlib.axis.YTick object at 0x0000028962AB9250>, <matplotlib.axis.YTick object at 0x0000028962AB8D70>], [Text(0, 0, 'Obesity_Women'), Text(0, 1, 'Obesity_Men'), Text(0, 2, 'BloodSugar_Total'), Text(0, 3, 'Gender_Obesity_Gap')])
plt.title("Correlation Matrix of Selected NFHS-5 Indicators")
Text(0.5, 1.0, 'Correlation Matrix of Selected NFHS-5 Indicators')
plt.tight_layout()
plt.show()
df_pivot["Hypertension_Gap"] = df_pivot["Hypertension_Women"] - df_pivot["Hypertension_Men"]
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Hypertension_Women'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    df_pivot["Hypertension_Gap"] = df_pivot["Hypertension_Women"] - df_pivot["Hypertension_Men"]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Hypertension_Women'
matches = [col for col in df["indicator"].unique() if "pressure" in col.lower() or "hypertension" in col.lower()]
print(matches)
['105. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)', '106. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)', '107. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)', '108. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)', '109. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)', '110. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)']
rename_map.update({
    "105. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)": "BP_Mild",
    "106. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)": "BP_Severe",
    "107. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)": "BP_Total",
    "108. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)": "BP_Mild_Duplicate",
    "109. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)": "BP_Severe_Duplicate",
    "110. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)": "BP_Total_Duplicate"
})

df_pivot = df.pivot_table(index="state", columns="indicator", values="nfhs5_total").reset_index()
df_pivot = df_pivot.rename(columns=rename_map)
plt.figure(figsize=(10,6))
<Figure size 1000x600 with 0 Axes>
plt.bar(df_pivot["state"], df_pivot["BP_Mild"], label="Mild", color="orange")
<BarContainer object of 37 artists>
plt.bar(df_pivot["state"], df_pivot["BP_Severe"], label="Severe", color="red", alpha=0.7)
<BarContainer object of 37 artists>
plt.xticks(rotation=90)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [Text(0, 0, 'Andaman & Nicobar Islands'), Text(1, 0, 'Andhra Pradesh'), Text(2, 0, 'Arunachal Pradesh'), Text(3, 0, 'Assam'), Text(4, 0, 'Bihar'), Text(5, 0, 'Chandigarh'), Text(6, 0, 'Chhattisgarh'), Text(7, 0, 'Dadra & Nagar Haveli and Daman & Diu'), Text(8, 0, 'Goa'), Text(9, 0, 'Gujarat'), Text(10, 0, 'Haryana'), Text(11, 0, 'Himachal Pradesh'), Text(12, 0, 'India'), Text(13, 0, 'Jammu & Kashmir'), Text(14, 0, 'Jharkhand'), Text(15, 0, 'Karnataka'), Text(16, 0, 'Kerala'), Text(17, 0, 'Ladakh'), Text(18, 0, 'Lakshadweep'), Text(19, 0, 'Madhya Pradesh'), Text(20, 0, 'Maharashtra'), Text(21, 0, 'Manipur'), Text(22, 0, 'Meghalaya'), Text(23, 0, 'Mizoram'), Text(24, 0, 'NCT Delhi'), Text(25, 0, 'Nagaland'), Text(26, 0, 'Odisha'), Text(27, 0, 'Puducherry'), Text(28, 0, 'Punjab'), Text(29, 0, 'Rajasthan'), Text(30, 0, 'Sikkim'), Text(31, 0, 'Tamil Nadu'), Text(32, 0, 'Telangana'), Text(33, 0, 'Tripura'), Text(34, 0, 'Uttar Pradesh'), Text(35, 0, 'Uttarakhand'), Text(36, 0, 'West Bengal')])
plt.ylabel("Prevalence (%)")
Text(0, 0.5, 'Prevalence (%)')
plt.title("Blood Pressure Levels by State")
Text(0.5, 1.0, 'Blood Pressure Levels by State')
plt.legend()
<matplotlib.legend.Legend object at 0x0000028964403D40>
plt.tight_layout()
plt.show()
plt.figure(figsize=(8,6))
<Figure size 800x600 with 0 Axes>
plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Anaemia_Women'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Anaemia_Women'
matches = [col for col in df["indicator"].unique() if "anaemia" in col.lower()]
print(matches)
[]
matches = [col for col in df["indicator"].unique() if "anemia" in col.lower()]
print(matches)
[]
for col in df["indicator"].unique():
    print(col)

    
1. Female population age 6 years and above who ever attended school (%)
2. Population below age 15 years (%)
3. Sex ratio of the total population (females per 1,000 males)
4. Sex ratio at birth for children born in the last five years (females per 1,000 males)
5. Children under age 5 years whose birth was registered with the civil authority (%)
6. Deaths in the last 3 years registered with the civil authority (%)
7. Population living in households with electricity (%)
8. Population living in households with an improved drinking-water source1 (%)
9. Population living in households that use an improved sanitation facility2 (%)
10. Households using clean fuel for cooking3 (%)
11. Households using iodized salt (%)
12. Households with any usual member covered under a health insurance/financing scheme (%)
13. Children age 5 years who attended pre-primary school during the school year 2019-20 (%)
14. Women who are literate4 (%)
15. Men who are literate4 (%)
16. Women with 10 or more years of schooling (%)
17. Men with 10 or more years of schooling (%)
18. Women who have ever used the internet (%)
19. Men who have ever used the internet (%)
20. Women age 20-24 years married before age 18 years (%)
21. Men age 25-29 years married before age 21 years (%)
22. Total fertility rate (children per woman)
23. Women age 15-19 years who were already mothers or pregnant at the time of the survey (%)
24. Adolescent fertility rate for women age 15-19 years5
25. Neonatal mortality rate (NNMR)
26. Infant mortality rate (IMR)
27. Under-five mortality rate (U5MR)
28. Any method6 (%)
29. Any modern method6 (%)
30. Female sterilization (%)
31. Male sterilization (%)
32. IUD/PPIUD (%)
33. Pill (%)
34. Condom (%)
35. Injectables (%)
36. Total unmet need7 (%)
37. Unmet need for spacing7 (%)
38. Health worker ever talked to female non-users about family planning (%)
39. Current users ever told about side effects of current method8 (%)
40. Mothers who had an antenatal check-up in the first trimester (%)
41. Mothers who had at least 4 antenatal care visits (%)
42. Mothers whose last birth was protected against neonatal tetanus9 (%)
43. Mothers who consumed iron folic acid for 100 days or more when they were pregnant (%)
44. Mothers who consumed iron folic acid for 180 days or more when they were pregnant (%)
45. Registered pregnancies for which the mother received a Mother and Child Protection (MCP) card (%)
46. Mothers who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)
47. Average out-of-pocket expenditure per delivery in a public health facility (Rs.)
48. Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)
49. Children who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)
50. Institutional births (%)
51. Institutional births in public facility (%)
52. Home births that were conducted by skilled health personnel10 (%)
53. Births attended by skilled health personnel10 (%)
54. Births delivered by caesarean section (%)
55. Births in a private health facility that were delivered by caesarean section (%)
56. Births in a public health facility that were delivered by caesarean section (%)
57. Children age 12-23 months fully vaccinated based on information from either vaccination card or mother's recall11 (%)
58. Children age 12-23 months fully vaccinated based on information from vaccination card only12 (%)
59. Children age 12-23 months who have received BCG (%)
60. Children age 12-23 months who have received 3 doses of polio vaccine13 (%)
61. Children age 12-23 months who have received 3 doses of penta or DPT vaccine (%)
62. Children age 12-23 months who have received the first dose of measles-containing vaccine (MCV) (%)
63. Children age 24-35 months who have received a second dose of measles-containing vaccine (MCV) (%)
64. Children age 12-23 months who have received 3 doses of rotavirus vaccine14 (%)
65. Children age 12-23 months who have received 3 doses of penta or hepatitis B vaccine (%)
66. Children age 9-59 months who received a vitamin A dose in the last 6 months (%)
67. Children age 12-23 months who received most of their vaccinations in a public health facility (%)
68. Children age 12-23 months who received most of their vaccinations in a private health facility (%)
69. Prevalence of diarrhoea in the 2 weeks preceding the survey (%)
70. Children with diarrhoea in the 2 weeks preceding the survey who received oral rehydration salts (ORS) (%)
71. Children with diarrhoea in the 2 weeks preceding the survey who received zinc (%)
72. Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%)
73. Prevalence of symptoms of acute respiratory infection (ARI) in the 2 weeks preceding the survey (%)
74. Children with fever or symptoms of ARI in the 2 weeks preceding the survey taken to a health facility or health provider (%)
75. Children under age 3 years breastfed within one hour of birth15 (%)
76. Children under age 6 months exclusively breastfed16 (%)
77. Children age 6-8 months receiving solid or semi-solid food and breastmilk16 (%)
78. Breastfeeding children age 6-23 months receiving an adequate diet16, 17  (%)
79. Non-breastfeeding children age 6-23 months receiving an adequate diet16, 17 (%)
80. Total children age 6-23 months receiving an adequate diet16, 17  (%)
81. Children under 5 years who are stunted (height-for-age)18 (%)
82. Children under 5 years who are wasted (weight-for-height)18 (%)
83. Children under 5 years who are severely wasted (weight-for-height)19 (%)
84. Children under 5 years who are underweight (weight-for-age)18 (%)
85. Children under 5 years who are overweight (weight-for-height)20 (%)
86. Women whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2)21 (%)
87. Men whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2) (%)
88. Women who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)
89. Men who are overweight or obese (BMI ≥25.0 kg/m2) (%)
90. Women who have high risk waist-to-hip ratio (≥0.85) (%)
91. Men who have high risk waist-to-hip ratio (≥0.90) (%)
92. Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)
93. Non-pregnant women age 15-49 years who are anaemic (<12.0 g/dl)22 (%)
94. Pregnant women age 15-49 years who are anaemic (<11.0 g/dl)22 (%)
95. All women age 15-49 years who are anaemic22 (%)
96. All women age 15-19 years who are anaemic22 (%)
97. Men age 15-49 years who are anaemic (<13.0 g/dl)22 (%)
98. Men age 15-19 years who are anaemic (<13.0 g/dl)22 (%)
99. Blood sugar level - high (141-160 mg/dl)23 (%)
100. Blood sugar level - very high (>160 mg/dl)23 (%)
101. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
102. Blood sugar level - high (141-160 mg/dl)23 (%)
103. Blood sugar level - very high (>160 mg/dl)23 (%)
104. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)
105. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)
106. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)
107. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)
108. Mildly elevated blood pressure (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)
109. Moderately or severely elevated blood pressure (Systolic ≥160 mm of Hg and/or Diastolic ≥100 mm of Hg) (%)
110. Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)
111. Ever undergone a screening test for cervical cancer (%)
112. Ever undergone a breast examination for breast cancer (%)
113. Ever undergone an oral cavity examination for oral cancer (%)
114. Ever undergone an oral cavity examination for oral cancer (%)
115. Women who have comprehensive knowledge24 of HIV/AIDS (%)
116. Men who have comprehensive knowledge24 of HIV/AIDS (%)
117. Women who know that consistent condom use can reduce the chance of getting HIV/AIDS (%)
118. Men who know that consistent condom use can reduce the chance of getting HIV/AIDS (%)
119. Currently married women who usually participate in three household decisions25 (%)
120. Women who worked in the last 12 months and were paid in cash (%)
121. Women owning a house and/or land (alone or jointly with others) (%)
122. Women having a bank or savings account that they themselves use (%)
123. Women having a mobile phone that they themselves use (%)
124. Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)
125. Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)
126. Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)
127. Young women age 18-29 years who experienced sexual violence by age 18 (%)
128. Women age 15 years and above who use any kind of tobacco (%)
129. Men age 15 years and above who use any kind of tobacco (%)
130. Women age 15 years and above who consume alcohol (%)
131. Men age 15 years and above who consume alcohol (%)
66. Children age 9-35 months who received a vitamin A dose in the last 6 months (%)
rename_map.update({
    "92. Children age 6-59 months who are anaemic (<11.0 g/dl) (%)": "Anaemia_Children",
    "95. All women age 15-49 years who are anaemic (%)": "Anaemia_Women",
    "97. Men age 15-49 years who are anaemic (<13.0 g/dl) (%)": "Anaemia_Men"
})


df_pivot = df.pivot_table(index="state", columns="indicator", values="nfhs5_total").reset_index()
df_pivot = df_pivot.rename(columns=rename_map)
plt.figure(figsize=(8,6))
<Figure size 800x600 with 0 Axes>
plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Anaemia_Women'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Anaemia_Women'
>>> rename_map.update({
...     "92. Children age 6-59 months who are anaemic (<11.0 g/dl) (%)": "Anaemia_Children",
...     "95. All women age 15-49 years who are anaemic (%)": "Anaemia_Women",
...     "97. Men age 15-49 years who are anaemic (<13.0 g/dl) (%)": "Anaemia_Men"
... })
... 
>>> 
>>> df_pivot = df.pivot_table(index="state", columns="indicator", values="nfhs5_total").reset_index()
>>> df_pivot = df_pivot.rename(columns=rename_map)
>>> plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Anaemia_Women'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Anaemia_Women'
print(df_pivot.columns.tolist())

['state', '1. Female population age 6 years and above who ever attended school (%)', '10. Households using clean fuel for cooking3 (%)', 'BloodSugar_VeryHigh', 'BloodSugar_Total', '102. Blood sugar level - high (141-160 mg/dl)23 (%)', '103. Blood sugar level - very high (>160 mg/dl)23 (%)', '104. Blood sugar level - high or very high (>140 mg/dl) or taking medicine to control blood sugar level23 (%)', 'BP_Mild', 'BP_Severe', 'BP_Total', 'BP_Mild_Duplicate', 'BP_Severe_Duplicate', '11. Households using iodized salt (%)', 'BP_Total_Duplicate', '111. Ever undergone a screening test for cervical cancer (%)', '112. Ever undergone a breast examination for breast cancer (%)', '113. Ever undergone an oral cavity examination for oral cancer (%)', '114. Ever undergone an oral cavity examination for oral cancer (%)', '115. Women who have comprehensive knowledge24 of HIV/AIDS (%)', '116. Men who have comprehensive knowledge24 of HIV/AIDS (%)', '117. Women who know that consistent condom use can reduce the chance of getting HIV/AIDS (%)', '118. Men who know that consistent condom use can reduce the chance of getting HIV/AIDS (%)', '119. Currently married women who usually participate in three household decisions25 (%)', '12. Households with any usual member covered under a health insurance/financing scheme (%)', '120. Women who worked in the last 12 months and were paid in cash (%)', '121. Women owning a house and/or land (alone or jointly with others) (%)', '122. Women having a bank or savings account that they themselves use (%)', '123. Women having a mobile phone that they themselves use (%)', '124. Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)', '125. Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)', '126. Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)', '127. Young women age 18-29 years who experienced sexual violence by age 18 (%)', '128. Women age 15 years and above who use any kind of tobacco (%)', '129. Men age 15 years and above who use any kind of tobacco (%)', '13. Children age 5 years who attended pre-primary school during the school year 2019-20 (%)', '130. Women age 15 years and above who consume alcohol (%)', '131. Men age 15 years and above who consume alcohol (%)', '14. Women who are literate4 (%)', '15. Men who are literate4 (%)', '16. Women with 10 or more years of schooling (%)', '17. Men with 10 or more years of schooling (%)', '18. Women who have ever used the internet (%)', '19. Men who have ever used the internet (%)', '2. Population below age 15 years (%)', '20. Women age 20-24 years married before age 18 years (%)', '21. Men age 25-29 years married before age 21 years (%)', '22. Total fertility rate (children per woman)', '23. Women age 15-19 years who were already mothers or pregnant at the time of the survey (%)', '24. Adolescent fertility rate for women age 15-19 years5', '25. Neonatal mortality rate (NNMR)', '26. Infant mortality rate (IMR)', '27. Under-five mortality rate (U5MR)', '28. Any method6 (%)', '29. Any modern method6 (%)', '3. Sex ratio of the total population (females per 1,000 males)', '30. Female sterilization (%)', '31. Male sterilization (%)', '32. IUD/PPIUD (%)', '33. Pill (%)', '34. Condom (%)', '35. Injectables (%)', '36. Total unmet need7 (%)', '37. Unmet need for spacing7 (%)', '38. Health worker ever talked to female non-users about family planning (%)', '39. Current users ever told about side effects of current method8 (%)', '4. Sex ratio at birth for children born in the last five years (females per 1,000 males)', '40. Mothers who had an antenatal check-up in the first trimester (%)', '41. Mothers who had at least 4 antenatal care visits (%)', '42. Mothers whose last birth was protected against neonatal tetanus9 (%)', '43. Mothers who consumed iron folic acid for 100 days or more when they were pregnant (%)', '44. Mothers who consumed iron folic acid for 180 days or more when they were pregnant (%)', '45. Registered pregnancies for which the mother received a Mother and Child Protection (MCP) card (%)', '46. Mothers who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)', '47. Average out-of-pocket expenditure per delivery in a public health facility (Rs.)', '48. Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)', '49. Children who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)', '5. Children under age 5 years whose birth was registered with the civil authority (%)', '50. Institutional births (%)', '51. Institutional births in public facility (%)', '52. Home births that were conducted by skilled health personnel10 (%)', '53. Births attended by skilled health personnel10 (%)', '54. Births delivered by caesarean section (%)', '55. Births in a private health facility that were delivered by caesarean section (%)', '56. Births in a public health facility that were delivered by caesarean section (%)', "57. Children age 12-23 months fully vaccinated based on information from either vaccination card or mother's recall11 (%)", '58. Children age 12-23 months fully vaccinated based on information from vaccination card only12 (%)', '59. Children age 12-23 months who have received BCG (%)', '6. Deaths in the last 3 years registered with the civil authority (%)', '60. Children age 12-23 months who have received 3 doses of polio vaccine13 (%)', '61. Children age 12-23 months who have received 3 doses of penta or DPT vaccine (%)', '62. Children age 12-23 months who have received the first dose of measles-containing vaccine (MCV) (%)', '63. Children age 24-35 months who have received a second dose of measles-containing vaccine (MCV) (%)', '64. Children age 12-23 months who have received 3 doses of rotavirus vaccine14 (%)', '65. Children age 12-23 months who have received 3 doses of penta or hepatitis B vaccine (%)', '66. Children age 9-35 months who received a vitamin A dose in the last 6 months (%)', '66. Children age 9-59 months who received a vitamin A dose in the last 6 months (%)', '67. Children age 12-23 months who received most of their vaccinations in a public health facility (%)', '68. Children age 12-23 months who received most of their vaccinations in a private health facility (%)', '69. Prevalence of diarrhoea in the 2 weeks preceding the survey (%)', '7. Population living in households with electricity (%)', '70. Children with diarrhoea in the 2 weeks preceding the survey who received oral rehydration salts (ORS) (%)', '71. Children with diarrhoea in the 2 weeks preceding the survey who received zinc (%)', '72. Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%)', '73. Prevalence of symptoms of acute respiratory infection (ARI) in the 2 weeks preceding the survey (%)', '74. Children with fever or symptoms of ARI in the 2 weeks preceding the survey taken to a health facility or health provider (%)', '75. Children under age 3 years breastfed within one hour of birth15 (%)', '76. Children under age 6 months exclusively breastfed16 (%)', '77. Children age 6-8 months receiving solid or semi-solid food and breastmilk16 (%)', '78. Breastfeeding children age 6-23 months receiving an adequate diet16, 17  (%)', '79. Non-breastfeeding children age 6-23 months receiving an adequate diet16, 17 (%)', '8. Population living in households with an improved drinking-water source1 (%)', '80. Total children age 6-23 months receiving an adequate diet16, 17  (%)', '81. Children under 5 years who are stunted (height-for-age)18 (%)', '82. Children under 5 years who are wasted (weight-for-height)18 (%)', '83. Children under 5 years who are severely wasted (weight-for-height)19 (%)', '84. Children under 5 years who are underweight (weight-for-age)18 (%)', '85. Children under 5 years who are overweight (weight-for-height)20 (%)', '86. Women whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2)21 (%)', '87. Men whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2) (%)', 'Obesity_Women', 'Obesity_Men', '9. Population living in households that use an improved sanitation facility2 (%)', '90. Women who have high risk waist-to-hip ratio (≥0.85) (%)', '91. Men who have high risk waist-to-hip ratio (≥0.90) (%)', '92. Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)', '93. Non-pregnant women age 15-49 years who are anaemic (<12.0 g/dl)22 (%)', '94. Pregnant women age 15-49 years who are anaemic (<11.0 g/dl)22 (%)', '95. All women age 15-49 years who are anaemic22 (%)', '96. All women age 15-19 years who are anaemic22 (%)', '97. Men age 15-49 years who are anaemic (<13.0 g/dl)22 (%)', '98. Men age 15-19 years who are anaemic (<13.0 g/dl)22 (%)', 'BloodSugar_High']
df_pivot = df_pivot.rename(columns={
    "92. Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)": "Anaemia_Children",
    "95. All women age 15-49 years who are anaemic22 (%)": "Anaemia_Women",
    "97. Men age 15-49 years who are anaemic (<13.0 g/dl)22 (%)": "Anaemia_Men"
})

plt.scatter(df_pivot["Anaemia_Women"], df_pivot["Obesity_Women"], color="purple")
<matplotlib.collections.PathCollection object at 0x0000028962ACD6A0>
for i, row in df_pivot.iterrows():
    plt.text(row["Anaemia_Women"]+0.2, row["Obesity_Women"]+0.2, row["state"][:3], fontsize=8)

    
Text(57.7, 38.300000000000004, 'And')
Text(59.0, 36.5, 'And')
Text(40.5, 24.099999999999998, 'Aru')
Text(66.10000000000001, 15.399999999999999, 'Ass')
Text(63.7, 16.1, 'Bih')
Text(60.5, 44.2, 'Cha')
Text(61.0, 14.299999999999999, 'Chh')
Text(62.7, 27.0, 'Dad')
Text(39.2, 36.300000000000004, 'Goa')
Text(65.2, 22.8, 'Guj')
Text(60.6, 33.300000000000004, 'Har')
Text(53.2, 30.599999999999998, 'Him')
Text(57.2, 24.2, 'Ind')
Text(66.10000000000001, 29.5, 'Jam')
Text(65.5, 12.1, 'Jha')
Text(48.0, 30.3, 'Kar')
Text(36.5, 38.300000000000004, 'Ker')
Text(93.0, 28.5, 'Lad')
Text(26.0, 33.7, 'Lak')
Text(54.900000000000006, 16.8, 'Mad')
Text(54.400000000000006, 23.599999999999998, 'Mah')
Text(29.599999999999998, 34.300000000000004, 'Man')
Text(54.0, 11.7, 'Meg')
Text(35.0, 24.4, 'Miz')
Text(50.1, 41.5, 'NCT')
Text(29.099999999999998, 14.6, 'Nag')
Text(64.5, 23.2, 'Odi')
Text(55.300000000000004, 46.400000000000006, 'Pud')
Text(58.900000000000006, 41.0, 'Pun')
Text(54.6, 13.1, 'Raj')
Text(42.300000000000004, 34.900000000000006, 'Sik')
Text(53.6, 40.6, 'Tam')
Text(57.800000000000004, 30.3, 'Tel')
Text(67.4, 21.7, 'Tri')
Text(50.6, 21.5, 'Utt')
Text(42.800000000000004, 29.9, 'Utt')
Text(71.60000000000001, 22.9, 'Wes')
plt.xlabel("Anaemia in Women (%)")
Text(0.5, 0, 'Anaemia in Women (%)')
plt.ylabel("Obesity in Women (%)")
Text(0, 0.5, 'Obesity in Women (%)')
plt.title("Anaemia vs Obesity in Women (State-wise)")
Text(0.5, 1.0, 'Anaemia vs Obesity in Women (State-wise)')
plt.tight_layout()
plt.show()
import folium
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
folium.Choropleth(
    geo_data=r"C:\Users\Lenovo\Downloads\india-composite.geojson",   # path or URL to GeoJSON
    data=df_pivot,
    columns=["state","Obesity_Women"],  # link your DataFrame
    key_on="feature.properties.ST_NM",  # depends on GeoJSON field name
    fill_color="YlOrRd",
    legend_name="Obesity in Women (%)"
).add_to(m)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1683, in __init__
    self.geojson = GeoJson(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 738, in __init__
    self._validate_function(style_function, "style_function")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 813, in _validate_function
    if not callable(func) or not isinstance(func(test_feature), dict):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1663, in style_function
    color, opacity = color_scale_fun(x)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1635, in color_scale_fun
    raise ValueError(f"key_on `{key_on!r}` not found in GeoJSON.")
ValueError: key_on `'properties.ST_NM'` not found in GeoJSON.
import json
with open(r"C:\Users\Lenovo\Downloads\india-composite.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)

    
print(geo["features"][0]["properties"])
{}
folium.Choropleth(
    geo_data=r"C:\Users\Lenovo\Downloads\india-soi.geojson",  # <-- use state boundaries file
    data=df_pivot,
    columns=["state","Obesity_Women"],
    key_on="feature.properties.NAME_1",   # property for state names
    fill_color="YlOrRd",
    legend_name="Obesity in Women (%)"
).add_to(m)
m.save("NFHS5_dashboard.html")
SyntaxError: multiple statements found while compiling a single statement
folium.Choropleth(
    geo_data=r"C:\Users\Lenovo\Downloads\india-soi.geojson",  # <-- use state boundaries file
    data=df_pivot,
    columns=["state","Obesity_Women"],
    key_on="feature.properties.NAME_1",   # property for state names
    fill_color="YlOrRd",
    legend_name="Obesity in Women (%)"
).add_to(m)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1683, in __init__
    self.geojson = GeoJson(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 738, in __init__
    self._validate_function(style_function, "style_function")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 813, in _validate_function
    if not callable(func) or not isinstance(func(test_feature), dict):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1663, in style_function
    color, opacity = color_scale_fun(x)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1635, in color_scale_fun
    raise ValueError(f"key_on `{key_on!r}` not found in GeoJSON.")
ValueError: key_on `'properties.NAME_1'` not found in GeoJSON.
folium.Choropleth(
    geo_data="https://raw.githubusercontent.com/udit-001/india-maps-data/main/geojson/india.geojson",
    data=df_pivot,
    columns=["state","Obesity_Women"],
    key_on="feature.properties.NAME_1",   # this is the property for state names
    fill_color="YlOrRd",
    legend_name="Obesity in Women (%)"
).add_to(m)

m.save("NFHS5_dashboard.html")
SyntaxError: multiple statements found while compiling a single statement
folium.Choropleth(
    geo_data="https://raw.githubusercontent.com/udit-001/india-maps-data/main/geojson/india.geojson",
    data=df_pivot,
    columns=["state","Obesity_Women"],
    key_on="feature.properties.NAME_1",   # this is the property for state names
    fill_color="YlOrRd",
    legend_name="Obesity in Women (%)"
).add_to(m)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1683, in __init__
    self.geojson = GeoJson(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 738, in __init__
    self._validate_function(style_function, "style_function")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 813, in _validate_function
    if not callable(func) or not isinstance(func(test_feature), dict):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1663, in style_function
    color, opacity = color_scale_fun(x)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\folium\features.py", line 1635, in color_scale_fun
    raise ValueError(f"key_on `{key_on!r}` not found in GeoJSON.")
ValueError: key_on `'properties.NAME_1'` not found in GeoJSON.
import requests
geo = requests.get("https://raw.githubusercontent.com/udit-001/india-maps-data/main/geojson/india.geojson").json()
print(geo["features"][0]["properties"])
SyntaxError: multiple statements found while compiling a single statement
geo = requests.get("https://raw.githubusercontent.com/udit-001/india-maps-data/main/geojson/india.geojson").json()
print(geo["features"][0]["properties"])
{'district': 'Aizawl', 'dt_code': '261', 'st_nm': 'Mizoram', 'st_code': '15', 'year': '2011_c'}
folium.Choropleth(
    geo_data="https://raw.githubusercontent.com/udit-001/india-maps-data/main/geojson/india.geojson",
    data=df_pivot,
    columns=["state","Obesity_Women"],
    key_on="feature.properties.st_nm",   # <-- use st_nm
    fill_color="YlOrRd",
    legend_name="Obesity in Women (%)"
).add_to(m)
<folium.features.Choropleth object at 0x000002896A81B9B0>
m.save("NFHS5_dashboard.html")

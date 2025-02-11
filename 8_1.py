import pandas as pd
from matplotlib import pyplot as plt
df_score=pd.read_excel("histograms.xlsx")
print(df_score)
import seaborn as sns
sns.histplot(df_score["Exam_Score"],kde=True)
plt.show()
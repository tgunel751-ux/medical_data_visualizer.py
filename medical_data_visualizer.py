import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv')
df.shape
df.info()
df.describe()
def overweight(x):
    BMI= x["weight"]/((x["height"]/100)**2)
    if  BMI>25:
        return 1
    else:
        return 0
df["overweight"]= df.apply(overweight,axis=1)
df["cholesterol"]=(df["cholesterol"]>1).astype(int)
df["gluc"]=(df["gluc"]>1).astype(int) 
df_cat=pd.melt(
    df,
    id_vars="cardio",
    value_vars=["cholesterol","gluc","smoke","alco","active","overweight"]

)    
df_cat=(
   df_cat.value_counts()
   .reset_index(name="total")
)
fig=(sns.catplot(x="variable",y="total" ,hue="value",col="cardio",kind="bar",data=df_cat
))
plt.show()
df_heat=df[(df["ap_lo"]<=df["ap_hi"])&(df["height"]>=df["height"].quantile(0.025))&(df["height"]<=df["height"].quantile(0.975))&(df["weight"]<=df["weight"].quantile(0.975))&(df["weight"]>=df["weight"].quantile(0.025))]
corr=df_heat.corr()
mask=np.triu(np.ones_like(corr,dtype=bool))
fig,ax=plt.subplots(figsize=(12,8))
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".1f",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink":0.5},
    ax=ax,
)
plt.show()


   
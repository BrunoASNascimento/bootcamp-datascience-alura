import pandas as pd

PATH= 'data/Kaggle_Sirio_Libanes_ICU_Prediction.xlsx'

df = pd.read_excel(PATH)
df.to_csv(f'{PATH.split(".")[0]}.csv')


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def printd(var, step):
    print(f"\n//--------------------------/{str(step)}/--------------------------//\n")
    print(var)
    print("\n//--------------------------//--------------------------//\n")

# 1
df = pd.read_csv('medical_examination.csv')

printd(df.head(), 1)

# 2
df['bmi'] = df['weight'] / ((df['height']/100) ** 2)
print("DONE")

df['overweight'] = (df['bmi'] > 25).astype(int)
print("DONE")

printd(df.head(), 2)

# 3

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
print("DONE")

df['gluc'] = (df['gluc'] > 1).astype(int)
print("DONE")


printd(df.head(), 3)

#5
df_cat = pd.melt(df, 
                
                id_vars=['cardio'],

                value_vars=['cholesterol', 'gluc', 'smoke', 'alco','active', 'overweight'],

                var_name='variables',

                value_name='value'
                )

printd(df_cat, 5)

# 6
df_cat = df_cat.groupby(['cardio', 'variables', 'value']).size().reset_index(name='total')
printd(df_cat, 6)

# 7
fig = sns.catplot(data=df_cat,
                  x='variables',
                  y='total',
                  hue='value',
                  col='cardio',
                  kind='bar',
                  height=6,          # Height of each panel
                  aspect=1.2         # Width-to-height ratio
                  )

plt.show()


# 4
def draw_cat_plot():



    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

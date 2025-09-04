import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['bmi'] = df['weight'] / (df['height'] ** 2)
df['overweight'] = 1 if df['bmi'] > 25 else 0

# 3
    # 0 good / 1 bad
df['cholesterol'] = 0 if df['cholesterol'] == 1 else 1
df['gluc'] = 0 if df['gluc'] == 1 else 1

# 4
def draw_cat_plot():

    # Creates an image with one graph (subplot)
    fig, ax = plt.subplots(figsize=(10, 6))


    sns.barplot(data=df, x='category', y='value', 
                
                hue='group', # Creates grouped/clustered bars based on the 'group' column
                ax=ax #Tells seaborn to draw on the specific axes object created above
                )

    # 5
    df_cat = pd.melt(df, 
                    value_vars=['cholesterol', 'gluc', 'smoke', 'alco',
                    'active', 'overweight'],
                    value_name='variables'
                    )


    # 6
    df_cat = None
    

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

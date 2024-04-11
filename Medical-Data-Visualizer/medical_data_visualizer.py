import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

def calc_overweight(bmi):
    if(bmi > 25):
        # is over weight
        return 1
    else:
        # not over weight
        return 0

def normalize(level):
    if level == 1:
        return 0
    elif level > 1:
        return 1

# Add 'overweight' column
height_in_meter = df['height'] * 0.01
bmi = df['weight'] / np.square(height_in_meter)

df['overweight'] = bmi.apply(calc_overweight)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(normalize)
df['gluc'] = df['gluc'].apply(normalize)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).size().rename(columns={'size' : 'total'}) # in long format

    # Draw the catplot with 'sns.catplot()'
    # hue = creates sub-group based on unique values
    # col = create seperate plots based on unique values
    fig = sns.catplot(data=df_cat, x='variable', y='total', kind='bar', hue='value', col='cardio').fig

    # Get the figure for the output
    # fig = plot.figure()

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                (df['height'] >= df['height'].quantile(0.025)) &
                (df['height'] <= df['height'].quantile(0.975)) &
                (df['weight'] >= df['weight'].quantile(0.025)) &
                (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt="0.1f", square=True, linewidths=0.5)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

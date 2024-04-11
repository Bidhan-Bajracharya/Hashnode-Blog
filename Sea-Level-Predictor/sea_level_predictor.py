import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s = 5)

    # Create first line of best fit
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    first_years = pd.Series(range(1880, 2051)) # x1
    y_pred = fit1.intercept + fit1.slope * first_years # y1
    plt.plot(first_years, y_pred, color='red')


    # Create second line of best fit
    df2 = df[df['Year'] >= 2000 ]
    
    fit2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    second_years = pd.Series(range(2000,2051)) # x2
    y_pred2 = fit2.intercept + fit2.slope * second_years # y2
    
    plt.plot(second_years, y_pred2, color='green')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date" , parse_dates=True)

# Clean data
bottom_threshold = df['value'].quantile(0.025)
top_threshold = df['value'].quantile(0.975)

df = df[(df['value'] > bottom_threshold) & (df['value'] < top_threshold)]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df,color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    
    # month order for df
    custom_month_order = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]
    
    # getting year and month (January, February, ..., December) from dateTime
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # arranging the month
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=custom_month_order, ordered=True)
    
    # average daily page view for each month grouped by year
    avg_grouped = df_bar.groupby(['year', 'month'])['value'].mean().reset_index(name='Average Page Views')
    
    # arranging data for the plot
    pivot_avg = avg_grouped.pivot(index='year', columns='month', values='Average Page Views')

    # Draw bar plot
    fig = pivot_avg.plot(kind='bar',figsize=(10, 6)).get_figure()
    plt.legend(title='Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # month order for plotting
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    fig = plt.figure(figsize=(14,6))

    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=month_order)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

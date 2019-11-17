# %% Define library imports
# Data wrangling
import pandas as pd

# Data modeling
from sklearn.ensemble import RandomForestClassifier

# Data visualisation
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


# %% Import data
df = pd.read_csv('multicollinearity/Data.csv', na_values='..')[:-5]


# %% Do basic cleaning of the data
# Drop uneeded columns
df = df.drop(['Country Name', 'Country Code', 'Series Code'], axis=1)

# Drop parameters with NaNs for all years
df = df.dropna(how='all', subset=df.columns[1:])
# Drop years with NaNs for all parameters
df = df.dropna(how='all', axis=1)

# %% Investigating the percentage of missing values per parameter
# Create the figure and the axes
fig, ax = plt.subplots(figsize=(15, 200))
# Calculate the percentages of non NaNs per param and create base bar plot
(df.notna().sum(axis=1) / len(df.columns)).sort_values().plot.barh(ax=ax)
# Set limits and labels
ax.set_xlim([0, 1])
ax.set(
    title='Percentage of non-missing values per parameter',
    xlabel='Non-missing values (%)',
    ylabel='Parameter index'
)
# Add lines for 50, 75, 90, 95, 99 percent
plt.axvline(x=0.50, color='red', linestyle='--', label='50%')
plt.axvline(x=0.75, color='red', linestyle='--', label='75%')
plt.axvline(x=0.90, color='red', linestyle='--', label='90%')
plt.axvline(x=0.95, color='red', linestyle='--', label='95%')
plt.axvline(x=0.99, color='red', linestyle='--', label='99%')
# Format the x-axis
ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
# Hide the legend
ax.legend().set_visible(False)


# %% Dropping parameters with too many NaNs
print(
    f'Setting threshold at more than 90% valid values keeping '
    + f'{len(df[(df.notna().sum(axis=1)/len(df.columns))>=0.9])/len(df):.2f}'
    + f'% of original parameters.'
)
df = df[(df.notna().sum(axis=1)/len(df.columns))>=0.9]


# %% Investigating the percentage of missing values per year
# Create the figure and the axes
fig, ax = plt.subplots(figsize=(15, 7))
# Calculate the percentages of non NaNs per year and create base bar plot
sdf = df.loc[:, '1970 [YR1970]':]
(sdf.notna().sum(axis=0) / len(sdf.index)).plot.bar(ax=ax)
# Set limits and labels
ax.set_ylim([0, 1])
ax.set(
    title='Percentage of non-missing values per year',
    ylabel='Non-missing values (%)',
    xlabel='Year'
)
# Add lines for 50, 75, 90, 95, 99 percent
plt.axhline(y=0.50, color='red', linestyle='--', label='50%')
plt.axhline(y=0.75, color='red', linestyle='--', label='75%')
plt.axhline(y=0.90, color='red', linestyle='--', label='90%')
plt.axhline(y=0.95, color='red', linestyle='--', label='95%')
plt.axhline(y=0.99, color='red', linestyle='--', label='99%')
# Format the x-axis
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
# Hide the legend
ax.legend().set_visible(False)

# %% Keeping years between 1975 and 2015
df = df.drop(
    [
        '1970 [YR1970]', 
        '1971 [YR1971]',
        '1972 [YR1972]',
        '1973 [YR1973]',
        '1974 [YR1974]',
        '2016 [YR2016]',
        '2017 [YR2017]',
        '2018 [YR2018]',
        '2019 [YR2019]'
    ],
    axis=1
)

# %% Investigate the NaNs in remaining columns


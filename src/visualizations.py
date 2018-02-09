
'''
Since I will be building a model to predict churn, I first had to create a column
for our target variable. To create our target variable, I had to change the date
strings to datetime types, and then create a column that indicated whether or not
a customer had churned based on if their last trip date was before or after June 1st 2014,
which is 30 days prior to the gathering of the data.  I then visualized the data
to find patterns amongst the features. Using seaborn, I created violin plots that
tells us that there are more outliers in the active population for distance traveled(they
stay active because they appreciate it in a bind when taking that round trip from
Denver to Grand Junction for a Tinder date). We also saw that the inactive members
are not necessarily inactive because of a dissatisfaction with their driver or a
poor rating by their driver.  There are more outliers in the inactive for avg_surge,
which goes to show maybe they only used it in a bind, while active are more likely
to use the company during a surge. Active members love it, especially outliers,
who took 120 trips in the first 30 days. We noticed that inactive members were
much more likely to use it only during the weekdays or only during the weekends;
we figured they might be inactive since they only used it when other transportation
was down.  With the categorical countplots we figured that our company might want
to reach out to Android users because of their little use.  We also want to know
what's going on in King's Landing that makes their population so active.  For luxury
car use, we might want to incentivize luxury car users.  Take a look!
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import seaborn as sns

def add_target_clean(df):
    active_date = date(2014,6,1)
    df['last_trip_date'] = pd.to_datetime(df['last_trip_date'])
    df['signup_date'] = pd.to_datetime(df['signup_date']) #after looking at this, we decided it wasn't relevant to churn so we dropped it
    df['active'] = (df['last_trip_date'] > active_date).astype(int)
    df['iPhone'] = (df['phone'] == 'iPhone').astype(int)
    df['luxury_car_user'] = df['luxury_car_user'].astype(int)
    df.drop(['signup_date', 'last_trip_date', 'phone'], axis = 1, inplace = True)
    return df

def plot_quantitative_violinplot(df):
    df_num_columns = df.select_dtypes(include=[np.number])
    df_boxplot_columns = [column for column in df_num_columns if column not in ['active', 'iPhone', 'luxury_car_user']]
    fig = plt.figure(figsize=(15,6))
    for ind, column in enumerate(df_boxplot_columns):
        ax = fig.add_subplot(1,len(df_boxplot_columns),ind+1)
        ax = sns.violinplot(x = df['active'], y = df[column], data = df)
        ax.yaxis.label.set_visible(False)
        ax.get_figure().gca().set_title(column)
    plt.tight_layout()
    plt.show()

def plot_categorical_countplot(df, column):
    fig = plt.figure(figsize=(15,6))
    ax = fig.add_subplot(1,1,1)
    ax = sns.countplot(x = df[column], hue = df['active'], data = df)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    #df = pd.read_csv('data/churn.csv')
    #df_test = pd.read_csv('data/churn_test.csv')
    df_train = pd.read_csv('data/churn_train.csv')
    df_train = add_target_clean(df_train)
    #df_test = clean_data_mine(df_test)
    plot_quantitative_violinplot(df_train)
    plot_categorical_countplot(df_train, 'iPhone')
    plot_categorical_countplot(df_train, 'city')
    plot_categorical_countplot(df_train, 'luxury_car_user')

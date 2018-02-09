'''
We found there were a large number of nulls, especially in the rating columns, which
makes sense considering riders are not required to rate their drivers.  We decided
to fill them using MICE, from the fancyimpute library; MICE is an iterative algorithm
based on chained equations that uses an imputation model specified separately for
each variable and involving the other variables and predictors.  MICE has shown to
be a better method for filling nulls than just replacing the nulls with the mean.
We then decided to check the average cross validation scores on many popular algorithms
that we thought would be relevant considering the data. We got the average cross
validation scores of:
                        CVMean       Std
XGBClassifier        0.791850  0.006198
Linear SVC           0.728150  0.005835
Gradient Boosting    0.791000  0.005973
Logistic Regression  0.726550  0.004853
KNN                  0.761575  0.006027
Decision Tree        0.708250  0.005560
Naive Bayes          0.705750  0.005501
Random Forest        0.759600  0.005947

The XGBClassifier shows to have the highest average accuracy so we will continue
with the XGBClassifier as our model; we also like the XGBClassifier since it includes
regression penalties for features that don't have much of an effect.  To make our
model even better, we will look at how changing hyperparameters
could improve our model.  We did a gridsearch to determine our best hyperparameters.
'''

import pandas as pd
import numpy as np
from datetime import date
from sklearn.preprocessing import StandardScaler
from fancyimpute import MICE
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier


def clean_fill_nulls(df):
    active_date = date(2014,6,1)
    df['last_trip_date'] = pd.to_datetime(df['last_trip_date'])
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    #df['iPhone'] = (df['phone'] == 'iPhone').astype(int)
    df['luxury_car_user'] = df['luxury_car_user'].astype(int)
    df['active'] = (df['last_trip_date'] > active_date).astype(int)
    df.drop(['signup_date', 'last_trip_date'], axis = 1, inplace = True)
    df = pd.get_dummies(df, columns=['city', 'phone'])

    #y = df.pop('active').values
    array = df.values.astype(float)
    array_filled_mice = MICE(n_imputations=6700).complete(array)
    scaler = StandardScaler()
    array_filled_mice = scaler.fit_transform(array_filled_mice)
    columns = ['avg_dist', 'avg_rating_by_driver', 'avg_rating_of_driver',
    'avg_surge', 'surge_pct', 'trips_in_first_30_days', 'luxury_car_user',
    'weekday_pct', 'active', 'city_Astapor', "city_King's Landing", 'city_Winterfell',
    'phone_Android', 'phone_iPhone']
    return pd.DataFrame(array_filled_mice, columns = columns)

def get_cross_val_simple_models(df):
    kfold = KFold(n_splits=10, random_state=22) #splits data into 10 parts
    xyz = []
    accuracy = []
    std = []
    classifiers = ['XGBClassifier', 'Linear SVC', 'Gradient Boosting', 'Logistic Regression', 'KNN', 'Decision Tree', 'Naive Bayes',
    'Random Forest']
    models = [XGBClassifier(), LinearSVC(), GradientBoostingClassifier(),LogisticRegression(),KNeighborsClassifier(n_neighbors=9),
    DecisionTreeClassifier(),GaussianNB(), RandomForestClassifier()]
    y = df.pop('active').values.astype(int)
    X = df.values.astype(float)
    for idx, i in enumerate(models):
        model = i
        cv_result = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
        xyz.append(cv_result.mean())
        std.append(cv_result.std())
        accuracy.append(cv_result)
        #print ('Done with {0}'.format(classifiers[idx]))
    cross_val_df = pd.DataFrame({'CVMean':xyz, 'Std':std}, index = classifiers)
    return cross_val_df

def get_parameters(df):
    y = df.pop('active').values.astype(int)
    X = df.values.astype(float)
    model = XGBClassifier()
    param = {'n_estimators':[50,100,150,200, 1000],'max_depth':[2,3,4,5,6,7,8,9],
     'min_child_weight':[1,2,3,4,5],'colsample_bytree':[0.2,0.6,0.8],
     'colsample_bylevel':[0.2,0.6,0.8], 'gamma':[2,3,4], 'learning_rate':[.01, .05, .1],
     'reg_alpha':[.3,.4,.5], 'reg_lambda':[.6, .7, .8, .9], 'subsample':[.4,.5,.6]}
    gsearch = GridSearchCV(estimator = XGBClassifier(objective = 'reg:linear', seed = 1),
    param_grid = param, scoring = 'accuracy', cv = 3, verbose = 1)
    gsearch.fit(X,y)
    return gsearch.best_score_, gsearch.best_params_


def XGB_model(df):
    y = df.pop('active').values.astype(int)
    X = df.values.astype(float)
    model = XGBClassifier(colsample_bytree=0.55, gamma=3, learning_rate=0.05,
    max_depth=3, min_child_weight=1.5, n_estimators=2200, reg_alpha=0.4640,
    reg_lambda=0.8571, subsample=0.5213, silent=1, nthread = -1, seed=5)
    model.fit(X, y)
    return (np.mean(cross_val_score(model, X, y)))

if __name__ == '__main__':
    #df = pd.read_csv('data/churn.csv')
    df_train = pd.read_csv('data/churn_train.csv')
    cleaned_train = clean_fill_nulls(df_train)
    #print (get_cross_val_simple_models(df_train))
    #print (XGB_model(cleaned_train)) #0.796574989746
    #WATCH OUT, THIS TAKES TOO LONG, YOU SHOULD DO EACH ONE BY HAND, OR NOT HAVE SO MANY PARAMETERS
    print (get_parameters(cleaned_train))

    #df_test = pd.read_csv('data/churn_test.csv')
    #df_test = clean_fill_nulls(df_test)

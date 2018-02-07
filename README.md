# Predicting Customer Retention Case Study

# Table of contents
1. [Motivation](#motivation)
2. [Data](#data)
3. [Feature Engineering](#feature_engineering)
4. [Exploratory Data Analysis](#EDA)
5. [Recommender Methods](#methods)
6. [Feature Importance](#featureimportance)
7. [Future Direction](#futuredirection)
8. [References](#references)


## Motivation <a name="motivation"></a>

This project was done as a case study while I was a Data Science Immersive student
at Galvanize in Denver, CO.  The objective was to create a model that would predict
customer retention for a ride-sharing company using their data on users
provided over a six month period.  Using the model, I was tasked with determining
which features were most influential in loss of retention and then making a plan
for how the company could use this information to increase retention.


## Data <a name="data"></a>

Here is a detailed description of the data received on each user:

* `city`: city this user signed up in phone: primary device for this user
* `signup_date`: date of account registration; in the form `YYYYMMDD`
* `last_trip_date`: the last time this user completed a trip; in the form `YYYYMMDD`
* `avg_dist`: the average distance (in miles) per trip taken in the first 30 days after signup
* `avg_rating_by_driver`: the rider’s average rating over all of their trips
* `avg_rating_of_driver`: the rider’s average rating of their drivers over all of their trips
* `surge_pct`: the percent of trips taken with surge multiplier > 1
* `avg_surge`: The average surge multiplier over all of this user’s trips
* `trips_in_first_30_days`: the number of trips this user took in the first 30 days after signing up
* `luxury_car_user`: TRUE if the user took a luxury car in their first 30 days; FALSE otherwise
* `weekday_pct`: the percent of the user’s trips occurring during a weekday


## Feature Engineering <a name="feature_engineering"></a>

The data was pulled on July 1, 2014; it captures a six month period for users who
created an account in January 2014.  The company considers a user retained, or active,
if they used the ride-sharing company anytime in the 30 days before the data was
pulled; otherwise, the user is considered inactive, and not retained as a customer.  

Since I will be building a model to predict retention, I first had to create a column
for our target variable. To create our target variable, I had to change the date
strings to datetime types, and then create a column that indicated whether or not
a customer had churned based on if their last trip date was before or after June
1st 2014, which is 30 days prior to the gathering of the data.  


## Exploratory Data Analysis through Visualizations and Maps <a name="EDA"></a>

I knew that visualizing the data would help me to find patterns amongst the features.
Using seaborn, I created violin plots that tell us that there are more outliers
in the active population for distance traveled.  These users most likely stay active
because they can use the ride-sharing company when on a business trip that requires
the user to fly into a distant airport.  We also saw that the inactive members are
not necessarily inactive because of a dissatisfaction with their driver or a
poor rating by their driver.  There are more outliers in the inactive for avg_surge,
which goes to show maybe they only used it in a bind, while active users are more likely
to use the company during a surge. Active members use the service often, especially
the outliers, who took 120 trips in the first 30 days. We noticed that inactive
members weremuch more likely to use it only during the weekdays or only during the weekends;
we figured they might be inactive since they only used it when other transportation
was not available.   

![Violin Plots of Features](images/violin_plots_active_inactive1.png)

With the categorical countplots we figured that our company might want
to reach out to Android users because of their little use.  

![Count Plot for iPhone versus Android](images/count_plots_iphone1.png)

We also want to know what's going on in King's Landing that makes their population
so active.  

![Count Plot Depending on City](images/count_plots_city1.png)

For luxury car use, we might want to incentivize luxury car users.

![Count Plot Depending on Luxury Usage](images/count_plots_luxury_car1.png)

## Methods <a name="methods"></a>

## Feature Importance <a name="featureimportance"></a>

## Future Direction <a name="futuredirection"></a>

- A presentation including the following points:
  - How did you compute the target?
  - What model did you use in the end? Why?
  - Alternative models you considered? Why are they not good enough?
  - What performance metric did you use to evaluate the *model*? Why?
  - Based on insights from the model, what actionable plans do you propose to
    reduce churn?
  - What are the potential impacts of implementing these plans or decisions?
    What performance metrics did you use to evaluate these *decisions*, why?

## References <a name="references"></a>

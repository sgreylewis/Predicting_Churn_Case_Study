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
for our target variable of retention that indicated whether or not a customer was
active based on if their last trip date was before or after June 1st, 2014.  


## Exploratory Data Analysis through Visualizations <a name="EDA"></a>

I knew that visualizing the data would help me to find patterns amongst the features.
The first violin plot in the diagram below tells us that there are more outliers in the active population for average distance traveled; these users potentially
stay active because they can use the ride-sharing company when on a business trip
that requires the user to fly into a distant airport.  In the second and third plots,
you can see that the inactive members are not necessarily inactive because of a dissatisfaction with their driver or a poor rating by their driver.  In the fourth
plot, there are more outliers amongst the inactive users for avg_surge(the average
surge level ridden duing a surge time); this suggests those customers only used
it in a bind, as most active users avoid riding when there's a high surge;
still the fifth plot shows that active users on average had a higher
percentage of surge rides than inactive users.  The sixth plot tells us that the
active members use the service often, especially the outliers, who took 120 trips
in the first 30 days. In the seventh plot, I noticed that inactive members were much more likely to use it only during the weekdays or only during the weekends; one can imagine that they might be inactive since they only used it when other transportation was not available.   

![Violin Plots of Features](images/violin_plots_active_inactive1.png)


You can see in the countplot below, the population of people using the service mostly have iPhones; Android users aren't using the service either because it's not easy
to access on an Android, not well marketed to Android users, or simply because more people have iPhones than Androids.  

![Count Plot for iPhone versus Android](images/count_plots_iphone1.png)


The real names of the cities in our data were replaced in order to conceal identity; still you can see from the countplot below that King's Landing is having much greater success in retaining its users than Astapor and Winterfell, even though the latter cities had many more users over the past six months.  To better understand why Astapor only retained about 25% of their customers from the past six months, we'd need take
a closer look at the demographics of Astapor and the ride-sharing marketing strategies
 in that city compared to King's Landing.  

![Count Plot Depending on City](images/count_plots_city1.png)


The plot below shows that half of the users who were luxury car users are now inactive,
while 70% of the users who were not luxury car users are now inactive.

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

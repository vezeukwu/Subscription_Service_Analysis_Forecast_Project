## Data Quality Check and Pattern Recognition

#importing the libraries to work with
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
d1 = pd.read_csv("actions2load.csv")
d1

#I'm trying to copy the original dataset given with only columns that have object types
obj_d1 = d1.select_dtypes(include=['object']).copy()
obj_d1.head()

#I'm trying to clean up null values in the dataset given, so this code below calls up all the rows with NAN
obj_d1[obj_d1.isnull().any(axis=1)]

#Checking to know the value with the most count. I need this to fill up the NAN columns
obj_d1["additional_data"].value_counts()

#I replaced the NAN values with "https://www.google.com/" which is the most common value in the additional data column
obj_d1 = obj_d1.fillna({"additional_data": "https://www.google.com/"})
obj_d1

#I checked to see if there are still any missing values
obj_d1.isnull().sum()

#im trying to use label encoding method to convert the values in event_type to numbers. So first i changed the data type of event_type to category
obj_d1["event_type"] = obj_d1["event_type"].astype('category')
obj_d1.dtypes

#then i assigned the encoded variable to a new column
obj_d1["event_type_cat"] = obj_d1["event_type"].cat.codes
obj_d1.head()

#im trying to use label encoding method to convert the values in account_id to numbers. So i also changed the data type of account_id to category

obj_d1["account_id"] = obj_d1["account_id"].astype('category')
obj_d1.dtypes

#then i assigned the encoded variable to a new column
obj_d1["account_id_cat"] = obj_d1["account_id"].cat.codes
obj_d1.head()

## QUESTION 4:  Are there any extreme outliers (class imbalances) in the number of events?

#im trying to identify outliers
round(obj_d1.describe(), 3)

#Checking the distribution of the event_type variable. The histogram below is not skewed either to the left or right.
obj_d1.hist(figsize=(12, 10), bins=30, edgecolor = 'black')
plt.subplots_adjust(hspace=0.7, wspace=0.4)

#The difference between the 75% and max is not so high, so its not confiming the presence of outliers. 
#There are no potential outliers in the dataset.

#boxplot to examine outliers
import seaborn as sns
sns.boxplot(y=obj_d1['event_type_cat'])
plt.title('Boxplot')

## QUESTION 1:  Do events happen equally at different times of the day or are there patterns (give visualizations)?

#Confirming event_time data type is integer
obj_d1['event_time'].value_counts()

#converting the event_time integer data type to datetime format
obj_d1['event_time'] = pd.to_datetime(obj_d1['event_time'])
obj_d1['event_time']

#i used the code below to extract only the dates from the event_time column
obj_d1['event_date'] = obj_d1['event_time'].dt.date
obj_d1

#i used the code below to extract only the time from the event_time column
obj_d1['time_of_event'] = obj_d1['event_time'].dt.time
obj_d1

# i used the code below to extract the hour from the event_time column
obj_d1['event_hour'] = obj_d1['event_time'].dt.hour
obj_d1

obj_d1.info()

#Calculate the time intervals between events
obj_d1['Interval'] = obj_d1['event_time'].diff()
obj_d1['Interval']

# Calculate the mean, median, and standard deviation of the time intervals
mean_interval = obj_d1['Interval'].mean()
mean_interval

median_interval = obj_d1['Interval'].median()
std_interval = obj_d1['Interval'].std()

print('Mean interval:', mean_interval)
print('Median interval:', median_interval)
print('Standard deviation of interval:', std_interval)

#This indicates that the time intervals between event_types are relatively consistent, with a mean and median interval of 
#0 days00:00:05.001428133 and 0 days 00:00:02.328000 respectively and a standard deviation of 0 days 00:00:07.821278603. This 
#suggests that events are occurring equally at different times because the mean and median are not significantly different.

##VISUALIZATION

hourly_event = obj_d1.groupby('event_hour').size().reset_index(name='count')
hourly_event

# Create a bar chart of event frequency by hour of the day
plt.bar(hourly_event['event_hour'], hourly_event['count'])
plt.title('Frequency of events by hour of the day')
plt.xlabel('Hour of the day')
plt.ylabel('Number of events')
plt.show()

## QUESTION 3: Are there any gaps (missing data) in the record of any events?

obj_d1["event_type"].isnull().sum()

#There seems to be no missing data in the events record

## QUESTION 2: Analyze “a particular account_id” for insights on how the person uses the service at different times of the day (Visualizations)

# Filter the DataFrame to only include rows with the desired account ID
account_id = '89f7601cb558e1c47b00a7fabb6a466c'
filtered_obj_d1 = obj_d1[obj_d1['account_id'] == account_id]
filtered_obj_d1

# Extracting the relevant components for the selected account id
components = filtered_obj_d1[['event_type', 'event_time']]

# Plotting a bar chart of the components
components.plot(kind='bar')
plt.title('Components for Account ID {}'.format(account_id))
plt.xlabel('Component')
plt.ylabel('Value')
plt.show()

#Account id 89f7601cb558e1c47b00a7fabb6a466c uses the different services at almost same time of the day.
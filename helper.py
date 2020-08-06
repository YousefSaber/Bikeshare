import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (df, new york city, washington). we will use recursive functions to handle invaild inputs 
    city = input( "Choose the city to display its stats data (Your Options are `chicago`,`new york`,`washington`)\n ")
    city = city.lower() #handle upper casses character
    # get user input for month (all, january, february, ... , june)
    month = int(input("choose which month to filter data by your choices are (e.g., 1=Jan,....,12=Dec,13=All\n"))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = int(input("choose which day of week you want to filter your data by (e.g.,1=Saturday,2=sunday,.....,8=all\n"))

    if city not in ["chicago","new york","washington"]:   # we handle the errors here by recursions
        print("Invalid city")
        city, month, day = get_filters()
    if month not in range(1,14,1):
        print("invalid month int input")
        city, month, day = get_filters()

    if day not in range(1,9,1):
        print("Invalid int day input")
        city, month, day = get_filters()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
         city - name of the city to analyze
         month - name of the month to filter by, or "all" to apply no month filter
         day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    calendar.setfirstweekday(calendar.SATURDAY)

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    # filtering data 
    if month == 13 and day == 8:
        return df
    if month < 13 and day == 8 :  # notice that if the user chooses 8 then we won't filter because he choosed to show the data for all days the same applies to months with no 13
        df =df[(df["Start Time"].dt.month == month)]
        return df
    if month == 13 and day < 8:
        df =df[(df["Start Time"].dt.day == day)]
        return df
    if month < 13 and day < 8:
        df =df[(df["Start Time"].dt.month == month) & (df["End Time"].dt.dayofweek == day)]
        return df
        print(df)
        return df 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # display the most common month
    Most_Common_Month = df["Start Time"].dt.month.mode()
    month = calendar.month_name[Most_Common_Month[0]]
    Most_Common_Month_Count = df["Start Time"].dt.month.value_counts(sort = True)
    Most_Common_Month_Count = Most_Common_Month_Count.iloc[0] 
    print("The most common month : {} , count : {}".format(month,Most_Common_Month_Count))

    # display the most common day of week
    Most_common_day_of_week = df["Start Time"].dt.dayofweek.mode()
    dayofweek = calendar.day_name[Most_common_day_of_week[0]]
    Most_common_day_of_week_count = df["Start Time"].dt.dayofweek.value_counts()
    Most_common_day_of_week_count = Most_common_day_of_week_count.iloc[0]
    print("The most common day of week : {} , count : {}".format(dayofweek,Most_common_day_of_week_count))

    # display the most common start hour
    Most_common_Hour = df["Start Time"].dt.hour.mode()
    Most_common_Hour_count = df["Start Time"].dt.hour.value_counts()
    Most_common_Hour_count = Most_common_Hour_count.iloc[0]
    print("The most common hour :{} , count : {}".format(Most_common_Hour[0],Most_common_Hour_count))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""


    # display most commonly used start station

    Most_common_start_station = df["Start Station"].mode()
    Most_common_start_station_count = df["Start Station"].value_counts()
    Most_common_start_station_count = Most_common_start_station_count.iloc[0]

    print("The most common start station : {}, count : {}".format(Most_common_start_station[0],Most_common_start_station_count))
    # display most commonly used end station

    Most_common_end_station = df["End Station"].mode()
    Most_common_end_station_count = df["End Station"].value_counts()
    Most_common_end_station_count = Most_common_end_station_count.iloc[0]

    print("The most common end station : {}, count : {}".format(Most_common_end_station[0],Most_common_end_station_count))

    # display most frequent combination of start station and end station trip

    most_start_finish = df.groupby(["Start Station","End Station"]).size().idxmax()
    most_start_finish_count =   df[["Start Station","End Station"]].value_counts(sort=True).iloc[0]

    print("The most frequent combination of start and finish station : {} and {}, count : {}".format(most_start_finish[0],most_start_finish[1],most_start_finish_count))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




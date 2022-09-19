import time
import pandas as pd
import numpy as np

"""
Read data and create columns Month, Day of Week and Hour for filtering data.
"""
chicago_data = pd.read_csv("D:/Udacity/Python for Data Science/Bikeshare/chicago.csv")
newyork_data = pd.read_csv("D:/Udacity/Python for Data Science/Bikeshare/new_york_city.csv")
washington_data = pd.read_csv("D:/Udacity/Python for Data Science/Bikeshare/washington.csv")

chicago_data['Start Time'] = pd.to_datetime(chicago_data['Start Time'])
newyork_data['Start Time'] = pd.to_datetime(newyork_data['Start Time'])
washington_data['Start Time'] = pd.to_datetime(washington_data['Start Time'])

chicago_data['Month'] = chicago_data['Start Time'].dt.month_name(locale = 'English')
newyork_data['Month'] = newyork_data['Start Time'].dt.month_name(locale = 'English')
washington_data['Month'] = washington_data['Start Time'].dt.month_name(locale = 'English')

chicago_data['Day_of_Week'] = chicago_data['Start Time'].dt.day_name()
newyork_data['Day_of_Week'] = newyork_data['Start Time'].dt.day_name()
washington_data['Day_of_Week'] = washington_data['Start Time'].dt.day_name()

chicago_data['Hour'] = chicago_data['Start Time'].dt.hour
newyork_data['Hour'] = newyork_data['Start Time'].dt.hour
washington_data['Hour'] = washington_data['Start Time'].dt.hour

CITY_DATA = { "chicago": chicago_data,
              "new york": newyork_data,
              "washington": washington_data}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    invalid_city = False
    cities = ['chicago', 'new york', 'washington']

    while invalid_city == False:
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        if city in cities:
            invalid_city = True
        else:
            print("Invalid city's name. \nPlease try again.")
            continue

    # get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    invalid_month = False
    
    while invalid_month == False:
        filter_by_month = input("Would you like to filter by day of month? \nPlease type 'yes' or 'no': ").lower()
        if filter_by_month == 'yes':
            month = input("Which month from January to June would you like to see the data? ").title()
            if month in months:
                break
            else:
                print("Invalid month.")
                continue
        elif filter_by_month == 'no':
            month = months[6]
            break
        else:
            print("Invalid input. Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    invalid_day = False

    while invalid_day == False:
        filter_day = input("Would you like to filter by day of week? \nPlease type 'yes' or 'no': ").lower()
        if filter_day == 'yes':
            day = input("Which day would you like to see the data? ").title()
            if day in days:
                break
            else:
                print("Invalid day.")
                continue
        elif filter_day == 'no':
            day = days[7]
            break
        else:
            print("Invalid day. Please try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filter_data = CITY_DATA[city]
    if month == 'All' and day == 'All':
        df = filter_data
    elif month == 'All' and day != 'All':
        df = filter_data[(filter_data['Day_of_Week'] == day)]
    elif day == 'All' and month != 'All':
        df = filter_data[(filter_data['Month'] == month)]
    elif month != 'All' and day != 'All':
        df = filter_data[(filter_data['Month'] == month) & (filter_data['Day_of_Week'] == day)]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is:\n', df["Month"].mode().iloc[0])

    # TO DO: display the most common day of week
    print('The most common day of week is:\n', df["Day_of_Week"].mode().iloc[0])

    # TO DO: display the most common start hour
    print('The most common start hour is:\n', df["Hour"].mode().iloc[0])

    print("\nThis took %s seconds." % 
          (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is:\n', df["Start Station"].mode().iloc[0])


    # TO DO: display most commonly used end station
    print('The most commonly used end station is:\n', df["End Station"].mode().iloc[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most commonly used start and end station is:\n', df.groupby(["End Station", "Start Station"]).size().idxmax())

    print("\nThis took %s seconds." % 
          (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is:\n', df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print('Average travel time is:\n', df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    for idx, user_type in enumerate(df["User Type"].value_counts().index.tolist()):
        print('User types:', user_type)
        print('Count:', df["User Type"].value_counts()[idx])
    print('\n')
    # Display counts of gender
    if 'Gender' not in df.columns:
        print('There is no gender information')
    else:
        for idx, gender in enumerate(df["Gender"].value_counts().index.tolist()):
            print('Gender:', gender)
            print('Count:', df["Gender"].value_counts()[idx])
        
    print('\n')
    # Display earliest, most recent, and most common year of birth
    if 'Gender' not in df.columns:
        print('There is no year of birth information')
    else:
        print('The most earliest birth year is:\n', df["Birth Year"].min())
        print('The most recent birth year is:\n', df["Birth Year"].max())
        print('The most common birth year is:\n', df["Birth Year"].mode().iloc[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    """Display 5 lines of the raw data"""
    rows = 0
    show_data = 'False'
    while show_data == 'False':
        show_data = input("Would you like to see the 5 rows of the data?\nPlease type 'yes' or 'no'")
        if show_data == 'yes':
            rows += 5
            print(df.head(rows))
            show_data = 'False'
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
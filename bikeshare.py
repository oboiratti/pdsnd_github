import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in ('chicago', 'new york city', 'washington'):
        city = input('\nSelect which city you would like to see data for: Chicago, New York or Washington?\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in months:
        month = input('\nWhich month would you like to filter by: January, February, March, April, May or June? Enter "all" for no filter\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in days:
        day = input('\nWhich day would you like to filter by: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Enter "all" for no filter\n').lower()

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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_statistics(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: ", months[common_month].title())


    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day is: ", common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", common_end_station)



    # TO DO: display most frequent combination of start station and end station trip
    df['Station Start End Combination'] = df['Start Station'] + ' - ' + df['End Station']
    frequent_combination = df['Station Start End Combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is: ', frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of user types:\n', user_type_count)


    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('\nCount of gender:\n', gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('\nEarliest birth year: ', df['Birth Year'].min())
        print('Most Recent birth year: ', df['Birth Year'].max())
        print('Most common birth year: ', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """Display 5 rows of data on user request"""
    
    print('\nDisplaying 5 rows of data...\n')
    start_time = time.time()
    
    load_data = input('\nWould you like to see individual trip data? Enter yes or no.\n')
    start = 0
    while load_data != 'no':
        print(df.iloc[start: start + 5, 1:6])
        start += 5
        load_data = input('\nWould you like to see more individual trip data? Enter yes or no.\n').lower()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_statistics(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

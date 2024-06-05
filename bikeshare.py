import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def time_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['chicago', 'new york city', 'washington']
    city = input(
        'Would you like to see the data for Chicago, New York City or Washington?\n Please type out full name of the city in the question above.\n').lower()

    while city not in city_list:
        city = input(
            'Oops! The city you chose is not in here. Would you like to choose Chicago, New York or Washington?\n').lower()
    print('You are looking for data from', city.upper(), '! Let\'s continue～')

    # TO DO: get user input for month (all, january, february, ... , june)
    filter_list = ['month', 'day', 'both', 'none']
    get_filter = input(
        'Would you like to filter the data by month, day, both, or not at all?\n Type "none" for no time filter.\n').lower()

    while get_filter not in filter_list:
        get_filter = input(
            'Please type "month", "day", "both", or "none" for time filter.\n').lower()

    if get_filter in ('month', 'both'):
        month_list = ['january', 'february', 'march',
                      'april', 'may', 'june',
                      'july', 'august', 'september',
                      'october', 'november', 'december']
        month = input(
            'By which month would you like to filter your data? Type \'all\' for no month filter.\n').lower()

        while True:
            if month == 'all' or month in month_list:
                break
            month = input(
                'Invalid input. Please type out the full month name (e.g., "January") or "all" for no month filter.\n').lower()
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if get_filter in ('day', 'both'):
        weekday = ['monday', 'tuesday',
                   'wednesday', 'thursday',
                   'friday', 'saturday', 'sunday']
        day = input(
            'By which weekday would you like to filter your data? Type "all" for no weekday filter.\n').lower()

        while True:
            if day == 'all' or day in weekday:
                break
            day = input(
                'Invalid input. Please type out the full weekday name (e.g., "Monday") or "all" for no weekday filter.\n').lower()
    else:
        day = 'all'

    print('-'*40)
    return city, month, day, get_filter


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
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['Month'].str.lower() == month.lower()]
    if day != 'all':
        df = df[df['Day_of_week'].str.lower() == day.lower()]

    return df


def print_filter(city, month, day, get_filter):
    print('FILTER BY: ', city.upper())
    if get_filter in ('both', 'month'):
        print(month.upper())
    if get_filter in ('both', 'day'):
        print(day.upper())


def time_stats(df, city, month, day, get_filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print_filter(city, month, day, get_filter)

    # TO DO: display the most common month
    if get_filter in ('none', 'day'):
        print('Most popular month:', df['Month'].mode()[0])

    # TO DO: display the most common day of week
    if get_filter in ('none', 'month'):
        print('Most popular day of week:', df['Day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    start_hour = df['Start Time'].dt.hour.mode()[0]
    start_hour_count = df['Start Time'].dt.hour.value_counts()

    print('Most popular start hour is {} with {} times'.format(
        start_hour, start_hour_count[start_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city, month, day, get_filter):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print_filter(city, month, day, get_filter)
    
    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    count_start_station = len(df[df['Start Station'] == start_station])
    print('Popular Start Station: {} with {} times'.format(
        start_station, count_start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    count_end_station = len(df[df['End Station'] == end_station])
    print('Popular End Station: {} with {} times'.format(
        end_station, count_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Combination'] = df['Start Station'] + " - " + df['End Station']
    most_common_trip = df['Start_End_Combination'].mode()[0]
    count_trip = len(df[df['Start_End_Combination'] == most_common_trip])
    print('Popular trip: ', most_common_trip)
    print('Counts: ', count_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city, month, day, get_filter):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print_filter(city, month, day, get_filter)

    # TO DO: display total travel time
    print('Total Duration: ', df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print('Average Duration: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day, get_filter):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print_filter(city, month, day, get_filter)

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earliest year of birth: ', int(df['Birth Year'].min()))
    print('Most recent year of birth: ', int(df['Birth Year'].max()))
    print('Most common year of birht: ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays raw data upon request by the user."""
    start = 0
    while True:
        show_data = input(
            'Would you like to see 5 lines of raw data? Enter yes or no.\n').lower()
        while show_data not in ('yes', 'no'):
            show_data = input(
                'Invalid input.\nPlease type "yes" if you would like to see 5 lines of raw data.\nType "no" if you do not want to.\n').lower()

        if show_data == 'no':
            break

        print(df.iloc[start:start + 5])
        start += 5

        if start >= len(df):
            print('No more data to display')
            break

        show_data = input(
            'Would you like to see 5 more lines of raw data? Enter yes or no.\n').lower()
        if show_data == 'no':
            break


def main():
    while True:
        city, month, day, get_filter = time_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day, get_filter)
        station_stats(df, city, month, day, get_filter)
        trip_duration_stats(df, city, month, day, get_filter)
        user_stats(df, city, month, day, get_filter)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
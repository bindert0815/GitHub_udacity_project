import time
import datetime
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
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Please, type the name of the city you would like to see statistics for (chicago, new york city or washington):\n').lower())
            if city == 'chicago':
                print('You\'ve chosen', city)
            elif city == 'new york city':
                print('You\'ve chosen', city)
            elif city == 'washington':
                print('You\'ve chosen', city)
            else:
                print('Please select between "chicago", "new york city" or "washington". Try again!')
                quit()
            break
        except ValueError:
            print('That\'s not a valid string! Try again!')
            quit()

    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = str(input('\nPlease, select a month by entering "january", "february", "march", "april", "may", "june" or "all" for no filter:\n').lower())
            if month == 'january':
                print('You\'ve chosen', month)
            elif month == 'february':
                print('You\'ve chosen', month)
            elif month == 'march':
                print('You\'ve chosen', month)
            elif month == 'april':
                print('You\'ve chosen', month)
            elif month == 'may':
                print('You\'ve chosen', month)
            elif month == 'june':
                print('You\'ve chosen', month)
            elif month == 'all':
                print('You\'ve chosen', month)
            else:
                print('Please select between "january", "february", "march", "april", "may", "june" or "all". Try again!')
                quit()
            break
        except ValueError:
            print('That\'s not a valid string! Try again!')
            quit()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day = str(input('\nPlease, select a day by entering "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" or "all" for no filter:\n'))
            if day == 'monday':
                print('You\'ve chosen', day)
            elif day == 'tuesday':
                print('You\'ve chosen', day)
            elif day == 'wednesday':
                print('You\'ve chosen', day)
            elif day == 'thursday':
                print('You\'ve chosen', day)
            elif day == 'friday':
                print('You\'ve chosen', day)
            elif day == 'saturday':
                print('You\'ve chosen', day)
            elif day == 'sunday':
                print('You\'ve chosen', day)
            elif day == 'all':
                print('You\'ve chosen', day)
            else:
                print('Please select between "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" or "all". Try again!')
                quit()
            break
        except ValueError:
            print('That\'s not a valid string! Try again!')
            quit()


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if df.month.nunique() != 1:
        popular_month = df['month'].mode()[0]
        if popular_month == 1:
            print('The most common month is: January')
        elif popular_month == 2:
            print('The most common month is: February')
        elif popular_month == 3:
            print('The most common month is: March')
        elif popular_month == 4:
            print('The most common month is: April')
        elif popular_month == 5:
            print('The most common month is: May')
        elif popular_month == 6:
            print('The most common month is: June')

    # display the most common day of week
    if df.day_of_week.nunique() != 1:
        popular_day = df['day_of_week'].mode()[0]
        print('The most common day of the week is:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour is:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', popular_end_station)

    # display most frequent combination of start station and end station trip
    print('The most commonly used combination of start station and end station trip is:\n')
    print(df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', str(datetime.timedelta(seconds=total_travel_time)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time (in hours): ', str(datetime.timedelta(seconds=mean_travel_time)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts(dropna=True)
    print(user_types.iloc[0:].to_string(header=None))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts(dropna=True)
        print(gender.iloc[0:].to_string(header=None))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_earliest_year_of_birth = df['Birth Year'].min()
        print('Most earliest year of birth: ', int(most_earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print('Most recent year of birth: ', int(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth: ', int(most_common_year_of_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Asks the user if he/she would like to see some raw data. """
    c = 0
    while True:
        more_stats = str(input('\nWould you like to see raw trip data? Enter "yes" or "no".\n'))
        if more_stats.lower() != 'yes':
            print('It seems you don\'t want to see raw data anymore.')
            break
        else:
            i = c
            if i + 5 < len(df.index) - 1:
                for i in range(c, c+5):
                    print(df.iloc[i:i+1].to_dict())
                c += 5
            else:
                print('You would reach the end of the database.')
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
           
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters(): 
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
   
    while True:
        city = str(input('Which city do you want to search Chicago, New York City, or Washington? \n')).lower()
        if city in CITIES:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Okay! Please type the month name or type \'all\' to apply no month filter. \n')).lower()
        if month in MONTHS:
            break   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Almost done! Please type the week day or type \'all\' to apply no day filter. \n')).lower()
        if day in DAYS:
            break  

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()] 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day:', most_common_day)
    
    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_trip = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most common start end station trip: {}, {}'\
          .format(most_common_start_end_trip[0], most_common_start_end_trip[1]))
                         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time:', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        birth_year = df['Birth Year']
    
        earliest = birth_year.min()
        print('Most earliest birth year:', earliest)
    
        most_recent = birth_year.max()
        print('Most recent birth year:', most_recent)
    
        most_common_year = birth_year.value_counts().mode()
        print('Most common birth:', most_common_year)
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start_data = 0
        end_data = 5
        df_len = len(df.index)
        
        while start_data < df_len:
            viewData = input("\nWould you like to see the raw data? Type 'yes' or 'no'.\n").lower()
            if viewData.lower() == 'yes':
                print('Viewing data for only 5 rows')
                if end_data > df_len:
                    end_data = df_len
                print(df.iloc[start_data:end_data])
                start_data += 5    
                end_data += 5      
            else:
                break
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	    main()

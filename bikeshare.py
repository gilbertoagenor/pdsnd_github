import time
import pandas as pd
import numpy as np

"""change 1"""
"""change 2"""
"""change 3"""
"""change 4"""

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    
    city = (input('What city would you like to visit (current options are Chicago, New York City and Washington)? ').lower()).strip()
    errorcount = 0
    while city not in ['chicago', 'new york city', 'washington']:
        errorcount += 1
        print("City input was not valid")
        if errorcount % 3 != 0:
            city = (input ("Valid options are Chicago, New York City and Washington. Please try again ").lower()).strip()
        else:
            city = (input ("It looks like you are having issues. Your spelling should be exactly as shown here: Chicago, New York City or Washington.\nPlease Choose a City: ").lower()).strip()

    # TO DO: get user input for month (all, january, february, ... , june)

    month = (input('What month would you like to get data from? (current options are All, January, February, March, April, May and June)? ').lower()).strip()
    errorcount = 0
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        errorcount += 1
        print("Month input was not valid")
        if month.isnumeric():
            print("It looks like your input is a number. Unfortunately for this routine the month input must be spelled")
        if errorcount % 3 != 0:
            month = (input ("Valid options are All, January, February, March, April, May and June. Please try again ").lower()).strip()
        else:
            month = (input ("It looks like you are having issues. Your spelling should be exactly as shown here: All, January, February, March, April, May or June.\nPlease Choose a Month: ").lower()).strip()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = (input('What Day of the Week would you like to get data from? (current options are All, Mon, Tue, Wed, Thu, Fri, Sat and Sun)? ').lower()).strip()
    errorcount = 0
    while day not in ['all','mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
        errorcount += 1
        print("Day of the Week input was not valid")
        if day.isnumeric() or len(day) != 3:
            print("For this routine the Day of the Week input must be spelled with 3 letters")
        if errorcount % 3 != 0:
            day = (input ("Valid options are All, Mon, Tue, Wed, Thu, Fri, Sat and Sun. Please try again ").lower()).strip()
        else:
            day = (input ("It looks like you are having issues. Your spelling should be exactly as shown here: All, Mon, Tue, Wed, Thu, Fri, Sat or Sun\nPlease Choose a Day of the Week: ").lower()).strip()
    
    city = city.title()
    month = month.title()
    day = day.title()
                
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
    
    city = CITY_DATA.get(city)
       
    df = pd.read_csv('{}'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['week_day'] = df['Start Time'].dt.strftime('%a')
       
    if month != 'All':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['week_day'] == day]

    return df

    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['week_day'].mode()[0]
    print('Most Common Day of the Week is: ', popular_day)

    # TO DO: display the most common start hour
    popular_hour = (df['Start Time'].dt.strftime('%-H')).mode()[0]
    print('Most Common Start Hour is: ', popular_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Most Common Start Station is: ', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['Start Station'].mode()[0]
    print('Most Common End Station is: ', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df["comb"] = "From " + df["Start Station"] + " to " + df["End Station"]
    popular_combstation = df["comb"].mode()[0]
    print('Most Common Station Combination is: ', popular_combstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("The total travel time in hours is: ", int(total_duration))

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean() / 60.0
    print("The mean travel time in minutes is: ", int(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of User Gender
    try:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    except:
        print("There is no 'Gender' column in this file.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        Common_birth = df['Birth Year'].mode()[0]
        print('Earliest Year of Birth is: ', earliest_birth)
        print('Most Recent Year of Birth is: ', recent_birth)
        print('Most Common Year of Birth is: ', Common_birth)
    except:
        print("There are no birth year details in this file.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Prints Raw Data (acording to filters). 5 rows will added in each press"""
    
    x = 0
    raw = 0
    while raw != "no":
        if x == 0:
            raw = (input('Would you like to see raw data (Please type Yes or No)? ').lower()).strip()
            while raw not in ['yes','no']:
                raw = (input('Sorry, I did not Understand your answer. Would you like to see raw data (Please type Yes or No)? ').lower()).strip()
        else:
            raw = (input('Would you like to see the next 5 rows of raw data (Please type Yes or No)? ').lower()).strip()
            while raw not in ['yes','no']:
                raw = (input('Sorry, I did not Understand your answer. Would you like to see the next 5 rows of raw data (Please type Yes or No)? ').lower()).strip()
        if raw == "yes":
            x = x+5
            print(df[x-5:x])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print("Thank you for the Inputs!\nWe will now show data from {} Filtered by the Month of {} and the Day of the Week {}!".format(city, month,day))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)      
        raw_data(df)

        restart = (input('Would you like to Restart (Please type Yes or No)? ').lower()).strip()
        while restart not in ['yes','no']:
            restart = (input('Sorry, I did not Understand your answer. Would you like to Restart (Please type Yes or No)?  ').lower()).strip()
        if restart != 'yes':
            break
        
if __name__ == "__main__":
	main()

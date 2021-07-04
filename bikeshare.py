import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    check=True
    while check:
        weekDays = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
        months = ("january","february","march","april","may","june")
        cities = ("chicago","new york","washington")
        filters = ("month","both","day","none")
        city=input("please choose a city chicago , new york or washington : ").lower()
        filterValue=input("please choose a filter month , day ,both or none : ").lower()
        if(filterValue=="month"):
            day=0
            month=input("Please choose a month from january to june : ").lower()
        elif(filterValue=="day"):
            month=0
            day=input("Please choose a day of weeks (monday, tuesday, ... sunday) : ").lower()
        elif(filterValue=="both"):
            day=input("Please choose a day of weeks (monday, tuesday, ... sunday) : ").lower()
            month=input("Please choose a month from january to june  : ").lower()
        elif(filterValue=="none"):
            day=0
            month=0
        try:
            if((city not in cities) or (month not in months and month != 0) or (day not in weekDays and day != 0) or (filterValue not in filters)):
                print("invalid data you will have to satrt all over again")
            else:
                check=False
        except ValueError:
            print("invalid data you will have to satrt all over again")
            check=True
    return city,day,month

def load_data(city, month, day):
    data = pd.read_csv(CITY_DATA[city])
    if(month==0 and day==0):
        df=data
    elif(month==0):
        df=data[pd.to_datetime(data['Start Time']).dt.day_name()==day.capitalize()]
    elif(day==0):
        df=data[pd.to_datetime(data['Start Time']).dt.month_name()==month.capitalize()]
    else:
        df=data[(pd.DatetimeIndex(data['Start Time']).day_name()==day.capitalize()) & (pd.DatetimeIndex(data['Start Time']).month_name()==month.capitalize())]
    return df;

def display_data(df2):
    i= 0
    df = df2.copy()
    while True:
        rows = input("Do you want to see first 5 rows? Yes or No \n ").lower()
        if rows not in ['yes', 'no']:
            rows = input("You wrote the wrong word. Please type Yes or No.\n").lower()
        elif rows == 'yes':
            print(df.iloc[i : i + 5])
            i+=5
            next_rows = input("Do you want to see next 5? Yes or No \n").lower()
            if next_rows == 'no':
                break
            elif next_rows == 'yes':
                print(df.iloc[i : i + 5])
        elif rows == 'no':
            return



def time_stats(df2):
    df = df2.copy()
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    common_month = df['Start Time'].dt.month_name().mode()[0]
    print('Most Common Month :', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    common_day = df['Start Time'].dt.day_name().mode()[0]
    print('Most Common day :', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common hour :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df2):
    """Displays statistics on the most popular stations and trip."""
    df=df2.copy()

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common start station :' , common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common end station : ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df[['Start Station','End Station']].value_counts().idxmax()
    print("The most frequent combination of start station and end station trip : " , common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df2):
    """Displays statistics on the total and average trip duration."""
    df=df2.copy()

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is {} hours".format(round(total_time)))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is {} hours".format(round(mean_travel)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df2):
    """Displays statistics on bikeshare users."""
    df = df2.copy()
    if "Gender" and "Birth Year" in df:
        df["Gender"] = df['Gender'].fillna("Unknown")
    else:
        df["Gender"] = 'Unknown'
        df["Birth Year"] = "No valid data"

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user type : \n' ")
    print("{} \n".format(user_types))
    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("Counts of gender : \n' ")
    print("{} \n".format(gender))
    # TO DO: Display earliest, most recent, and most common year of birth
    df["Birth Yearer"] = df['Birth Year'].dropna()
    print("Earliest year of birth: {} \nMost recent year of birth : {} \nMost common year of birth : {}  ".format(min(df['Birth Year']),max(df['Birth Year']),df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    getfilters=get_filters()
    city=getfilters[0]
    day=getfilters[1]
    month2=getfilters[2]
    df=load_data(city,month2,day)
    display_data(df)
    time_stats(df)
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if(restart.lower()=="yes"):
        main()

if __name__ == "__main__":
	main()

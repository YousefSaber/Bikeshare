from helper import *

def main():
        city, month, day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        x = input(" Do you want to exit? (yes/no)")
        x = x.lower()
        if x == "no":
            return True
        elif x == "yes":
            return False
        else:
            print("invalid input")
            return True
status = True
while status:
    status = main()

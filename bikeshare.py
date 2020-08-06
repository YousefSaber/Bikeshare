from helper import *

def main():
        city, month, day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
status = True
while status:
    main()

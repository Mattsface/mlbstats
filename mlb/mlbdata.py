import os

import pandas as pd
import datetime as dt
# from sqlalchemy import create_engine

from .paths import *

def get(df_title) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR + f"{df_title}.csv",index_col=False)

def get_teams_df(year=None) -> pd.DataFrame:
    teams_df = pd.read_csv(
        TEAMS_CSV,
        index_col=False,
        dtype={'mlbam':'int32','season':'int32','venue_mlbam':'int32'})
    if year is None:
        return teams_df
    else:
        df = teams_df
        df = df[df["season"]==year]
        return df

def get_standings_df() -> pd.DataFrame:
    """Standings for each season"""
    try:
        df = pd.read_csv(YBY_STANDINGS_CSV,index_col=False)

        return df

    except Exception as e:
        print(e)
        return None

def get_yby_records(raw=False) -> pd.DataFrame:
    """Record splits by season for each team"""
    try:
        df = pd.read_csv(YBY_RECORDS_CSV,index_col=False)
        return df

    except Exception as e:
        print(e)

def get_people_df() -> pd.DataFrame:
    df = pd.read_csv(
        PEOPLE_CSV,
        index_col=False,
        dtype={'mlbam':'int32','year_debut':'int32','year_recent':'int32'})
    return df

def get_seasons_df() -> pd.DataFrame:
    try:
        cols = ['preSeasonStartDate','preSeasonEndDate','seasonStartDate','seasonEndDate','springStartDate','springEndDate','regularSeasonStartDate','regularSeasonEndDate','allStarDate','postSeasonStartDate','postSeasonEndDate','offSeasonStartDate','offSeasonEndDate']

        df = pd.read_csv(SEASONS_CSV,index_col=False)

        df[cols] = df[cols].apply(pd.to_datetime,format=r"%Y-%m-%d")
        return df
    except Exception as e:
        print(e)

def get_venues_df(active_only=False) -> pd.DataFrame:
    """Get Dataframe of Venues
    
    Parameters:
    -----------
    active_only : bool, default False
        set to True to retrieve data for only currently active venues
    
    """

    df = pd.read_csv(
        VENUES_CSV,
        index_col=False,
        dtype={'mlbam':'int32','tz_offset':'int32'})

    if active_only is True:
        df = df[df["active"]==True].reset_index(drop=True)
    
    return df

def get_season_info(date=None) -> tuple:
    """
    Get current season in-progress and most recently completed season, 
    given a specified date

    Parameters:
    -------------
    date: str, 
        format - `mm/dd/yyyy`\n\t\tDefault: current date
    
    """
    
    if date is None:
        current_date = dt.datetime.today()
        using_pretend = False
    else:
        using_pretend = True
        pretend_current = dt.datetime.strptime(date,r"%m/%d/%Y")
        current_date = pretend_current
    try:

        df = get_seasons_df()
        if using_pretend is False:
            df = df.head(4)

        df = df.rename(columns={'seasonStartDate':'start',
                                'seasonEndDate':'end'})

        df_dates = df
        # return df_dates

        for row in range(len(df_dates)):
            if df_dates.iloc[row].start <= current_date <= df_dates.iloc[row].end:
                seasonInProgress = current_date.year
                seasonCompleted = seasonInProgress - 1

                season_info = {'in_progress':seasonInProgress,
                               'last_completed':seasonCompleted}
                return season_info
                # return seasonInProgress, seasonCompleted

        seasonInProgress = None

        for row in range(len(df_dates)):
            # if df_dates.iloc[row].start.date().year == current_date.year:
            if df_dates.iloc[row].start.year == current_date.year:
                curr_year_row = df_dates.iloc[row]
                # if current_date < curr_year_row.start.date():
                if current_date < curr_year_row.start:
                    seasonCompleted = current_date.year - 1
                    season_info = {'in_progress':seasonInProgress,
                                   'last_completed':seasonCompleted}
                    return season_info

                # elif current_date > curr_year_row.end.date():
                elif current_date > curr_year_row.end:
                    seasonCompleted = current_date.year
                    season_info = {'in_progress':seasonInProgress,
                                   'last_completed':seasonCompleted}
                    return season_info

                else:
                    print("Hmm...didn't work. Here is the dataframe again\n")
                    return df_dates

    except Exception as e:
        print(e)

def get_hall_of_fame() -> pd.DataFrame:
    """Get Hall of Fame Data"""
    return pd.read_csv(HALL_OF_FAME_CSV,index_col=False)

def get_broadcasts_df() -> pd.DataFrame:
    """Get Broadcasts data (types, names, ids...)"""
    return pd.read_csv(BROADCASTS_CSV,index_col=False)

def get_bbref_data() -> pd.DataFrame:
    """Reference dataframe for player's 'Baseball-Reference' & 
    MLB Advanced Media IDs
    
    """
    
    return pd.read_csv(BBREF_DATA_CSV,index_col=False,dtype={'mlb_ID':'int32'})

def get_bbref_hitting_war_df() -> pd.DataFrame:
    df = pd.read_csv(BBREF_BATTING_DATA_CSV)
    return df

def get_bbref_pitching_war_df() -> pd.DataFrame:
    df = pd.read_csv(BBREF_PITCHING_DATA_CSV)
    return df

def get_leagues_df() -> pd.DataFrame:
    try:
        df = pd.read_csv(LEAGUES_CSV,index_col=False)

        return df

    except Exception as e:
        print(e)
        
def get_teams_from_register_df(match_columns=False) -> pd.DataFrame:
    """Periodically updated dataset of team ids (similar to the 'mlb.teams()' 
    output. This is purely a convenience function if additional 
    cross-referencing is needed. It may or may not match the rest of the data 
    retrieved using the other functions.
    
    Paramaters:
    -----------
    match_columns : bool, default = False
        If set to 'True', the column labels will be changed to best match 
        the labels used in the rest of the library. Otherwise, the data will 
        be returned unaltered.
        
    """
    
    url = "https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/Teams.csv"
    df = pd.read_csv(url,index_col=False)
    if match_columns is True:
        df = df.rename(columns={'lgID'})
    return df

    
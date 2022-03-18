"""
# SimpleStatsMLB

Python Wrapper for the MLB Stats API - https://statsapi.mlb.com

- Author: Joe Rechenmacher
- GitHub Profile: https://github.com/joerex1418

### Copyright Notice
This repository and its author are not affiliated with the MLB in any way. Use of MLB data is subject to the notice posted at http://gdx.mlb.com/components/copyright.txt.

Overview
--------
SimpleStatsMLB is designed to make retrieving and visualizing MLB data as easy & intuitive as possible.
    
With a variety of data tables, 4 primary classes, and almost 40 functions, getting the baseball information you need should be a "can-o-corn".

-------------------------------------------------------------------------------------------------------
Highlights
----------
### 4 Primary Classes designed to quickly make hundreds of API calls at once
    * `Person` - instances represent a specific person affiliated with the MLB
        * Primary usage is for the retrieval of player bios and stats
    * `Franchise` - instances represent an MLB franchise (i.e. the parent org for specific team)
    * `Team` - instances represent a specific team for a specified season
    * `Game` - instances represent LIVE data for a game
        * Available data includes scores, game stats, lineups, pitch logs, play logs, weather, 
        attendance, venue info, and more!
        
### Pitch & Play Finder!
    * With the `pitch_search` and `play_search` functions, you'll be able to search for any 
    plays/pitches over recent years with detailed information 

### Schedule
    * Need the entire 2021 schedule? Or just the 2005 schedule for the Chicago White Sox?
    Either way, getting the dates that you need is easy with the `schedule` function
    
### Just need to know when your team is playing next? 
    * Use the `next_game` function to get the 'when', 'who', and 'where' for your favorite team's next matchup


### Find out more by clicking the links below!
-------------------------------------------------------------------------------------------------------    
- Source: https://github.com/joerex1418/simplestats-mlb
- Issues: https://github.com/joerex1418/simplestats-mlb/issues
- License: https://raw.githubusercontent.com/joerex1418/simplestats-mlb/master/LICENSE

"""


from .classes import Person
from .classes import Franchise
from .classes import Team
from .classes import Game
franchise = Franchise
person = Person
team = Team
game = Game

from .classes import api


from .functions import play_search
from .functions import pitch_search
from .functions import game_search
# from .functions import get_matchup_stats
from .functions import leaderboards
from .functions import last_game
from .functions import next_game
from .functions import find_team
from .functions import find_player
from .functions import find_venue
from .functions import schedule
from .functions import free_agents
from .functions import player_bio
from .functions import player_stats
from .functions import player_hitting
from .functions import player_pitching
from .functions import player_fielding
from .functions import player_hitting_advanced
from .functions import player_pitching_advanced
from .functions import player_game_logs
from .functions import player_date_range
from .functions import player_date_range_advanced
from .functions import player_splits
from .functions import player_splits_advanced
from .functions import team_hitting
from .functions import team_pitching
from .functions import team_fielding
from .functions import team_hitting_advanced
from .functions import team_pitching_advanced
from .functions import team_roster
from .functions import team_game_logs
from .functions import team_appearances
from .functions import league_hitting
from .functions import league_pitching
from .functions import league_fielding
from .functions import league_hitting_advanced
from .functions import league_pitching_advanced
from .functions import league_leaders

# from .functions import _player_data
# from .functions import _franchise_data
# from .functions import _team_data

player_batting = player_hitting
team_batting = team_hitting

from .functions import game_highlights
from .functions import get_video_link


from .utils import keys
from .utils import timeutils
from .utils import default_season
from .utils import metadata

from .utils import COLS_HIT
# from .utils import utc_zone
# from .utils import et_zone
# from .utils import ct_zone
# from .utils import iso_format
# from .utils import maketable
# from .utils import showtable

# from .utils import compile_codes
# from .utils import draw_pitches
# from .utils import draw_strikezone
# from .utils import simplify_time
# from .utils import prettify_time
# from .utils import prepare_game_data
# from .utils import curr_year as current_year

from .mlbdata import get
from .mlbdata import save_all
from .mlbdata import save_bios
from .mlbdata import save_teams
from .mlbdata import save_venues
from .mlbdata import save_people
from .mlbdata import save_seasons
from .mlbdata import save_standings
from .mlbdata import save_yby_records
from .mlbdata import get_season_info
from .mlbdata import get_bios_df as bios
from .mlbdata import get_teams_df as teams
from .mlbdata import get_people_df as people
from .mlbdata import get_venues_df as venues
from .mlbdata import get_leagues_df as leagues
from .mlbdata import get_seasons_df as seasons
from .mlbdata import get_standings_df as standings
from .mlbdata import get_yby_records as yby_records
from .mlbdata import get_hall_of_fame as hall_of_fame
from .mlbdata import get_broadcasts_df as broadcasts
from .mlbdata import get_bbref_hitting_war_df as bbref_war_hit
from .mlbdata import get_bbref_pitching_war_df as bbref_war_pitch

from .updatedb import update_hof
from .updatedb import update_bios
from .updatedb import update_people
from .updatedb import update_venues
from .updatedb import update_seasons
from .updatedb import update_leagues
from .updatedb import update_yby_records
from .updatedb import update_bbref_hitting_war
from .updatedb import update_bbref_pitching_war
update_bbref_batting_war = update_bbref_hitting_war


from .transactions import draft as get_draft
from .transactions import prospects as get_prospects
from .transactions import free_agents as get_free_agents
from .transactions import transactions as get_transactions

# from .utils_team import team_leaders

from .async_mlb import fetch
from .async_mlb import fetch_text

from .constants import (
    BASE,
    GAME_TYPES_ALL,
    BAT_FIELDS,
    BAT_FIELDS_ADV,
    PITCH_FIELDS,
    PITCH_FIELDS_ADV,
    FIELD_FIELDS,
    STATDICT,
    LEAGUE_IDS,
    COLS_HIT,
    COLS_HIT_ADV,
    COLS_PIT,
    COLS_PIT_ADV,
    COLS_FLD,
    W_SEASON,
    WO_SEASON
)
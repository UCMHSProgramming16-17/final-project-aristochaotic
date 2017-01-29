import requests
import logging

# logging configuration
logging.basicConfig(level=logging.INFO)

# current year
current_year = 2016

# set up a session
s = requests.Session()
s.headers.update({'X-TBA-APP-ID': 'jgerstein:TBAT:v2'})

base_url = 'https://www.thebluealliance.com/api/v2/'
team_url = base_url + 'team/frc'
event_url = base_url + 'event/'
district_url = base_url + 'district/'


def process_data(info):
    """Processes data from an API call to return it to the function from which it's called"""
    data = info.json()
    logging.debug(data)
    return data


def get_api_status():
    """Checks status of the API"""
    r = s.get(base_url + 'status')
    return process_data(r)


def get_team_info(team_number):
    """Gets info about a team"""
    r = s.get(team_url + str(team_number))
    return process_data(r)


def get_team_list(page_num):
    """Gets the specified page of the team list"""
    r = s.get(base_url + 'teams/' + str(page_num))
    return process_data(r)


def get_all_teams():
    """Returns a list of all teams"""
    # Create list to store teams in
    all_teams=[]
    page = 0
    # Will continue indefinitely
    while True:
        current_page = get_team_list(page)
        # Exit loop if team list contains no teams - we're at the end
        if len(current_page) == 0:
            break
        else:
            for team in current_page:
                all_teams.append(team)
        page += 1
    logging.debug(all_teams)
    return all_teams


def get_team_events(team_number, year=current_year):
    """Gets team events for a given year. Defaults to current_year"""
    r = s.get(team_url + str(team_number) + '/' + str(year) + '/events')
    return process_data(r)


def get_team_event_awards(team_number, event):
    """Gets a team's awards for a specified event"""
    r = s.get(team_url + str(team_number) + '/event/' + event + '/awards')
    return process_data(r)


def get_team_event_matches(team_number, event):
    """Gets a team's matches for a specified event"""
    r = s.get(team_url + str(team_number) + '/event/' + event + '/matches')
    return process_data(r)


def get_team_years_participated(team_number):
    """Gets a team's years participated in FRC"""
    r = s.get(team_url + str(team_number) + '/years_participated')
    return process_data(r)


def get_team_media(team_number, year=current_year):
    """Returns a team's media for a specific year. Defaults to current_year"""
    r = s.get(team_url + str(team_number) + '/' + str(year) + '/media')
    return process_data(r)


def get_team_event_history(team_number):
    """Returns a team's event history"""
    r = s.get(team_url + str(team_number) + '/history/events')
    return process_data(r)


def get_team_awards_history(team_number):
    """Gets a specified team's historical awards"""
    r = s.get(team_url + str(team_number) + '/history/awards')
    return process_data(r)


def get_team_robot_history(team_number):
    """Gets a specified team's historical robot info"""
    r = s.get(team_url + str(team_number) + '/history/robots')
    return process_data(r)


def get_team_district_history(team_number):
    """Gets historical data about a team's district membership"""
    r = s.get(team_url + str(team_number) + '/history/districts')
    return process_data(r)


def get_events_by_year(year=current_year):
    """Gets list of events for the specified year. Defaults to current_year"""
    r = s.get(base_url + 'events/' + str(year))
    return process_data(r)


def get_event_info(event_key):
    """Gets info about specified event"""
    r = s.get(event_url + str(event_key))
    return process_data(r)


def get_event_teams(event_key):
    """Gets teams in attendance at specified event"""
    r = s.get(event_url + str(event_key) + '/teams')
    return process_data(r)


def get_event_matches(event_key):
    """Gets matches for specified event"""
    r = s.get(event_url + str(event_key) + '/matches')
    return process_data(r)


def get_event_stats(event_key):
    """Gets stats for specified event"""
    r = s.get(event_url + str(event_key) + '/stats')
    return process_data(r)


def get_event_rankings(event_key):
    """Gets rankings for specified event"""
    r = s.get(event_url + str(event_key) + '/rankings')
    return process_data(r)


def get_event_awards(event_key):
    """Gets awards for specified event"""
    r = s.get(event_url + str(event_key) + '/awards')
    return process_data(r)


def get_event_district_points(event_key):
    """Gets district points for specified event"""
    r = s.get(event_url + str(event_key) + '/district_points')
    return process_data(r)


def get_match(match_key):
    """Gets data for a specified match"""
    r = s.get(base_url + 'match/' + str(match_key))
    return process_data(r)


def get_districts(year=current_year):
    """Gets a list of districts for the specified year. Defaults to current_year"""
    r = s.get(base_url + 'districts/' + str(year))
    return process_data(r)


def get_district_events(district_key, year=current_year):
    """Gets events for a district in a specified year. Defaults to current_year"""
    r = s.get(district_url + district_key + '/' + str(year) + '/events')
    return process_data(r)


def get_district_rankings(district_key, year=current_year):
    """Gets rankings for a district in a specified year. Defaults to current_year"""
    r = s.get(district_url + district_key + '/' + str(year) + '/rankings')
    return process_data(r)


def get_district_teams(district_key, year=current_year):
    """Gets teams for a district in a specified year. Defaults to current_year"""
    r = s.get(district_url + district_key + '/' + str(year) + '/teams')
    return process_data(r)


# Test below this line

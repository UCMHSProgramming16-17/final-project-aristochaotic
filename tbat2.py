import tbat
import logging
import pickle

logging.basicConfig(level=logging.INFO)

data_folder = 'cached_data/'


class Team(object):

    def __init__(self, results):
        """Return a Team object corresponding to the specified team"""
        self.website = results['website']
        self.nickname = results['nickname']
        self.city = results['locality']
        self.region = results['region']
        self.country = results['country_name']
        self.location = results['location']
        self.team_number = results['team_number']
        self.name = results['name']
        self.rookie_year = results['rookie_year']
        self.motto = results['motto']
        self.key = results['key']
        self.years_active = tbat.get_team_years_participated(results['team_number'])
        events = []
        temp_events = tbat.get_team_event_history(results['team_number'])
        for event in temp_events:
            events.append(event['key'])
        self.event_history = events
        self.award_history = tbat.get_team_awards_history(results['team_number'])


class Event(object):

    def __init__(self, results):
        self.name = results['name']
        self.type_const = results['event_type']
        self.district_const = results['event_district']
        # # self.facebook_eid = results['facebook_eid']
        self.event_code = results['event_code']
        self.week = results['week']
        self.start_date = results['start_date']
        self.location = results['location']
        self.event_type = results['event_type_string']
        self.alliances = results['alliances']
        self.end_date = results['end_date']
        self.key = results['key']
        self.short_name = results['short_name']
        self.website = results['website']
        self.webcast = results['webcast']
        self.venue_address = results['venue_address']
        self.year = results['year']
        self.district = results['event_district_string']
        self.official = results['official']
        self.timezone = results['timezone']
        event_teams = []
        teams_ = tbat.get_event_teams(self.key)
        for t in teams_:
            event_teams.append(t['team_number'])
        self.teams = event_teams



def update_event_keys():
    event_keys = {}
    for year in range(1992, tbat.current_year + 1):
        event_keys[year] = []
        events = tbat.get_events_by_year(year)
        for event in events:
            event_keys[year].append(event['key'])        
    with open(data_folder + 'event_keys.p', 'wb') as file:
        pickle.dump(event_keys, file)
    return event_keys


def load_event_keys():
    with open(data_folder + 'event_keys.p', 'rb') as file:
        event_keys = pickle.load(file)
    return event_keys


def update_individual_event(event_key):
    """Fetches event info about specified event."""
    # Get info about event
    e = tbat.get_event_info(event_key)
    # Create event object
    event = Event(e)
    filename = str(event_key) + '.p'
    with open(data_folder + filename, 'wb') as file:
        pickle.dump(event, file)
    return event


def load_individual_event(event_key):
    filename = str(event_key) + '.p'
    with open(data_folder + filename, 'rb') as file:
        event = pickle.load(file)
    return event


def update_all_teams(test=''):
    """Fetches all team info. Do only as needed."""
    # Get all teams
    if(test == 'test'):
        all_teams = tbat.get_team_list(0)
    else:
        all_teams = tbat.get_all_teams()

    # Create objects
    teams = {}
    for team in all_teams:
        teams[team['team_number']] = Team(team)
        logging.info('%s complete' % team['team_number'])
    with open(data_folder + 'all_teams.p', 'wb') as file:
        pickle.dump(teams, file)
    return teams


def load_all_teams():
    """Loads the save team info. Remember to import the Team class"""
    with open(data_folder + 'all_teams.p', 'rb') as file:
        teams = pickle.load(file)
    return teams


# Test below this line
if __name__ == "__main__":
    # bri = load_individual_event('2016njbri')
    # print(dir(bri))
    all_events = update_event_keys()
    print(all_events[2016])

# TBAT2

TBAT2 uses TBAT to update and load information in a more coherent format. So far, I've got a model for teams and a model for events.

<!-- MarkdownTOC -->

- [Information Models](#information-models)
    - [Team](#team)
    - [Event](#event)
- [Methods](#methods)
    - [update_event_keys\(\)](#updateeventkeys)
    - [load_event_keys\(\)](#loadeventkeys)
    - [update_individual_event\(\)](#updateindividualevent)
    - [load_individual_event\(\)](#loadindividualevent)
    - [update_all_teams\(\)](#updateallteams)
    - [load_all_teams\(\)](#loadallteams)

<!-- /MarkdownTOC -->

<a name="information-models"></a>
# Information Models

<a name="team"></a>
## Team

Attributes

name | description | example | data type
---- | ----------- | ------- | ---------
website | team's website | http://www.team1257.org | string
nickname | team's nickname | Parallel Universe | string
city | team's city | Scotch Plains | string
region | team's state/province/equivalent | New Jersey | string
country | team's country | USA | string
location | long-form address | Scotch Plains, New Jersey 07076, USA | string 
team_number | team's number | 1257 | integer
name | team's full official name | TE Connectivity / Google / Formlabs & Union Cty Voc Tech | string
rookie_year | team's rookie year | 2004 | integer
motto | team's motto |   | string
key | team key for API use | frc1257 | string
years_active | years team participated in FRC | [2004, 2005, 2006, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017] | list of integers
event_history | all event keys team has attended | ['2004md', '2004nj', '2004wpi', '2005cur', '2005md', '2005ny', '2006nj', '2009ny', '2010nj', '2011ny', '2012njf', '2012phl', '2013njbrg', '2013njewn', '2014mrcmp', '2014njbri', '2014njcli', '2015mrcmp', '2015njfla', '2015njnbr', '2016arc', '2016iri', '2016mrcmp', '2016njbri', '2016njfla', '2016njmm', '2017njbri', '2017pahat'] | list of strings
award_history | list of team's awards | figure out how to show this later | list of award models

<a name="event"></a>
## Event

Attributes

name | description | example | data type
---- | ----------- | ------- | ---------
name | official name of event | MAR District - Mt. Olive Event | string
type_const | constant representing event type | 1 | integer
district_const | constant representing district | 2 | integer
event_code | official event code | njfla | string
week | week of event | 1 | integer
start_date | event's start date | 2016-03-04 | string
end_date | event's end date | 2016-03-06 | string
location | event location | Flanders, NJ 07836, USA | string
alliances | list of playoff alliances | figure out how to represent this later | list of dictionaries
key | event key for API use | 2016njfla | string
short_name | event's short name | Mt. Olive | integer
website | event website | http://www.midatlanticrobotics.com | string
webcast | webcast locations | figure out how to represent this later | list of dictionaries
venue_address | long-form address of event venue | Mt. Olive High School\n18 Cory Road\nFlanders, NJ 07836\nUSA | string
year | year of event | 2016 | integer
district | official name of district | Mid Atlantic | string
official | states whether event is official | True | boolean
timezone | timezone of event location | America/New_York | string
teams | list of teams in attendance | [11, 1143, 1228, 1257, 1279, 1403, 1676, 1811, 1923, 193, 2070, 219, 222, 223, 224, 2554, 2577, 2600, 303, 3142, 3340, 3515, 3637, 4035, 41, 4281, 4285, 4361, 4475, 4573, 4653, 5310, 56, 5624, 6015, 6016, 613, 75, 752] | list of integers

<a name="methods"></a>
# Methods

<a name="updateeventkeys"></a>
## update_event_keys()

```python
update_event_keys()

# example
>>> events = tbat2.update_event_keys()
>>> events
{
    1992: ['1992cmp'],
    ...
    1996: ['1996cmp', '1996nh'],
    ...
    2004: ['2004arc', '2004az', '2004ca', '2004cmp', '2004co', '2004ct', '2004cur', '2004dt', '2004fl', '2004ga', '2004gal', '2004gl', '2004il', '2004li', '2004md', '2004mi', '2004mo', '2004new', '2004nh', '2004nj', '2004ny', '2004oh', '2004on', '2004or', '2004pa', '2004pit', '2004sac', '2004sc', '2004sj', '2004tx', '2004va', '2004wpi'],
}
```

Returns a dictionary containing all event keys, sorted by year. Also pickles the data to a file called event_keys.p


<a name="loadeventkeys"></a>
## load_event_keys()

```python
load_event_keys()

# example
>>> events = tbat2.load_event_keys()
>>> events
{
    1992: ['1992cmp'],
    ...
    1996: ['1996cmp', '1996nh'],
    ...
    2004: ['2004arc', '2004az', '2004ca', '2004cmp', '2004co', '2004ct', '2004cur', '2004dt', '2004fl', '2004ga', '2004gal', '2004gl', '2004il', '2004li', '2004md', '2004mi', '2004mo', '2004new', '2004nh', '2004nj', '2004ny', '2004oh', '2004on', '2004or', '2004pa', '2004pit', '2004sac', '2004sc', '2004sj', '2004tx', '2004va', '2004wpi'],
}
```

Unpickles the file created by update_event_keys() and returns it as a dictionary. Doesn't work if the file doesn't exist

<a name="updateindividualevent"></a>
## update_individual_event()

```python
update_individual_event(event_key)

# example
>>> mo = tbat2.update_individual_event('2016njfla')
>>> mo.name
'MAR District - Mt. Olive Event'
>>> mo.short_name
'Mt. Olive'
>>> mo.key
'2016njfla'
>>> mo.district
'Mid Atlantic'
>>> mo.year
2016
>>> mo.week
1
```

Returns an instance of the Event class referring to the specified event. Also pickles the data to a file named for the event key.

<a name="loadindividualevent"></a>
## load_individual_event()

```python
load_individual_event(event_key)

# example
>>> mo = tbat2.load_individual_event('2016njfla')
>>> mo.name
'MAR District - Mt. Olive Event'
>>> mo.short_name
'Mt. Olive'
>>> mo.key
'2016njfla'
>>> mo.district
'Mid Atlantic'
>>> mo.year
2016
>>> mo.week
1
```

Unpickles the file created by update_individual_event() and returns the instance of the Event class created. Doesn't work if the file doesn't exist.

<a name="updateallteams"></a>
## update_all_teams()

```python
update_all_teams()

# example
>>> all_teams = tbat2.update_all_teams()
INFO:root:1 complete
INFO:root:4 complete
...
INFO:root:6764 complete
INFO:root:6765 complete
>>> all_teams[1257]
<tbat2.Team object at 0x000001B555516978>
>>> all_teams[1257].nickname
'Parallel Universe'
```

Returns a dictionary containing an instance of the Team class for each team. Dictionary keys are team numbers. Also pickles the data to a file called all_teams.p

<a name="loadallteams"></a>
## load_all_teams()
```python
load_all_teams()

# example
>>> all_teams = tbat2.load_all_teams()
>>> all_teams[1257]
<tbat2.Team object at 0x000001B555516978>
>>> all_teams[1257].nickname
'Parallel Universe'
```

Unpickles the file created by update_all_teams() and returns the dictionary created. Doesn't work if the file doesn't exist.

import requests
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = requests.get(url)

    # raise exception if status code is not 200
    req.raise_for_status()

    soup = BeautifulSoup(req.text, 'html.parser')

    most_recent_events_tag = soup.find('div', {'class': 'most-recent-events'})
    events = most_recent_events_tag.find('ul', {'class': 'list-recent-events'})
    most_recent_events = events.findAll('li')

    for event in most_recent_events:
        event_details = dict()
        event_details['name'] = event.find('h3', {'class': 'event-title'})
        event_details['location'] = event.find('span', {'class': 'event-location'})
        event_details['time'] = event.find('time')
        print event_details


url = 'https://www.python.org/events/python-events/'
get_upcoming_events(url)

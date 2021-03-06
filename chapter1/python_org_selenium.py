from selenium import webdriver

def get_upcoming_events(url):
    driver = webdriver.Firefox()
    driver.get(url)
    xpath = '//div[@class="shrubbery"]/ul[contains(@class, "list-recent-events")]/li'
    upcoming_events = driver.find_elements_by_xpath(xpath)

    for event in upcoming_events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        print event_details

    driver.close()


url = 'https://www.python.org/events/python-events/'
get_upcoming_events(url)

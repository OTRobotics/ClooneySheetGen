import requests  # Must be installed via pip.


class FRCAPI:
    path = ""
    s = requests.Session()  # This prevents us from repeatedly opening and closing a socket
    tbaBaseURL = 'https://www.thebluealliance.com/api/v3/'
    frcEventsBaseURL = 'https://frc-api.firstinspires.org/v2.0/'

    def __init__(self, tba, frc):
        self.tba = tba
        self.frc = frc
        self.header = {
            'X-TBA-Auth-Key': tba,
            'Authorization': 'Basic ' + frc,
            'Accept': 'application/json'
        }

    def getTBA(self, url):
        return self.s.get(self.tbaBaseURL + url, headers=self.header).json()

    def getFRCEvents(self, url):
        req = self.s.get(self.frcEventsBaseURL + url, headers=self.header)
        print (url)
        if req.status_code >= 400:
            print(req.status_code)
            return "401"
        return req.json()

    def getEventName(self, event):
        events = self.getFRCEvents("2018/events?eventCode=" + event)
        if str(events).startswith("Invalid Event Requested") or str(events).startswith("401"):
            return None

        event = events['Events'][0]
        return event["name"]

    def getFRCSchedule(self, event):
        schedule = self.getFRCEvents("2018/schedule/" + event + "?tournamentLevel=qual")
        if str(schedule).startswith("Invalid Event Requested") or str(schedule).startswith("401"):
            return None

        matches = schedule['Schedule']

        schedule = {

        }
        for match in matches:
            number = match['matchNumber']
            teams = match['teams']
            stations = {
                'Red1': '',
                'Red2': '',
                'Red3': '',
                'Blue1': '',
                'Blue2': '',
                'Blue3': ''
            }
            for team in teams:
                stations[team['station']] = team['teamNumber']
                schedule[number] = stations
        return schedule

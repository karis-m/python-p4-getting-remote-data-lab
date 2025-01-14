import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        # print(response.content)
        return response.content
    
    def load_json(self):
        peoples_list = []

        people = json.loads(self.get_response_body())
        
        for person in people:
            peoples_list.append(person)
            print(peoples_list)
        return peoples_list

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()

# get_requester.get_response_body()
import json 
import facebook

ACCESS_TOKEN = "EAACI2oZAFAyABALCZB7fF9juDj9uR4ZAe4oDHO3JZBrXlYEBiZCbvKgd7cwze05PnYJ8WTZCseLYFfZBu7u5qj4JbvZBFs8Ot4VHcyCKqR7HoDiXHo9TuoMvyYpVWWMWyYjWi9O2vaQWAHZCrvrqqRWIZBK7T0ZAe9uJRMZD"

def main():
    token = ACCESS_TOKEN
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me',fields='first_name,location,link,email,posts')

    print("Printing profile: ")
    print(type(profile))

    print(json.dumps(profile,indent=4))
    print(type(json.dumps(profile,indent=4)))

if __name__ == '__main__':
        main()




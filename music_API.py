import requests
import json
import sqlite3

url = "https://musicbrainz.org/ws/2/artist/"
pay_load = {'query': 'Thom Yorke', 'fmt': 'json'}
response = requests.get(url, params=pay_load)
print("Status Code:", response.status_code)
print("Headers:", response.headers)
print("Response Text:", response.text)

content = response.json()
print(json.dumps(content, indent=4))

with open('artist_data.json', 'w') as f:
    json.dump(content, f, indent=4)

print("Artist Name:", content["artists"][0]["name"])
print("Artist ID:", content["artists"][0]["id"])
print("Artist Type:", content["artists"][0]["type"])



conn = sqlite3.connect('artists.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Artist 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              gender TEXT,
              type TEXT,
              birth_year INTEGER,
              nationality TEXT)''')

c.execute("INSERT INTO Artist (name, gender, type, birth_year, nationality) VALUES ('Thom Yorke', 'Male', 'Person', 1968, 'English')")

conn.commit()
conn.close()




 















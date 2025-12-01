# Fetch Input
import requests

SESSION_COOKIE = "53616c7465645f5f5d4b262b6473136e17634719c6129df046cd548d781b5b4523d9326759da7574a67d8dc5176ec4d122d9420f3e04c5a92b9e00ca2670dd58"

url = "https://adventofcode.com/2025/day/1/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers).text


# Store Input In List
input = response.split('\n')
start = 50
for i in range(0,len(input)-1):
    # string number 
    sez = input[i].strip('RL')
    sez = int(sez)
 
    if 'R' in input[i]:
        if 99-start > sez :
            pass
        
    else:
        pass
    
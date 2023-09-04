import os
import requests
from replit import db

def get_result(query):
  app_id = os.environ['AppID']
  base_url = "http://api.wolframalpha.com/v1/result"
  params = {
      "i": query,
      "appid": app_id,
  }
    
  response = requests.get(base_url, params=params)
    
  if response.status_code == 200:
    try:
      db["Proper Result"] = True
      return response.text
    except Exception as e:
      db["Proper Result"] = False
      print(f"An unexpected error occurred: {e}")
      return f"Error: Received status code {response.status_code}"
  elif response.status_code == 501:
    db["Proper Result"] = False
    return "The input value cannot be interpreted by the API."
  elif response.status_code == 400:
    db["Proper Result"] = False
    return "The API did not find an input parameter while parsing."
  else:
    db["Proper Result"] = False
    print(f"Received unexpected status code {response.status_code}: {response.text}")
    return f"Error: Received status code {response.status_code}"
import os

# Retrieve API key from the environment
rapidapi_key = os.getenv("RAPIDAPI_KEY")

if not rapidapi_key:
    raise ValueError("RAPIDAPI_KEY not found! Make sure it's set as an environment variable.")

print(f"API Key Loaded Successfully: {rapidapi_key[:5]}********")

import requests
import os

class PropertyAnalysis:
    def __init__(self):
        self.properties = []
        self.rapidapi_key = os.getenv("RAPIDAPI_KEY")  # Fetch API key

        if not self.rapidapi_key:
            raise ValueError("RAPIDAPI_KEY not found! Ensure it is set as an environment variable.")

    def fetch_property_data(self, zpid):
        """Fetch property details from Zillow API using RapidAPI"""
        url = "https://zillow-com1.p.rapidapi.com/property"
        params = {"zpid": zpid}  # Property ID (ZPID)

        headers = {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": "zillow-com1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if data:
                return {
                    'Address': data.get("address", "Unknown"),
                    'Purchase Price': data.get("price", 250000),
                    'Expected Rent': data.get("rentZestimate", 1800),
                    'Monthly Expenses': 300,  # Default value, can be improved
                    'Vacancy Rate': 0.05,
                    'Maintenance Rate': 0.1,
                    'Management Fee Rate': 0.1
                }
        else:
            print(f"Failed to fetch data for ZPID {zpid}. Response: {response.text}")
        
        return None

# Usage Example
property_analysis = PropertyAnalysis()
zpid = "19971282"  # Example Zillow Property ID
property_data = property_analysis.fetch_property_data(zpid)

if property_data:
    print("Property Data Retrieved:", property_data)

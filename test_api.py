import requests

url = "https://roshni-sts-api.hf.space/"

data = {
    "text1": "India won the cricket match yesterday.",
    "text2": "The cricket game was won by India last night."
}

response = requests.post(url, json=data)

# Print raw response
print("Raw response:", response.text)

# Convert to JSON
try:
    print("JSON response:", response.json())
except Exception as e:
    print("JSON decode error:", e)

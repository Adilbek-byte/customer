import requests

url = "https://example.com/custom_data.csv"
response = requests.get(url)

if response.status_code == 200:
    with open("custom_data.csv", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    print("Failed to download file")

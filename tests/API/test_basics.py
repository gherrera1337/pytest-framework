import requests, json

baseURI = "https://petstore.swagger.io/v2/pet/"
petID = "1"

# Test to get pets by ID
def test_getPetById():
    url = baseURI + petID
    headers = {"Content-Type": "application/json"}

    print("\n Request URL: ", url)
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent= 3))

    assert data["id"] == 1


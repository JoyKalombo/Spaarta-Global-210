import json

# The following code shows how to convert from JSON to PythonDictionary
# some random JSON object (which is essentially a big string of key:value pairs):
europe = '{' \
         '"country":"France", ' \
         '"capital":"Paris", ' \
         '"language(s)_spoken":"French"' \
         '}'

# parse europe(this will convert from JSON to Python Dictionary
pythonDictionary = json.loads(europe)

print(pythonDictionary["capital"])
# End of code

#The following code shows how to convert from pythonDictionary to JSON
# some random python object(aka a dictionary):
southAmerica = {
    "country": "Argentina",
    "capital": "Buenos Aires",
    "language(s)_spoken": "Spanish"
}

#parse southAmerica into the following method to convert from python Dictionary to JSON object
JSON = json.dumps(southAmerica)

print(JSON)

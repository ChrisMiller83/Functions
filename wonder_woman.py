superhero = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
    }
}

lasso = superhero["gear"][0]
print(lasso)

for item in superhero["gear"]:
    print("%s has %s" % (superhero["name"], item))
states = {
    "CA": {},
    "VA": {},
    "MD": {},
    "RI": {},
    "NV": {}
}

print(states["CA"])
print(states["NV"])

nested_dictionary = {
    "CA": {
        "NAME": "Californa",
        "POPULATION": 398648290
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1000600
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 5000000
    }

}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["CA"]["NAME"])

nested_dictionary = {
    "CA": {
        "NAME": "Californa",
        "POPULATION": 398648290,
        "CITIES": [
            "Fresno"
            " San Fransico"
            " Los Angles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000,
        "CITIES": [
            "Richmond"
            "Norfolk"
            "Alexandria"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000,
        "CITIES": [
            "Bethesda",
            "Newport",
            "Warwick"

        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1000600,
        "CITIES": {}
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 5000000
    }

}
print(nested_dictionary["MD"]["CITIES"][0])
print(nested_dictionary["VA"]["NAME"])

print(nested_dictionary.keys())
print(nested_dictionary.items())

print()
for key, value in nested_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

# We're going to make this look great...
for states, facts in nested_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print("=" * 20)

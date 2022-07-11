RULES_SETUP = {
    "no_income": {
        "turns_ineligible": ["disability"]
    },
    "no_vehicle": {
        "turns_ineligible": ["auto"]
    },
    "no_house": {
        "turns_ineligible": ["home"]
    },
    "advanced_age": {
        "turns_ineligible": ["disability", "life"]
    },
    "young_age": {
        "score_impacts": {
            "life": -2,
            "disability": -2,
            "home": -2,
            "auto": -2
        }
    },
    "middle_age": {
        "score_impacts": {
            "life": -1,
            "disability": -1,
            "home": -1,
            "auto": -1
        }
    },
    "high_income": {
        "score_impacts": {
            "life": -1,
            "disability": -1,
            "home": -1,
            "auto": -1
        }
    },
    "mortgaged_house": {
        "score_impacts": {
            "disability": 1,
            "home": 1
        }
    },
    "has_dependents": {
        "score_impacts": {
            "disability": 1,
            "life": 1
        }
    },
    "is_married": {
        "score_impacts": {
            "disability": -1,
            "life": 1
        }
    },
    "new_vehicle": {
        "score_impacts": {
            "auto": 1
        }
    }
}
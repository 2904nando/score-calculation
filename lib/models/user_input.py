import datetime

class UserInput:

    class FIELDS_AND_VALUES:
        SINGLE = 'single'
        MARRIED = 'married'
        HOUSE_OWNERSHIP_STATUS_FIELD = 'ownership_status'
        OWNED = 'owned'
        MORTGAGED = 'mortgaged'
        VEHICLE_YEAR_FIELD = 'year'
        MARITAL_STATUS_VALUES = [SINGLE, MARRIED]
        HOUSE_STATUS_VALUES = [OWNED, MORTGAGED]

    def __init__(self,
        age=None,
        dependents=None,
        house=None,
        income=None,
        marital_status=None,
        risk_questions=None,
        vehicle=None
    ):
        self.age = age
        self.dependents = dependents
        self.house = house
        self.income = income
        self.marital_status = marital_status
        self.risk_questions = risk_questions
        self.vehicle = vehicle

        if not self._validateInputs():
            raise Exception('Invalid Input!')

        self.startingInsuranceScore = sum(self.risk_questions)

    @property
    def no_income(self):
        return not self.income

    @property
    def no_house(self):
        return not self.house
    
    @property
    def no_vehicle(self):
        return not self.vehicle

    @property
    def advanced_age(self):
        return self.age > 60

    @property
    def young_age(self):
        return self.age < 30

    @property
    def middle_age(self):
        return self.age >= 30 and self.age < 40
    
    @property
    def high_income(self):
        return self.income > 200000
    
    @property
    def mortgaged_house(self):
        if self.house:
            return self.house.get(UserInput.FIELDS_AND_VALUES.HOUSE_OWNERSHIP_STATUS_FIELD, "") == UserInput.FIELDS_AND_VALUES.MORTGAGED
        else:
            return False

    @property
    def has_dependents(self):
        return self.dependents > 0

    @property
    def is_married(self):
        return self.marital_status == UserInput.FIELDS_AND_VALUES.MARRIED
    
    @property
    def new_vehicle(self):
        if self.vehicle:
            now = datetime.datetime.now()
            vehicle_age = now.year - self.vehicle.get(UserInput.FIELDS_AND_VALUES.VEHICLE_YEAR_FIELD, 0)
            return vehicle_age <= 5
        else:
            return False

    def _validateInputs(self):
        if not self._validate_numeric_field(self.age):
            return False
        if not self._validate_numeric_field(self.dependents):
            return False
        if not self._validate_numeric_field(self.income):
            return False
        if not self._validate_marital_status_field():
            return False
        if not self._validate_risk_answers_field():
            return False
        if not self._validate_house_field():
            return False
        if not self._validate_vehicle_field():
            return False
        
        return True

    def _validate_numeric_field(self, fieldValue):
        if not isinstance(fieldValue, int) or fieldValue < 0:
            return False
        return True
    
    def _validate_marital_status_field(self):
        if not isinstance(self.marital_status, str) or self.marital_status not in UserInput.FIELDS_AND_VALUES.MARITAL_STATUS_VALUES:
            return False
        return True

    def _validate_risk_answers_field(self):
        if (not isinstance(self.risk_questions, list) or
            len(self.risk_questions) != 3 or
            len([answer for answer in self.risk_questions if answer in [0,1]]) != 3
        ):
            return False
        return True

    def _validate_house_field(self):
        if not self.house:
            return True
        houseStatus = self.house.get(UserInput.FIELDS_AND_VALUES.HOUSE_OWNERSHIP_STATUS_FIELD, None)
        if (isinstance(self.house, dict) and 
            isinstance(houseStatus, str) and
            houseStatus in UserInput.FIELDS_AND_VALUES.HOUSE_STATUS_VALUES
        ):
            return True
        return False

    def _validate_vehicle_field(self):
        if not self.vehicle:
            return True
        vehicleYear = self.vehicle.get(UserInput.FIELDS_AND_VALUES.VEHICLE_YEAR_FIELD, None)
        if (isinstance(self.vehicle, dict) and 
            isinstance(vehicleYear, int)
        ):
            return True
        return False
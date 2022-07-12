class Insurance:

    class SCORE:
        INELIGIBLE = 'ineligible'
        ECONOMIC = 'economic'
        REGULAR = 'regular'
        RESPONSIBLE = 'responsible'

    def __init__(self, insuranceName:str=None, startingScore:int=None):
        self.score = startingScore
        self.insuranceName = insuranceName
        self.ineligibleStatus = False

    @property
    def calculated_risk(self):
        return Insurance.SCORE.INELIGIBLE if self.ineligibleStatus else self.calculate_score()

    def setIneligible(self):
        self.ineligibleStatus = True
    
    def addPoints(self, points: int):
        if not self.ineligibleStatus:
            self.score += points

    def calculate_score(self):
        if self.score <= 0:
            return Insurance.SCORE.ECONOMIC
        elif self.score == 1 or self.score == 2:
            return Insurance.SCORE.REGULAR
        elif self.score >= 3:
            return Insurance.SCORE.RESPONSIBLE
from lib.models.user_input import UserInput

from config.config import RULES_SETUP

class InsuranceRiskRules:

    class CONFIGS:
        TURNS_INELIGIBLE = "turns_ineligible"
        SCORE_IMPACTS = "score_impacts"

    def __init__(self, userInput: UserInput, insurancesList):
        self.userInput = userInput
        self.insurancesList = insurancesList

    def calculate_insurance_risks(self):
        for ruleName, ruleConfig in RULES_SETUP.items():
            if getattr(self.userInput, ruleName):
                self._apply_rule(ruleConfig)
        return self.insurancesList
    
    def _apply_rule(self, ruleConfig:dict):
        ineligibleList = ruleConfig.get(InsuranceRiskRules.CONFIGS.TURNS_INELIGIBLE, [])
        for insurance in self.insurancesList:
            if insurance.insuranceName in ineligibleList:
                insurance.setIneligible()
        impactedScores = ruleConfig.get(InsuranceRiskRules.CONFIGS.SCORE_IMPACTS, {})
        for insurance in self.insurancesList:
            insurance.addPoints(impactedScores.get(insurance.insuranceName, 0))
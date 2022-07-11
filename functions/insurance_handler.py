from lib.models.insurance import Insurance
from lib.models.user_input import UserInput
from lib.models.insurance_risk_rule import InsuranceRiskRules

def calculate_scores(userInput):
    validatedUserInput = UserInput(**userInput)
    startingInsuranceScore = validatedUserInput.startingInsuranceScore

    insurances = _build_insurances(['auto', 'disability', 'home', 'life'], startingInsuranceScore)
    calculatedInsurances = _apply_rules(userInput=validatedUserInput, insurancesList=insurances)

    return {
        insurance.insuranceName: insurance.calculated_risk
        for insurance in calculatedInsurances
    }

def _build_insurances(insurancesList, startingScore):
    return [Insurance(insuranceName=insurance, startingScore=startingScore) for insurance in insurancesList]

def _apply_rules(userInput, insurancesList):
    insuranceRules = InsuranceRiskRules(userInput=userInput, insurancesList=insurancesList)
    insuranceRules.calculate_insurance_risks()
    return insuranceRules.insurancesList
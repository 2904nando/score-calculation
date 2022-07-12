import pytest
from lib.models.user_input import UserInput

class TestUserInput():
    @pytest.mark.parametrize('field,    input,                              function,                           pass_param, expected_result', [
        pytest.param("age",             10,                                 "_validate_numeric_field",          True,       True,           id='01 - numeric_success'),
        pytest.param("age",             0,                                  "_validate_numeric_field",          True,       True,           id='02 - numeric_success_2'),
        pytest.param("age",             -1,                                 "_validate_numeric_field",          True,       False,          id='03 - numeric_fail_negative'),
        pytest.param("age",             "fail",                             "_validate_numeric_field",          True,       False,          id='04 - numeric_fail_type'),
        pytest.param("house",           {"ownership_status": "mortgaged"},  "_validate_house_field",            False,      True,           id='05 - house_success'),
        pytest.param("house",           {"ownership_status": "owned"},      "_validate_house_field",            False,      True,           id='06 - house_success_2'),
        pytest.param("house",           {"fail": "fail"},                   "_validate_house_field",            False,      False,          id='07 - house_fail_invalid'),
        pytest.param("house",           "fail",                             "_validate_house_field",            False,      False,          id='08 - house_fail_type'),
        pytest.param("house",           None,                               "_validate_house_field",            False,      True,           id='09 - house_success_none'),
        pytest.param("marital_status",  "married",                          "_validate_marital_status_field",   False,      True,           id='10 - marital_success'),
        pytest.param("marital_status",  "single",                           "_validate_marital_status_field",   False,      True,           id='11 - marital_success_2'),
        pytest.param("marital_status",  "fail",                             "_validate_marital_status_field",   False,      False,          id='12 - marital_fail_type'),
        pytest.param("risk_questions",  [0,0,0],                            "_validate_risk_answers_field",     False,      True,           id='13 - risk_success'),
        pytest.param("risk_questions",  [0,0],                              "_validate_risk_answers_field",     False,      False,          id='14 - risk_fail_invalid'),
        pytest.param("risk_questions",  ["fail", "fail", "fail"],           "_validate_risk_answers_field",     False,      False,          id='15 - risk_fail_invalid_2'),
        pytest.param("risk_questions",  "fail",                             "_validate_risk_answers_field",     False,      False,          id='16 - risk_fail_type'),
        pytest.param("vehicle",         {"year": 2018},                     "_validate_vehicle_field",          False,      True,           id='17 - vehicle_success'),
        pytest.param("vehicle",         {"fail": 2018},                     "_validate_vehicle_field",          False,      False,          id='18 - vehicle_fail_invalid'),
        pytest.param("vehicle",         {"year": -1},                       "_validate_vehicle_field",          False,      False,          id='19 - vehicle_fail_invalid_2'),
        pytest.param("vehicle",         "fail",                             "_validate_vehicle_field",          False,      False,          id='20 - vehicle_fail_type'),
        pytest.param("vehicle",         None,                               "_validate_vehicle_field",          False,      True,           id='21 - vehicle_success_none'),
    ])
    def test_user_input_validations(self, field, input, function, pass_param, expected_result):
        baseUserInput = UserInput(
            age=0, dependents=0, house=None, income=0,
            marital_status='married', risk_questions=[0,0,0],
            vehicle=None
        )
        setattr(baseUserInput, field, input)
        params = [] if not pass_param else [input]
        result = getattr(baseUserInput, function)(*params)

        assert(result == expected_result)
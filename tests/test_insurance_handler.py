import pytest
from functions import insurance_handler as InsuranceHandler

class TestGeneralScenarios():
    @pytest.mark.parametrize('mock_loader_params', [
        pytest.param({'input': 'base_case',     'output': 'base_case'},     id='01 - base_case'),
        pytest.param({'input': 'no_house',      'output': 'no_house'},      id='02 - no_house'),
        pytest.param({'input': 'no_vehicle',    'output': 'no_vehicle'},    id='03 - no_vehicle'),
        pytest.param({'input': 'with_income',   'output': 'with_income'},   id='04 - with_income'),
        pytest.param({'input': 'over_60',       'output': 'over_60'},       id='05 - over_60'),
        pytest.param({'input': 'young_age',     'output': 'young_age'},     id='06 - young_age'),
    ])
    def test_calculate_scores_success(self, mock_loader_params, mock_loader):
        result = InsuranceHandler.calculate_scores(mock_loader['input'])
        assert result == mock_loader['output']
    
    @pytest.mark.parametrize('mock_loader_params,   expected_exception', [
        pytest.param({'input': 'fail_numeric_age'},         Exception,       id='01 - fail_age'),
        pytest.param({'input': 'fail_numeric_dependents'},  Exception,       id='02 - fail_dependents'),
        pytest.param({'input': 'fail_numeric_dependents'},  Exception,       id='03 - fail_dependents'),
        pytest.param({'input': 'fail_house_key'},           Exception,       id='04 - fail_house_key'),
        pytest.param({'input': 'fail_house_value'},         Exception,       id='05 - fail_house_value'),
        pytest.param({'input': 'fail_numeric_income'},      Exception,       id='06 - fail_numeric_income'),
        pytest.param({'input': 'fail_marital_value'},       Exception,       id='07 - fail_marital_value'),
        pytest.param({'input': 'fail_risk'},                Exception,       id='08 - fail_risk'),
        pytest.param({'input': 'fail_vehicle_key'},         Exception,       id='09 - fail_vehicle_key'),
        pytest.param({'input': 'fail_vehicle_value'},       Exception,       id='10 - fail_vehicle_value'),
    ])
    def test_calculate_scores_fail(self, mock_loader_params, mock_loader, expected_exception):
        pytest.raises(expected_exception, InsuranceHandler.calculate_scores, mock_loader['input'])
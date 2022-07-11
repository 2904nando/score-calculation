import pytest
from functions import insurance_handler as InsuranceHandler
import json

class TestGeneralScenarios():
    @pytest.mark.parametrize('mock_loader_params', [
        pytest.param({'input': 'base_case', 'output': 'base_case'}, id='01 - base_case')
    ])
    def test_calculate_scores_success(self, mock_loader_params, mock_loader):
        result = InsuranceHandler.calculate_scores(mock_loader['input'])
        assert result == mock_loader['output']
    
    @pytest.mark.parametrize('mock_loader_params,   expected_exception', [
        pytest.param({'input': 'fail_numeric'},        Exception,                 id='01 - base_case')
    ])
    def test_calculate_scores_fail(self, mock_loader_params, mock_loader, expected_exception):
        pytest.raises(expected_exception, InsuranceHandler.calculate_scores, mock_loader['input'])
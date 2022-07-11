import json
import pytest

import os 

here = os.path.dirname(os.path.realpath(__file__))
MOCKS_FOLDER = os.path.join(here, '..', 'mocks')

@pytest.fixture
def mock_loader(request):
    mock_files = request.node.funcargs['mock_loader_params']

    result = {}
    for folder, file in mock_files.items():
        with open(os.path.join(MOCKS_FOLDER, folder, f'{file}.json'),'r',encoding="utf-8") as fp:
            result[folder] = json.loads(fp.read())
    
    return result
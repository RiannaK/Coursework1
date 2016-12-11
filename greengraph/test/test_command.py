import sys
from mock import patch
from greengraph.command import process as sut
from matplotlib import pyplot as plt
from greengraph.graph import Greengraph
import yaml
import os

@patch.object(plt, 'plot')
@patch.object(plt, 'xlabel')
@patch.object(plt, 'ylabel')
@patch.object(plt, 'title')
@patch.object(plt, 'show')
@patch.object(plt, 'savefig')
@patch.object(Greengraph, 'green_between')
def test_command_process(mock_green_between, mock_savefig, mock_show, mock_title, mock_ylabel, mock_xlabel, mock_plot):
    """Tests the command line entry point"""
    # Arrange
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_command_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_command_process']

    for fixture in fixtures:

        mock_args = fixture.pop('mock_args')
        steps = fixture.pop('steps')
        title = fixture.pop('title')
        output = fixture.pop('output')

        sys.argv = mock_args

        # Act
        sut()

        # Assert
        mock_green_between.assert_called_with(steps)
        mock_title.assert_called_with(title)
        mock_savefig.assert_called_with(output)

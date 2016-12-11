import sys
from mock import patch
from greengraph.command import process as sut
from matplotlib import pyplot as plt
from greengraph.graph import Greengraph


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
    mock_args = ["some_file.py", "--from", "Bristol", "--to", "Cambridge", "--steps", "5", "--out", "some_file.png"]
    sys.argv = mock_args

    # Act
    sut()

    # Assert
    mock_green_between.assert_called_with(5)
    mock_title.assert_called_with("Graph of green pixel count from Bristol to Cambridge")
    mock_savefig.assert_called_with("some_file.png")



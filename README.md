Assignment 1: Greengraph
========================

| Branch | Status | Coverage | 
| ------ | ------ | -------- |
| Master |[![Build Status](https://travis-ci.org/RiannaK/Coursework1.svg?branch=master)](https://travis-ci.org/RiannaK/Coursework1)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework1/badge.svg?branch=master)](https://coveralls.io/github/RiannaK/Coursework1?branch=master) |
| Develop |[![Build Status](https://travis-ci.org/RiannaK/Coursework1.svg?branch=develop)](https://travis-ci.org/RiannaK/Coursework1)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework1/badge.svg?branch=develop)](https://coveralls.io/github/RiannaK/Coursework1?branch=develop) |

###What does it do?
Greengraph's aim is to show the amount of green between two places. It is based on the number of green pixels within satellite images that are taken at a given number of steps between two specified places. The output shows a plot of the green pixel count at each step, indicating how green the space between the two places is. 

The example below shows the green pixel count between Bristol, UK and Cambridge, UK when considering 50 steps between them:

<img src="https://github.com/RiannaK/Coursework1/blob/master/Resources/Bristol_Cam_50.png" alt="Sample output from greengraph script" width="50%" height="50%"/>

###How to Install

There are two options to install the package: manually download and install, or install directly from GitHub using the standard pip command.

Downloading from GitHub?
 
 * Download the package as a zip file from GitHub
 * From the command line, install using the following command:
	- For Windows users ```python setup.py install```
	- For Mac and Linux ```sudo python setup.py install```
 
Installing directly from GitHub?
 
 * Type ```pip install git+git://github.com/RiannaK/Coursework1.git``` into the terminal


###How to Use

Once installed, the greengraph script can be called from the command line using the following syntax:

```graph --from Bristol --to Cambridge --steps 50 --out Bristol_Cam_50.png```

Firstly, consider the two places to analyse, and in how many steps? In the above, Bristol and Cambridge, in 50 steps, were chosen.

There are four command line arguments:

| Arg long | Arg short |    Default     | 
| -------- | ----------| -------------- |
| --from   |   -f      | London         | 
| --to     |   -t      | Oxford         | 
| --steps  |   -s      | 10             | 
| --out    |   -o      | GreenGraph.png | 


If an input is not specified it will run with the default. 
For example, if only ```graph --from Bristol ``` was input, the output will be returned as though ```graph --from Bristol --to Oxford --steps 10 --out GreenGraph.png``` had been input.

The output graph will be generated automatically as a pop-up on the screen, and will also be saved in the current directory. Unless specified, the default file name for this image is 'GreenGraph.png'.

This assignment was completed as part of the UCL [MPHYG0001: Research Software Engineering with Python course] (http://github-pages.ucl.ac.uk/rsd-engineeringcourse/).

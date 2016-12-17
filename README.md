Assignment 1: Greengraph
========================

| Branch | Status | Coverage | 
| ------ | ------ | -------- |
| Master |[![Build Status](https://travis-ci.org/RiannaK/Coursework1.svg?branch=master)](https://travis-ci.org/RiannaK/Coursework1)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework1/badge.svg?branch=master)](https://coveralls.io/github/RiannaK/Coursework1?branch=master) |
| Develop |[![Build Status](https://travis-ci.org/RiannaK/Coursework1.svg?branch=develop)](https://travis-ci.org/RiannaK/Coursework1)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework1/badge.svg?branch=develop)](https://coveralls.io/github/RiannaK/Coursework1?branch=develop) |

###What does it do?
Greengraph's aim is to show the amount of green between two places. It is based on the number of green pixels within satellite images that are taken at a given number of steps between two specified places. The output shows a plot of the green pixel count at each step, indicating how green the space between the two places is. 

The example below shows the green pixel count between Bristol, UK and Cambridge, UK when considering 10 steps between them:

![insert image of output graph of Briz to Cam in 10 steps] <img src=>

###How to Install

There are two options to install the package: manually download and install, or install directly from GitHub using the standard pip command.

 Downloading from GitHub?
 
 * Download the package as a zip file from GitHub
 * Go to command line and install using the following command:
	- For Windows users ```python setup.py install```
	- For Mac and other users ```sudo python setup.py install``` 
 * Then 
 * See below for an example of how to use the library
 
 Installing directly from GitHub?
 
 * Type (sudo - needed?) ```pip install git+git://github.com/RiannaK/Coursework1.git``` into the terminal
 * Then 
 * See below for an example of how to use the library

###How to Use

Ultimately the command line will look something like this:

```graph --from Bristol --to Cambridge --steps 10 --out Bristol_Cam_10.png ```

Firstly, consider the two places to analyse, and in how many steps? In the above, Bristol and Cambridge, in 10 steps, were chosen.

There are four command line arguments:

| Input long | Input short |    Default    | 
| ---------- | ----------- | ------------- |
| --from     |   -f        | London        | 
| --to       |   -t        | Oxford        | 
| --steps    |   -s        | 10            | 
| --out      |   -o        | GreenGraph.py | 


If an input is not specified it will run with the default. 
For example, if only ```graph --from Bristol ``` was input, the output will be returned as though ```graph --from Bristol --to Oxford --steps 10 --out GreenGraph.png``` had been input.

The output graph will be generated automatically as a pop-up on the screen, and will also be saved in the file location of the script (i.e. where it was called?). Unless specified, the default file name for this image is 'GreenGraph.png'.



This assignment was completed as part of the UCL [MPHYG0001: Research Software Engineering with Python course] (http://github-pages.ucl.ac.uk/rsd-engineeringcourse/).

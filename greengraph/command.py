from matplotlib import pyplot as plt
from argparse import ArgumentParser
from greengraph.graph import Greengraph


def process():
    # Create the argument parser.
    parser = ArgumentParser(
        description="Command line tool for generating a measure of the amount of green between two cities.")

    # Now we add the arguments.
    parser.add_argument('-f', '--from', type=str, default='London', dest='FROM', help='location to plot green from')

    parser.add_argument('-t', '--to', type=str, default='Oxford', help='location to plot green to')

    parser.add_argument('-s', '--steps', type=int, default=10,
                        help='the number of points to sample between the two locations')

    parser.add_argument('-o', '--out', type=str, default='GreenGraph.png',
                        help='the file name for the PNG file. File must end in .png')

    # Parse the args
    arguments = parser.parse_args()

    # Run the main body of code
    my_graph = Greengraph(arguments.FROM, arguments.to)
    data = my_graph.green_between(arguments.steps)

    # Create the plot
    title = 'Graph of green pixel count from {0} to {1}'.format(arguments.FROM, arguments.to)
    plt.plot(data)
    plt.xlabel('Step')
    plt.ylabel('Green pixels')
    plt.title(title)
    plt.show()
    plt.savefig(arguments.out) # fixme no image is shown

if __name__ == "__main__":
    process()

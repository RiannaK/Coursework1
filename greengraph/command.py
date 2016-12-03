from matplotlib import pyplot as plt
from argparse import ArgumentParser
from greengraph.graph import Greengraph


def process():

    # greengraph --from London --to Oxford --steps 10 --out graph.png
    parser = ArgumentParser(description="Graph green between cities")

    parser.add_argument('--from1',   '-f')
    parser.add_argument('--to',     '-t')
    parser.add_argument('--steps',  '-s')
    parser.add_argument('--out',    '-o')

    arguments = parser.parse_args()

    my_graph = Greengraph(arguments.from1, arguments.to)
    data = my_graph.green_between(arguments.steps)
    plt.plot(data)

if __name__ == "__main__":
    process()

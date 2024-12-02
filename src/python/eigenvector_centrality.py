#/usr/bin/env python3
import argparse
import csv


class Graph:
    def __init__(self, w, h):
        self.graph = [[0 for x in range(w)] for y in range(h)]

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u][v] = 1

    def eigenvector_centrality(self):
        new_eigencentres = [0 for x in range(len(self.graph))]
        old_eigencentres = [0 for x in range(len(self.graph))]
        print("Iteration 1")
        for i in range(len(self.graph)):
            score = 0
            for j in range(len(self.graph)):
                score += self.graph[i][j]*(old_eigencentres[j] if old_eigencentres[j] != 0 else 1)
            new_eigencentres[i] = score
        print(new_eigencentres)
        for i in range(len(old_eigencentres)):
            old_eigencentres[i] = new_eigencentres[i]

        print("Iteration 2")
        for i in range(len(self.graph)):
            score = 0
            for j in range(len(self.graph)):
                score += self.graph[i][j]*(old_eigencentres[j] if old_eigencentres[j] != 0 else 1)
            new_eigencentres[i] = score
        print(new_eigencentres)
        for i in range(len(old_eigencentres)):
            old_eigencentres[i] = new_eigencentres[i]

        print("Iteration 3")
        for i in range(len(self.graph)):
            score = 0
            for j in range(len(self.graph)):
                score += self.graph[i][j]*(old_eigencentres[j] if old_eigencentres[j] != 0 else 1)
            new_eigencentres[i] = score
        print(new_eigencentres)
        for i in range(len(old_eigencentres)):
            old_eigencentres[i] = new_eigencentres[i]

        print("Iteration 4")
        for i in range(len(self.graph)):
            score = 0
            for j in range(len(self.graph)):
                score += self.graph[i][j]*(old_eigencentres[j] if old_eigencentres[j] != 0 else 1)
            new_eigencentres[i] = score
        print(new_eigencentres)
        for i in range(len(old_eigencentres)):
            old_eigencentres[i] = new_eigencentres[i]

graph = None

def main():
    args = configure_arguments()
    graph = load_graph(args)
    graph.eigenvector_centrality()

def load_graph(args):
    with open(args.nodes) as nodes:
        reader = csv.DictReader(nodes)
        dimension = len(list(reader)) + 1
        graph = Graph(dimension, dimension)
    with open(args.edges) as edges:
        reader = csv.DictReader(edges)
        for row in reader:
            graph.add_edge(int(row['station1']) - 1, int(row['station2']) - 1)
            graph.add_edge(int(row['station2']) - 1, int(row['station1']) - 1)
    return graph


def configure_arguments():
    parser = argparse.ArgumentParser(
        prog='eigenvector_centrality',
        description='Claculate the eigenvector centrality of a graph')
    parser.add_argument('nodes', type=str, help='File with the nodes')
    parser.add_argument('edges', type=str, help='File with the edges')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()

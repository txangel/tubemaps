#/usr/bin/env python3
import argparse
import csv


class Graph:
    def __init__(self, w, h):
        self.graph = [[0 for x in range(w)] for y in range(h)]

    def add_edge(self, in_u, in_v):
        u = in_u - 1
        v = in_v - 1
        if u not in self.graph:
            self.graph[u][v] = 1

    def eigenvector_centrality(self):
        new_eigencentres = self.init_eigenvector()
        old_eigencentres = self.init_eigenvector()
        for iteration in range(5000):
            sum = 0
            for i in range(len(self.graph)):
                score = 0
                for j in range(len(self.graph)):
                    score += self.graph[i][j]*(old_eigencentres[j]['score'] if old_eigencentres[j]['score'] != 0 else 1)
                    sum += score
                new_eigencentres[i]['score'] = score
            for x in new_eigencentres:
                x['score'] = x['score']/sum

            diff = 0
            for i,x in enumerate(old_eigencentres):
                diff += abs(x['score'] - new_eigencentres[i]['score'])
            if diff < 0.000000001:
                break

            for i,x in enumerate(old_eigencentres):
                x['score'] = new_eigencentres[i]['score']


        return sorted(new_eigencentres, key=lambda x: x['score'], reverse=True)

    def init_eigenvector(self):
        eigenvector = []
        for i in range(1, len(self.graph)+1, 1):
            eigenvector.append({'name': self.index[i] if i in self.index else 'UNKNOWN', 'score': 0})
        return eigenvector

    def set_index(self, index):
        self.index = index


def main():
    args = configure_arguments()
    graph = load_graph(args)
    eigenvector_centers = graph.eigenvector_centrality()

    for x in eigenvector_centers:
        print("{}, {}".format(x['name'], x['score']))

def load_graph(args):

    with open(args.nodes) as nodes:
        reader = csv.DictReader(nodes)
        dimension = 0
        index = {}
        for row in reader:
            id = int(row['id'])
            index[id] = row['name']
            if  id > dimension:
                dimension = id

        graph = Graph(dimension, dimension)
        graph.set_index(index)
    with open(args.edges) as edges:
        reader = csv.DictReader(edges)
        for row in reader:
            graph.add_edge(int(row['station1']), int(row['station2']))
            graph.add_edge(int(row['station2']), int(row['station1']))
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

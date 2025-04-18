import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

STATIONS_PATH = "data/railway_stations.csv"
TRACKS_PATH = "data/railway_tracks.csv"

REDUCE_DATA_FOR_DRAWING = True

nodesFrame = pd.read_csv(STATIONS_PATH)
edgesFrame = pd.read_csv(TRACKS_PATH)

graph = nx.Graph()

for index, row in edgesFrame.iterrows():
    # Add nodes if they don't exist
    if not graph.has_node(row['Station_A']):
        graph.add_node(row['Station_A'])
    if not graph.has_node(row['Station_B']):
        graph.add_node(row['Station_B'])
    # Add edge with weight
    graph.add_edge(row['Station_A'], row['Station_B'], weight=row['Length'])

nx.draw(graph, with_labels=True)
plt.show()
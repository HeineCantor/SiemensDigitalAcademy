import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

STATIONS_PATH = "data/railway_stations.csv"
TRACKS_PATH = "data/railway_tracks.csv"
TRAIN_TABLE_PATH = "data/train_table.csv"

REDUCE_DATA_FOR_DRAWING = False
LABELS_SHOWN = False

SELECTED_TRAIN_ID = None

nodesFrame = pd.read_csv(STATIONS_PATH)
edgesFrame = pd.read_csv(TRACKS_PATH)
trainTableFrame = pd.read_csv(TRAIN_TABLE_PATH)

graph = nx.Graph()

# Remove some edges for drawing
if REDUCE_DATA_FOR_DRAWING:
    # Select a subset of edges
    edgesFrame = edgesFrame.sample(frac=0.01, random_state=1)

trackList = []
if SELECTED_TRAIN_ID is not None:
    for index, row in trainTableFrame.iterrows():
        if row['Train'] == SELECTED_TRAIN_ID:
            trackList.append(row['Track'])

edgeColorMap = []

for index, row in edgesFrame.iterrows():
    # Add nodes if they don't exist
    if not graph.has_node(row['Station_A']):
        graph.add_node(row['Station_A'])
    if not graph.has_node(row['Station_B']):
        graph.add_node(row['Station_B'])
    # Add edge with weight
    graph.add_edge(row['Station_A'], row['Station_B'], weight=row['Length'], label=row['Track'])
    if SELECTED_TRAIN_ID is not None:
        if row['Track'] in trackList:
            edgeColorMap.append('red')
        else:
            edgeColorMap.append('gray')
    else:
        edgeColorMap.append('gray')
    
print(f"Plotting for selected train ID: {SELECTED_TRAIN_ID}")

pos = nx.spring_layout(graph, seed=42)  # positions for all nodes (to keep it the same every time)

nx.draw(graph, pos=pos, with_labels=LABELS_SHOWN, edge_color=edgeColorMap, node_size=10, font_size=8)

plt.show()
from nilearn import plotting

def PlotConnectome(AdjMatrix, AtlasCoords, Title, EdgeThreshold=0.8):
    plotting.plot_connectome(AdjMatrix, AtlasCoords, edge_threshold=str(EdgeThreshold * 10) + "%", title=Title)

import os 
import geemap

import laspy
import geemap.colormaps as cm

FileName = ("Lidar Data\points.las")
LASFile = geemap.read_lidar(FileName)

#print(LASFile.header.point_count)

# This point_format consist of data inside the LAS file of the point cloud
LasList = list(LASFile.point_format.dimension_names)

#print(LasList)
cm.plot_colormaps()
geemap.view_lidar(FileName,cmap="gist_earth",backend="pyvista")

geemap.view_lidar(FileName,backend="ipygany",background="white")

geemap.view_lidar(FileName,cmap="viridis_r",backend="panel")






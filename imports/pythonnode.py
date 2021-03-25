import numpy
node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

filePath = hou.Node.evalParm(node, "filename") #need to add parameter file using right click over node

data = numpy.load(filePath)
data = data

data = data.astype(numpy.float64)
dimensions = data.shape
xres = dimensions[0]
yres = dimensions[1]
zres = dimensions[2]
volume_bbox = hou.BoundingBox(0, 0, 0,xres , yres, zres)
volumeX = geo.createVolume( xres, yres, zres, volume_bbox)
volumeX.setAllVoxels (data.flatten(order='F'))
volumeY = geo.createVolume( xres, yres, zres, volume_bbox)
volumeY.setAllVoxels (data.flatten(order='F'))
volumeZ = geo.createVolume( xres, yres, zres, volume_bbox)
volumeZ.setAllVoxels (data.flatten(order='F')) 

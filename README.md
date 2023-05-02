# QGIS-Regularize-Building-Footprints
This QGIS plugin regularizes building footprints detected with deep learning, including binary semantic and instance segmentation.

The regularization approach [projectRegularization](https://github.com/zorzi-s/projectRegularization) was implemented from the publication Machine-learned regularization and polygonization of building segmentation masks", ICPR 2021 on the MapAI: Precision in building segmentation challenge. We have developed an end-to-end binary semantic segmentation workflow in PyTorch and applied it on the MapAI dataset. The developed framework [mapAI regularizaton](https://github.com/s1m0nS/mapAI-regularization) can be used to produce building segmentation maps for the plugin.

Note that the plugin supports other segmentations too.

### Input:
- segmented image either in .PNG or .TIF

### Output:
- regularized image in .PNG or .TIF
- vector file from regularization in .GPKG

The GUI is presented below and the functionality is shown.


Note that this repo is a work in progress, the expected working version is 24/06/2023.

<p align="center">
  <img src="https://github.com/s1m0nS/QGIS-Regularize-Building-Footprints/blob/main/img/plugin-gui.png"
  title="The user interface of the plugin"
  width="450" height="600"
  align="center"/>
</p>

<p align="center">
  <img src="https://github.com/s1m0nS/QGIS-Regularize-Building-Footprints/blob/main/img/plugin-regularization.png"
  alt="The plugin GUI"
  title="Regularization option"
  width="450" height="600"
  align="left"/>
  
  <img src="https://github.com/s1m0nS/QGIS-Regularize-Building-Footprints/blob/main/img/plugin-vectorization.png"
  title="Vectorization option"
  width="450" height="600"
  align="right"/>
       
  </p>
  



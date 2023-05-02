# QGIS-Regularize-Building-Footprints
This QGIS plugin regularizes building footprints detected with deep learning, including binary semantic and instance segmentation images.

The regularization approach is implemented from [projectRegularization](https://github.com/zorzi-s/projectRegularization), from the publication Machine-learned regularization and polygonization of building segmentation masks", ICPR 2021.

The end-to-end binary semantic segmentation workflow on the MapAI dataset can be used to produce segmentation maps for the plugin: [mapAI regularizaton](https://github.com/s1m0nS/mapAI-regularization).

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
  



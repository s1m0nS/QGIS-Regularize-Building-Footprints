# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Regularization
                                 A QGIS plugin
 This plugin regularizes building footprints detected with deep learning.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-11
        copyright            : (C) 2023 by Simon Šanca
        email                : simon.sanca22@gmail.comˇ
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Regularization class from file Regularization.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .BuildingRegularization import Regularization
    return Regularization(iface)

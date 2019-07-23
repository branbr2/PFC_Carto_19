# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EDGVConverter
                                 A QGIS plugin
 This plugin converts the data from EDGV-2.1.3 to EDGV-3.0.
                             -------------------
        begin                : 2019-05-16
        copyright            : (C) 2019 by IME_Carto_2019
        email                : bryan.andrade.ime@gmail.com
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
    """Load EDGVConverter class from file EDGVConverter.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .EDGV_Converter import EDGVConverter
    return EDGVConverter(iface)

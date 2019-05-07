# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SaveQML
                                 A QGIS plugin
 This plugin saves qml file
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-04-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Tomáš Bouček
        email                : tom.boucek@seznam.cz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the DockWidget
from .save_qml_dockwidget import SaveQMLDockWidget

import os
from qgis.utils import iface
from qgis.core import QgsProject, QgsMapLayer, Qgis
from PyQt5.QtWidgets import QFileDialog

class SaveQML:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'SaveQML_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Save QML')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'SaveQML')
        self.toolbar.setObjectName(u'SaveQML')

        #print "** INITIALIZING SaveQML"

        self.pluginIsActive = False
        self.dockwidget = None


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('SaveQML', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/save_qml/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Save QML'),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        #print "** CLOSING SaveQML"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        #print "** UNLOAD SaveQML"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Save QML'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True

            #print "** STARTING SaveQML"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = SaveQMLDockWidget()

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget)
            self.dockwidget.show()
            
            self.dockwidget.toolButton.clicked.connect(self.output_dir)
            self.dockwidget.SaveButton.clicked.connect(self.save_qml_file)
            self.dockwidget.lineEdit.setReadOnly(True)
            
    def output_dir(self):
        self.dirname = QFileDialog.getExistingDirectory(
            self.dockwidget, "Select output directory ", os.path.expanduser("~")
        )
        self.dockwidget.lineEdit.setText(self.dirname)
            
    def save_qml_file(self):
        layer_list = []
        for layer in QgsProject.instance().mapLayers().values():
            if layer.type() == QgsMapLayer.VectorLayer or layer.type() == QgsMapLayer.RasterLayer:
                layer_list.append(layer)
            else:
                continue

        if len(layer_list) == 0:
            iface.messageBar().pushMessage('Current project does not have any valid layers', level = Qgis.Warning, duration = 5)
        else:
            if self.dockwidget.checkBox.isChecked():
                if self.dockwidget.lineEdit.text() == '':
                    iface.messageBar().pushMessage('Output directory not defined', level = Qgis.Warning, duration = 5)
                else:
                    layers_count = 0
                    for layers in layer_list:
                        output_file = os.path.join(self.dirname, '{}.qml'.format(layers.name()))
                        layers.saveNamedStyle(output_file)
                        if not os.path.exists(output_file):
                            iface.messageBar().pushMessage('Failed creating output file {}'.format(output_file), level = Qgis.Critical, duration = 5)
                        else:
                            layers_count = layers_count + 1
                    if layers_count == 1:
                        iface.messageBar().pushMessage('1 QML file saved to directory {}'.format(self.dirname), level = Qgis.Success, duration = 5)
                    else:
                        iface.messageBar().pushMessage('{0} QML files saved to directory {1}'.format(layers_count,self.dirname), level = Qgis.Success, duration = 5)
            else:
                if self.dockwidget.lineEdit.text() == '':
                    iface.messageBar().pushMessage('Output directory not defined', level = Qgis.Warning, duration = 5)
                else:
                    saved_layer = 0
                    exist_layer = 0
                    exist_layer_name = []
                    for layers in layer_list:
                        output_file = os.path.join(self.dirname, '{}.qml'.format(layers.name()))
                        if os.path.exists(output_file):
                            exist_layer = exist_layer + 1
                            exist_layer_name.append('{}.qml'.format(layers.name()))
                        else:
                            layers.saveNamedStyle(output_file)
                            if not os.path.exists(output_file):
                                iface.messageBar().pushMessage('Failed creating output file {}'.format(output_file), level = Qgis.Critical, duration = 5)
                            else:
                                saved_layer = saved_layer + 1
                    if exist_layer == 0:
                        if saved_layer == 1:
                            iface.messageBar().pushMessage('1 QML file saved to directory {}'.format(self.dirname), level = Qgis.Success, duration = 5)
                        else:
                            iface.messageBar().pushMessage('{0} QML files saved to directory {1}'.format(saved_layer,self.dirname), level = Qgis.Success, duration = 5)
                    elif saved_layer == 0:
                        iface.messageBar().pushMessage('QML files ({0}) already exist in directory {1}'.format(', '.join(exist_layer_name),self.dirname), level = Qgis.Warning, duration = 5)
                    else:
                        if saved_layer == 1:
                            iface.messageBar().pushMessage('1 QML file saved to directory {}'.format(self.dirname), level = Qgis.Success, duration = 5)
                            iface.messageBar().pushMessage('QML files ({0}) already exist in directory {1}'.format(', '.join(exist_layer_name),self.dirname), level = Qgis.Warning, duration = 5)
                        else:
                            iface.messageBar().pushMessage('{0} QML files saved to directory {1}'.format(saved_layer,self.dirname), level = Qgis.Success, duration = 5)
                            iface.messageBar().pushMessage('QML files ({0}) already exist in directory {1}'.format(', '.join(exist_layer_name),self.dirname), level = Qgis.Warning, duration = 5)
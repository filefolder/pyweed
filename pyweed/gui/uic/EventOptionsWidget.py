# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventOptionsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EventOptionsWidget(object):
    def setupUi(self, EventOptionsWidget):
        EventOptionsWidget.setObjectName("EventOptionsWidget")
        EventOptionsWidget.resize(266, 641)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventOptionsWidget.sizePolicy().hasHeightForWidth())
        EventOptionsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(EventOptionsWidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeGroupBox = QtWidgets.QGroupBox(EventOptionsWidget)
        self.timeGroupBox.setObjectName("timeGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.timeGroupBox)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(4)
        self.formLayout_3.setVerticalSpacing(1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.starttimeLabel = QtWidgets.QLabel(self.timeGroupBox)
        self.starttimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.starttimeLabel.setObjectName("starttimeLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.starttimeLabel)
        self.starttimeDateTimeEdit = QtWidgets.QDateTimeEdit(self.timeGroupBox)
        self.starttimeDateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starttimeDateTimeEdit.setCalendarPopup(True)
        self.starttimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.starttimeDateTimeEdit.setObjectName("starttimeDateTimeEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.starttimeDateTimeEdit)
        self.endtimeLabel = QtWidgets.QLabel(self.timeGroupBox)
        self.endtimeLabel.setObjectName("endtimeLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.endtimeLabel)
        self.endtimeDateTimeEdit = QtWidgets.QDateTimeEdit(self.timeGroupBox)
        self.endtimeDateTimeEdit.setCalendarPopup(True)
        self.endtimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.endtimeDateTimeEdit.setObjectName("endtimeDateTimeEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endtimeDateTimeEdit)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.time30DaysToolButton = QtWidgets.QToolButton(self.timeGroupBox)
        self.time30DaysToolButton.setObjectName("time30DaysToolButton")
        self.horizontalLayout_2.addWidget(self.time30DaysToolButton)
        self.time1YearToolButton = QtWidgets.QToolButton(self.timeGroupBox)
        self.time1YearToolButton.setObjectName("time1YearToolButton")
        self.horizontalLayout_2.addWidget(self.time1YearToolButton)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.timeGroupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.timeFromStationsToolButton = QtWidgets.QToolButton(self.timeGroupBox)
        self.timeFromStationsToolButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeFromStationsToolButton.sizePolicy().hasHeightForWidth())
        self.timeFromStationsToolButton.setSizePolicy(sizePolicy)
        self.timeFromStationsToolButton.setObjectName("timeFromStationsToolButton")
        self.verticalLayout_2.addWidget(self.timeFromStationsToolButton)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.magnitudeGroupBox = QtWidgets.QGroupBox(EventOptionsWidget)
        self.magnitudeGroupBox.setObjectName("magnitudeGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.magnitudeGroupBox)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.magnitudeLayout = QtWidgets.QHBoxLayout()
        self.magnitudeLayout.setSpacing(0)
        self.magnitudeLayout.setObjectName("magnitudeLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.magnitudeGroupBox)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.minMagDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.magnitudeGroupBox)
        self.minMagDoubleSpinBox.setDecimals(1)
        self.minMagDoubleSpinBox.setMinimum(-2.0)
        self.minMagDoubleSpinBox.setMaximum(10.0)
        self.minMagDoubleSpinBox.setObjectName("minMagDoubleSpinBox")
        self.horizontalLayout_15.addWidget(self.minMagDoubleSpinBox)
        self.label_11 = QtWidgets.QLabel(self.magnitudeGroupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.maxMagDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.magnitudeGroupBox)
        self.maxMagDoubleSpinBox.setDecimals(1)
        self.maxMagDoubleSpinBox.setMaximum(10.0)
        self.maxMagDoubleSpinBox.setObjectName("maxMagDoubleSpinBox")
        self.horizontalLayout_15.addWidget(self.maxMagDoubleSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.magnitudeGroupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.magTypeComboBox = QtWidgets.QComboBox(self.magnitudeGroupBox)
        self.magTypeComboBox.setEnabled(True)
        self.magTypeComboBox.setObjectName("magTypeComboBox")
        self.magTypeComboBox.addItem("")
        self.magTypeComboBox.addItem("")
        self.magTypeComboBox.addItem("")
        self.magTypeComboBox.addItem("")
        self.magTypeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.magTypeComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(1, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.magnitudeLayout.addLayout(self.verticalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.magnitudeLayout.addItem(spacerItem3)
        self.magnitudeLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.magnitudeLayout)
        self.verticalLayout.addWidget(self.magnitudeGroupBox)
        self.depthGroupBox = QtWidgets.QGroupBox(EventOptionsWidget)
        self.depthGroupBox.setObjectName("depthGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.depthGroupBox)
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.depthLayout = QtWidgets.QHBoxLayout()
        self.depthLayout.setSpacing(0)
        self.depthLayout.setObjectName("depthLayout")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.depthGroupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        self.minDepthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.depthGroupBox)
        self.minDepthDoubleSpinBox.setDecimals(1)
        self.minDepthDoubleSpinBox.setMaximum(6800.0)
        self.minDepthDoubleSpinBox.setObjectName("minDepthDoubleSpinBox")
        self.horizontalLayout_16.addWidget(self.minDepthDoubleSpinBox)
        self.label_12 = QtWidgets.QLabel(self.depthGroupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.maxDepthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.depthGroupBox)
        self.maxDepthDoubleSpinBox.setDecimals(1)
        self.maxDepthDoubleSpinBox.setMaximum(6800.0)
        self.maxDepthDoubleSpinBox.setObjectName("maxDepthDoubleSpinBox")
        self.horizontalLayout_16.addWidget(self.maxDepthDoubleSpinBox)
        self.depthLayout.addLayout(self.horizontalLayout_16)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.depthLayout.addItem(spacerItem4)
        self.depthLayout.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.depthLayout)
        self.verticalLayout.addWidget(self.depthGroupBox)
        self.locationGroupBox = QtWidgets.QGroupBox(EventOptionsWidget)
        self.locationGroupBox.setObjectName("locationGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.locationFromStationsToolButton = QtWidgets.QToolButton(self.locationGroupBox)
        self.locationFromStationsToolButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationFromStationsToolButton.sizePolicy().hasHeightForWidth())
        self.locationFromStationsToolButton.setSizePolicy(sizePolicy)
        self.locationFromStationsToolButton.setObjectName("locationFromStationsToolButton")
        self.verticalLayout_6.addWidget(self.locationFromStationsToolButton)
        self.line_3 = QtWidgets.QFrame(self.locationGroupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.locationGlobalRadioButton = QtWidgets.QRadioButton(self.locationGroupBox)
        self.locationGlobalRadioButton.setChecked(True)
        self.locationGlobalRadioButton.setObjectName("locationGlobalRadioButton")
        self.horizontalLayout_7.addWidget(self.locationGlobalRadioButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.line_4 = QtWidgets.QFrame(self.locationGroupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.locationRangeRadioButton = QtWidgets.QRadioButton(self.locationGroupBox)
        self.locationRangeRadioButton.setChecked(False)
        self.locationRangeRadioButton.setObjectName("locationRangeRadioButton")
        self.horizontalLayout_4.addWidget(self.locationRangeRadioButton)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.locationRangeLayout = QtWidgets.QHBoxLayout()
        self.locationRangeLayout.setContentsMargins(12, -1, -1, -1)
        self.locationRangeLayout.setSpacing(0)
        self.locationRangeLayout.setObjectName("locationRangeLayout")
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.locationRangeLayout.addItem(spacerItem6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem7)
        self.locationRangeNorthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeNorthDoubleSpinBox.setMinimum(-90.0)
        self.locationRangeNorthDoubleSpinBox.setMaximum(90.0)
        self.locationRangeNorthDoubleSpinBox.setObjectName("locationRangeNorthDoubleSpinBox")
        self.horizontalLayout_23.addWidget(self.locationRangeNorthDoubleSpinBox)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.locationRangeWestDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeWestDoubleSpinBox.setMinimum(-180.0)
        self.locationRangeWestDoubleSpinBox.setMaximum(180.0)
        self.locationRangeWestDoubleSpinBox.setObjectName("locationRangeWestDoubleSpinBox")
        self.horizontalLayout_24.addWidget(self.locationRangeWestDoubleSpinBox)
        self.locationRangeEastDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeEastDoubleSpinBox.setMinimum(-180.0)
        self.locationRangeEastDoubleSpinBox.setMaximum(180.0)
        self.locationRangeEastDoubleSpinBox.setObjectName("locationRangeEastDoubleSpinBox")
        self.horizontalLayout_24.addWidget(self.locationRangeEastDoubleSpinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem9)
        self.locationRangeSouthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeSouthDoubleSpinBox.setMinimum(-90.0)
        self.locationRangeSouthDoubleSpinBox.setMaximum(90.0)
        self.locationRangeSouthDoubleSpinBox.setObjectName("locationRangeSouthDoubleSpinBox")
        self.horizontalLayout_25.addWidget(self.locationRangeSouthDoubleSpinBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.drawLocationRangeToolButton = QtWidgets.QToolButton(self.locationGroupBox)
        self.drawLocationRangeToolButton.setCheckable(True)
        self.drawLocationRangeToolButton.setObjectName("drawLocationRangeToolButton")
        self.verticalLayout_8.addWidget(self.drawLocationRangeToolButton, 0, QtCore.Qt.AlignHCenter)
        self.locationRangeLayout.addLayout(self.verticalLayout_8)
        spacerItem11 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.locationRangeLayout.addItem(spacerItem11)
        self.verticalLayout_10.addLayout(self.locationRangeLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_10)
        self.line = QtWidgets.QFrame(self.locationGroupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.locationDistanceFromPointRadioButton = QtWidgets.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromPointRadioButton.setEnabled(True)
        self.locationDistanceFromPointRadioButton.setObjectName("locationDistanceFromPointRadioButton")
        self.horizontalLayout_5.addWidget(self.locationDistanceFromPointRadioButton)
        spacerItem12 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.locationDistanceFromPointLayout = QtWidgets.QHBoxLayout()
        self.locationDistanceFromPointLayout.setContentsMargins(12, -1, -1, -1)
        self.locationDistanceFromPointLayout.setSpacing(0)
        self.locationDistanceFromPointLayout.setObjectName("locationDistanceFromPointLayout")
        spacerItem13 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.locationDistanceFromPointLayout.addItem(spacerItem13)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.locationGroupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.distanceFromPointMinRadiusDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointMinRadiusDoubleSpinBox.setMinimum(0.0)
        self.distanceFromPointMinRadiusDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointMinRadiusDoubleSpinBox.setObjectName("distanceFromPointMinRadiusDoubleSpinBox")
        self.horizontalLayout_14.addWidget(self.distanceFromPointMinRadiusDoubleSpinBox)
        self.label_17 = QtWidgets.QLabel(self.locationGroupBox)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_14.addWidget(self.label_17)
        self.distanceFromPointMaxRadiusDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setMinimum(0.0)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setObjectName("distanceFromPointMaxRadiusDoubleSpinBox")
        self.horizontalLayout_14.addWidget(self.distanceFromPointMaxRadiusDoubleSpinBox)
        self.horizontalLayout_14.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_21 = QtWidgets.QLabel(self.locationGroupBox)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_20.addWidget(self.label_21)
        self.distanceFromPointNorthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointNorthDoubleSpinBox.setMinimum(-90.0)
        self.distanceFromPointNorthDoubleSpinBox.setMaximum(90.0)
        self.distanceFromPointNorthDoubleSpinBox.setObjectName("distanceFromPointNorthDoubleSpinBox")
        self.horizontalLayout_20.addWidget(self.distanceFromPointNorthDoubleSpinBox)
        self.label_6 = QtWidgets.QLabel(self.locationGroupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_20.addWidget(self.label_6)
        self.distanceFromPointEastDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointEastDoubleSpinBox.setMinimum(-180.0)
        self.distanceFromPointEastDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointEastDoubleSpinBox.setObjectName("distanceFromPointEastDoubleSpinBox")
        self.horizontalLayout_20.addWidget(self.distanceFromPointEastDoubleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.drawDistanceFromPointToolButton = QtWidgets.QToolButton(self.locationGroupBox)
        self.drawDistanceFromPointToolButton.setCheckable(True)
        self.drawDistanceFromPointToolButton.setObjectName("drawDistanceFromPointToolButton")
        self.verticalLayout_4.addWidget(self.drawDistanceFromPointToolButton, 0, QtCore.Qt.AlignHCenter)
        self.locationDistanceFromPointLayout.addLayout(self.verticalLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.locationDistanceFromPointLayout.addItem(spacerItem14)
        self.verticalLayout_11.addLayout(self.locationDistanceFromPointLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout.addWidget(self.locationGroupBox)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)

        self.retranslateUi(EventOptionsWidget)
        QtCore.QMetaObject.connectSlotsByName(EventOptionsWidget)

    def retranslateUi(self, EventOptionsWidget):
        _translate = QtCore.QCoreApplication.translate
        self.timeGroupBox.setTitle(_translate("EventOptionsWidget", "Time"))
        self.starttimeLabel.setText(_translate("EventOptionsWidget", "start"))
        self.starttimeDateTimeEdit.setDisplayFormat(_translate("EventOptionsWidget", "yyyy-MM-dd hh:mm:ss"))
        self.endtimeLabel.setText(_translate("EventOptionsWidget", "end"))
        self.endtimeDateTimeEdit.setDisplayFormat(_translate("EventOptionsWidget", "yyyy-MM-dd hh:mm:ss"))
        self.time30DaysToolButton.setText(_translate("EventOptionsWidget", "Last 30 days"))
        self.time1YearToolButton.setText(_translate("EventOptionsWidget", "Last year"))
        self.timeFromStationsToolButton.setText(_translate("EventOptionsWidget", "Copy from Station Options <<"))
        self.magnitudeGroupBox.setTitle(_translate("EventOptionsWidget", "Magnitude"))
        self.label_16.setText(_translate("EventOptionsWidget", "min"))
        self.label_11.setText(_translate("EventOptionsWidget", "max"))
        self.label_7.setText(_translate("EventOptionsWidget", "type"))
        self.magTypeComboBox.setItemText(0, _translate("EventOptionsWidget", "All Types"))
        self.magTypeComboBox.setItemText(1, _translate("EventOptionsWidget", "Mw"))
        self.magTypeComboBox.setItemText(2, _translate("EventOptionsWidget", "mb"))
        self.magTypeComboBox.setItemText(3, _translate("EventOptionsWidget", "Ms"))
        self.magTypeComboBox.setItemText(4, _translate("EventOptionsWidget", "ML"))
        self.depthGroupBox.setTitle(_translate("EventOptionsWidget", "Depth (km)"))
        self.label_13.setText(_translate("EventOptionsWidget", "min"))
        self.label_12.setText(_translate("EventOptionsWidget", "max"))
        self.locationGroupBox.setTitle(_translate("EventOptionsWidget", "Location"))
        self.locationFromStationsToolButton.setText(_translate("EventOptionsWidget", "Copy from Station Options <<"))
        self.locationGlobalRadioButton.setText(_translate("EventOptionsWidget", "Global"))
        self.locationRangeRadioButton.setText(_translate("EventOptionsWidget", "Within lat/lon box"))
        self.drawLocationRangeToolButton.setText(_translate("EventOptionsWidget", "Draw on map"))
        self.locationDistanceFromPointRadioButton.setText(_translate("EventOptionsWidget", "Degrees from point"))
        self.label_10.setText(_translate("EventOptionsWidget", "min"))
        self.label_17.setText(_translate("EventOptionsWidget", "max"))
        self.label_21.setText(_translate("EventOptionsWidget", "lat"))
        self.label_6.setText(_translate("EventOptionsWidget", " lon"))
        self.drawDistanceFromPointToolButton.setText(_translate("EventOptionsWidget", "Draw on map"))


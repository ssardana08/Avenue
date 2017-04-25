
fontid_black = QtGui.QFontDatabase.addApplicationFont("../fonts/DINPro-Medium.otf")
familyname = QtGui.QFontDatabase.applicationFontFamilies(fontid_black)[0]
font = QtGui.QFont(familyname)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QDesktopServices

from . import wx

class Ui_infoform(object):
    def setupUi(self, infoform):
        infoform.setObjectName("infoform")
        infoform.setWindowModality(QtCore.Qt.NonModal)
        infoform.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(infoform.sizePolicy().hasHeightForWidth())
        infoform.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(infoform)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(infoform)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.anchorClicked.connect(self.openExternalLink)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(infoform)
        QtCore.QMetaObject.connectSlotsByName(infoform)
    def openExternalLink(self, url):
        # Open the link in the system browser
        QDesktopServices.openUrl(url)

    def retranslateUi(self, infoform):
        _translate = QtCore.QCoreApplication.translate
        infoform.setWindowTitle(_translate("infoform", "捐助该软件以便持续维护"))
        self.textBrowser.setHtml(_translate("infoform", """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<h1 style=" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:xx-large; font-weight:600;">捐助该软件以便能够持续维护 Donate to this project and support</span></h1>
<hr />
<p><a href="https://ko-fi.com/jianchang512"> 👑 Donate buy me a coffee </a></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">有不少朋友问到这个问题，简单说下。 本项目基于兴趣创建，在可预期的未来都没有商业计划，也就是你可以一直免费使用，或者fork后自己修改。不用担心收费问题。如果你遇到需要付费购买的，请果断拒绝然后来此使用免费开源的正版。</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">至于维护问题呢，开源嘛都是用爱发电，闲时就多花些精力在这上面，忙时可能就一段时间顾不上。当然了，如果觉得该项目对你有价值，并希望该项目能一直稳定持续维护，也欢迎各位捐助。如果你手头紧，那么也无需捐助，帮我点个star或提交个pr，或推荐有需要的朋友来使用，也是一种帮助。</p>
<hr />
<h2 style=" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:x-large; font-weight:600;">如何捐助</span></h2>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">你可以向微信或支付宝二维码付款，备注你的github名称</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/png/wx.png" width="240" /></p>
<hr />
<h2 style=" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:x-large; font-weight:600;">感谢所有捐助者</span></h2>
<h2 style="-qt-paragraph-type:empty; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large; font-weight:600;"><br /></h2>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">github用户<span style=" color:#00aa00;">yuppiesnotzhuhao </span> |  微信用户<span style=" color:#00aa00;">9*9</span> | 未署名的3位用户 | ID:BigD-a-yi</p>
<p><a href="https://github.com/jianchang512/pyvideotrans/blob/main/about.md">全局捐助列表</a></p>
<p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aa00;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aa00;"><br /></p></body></html>
"""))

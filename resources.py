# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.11.3)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xb9\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x80\x49\x44\x41\x54\x78\xda\xed\xd1\x61\x0e\x80\x20\
\x08\x06\x50\x38\x5c\x37\xe9\x56\x75\x92\x3a\x9c\xb1\x16\x85\x24\
\xce\xd2\xd6\x5a\xf0\x0b\xf1\xcb\xa7\x0b\x61\x80\x00\x0f\x16\x3a\
\xe0\xc0\x87\x80\xd0\x1f\x0e\x8e\xb8\xf7\xd6\x3c\xb5\xc7\x6b\x99\
\x5b\x01\xb9\xa1\x43\xd5\x40\xa0\xb2\x6e\x2d\x3f\xd2\x48\x6a\xfe\
\x32\x30\x0b\xa0\xdb\x82\x34\xd3\x3d\xe7\xb8\xb7\xb2\xb7\x81\xe8\
\xd6\x25\x00\x4c\xf4\x93\x33\xa1\x2b\x6b\x13\x90\xc1\xdc\x6b\x4a\
\x81\xe8\x95\x0c\x58\x07\xd6\xd6\x09\xc8\xbd\xa6\x19\xd0\xb2\x1c\
\xf8\x01\xb0\x00\x0e\x14\xae\x40\xa4\x68\x50\x22\x00\x00\x00\x00\
\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x07\
\x07\x3b\xe0\xb3\
\x00\x70\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x73\
\x00\x08\
\x08\xcb\x6b\x1c\
\x00\x73\
\x00\x61\x00\x76\x00\x65\x00\x5f\x00\x71\x00\x6d\x00\x6c\
\x00\x08\
\x0a\x61\x5a\xa7\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x2a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x2a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x6b\x4a\x93\x29\xcb\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

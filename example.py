#!/usr/bin/python
# -*- coding: utf-8 -*-

from DropBoxClass import DropBoxClass
import logging

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger("Example")

drop = DropBoxClass("your@mail.com", "thepassword")
drop.uploadFile("example.py")

print "Current freespace: %f MB" % drop.getFreeSpace()

# -*- coding: utf-8 -*-

"""WebHelpers used in indicator."""

#from webhelpers import date, feedgenerator, html, number, misc, text
from markupsafe import Markup

def bold(text):
    return Markup('<strong>%s</strong>' % text)
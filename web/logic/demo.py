# -*- coding:utf-8 -*-

import tornado,cStringIO

from inspect import isclass, ismethod, getmembers
from unittest import TestCase, TextTestRunner,TestSuite
from kpages import url, ContextHandler,get_modules
from kpages.utest import load_testcase,load_testsuites_bypath
class BaseHandler(ContextHandler,tornado.web.RequestHandler):
    pass


@url(r'/')
@url(r'/index')
class IndexHandler(BaseHandler):
	"""docstring for IndexHandler"""
	def get(self):
		self.render('invoice.html')

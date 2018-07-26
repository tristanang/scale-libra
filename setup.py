#!/usr/bin/env python

from distutils.core import setup

setup(name='scale-libra',
      version='0.1',
      description='Infrastructure as Code for Lightbound',
      author='Tristan Ang',
      author_email='theng@scalecomputing.com',
      packages=['scale_libra','scale_libra.graph','scale_libra.device','scale_libra.graph.device',],
     )

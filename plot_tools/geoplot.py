# -*- coding: utf-8 -*-
#
# Plot tools Geoplot class file.
# Copyright (C) 2018 Malte Ziebarth
# 
# This software is distributed under the MIT license.
# See the LICENSE file in this repository.

from .geoplot_base.rect import Rect
from .geoplot_base.base import GeoplotBase





# GEOPLOT:

class Geoplot(GeoplotBase):


	def __init__(self, ax, projection, limits_xy=None, gshhg_path=None):
		"""
		Init method.
		
		Required arguments:
		   ax         :
		   projection :
		   limits_xy  : [xlim, ylim]
		"""
		
		super().__init__(ax, projection, gshhg_path)
		
		self._gshhg_path = gshhg_path
		
		
		self._canvas = Rect(0,0,1,1)
		self._plot_canvas = self._canvas
		
		# Setup configuration:
		self._box_axes = True
		self._box_axes_width = 0.01
		
		# If limits are given, set them:
		if limits_xy is not None:
			self._user_xlim = limits_xy[0]
			self._user_ylim = limits_xy[1]
			self._xlim = self._user_xlim
			self._ylim = self._user_ylim


	def set_xlim(self, xlim):
		# TODO Sanity checks.
		self._user_xlim = xlim
		self._schedule_callback()

	def set_ylim(self, ylim):
		self._user_ylim = ylim
		self._schedule_callback()

	def coastline(self, level, **kwargs):
		"""
		
		"""
		if self._gshhg_path is None:
			raise RuntimeError("GSHHG not loaded!")
		
		# Schedule coastline:
		self._scheduled += [['coastline', False, (level,)]]
		self._schedule_callback()


	def imshow_projected(self, z, xlim, ylim, **kwargs):
		"""
		Plot a field (in projected coordinates) using imshow.
		"""
		# Check data limits:
		if xlim[0] < self._data_xlim[0]:
			self._data_xlim[0] = xlim[0]
		if xlim[1] > self._data_xlim[1]:
			self._data_xlim[1] = xlim[1]
		if ylim[0] < self._data_ylim[0]:
			self._data_ylim[0] = ylim[0]
		if ylim[1] > self._data_ylim[1]:
			self._data_ylim[1] = ylim[1]
		
		# Schedule plot:
		self._scheduled += [['imshow', False, (z, xlim,ylim,kwargs)]]
		self._schedule_callback()

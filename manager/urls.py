
# (C) British Crown Copyright 2011 - 2012, Met Office
#
# This file is part of metOcean-mapping.
#
# metOcean-mapping is free software: you can redistribute it and/or 
# modify it under the terms of the GNU Lesser General Public License 
# as published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
#
# metOcean-mapping is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with metOcean-mapping. If not, see <http://www.gnu.org/licenses/>.


from django.conf.urls.defaults import patterns, include, url

import settings

datatypes = 'stash|grib'

urlpatterns = patterns('manager.views',
    url(r'^$', 'tasks', name='tasks'),
    url(r'^list/(?P<datatype>(%s))/$' % datatypes,
        'list', name='list'),
    url(r'^list/(?P<datatype>(%s))/$' % datatypes,
        'listtype', name='listtype'),
    url(r'^new/(?P<datatype>(%s)[^/]+)/$' % datatypes, 
        'newshard', name='newshard'),
    url(r'^edit/(?P<datatype>(%s)[^/]+)/$' % datatypes, 
        'edit', name='edit'),
    url(r'^map/(?P<hashval>[a-f0-9]{32})/', 'mapdisplay', name='mapdisplay'),
    url(r'^search/$', 'search', name='search'),
)

#
# Copyright (C) 2007-2012 by Johan De Taeye, frePPLe bvba
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# file : $URL$
# revision : $LastChangedRevision$  $LastChangedBy$
# date : $LastChangedDate$

from django.conf.urls import patterns

import freppledb.input.views

# Automatically add these URLs when the application is installed
autodiscover = True

urlpatterns = patterns('',

  # Model list reports, which override standard admin screens
  (r'^admin/input/buffer/$', freppledb.input.views.BufferList.as_view()),
  (r'^admin/input/resource/$', freppledb.input.views.ResourceList.as_view()),
  (r'^admin/input/location/$', freppledb.input.views.LocationList.as_view()),
  (r'^admin/input/customer/$', freppledb.input.views.CustomerList.as_view()),
  (r'^admin/input/demand/$', freppledb.input.views.DemandList.as_view()),
  (r'^admin/input/item/$', freppledb.input.views.ItemList.as_view()),
  (r'^admin/input/load/$', freppledb.input.views.LoadList.as_view()),
  (r'^admin/input/flow/$', freppledb.input.views.FlowList.as_view()),  
  (r'^admin/input/calendar/$', freppledb.input.views.CalendarList.as_view()),
  (r'^admin/input/calendarbucket/$', freppledb.input.views.CalendarBucketList.as_view()),
  (r'^admin/input/operation/$', freppledb.input.views.OperationList.as_view()),
  (r'^admin/input/setupmatrix/$', freppledb.input.views.SetupMatrixList.as_view()),
  (r'^admin/input/suboperation/$', freppledb.input.views.SubOperationList.as_view()),
  (r'^admin/input/operationplan/$', freppledb.input.views.OperationPlanList.as_view()),
  (r'^admin/input/skill/$', freppledb.input.views.SkillList.as_view()),
  (r'^admin/input/resourceskill/$', freppledb.input.views.ResourceSkillList.as_view()),

  # Special reports
  (r'^admin/input/calendar/location/([^/]+)/$', freppledb.input.views.location_calendar),
  (r'^supplypath/([^/]+)/([^/]+)/$', freppledb.input.views.pathreport.viewupstream),
  (r'^whereused/([^/]+)/([^/]+)/$', freppledb.input.views.pathreport.viewdownstream),
  (r'^search/$', freppledb.input.views.search),  
)

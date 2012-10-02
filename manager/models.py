
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

import metOceanPrefixes as prefixes

from django.db import models

# Create your models here.

class State(object):
    STATES = (
        'Draft',
        'Proposed',
        'Approved',
        'Broken',
        'Deprecated',
    )

    def __init__(self, *args, **kwargs):
        state = kwargs.get('state', None)
        #super(State, self).__init__(*args, **kwargs)
        self.state = None
        if state is not None:
            if state in [x.lower() for x in self.STATES]:
                self.state = state
            else:
                raise Exception('state not recognised')

    def __repr__(self):
        return self.state

    @property
    def get_states(self):
        return self.STATES

class DataType(object):
    DATATYPES = (
        'STASH',
        'GRIB'
        )
    def __init__(self, *args, **kwargs):
        datatype = kwargs.get('datatype', None)
        #super(State, self).__init__(*args, **kwargs)
        self.datatype = None
        if datatype is not None:
            if datatype in [x.lower() for x in self.DATATYPES]:
                self.datatype = datatype
            else:
                raise Exception('datatype not recognised')

    def __repr__(self):
        return self.datatype

    @property
    def get_datatypes(self):
        return self.DATATYPES

class StateTransition(object):
    fromstate = None
    tostate = None
    transition_date = None

    VALID_TRANSITIONS = (
        ('Draft', 'Proposed'),
        ('Draft', 'Deprecated'),
        ('Draft', 'Broken'),
        ('Proposed', 'Draft'),
        ('Approved', 'Draft'),
        ('Broken', 'Deprecated'),
        ('Broken', 'Draft'),
        ('Deprecated', 'Draft'),
    )

    @property
    def has_allowed_transition(self):
        if (self.fromstate, self.tostate) in self.VALID_TRANSITIONS:
            return True
        else:
            return False
    

class BaseRecord(models.Model):
    '''represents the linkage between Standard Name and a sub-classed RDF type'''
    baserecordMD5 = models.CharField(max_length=32) 
    metadata_element = models.CharField(
        null=True, blank=True, 
        max_length=100, choices=[(x,y) for x,y in prefixes.Prefixes().datalist]) 
        # popup of all known namespaces
    local_name = models.CharField(max_length=40)
    standard_name = models.CharField(max_length=100, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    long_name = models.CharField(max_length=150, null=True, blank=True)

    # and field to set NEXT valid state

    def validate_for_transition(self):
        #raise NotImplementedError
        pass

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    watcher = models.BooleanField(default=True, editable=False)
    joined = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s, %s' % (
            self.name, 'Watcher' if self.watcher else 'Owner', self.email)

class Provenance(BaseRecord):
    provenanceMD5 = models.CharField(max_length=32) 
    last_edit = models.CharField(max_length=50)
    current_status = models.CharField(max_length=15)
    version = models.CharField(max_length=20)
    comment = models.CharField(max_length=200)
    reason = models.CharField(max_length=50)
    owners = models.ManyToManyField(Contacts, 
        through='ProvenanceContacts')
    previous = models.CharField(max_length=32)


class ProvenanceContacts(models.Model):
    provenance = models.ForeignKey(Provenance)
    contact = models.ForeignKey(Contacts)







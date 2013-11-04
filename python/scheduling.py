#!/usr/bin/env python3
#    Engineering Note 6: The Imagination (Algebra).
#    Copyright (C) 2013  Edward Jason Cozens
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from datetime import (
    datetime,
)

class Job():

    Pending = 'Pending'
    InProgress = 'In Progress'
    Complete = 'Complete'

    def __init__(self, startTime):
        self.__state = Job.Pending
        self.__lastTransitionTime = startTime

    def Next(self, transitionTime):
        self.__lastTransitionTime = transitionTime
        self.__state = Job.InProgress
    
    @property
    def State(self):
        return self.__state

    def GetTransitionTime(self, state):
        return self.__lastTransitionTime

        

print(__name__)

if __name__ == '__main__':
    print('Running Simulation')

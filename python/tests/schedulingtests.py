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
from unittest import (
    TestCase,
    TestSuite,
    TestLoader,
    )

from datetime import (
    datetime,
    )

from scheduling import (
    Job,
    )

class JobTests(TestCase):

    def test_new_Job(self):
        jobStartTime = datetime(2020, 2, 1)
        job = Job(jobStartTime)
        self.assertEqual(job.State, Job.Pending)
        self.assertEqual(job.GetTransitionTime(Job.Pending), jobStartTime)

    def test_Pending_next_InProgress(self):
        job = Job(datetime(2020, 2, 1))
        inProgressStart = datetime(2013, 12, 2)
        job.Next(inProgressStart)
        self.assertEqual(job.State, Job.InProgress)
        self.assertEqual(job.GetTransitionTime(Job.InProgress), inProgressStart)

def alltests():
    return TestSuite([
        TestLoader().loadTestsFromTestCase(JobTests),
    ])



using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spike01_Tests
{
    public class JobsGenerator : IJobsGenerator
    {
        private List<DateTime> _jobs;

        public JobsGenerator()
        {
            _jobs = new List<DateTime>();
        }

        public List<DateTime> Jobs
        {
            get { return _jobs; }
        }

        public void AddJobs(int numberOfJobs)
        {
            for (var jobCount = 0; jobCount < numberOfJobs; jobCount++)
                _jobs.Add(new DateTime());
        }
    }
}

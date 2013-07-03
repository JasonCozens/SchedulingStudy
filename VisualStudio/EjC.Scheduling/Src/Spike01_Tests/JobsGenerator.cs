using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spike01_Tests
{
    public class JobsGenerator : IJobsGenerator
    {
        public List<DateTime> Jobs
        {
            get { return new List<DateTime>(); }
        }
    }
}

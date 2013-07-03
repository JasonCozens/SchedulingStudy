using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Spike01_Tests
{
    interface IJobsGenerator
    {
        List<DateTime> Jobs { get; }
    }
}

using System;
using System.Text;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Spike01_Tests
{
    /// <summary>
    /// Summary description for JobsGeneratorTests
    /// </summary>
    [TestClass]
    public class JobsGeneratorTests
    {
        [TestMethod]
        public void TestMethod1()
        {
            //Act
            IJobsGenerator jobGenerator = new JobsGenerator();
            //Assert
            Assert.AreEqual(0, jobGenerator.Jobs.Count);
        }
    }
}

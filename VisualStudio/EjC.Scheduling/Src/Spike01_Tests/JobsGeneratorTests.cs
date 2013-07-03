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
        public void NewJobGenerator_HasNoJobs()
        {
            //Act
            IJobsGenerator jobGenerator = new JobsGenerator();
            //Assert
            Assert.AreEqual(0, jobGenerator.Jobs.Count);
        }

        [TestMethod]
        public void AddJobs_AddsCorrectNumberOfJobs()
        {
            //Test data
            var numberOfJobs = 6;
            //Arrange
            IJobsGenerator jobGenerator = new JobsGenerator();
            //Act
            jobGenerator.AddJobs(numberOfJobs);
            //Assert
            Assert.AreEqual(numberOfJobs, jobGenerator.Jobs.Count);
        }
    }
}

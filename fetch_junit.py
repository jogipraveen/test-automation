#!/usr/bin/env python
"""
This script is used to fetch the list of failed Unit tests
fetch all files in 'core/build/test-results/' and found the list of failed tests
"""

import sys
import re
from os import listdir
from xml.dom import minidom
from os.path import isfile, join

if len(sys.argv) == 3:
    """ get the directory to check 'core/build/test-results' """
    dir_to_look=sys.argv[1] 
    failed_junit=[]
    onlyfiles = [f for f in listdir(dir_to_look) if isfile(join(dir_to_look, f))]
    """ if multiple files are there check all files """
    for i in onlyfiles: 
        update_dir=str(sys.argv[1])+ "/"
        xmldoc=minidom.parse(update_dir + i) #parse file
        testsuite=xmldoc.getElementsByTagName("testsuite")[0]
        status=xmldoc.getElementsByTagName("testsuite")[0].getAttribute("failures")
        if status != "0":
            testcase=testsuite.getElementsByTagName("testcase")
            t_name=testsuite.getElementsByTagName("testcase")[0].getAttribute("name")
            for test_cases in testcase:
                classname=test_cases.getAttribute("classname")
                name=test_cases.getAttribute("name")
                failure=test_cases.getElementsByTagName("failure") #check for failure exception
		for failed_test in failure:
                    junit_test=classname + "." +  name
                    failed_junit.append(junit_test) #append all tests to a list

    """com.cs.tools.content.MyDecksLoaderTest.testGetSlidesXMLHasImageAndThumbnailUrls
       package - com.cs.tools.content
       group - MyDecksLoaderTest
       test_name - testGetSlidesXMLHasImageAndThumbnailUrls"""
    for j in failed_junit:
        """ 
        Apply some regular expression to find test_name and group and package
        """
        lst1=j.split('.')
        test_name=lst1[-1]
        group=lst1[-2]
        val1=re.sub(r'.[a-zA-Z]*$', "", j)
        package=re.sub(r'.[a-zA-Z]*$', "", val1)
        url=sys.argv[2] +"testReport/junit/"+ package +"/"+ group +"/"+ test_name #generate URL
        print "["+ j +"]("+ url +")"
else:
    print "Incorrect number of arguments passed"

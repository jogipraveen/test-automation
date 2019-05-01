#!/usr/bin/env python
"""
This script is used to check failed tests in a xml file(TestNG)
parse number of failed tests in 'testng-results.xml' for the failed jobs
"""

import sys
from xml.dom import minidom

if len(sys.argv) == 2:
    xmldoc = minidom.parse(sys.argv[1])
    testng = xmldoc.getElementsByTagName("testng-results")[0].getAttribute("failed")  # Get the number of failed tests
    print(testng)
else:
    print("Incorrect number of arguments passed")

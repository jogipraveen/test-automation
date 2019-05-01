#!/usr/bin/env python
"""
This script is used to fetch the list of failed Unit tests
fetch all files in 'core/build/test-results/' and found the list of failed tests
"""

import sys
import re
import argparse
from os import listdir
from xml.dom import minidom
from os.path import isfile, join


def getargs():
    """
    Supports the following command-line arguments listed below.
    dir_name - directory to check the junit test results
    url - bitbucket/stash url
    """
    parser = argparse.ArgumentParser(description='fetch all failed unit tests')
    parser.add_argument('dir_name', help='directory to check the junit results')
    parser.add_argument('url', help='bitbucket/stash url')
    args = parser.parse_args()
    return args


def fetch_junit(dir_name, url):
    """ get the directory to check 'core/build/test-results' """
    dir_to_look = dir_name
    failed_junit = []
    onlyfiles = [f for f in listdir(dir_to_look) if isfile(join(dir_to_look, f))]
    """ if multiple files are there check all files """
    for i in onlyfiles:
        update_dir = str(directory) + "/"
        xmldoc = minidom.parse(update_dir + i)  # parse file
        testsuite = xmldoc.getElementsByTagName("testsuite")[0]
        status = xmldoc.getElementsByTagName("testsuite")[0].getAttribute("failures")
        if status != "0":
            testcase = testsuite.getElementsByTagName("testcase")
            t_name = testsuite.getElementsByTagName("testcase")[0].getAttribute("name")
            for test_cases in testcase:
                classname = test_cases.getAttribute("classname")
                name = test_cases.getAttribute("name")
                failure = test_cases.getElementsByTagName("failure")  # check for failure exception
                for failed_test in failure:
                    junit_test = classname + "." + name
                    failed_junit.append(junit_test)  # append all tests to a list

    """com.cs.tools.content.MyDecksLoaderTest.testGetSlidesXMLHasImageAndThumbnailUrls
       package - com.cs.tools.content
       group - MyDecksLoaderTest
       test_name - testGetSlidesXMLHasImageAndThumbnailUrls"""
    for j in failed_junit:
        """ 
        Apply some regular expression to find test_name and group and package
        """
        lst1 = j.split('.')
        test_name = lst1[-1]
        group = lst1[-2]
        val1 = re.sub(r'.[a-zA-Z]*$', "", j)
        package = re.sub(r'.[a-zA-Z]*$', "", val1)
        # Generate URL to publish failed test link in stash/bitbucket
        url = url + "testReport/junit/" + package + "/" + group + "/" + test_name
        print("[" + j + "] (" + url + ")")


def main():
    """ gather all command line arguments """
    args = getargs()
    dir_name = args.dir_name
    url = args.url
    fetch_junit(dir_name, url)


if __name__ == '__main__':
    main()

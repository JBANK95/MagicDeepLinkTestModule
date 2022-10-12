#!/usr/bin/env python
print("Hello World")


#!/bin/bash
import subprocess
import os
import re
import sys
import pathlib

class DeepLinkingCompliance:
    def __init__(self):
        self.temporaryFileStorePath = ".MagicDeeplinkConfig/AddedNewSwiftFilesList.txt"
        self.compliantViewControllerNames = []
        
       # self.getAddedSwiftFilesOnProject()
       # self.checkFilesForViewControllers()
       # if len(self.compliantViewControllerNames) > 0:
       #     self.checkInfoPlistForClassMapping()
'''
    # This function will find new swift files on project by using git diff command. Basically it will differentiate files with UMA-Origin and store list of files in temporary file.
    def getAddedSwiftFilesOnProject(self):
        self.create_file = subprocess.run(["touch", self.temporaryFileStorePath])
        self.git_branch_added_file_list = subprocess.run(["git", "diff", "--name-only", "--diff-filter=cdmrtuxb", "origin/UMA-Origin"], input=self.create_file.stdout, capture_output=True)
        self.list_only_uma_only_files = subprocess.run(["grep", "UMA/UMA_Main"], input=self.git_branch_added_file_list.stdout, capture_output=True)
        self.filter_swift_files_only = subprocess.run(["grep", ".*\\.swift$"], input=self.list_only_uma_only_files.stdout, capture_output=True)
        self.exclude_tests_files = subprocess.run(["grep", "-v", "Tests"], input=self.filter_swift_files_only.stdout, capture_output=True)
        self.store_output_in_file = subprocess.run(["tee", self.temporaryFileStorePath], input=self.exclude_tests_files.stdout, capture_output=True)
    
    # Get array from temporary files and access each file path
    def checkFilesForViewControllers(self):
        lines = []
        print("cd ..")
        with open(self.temporaryFileStorePath) as f:
            lines = f.readlines()
            self.deleteTempFile()
            for line in lines:
                self.processFileForProtocolCompliance(line)
    
    # Each files which are added need to check that it is UIViewController or not and check for  that confirms Routing Protocol by using regex.
    def processFileForProtocolCompliance(self, fileContents):
        textfile = open(fileContents.strip(), 'r')
        filetext = textfile.read()
                
        textfile.close()
    
        # Check if class extends UIViewController and does implement RoutingProtocol
        pattern = re.compile("class\s+(.*)\s*:(?=(.|\n)*UIViewController)(?=(.|\n)*RoutingProtocol)(.|\n)*{")
        matches = re.findall(pattern, filetext)

        # Match so class extends UIViewController and implements RoutingProtocol pull out class name and stor in array
        if len(matches) > 0:
            self.compliantViewControllerNames.append(matches[0][0])
        else:
            patternCheckViewController = re.compile("class\s+(.*)\s*:(?=(.|\n)*UIViewController)(.|\n)*{")
            matchesCheckViewController = re.findall(patternCheckViewController, filetext)
            if len(matchesCheckViewController) > 0:
                # Generic error message pass in xcode and exit further process.
                print("error: RoutingProtocol Missing: Please add RoutingProtocol and configure inside {} this file. For more details please read this page https://confluence.safeway.com/display/DMH/Magic+Deeplinking".format(fileContents))
                print("exit 0")
                try:
                    subprocess.check_output(shell=True,stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    raise RuntimeError("command return with error (code {}): {}".format(e.returncode, e.output))

    # Check configuration on plist file with that class name. that exists or not.
    def checkInfoPlistForClassMapping(self):
        DeepLinkingPushsectionMappingPlist = open("UMA/UMA_Main/MagicDeepLinking/DeepLinkingPushsectionMapping.plist", 'r')
        deeplinkPlist = DeepLinkingPushsectionMappingPlist.read()
        DeepLinkingPushsectionMappingPlist.close()
        for viewcontroller in self.compliantViewControllerNames:
            if viewcontroller in deeplinkPlist:
                print("configuration found")
            else:
                # Generic error message pass in xcode and exit further process.
                print("error: Missing {} configuration in DeepLinkingPushsectionMapping.plist: Please add RouterName as key and {} as value in DeepLinkingPushsectionMapping.plist. For more details please read this page https://confluence.safeway.com/display/DMH/Magic+Deeplinking".format(viewcontroller, viewcontroller))
                print("exit 0")
                try:
                    subprocess.check_output(shell=True,stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    raise RuntimeError("command return with error (code {}): {}".format(e.returncode, e.output))
        
    def deleteTempFile(self):
        file = pathlib.Path(self.temporaryFileStorePath)
        file.unlink()
   '''

DeepLinkingCompliance()


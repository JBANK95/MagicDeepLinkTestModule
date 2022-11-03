#!/usr/bin/env python3



import subprocess
import os
import re
import sys
import pathlib


class DeepLinkingCompliance:
    def __init__(self):
       
        self.module_name = "MagicDeepLinkTestModule"
        self.infoPlistMappingName = "DeepLinkingPushsectionMapping.plist"  # DO NOT RENAME
        self.pathToInfoPlistRoutesPath = "" # Add full path to the DeepLinkingPushSectionMapping.plist file if issues
        self.temporaryFileStorePath = "./AddedNewSwiftFilesList.txt"
        self.compliantViewControllerNames = []
        
        self.getAddedSwiftFilesOnProject()
        self.checkFilesForViewControllers()
        if len(self.compliantViewControllerNames) > 0:     
            self.checkInfoPlistForClassMapping()

    # This function will find new swift files on project by using git diff command. Basically it will differentiate files with UMA-Origin and store list of files in temporary file.
    def getAddedSwiftFilesOnProject(self):
        self.create_file = subprocess.run(["touch", self.temporaryFileStorePath])
        self.git_directory = subprocess.run(["pwd"], capture_output=True)
        self.runGitDiffAgainstOrigin()
      
        with open(self.temporaryFileStorePath, 'w') as f:
            for file_name in self.final_swift_files:
                f.write(f"%s\n" %(file_name))

    def runGitDiffAgainstOrigin(self):
        # Get reference to base PODS dir <PATH_TO_ECOM_REPO>/ecommobile_iOS/Pods then move up a level to grab podfile
        # to strip out the module name set above on line 16 and get path to it.  This is used to invoke git 
        # in the correct directory not ecommobile
        self.base_directory = os.getcwd()
        os.chdir("..")
        self.podfile_directory = os.getcwd()
        self.modulePath = self.getPathToModuleFromPodfile()


        # Keep older command iterations as reference
        # self.git_branch_added_file_list = subprocess.Popen(["git", "-C", self.git_directory.stdout.rstrip(), "diff", "--line-prefix=`git rev-parse --show-toplevel`/", "--name-only", "--diff-filter=cdmrtuxb", "origin/main"], shell=True)
        # self.git_branch_added_file_list = subprocess.Popen("git -C %s diff --line-prefix=`git rev-parse --show-toplevel`/ --name-only --diff-filter=cdmrtuxb origin/main" %(self.git_directory.stdout.rstrip()), stdout=subprocess.PIPE, shell=True)
        # cmd = "git -C %s diff --line-prefix=`git rev-parse --show-toplevel`/ --name-only --diff-filter=cdmrtuxb origin/main" %(self.modulePath)
        
        cmd = "git -C %s diff --name-only --diff-filter=cdmrtuxb origin/main" %(self.modulePath)
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, text=True, shell=True)
   
        self.git_branch_added_file_list, err = p.communicate()
        self.git_branch_added_file_list = self.git_branch_added_file_list.splitlines()

        self.final_swift_files = []
        for file in self.git_branch_added_file_list:
            if re.match(r".*.swift$", file):
                if re.match(r"(?!Tests)", file):
                    try: # if module is installed POD
                        open(file, 'r')
                        self.final_swift_files.append(file)
                    except: # if module is development POD
                        self.final_swift_files.append(self.modulePath + "/" + file)


    def getPathToModuleFromPodfile(self):
        podfile = self.podfile_directory + "/Podfile"
        with open(podfile) as f:
            lines = f.readlines()
            for line in lines:
                if self.module_name in line:
                    t = line.strip().split("=>")
                    finalModulePath = t[1].strip()[1:-1]
                    return finalModulePath
                
        return ""

    # Get array from temporary files and access each file path
    def checkFilesForViewControllers(self):
        lines = []
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
                print("error: RoutingProtocol Missing Please add RoutingProtocol and configure inside %s" %(fileContents))
                print("error: For more details please read this page https://confluence.safeway.com/pages/viewpage.action?pageId=197470484")
                sys.exit(1)

    # Check configuration on plist file with that class name. that exists or not.
    def checkInfoPlistForClassMapping(self):
        try:
            # Place plist on correct path
            DeepLinkingPushsectionMappingPlist = open(self.pathToInfoPlistRoutesPath, 'r')
            print("Attempting to open and check routes in file %s" %(self.pathToInfoPlistRoutesPath))
        except:
            try:
                # Should be <PATH_TO_CODE_DIR>/<PODNAME>/<PODNAME>/DeepLinkingPushsectionMapping.plist
                print("Attempting to open and check routes in file on path %s/%s/%s" %(self.modulePath, self.module_name, self.infoPlistMappingName))
                DeepLinkingPushsectionMappingPlist = open(self.modulePath + "/" + self.module_name + "/" + self.infoPlistMappingName, 'r')

            except:

                print("error: Couldn't open the deep linking push Section mapping pList file on the path %s/%s/%s" %(self.modulePath, self.module_name, self.infoPlistMappingName))
                print("error: For more details please read this page https://confluence.safeway.com/pages/viewpage.action?pageId=197470484")
                sys.exit(1)

        deeplinkPlist = DeepLinkingPushsectionMappingPlist.read()
        DeepLinkingPushsectionMappingPlist.close()
        for viewcontroller in self.compliantViewControllerNames:
            if viewcontroller in deeplinkPlist:
                print("configuration found")
            else:
                # Generic error message pass in xcode and exit further process.
                
                print("error: Missing %s configuration in DeepLinkingPushsectionMapping.plist Please add RouterName as key and %s as value in DeepLinkingPushsectionMapping.plist. For more details please read this page https://confluence.safeway.com/pages/viewpage.action?pageId=197470484" %(viewcontroller, viewcontroller))
                sys.exit(1)

    def deleteTempFile(self):
        file = pathlib.Path(self.temporaryFileStorePath)
        file.unlink()



DeepLinkingCompliance()





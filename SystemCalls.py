#!/usr/bin/env python3
from pprint import pprint as pp
import subprocess
import time
import os
# import urllib.parse as urlparse
# import sys
# import shutil


def main():
    """
    To interpret command from a url, pass the URL as a parameter in the main function
    url = 'http://foo.appspot.com/abc?def=ghi'
    parsed = urlparse.urlparse(url)
    """
    val = int(input("Press 1 for Git to TFS. \nPress 2 for TFS to Git.\n"))
    login()
    if val == 1:
        git_tfs()
    else:
        tfs_git()


def login():
    subprocess.call(["git", "config", "--global", "user.name", "aishwarye"])
    subprocess.call(["git", "config", "--global", "user.email", "721aish@gmail.com"])


def git_tfs():
    pp("Enter the TFS URL and Git URL: ")
    time.sleep(2)
    tfs_url = "http://tfs2.dell.com:8080/tfs/edell/BOSS/BOSS%20Team/versionControl?path=%24%2FBOSS%2FPROD%2FRELEASE" \
              "%2FPCFMIGRATION%2Fsource%2FDELLEMC_CONNVERSATIONAL_AI&version=T&_a=contents"  # sys.argv[0]
    git_url = "https://github.com/aishwarye/DormRoom"  # sys.argv[1]
    cmd = "{0} {1} --deep".format(tfs_url, git_url)
    pp(cmd)
    cwdir = 'C:\\Users\\Aishwarye_Chaudhary\\Downloads\\Hackathon\\DormRooms'
    time.sleep(2)
    pp(os.path.exists(cwdir))
    try:
        if os.path.exists(cwdir):
            pp("Directory exists.")
            subprocess.call(["git", "init"])
            # shutil.rmtree(cwdir)
            subprocess.call(["rmdir", cwdir])
            pp("Directory removed.")
    except FileNotFoundError:
        pass
    # subprocess.call(["rmdir", cwdir])
    time.sleep(2)
    """
    git init .
    git remote add -t \* -f origin <repository-url>
    git checkout master
    subprocess.call(["git-tfs", "clone", "--deep", tfs_url, git_url])
    """
    subprocess.call(["git", "clone", git_url, cwdir])
    # subprocess.call(["git", "init"])
    # subprocess.call(["git", "pull"])


def tfs_git():
    subprocess.call(["git", "pull"])
    subprocess.call(["git", "init"])
    subprocess.call(["git", "remote", "add", "-f", "origin", "https://github.com/aishwarye/DormRoom"])
    pp("Preparing to stage the files...")
    subprocess.call(["git", "add", "."])
    pp("Files staged.")
    pp("Committing the files now.")
    subprocess.call(["git", "commit", "--amend", "-m", "'Add existing file'"])
    pp("Now, pushing the changes.")
    subprocess.call(["git", "push", "-u", "-f", "origin", "master"])  # "--all" "DormRoom", "master"])
    pp("Pushed.")


if __name__ == '__main__':
    main()  # Pass sys.argv[0] as a parameter containing the URL

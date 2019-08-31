#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE, call

from sys import platform as _platform
from subprocess import Popen, PIPE, call
import os.path
import sys

FOLDERS = ["Train", "Validation"]


def check_exist():
  confirm = False
  if os.path.exists("data/{}".format(FOLDERS[0])):
    confirm = confirm or True
  if os.path.exists("data/{}".format(FOLDERS[1])):
    confirm = confirm or True
  return confirm


def delete_folders():
  if os.path.exists("data/{}".format(FOLDERS[0])):
    Popen("rm -r data/{}".format(FOLDERS[0]), stdout=PIPE, shell=True)
  if os.path.exists("data/{}".format(FOLDERS[1])):
    Popen("rm -r data/{}".format(FOLDERS[1]), stdout=PIPE, shell=True)


def download(command):
  cmd = Popen(command, stdout=PIPE, shell=True)
  output = cmd.communicate()[0]
  print(output.decode("utf-8"))


def continue_operation():
  if check_exist():
    verify = input("The operation delete folder data, continue? (y|n): ")
    if verify == "y":
      delete_folders()
      return True
    else:
      return False
  else:
    return True


if __name__ == "__main__":
  if continue_operation():
    folder_id_train = sys.argv[1]
    folder_id_validation = sys.argv[2]
    command = "cp libs/Linux/gdrive-linux-x64 data && cd data  && chmod +x gdrive-linux-x64 && ./gdrive-linux-x64 download --recursive {} && rm gdrive-linux-x64".format(
        folder_id_train)
    download(command)
    command = "cp libs/Linux/gdrive-linux-x64 data && cd data  && chmod +x gdrive-linux-x64 && ./gdrive-linux-x64 download --recursive {} && rm gdrive-linux-x64".format(
        folder_id_validation)
    download(command)

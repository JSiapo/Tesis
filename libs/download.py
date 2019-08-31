#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE, call

from sys import platform as _platform
from subprocess import Popen, PIPE, call
import os.path
import sys

def check_exist(data):
  if os.path.exists(data):
    return True
  else:
    return False


def delete_folders():
  if os.path.exists("data"):
    cmd = Popen("rm -r data", stdout=PIPE, shell=True)
    cmd.communicate()[0]


def download(command):
  cmd = Popen(command, stdout=PIPE, shell=True)
  output = cmd.communicate()[0]
  print(output.decode("utf-8"))


def validate_input(verify):
  if verify == "y" or verify == "yes" or verify == "":
    delete_folders()
    cmd_dir = Popen("mkdir data", stdout=PIPE, shell=True)
    cmd_dir.communicate()[0]
    init_file = open("data/__init__.py", "w")
    init_file.close()
    return True
  else:
    raise ValueError ("Error con input")


def continue_operation():
  if check_exist("data"):
    verify = input("The operation delete folder data, continue? (y|n): ")
    try:
      validate_input(verify)
      return True
    except ValueError:
      return False
  else:
    return True


def operation(folder_id_train=None, folder_id_validation=None):
  if (type(folder_id_train) != str and type(folder_id_validation) != str and folder_id_train != None and folder_id_validation != None):
    raise ValueError("Deben ser strings")
  else:
    command = "cp libs/Linux/gdrive-linux-x64 data && cd data  && chmod +x gdrive-linux-x64 && ./gdrive-linux-x64 download --recursive {} && rm gdrive-linux-x64".format(
        folder_id_train)
    download(command)
    command = "cp libs/Linux/gdrive-linux-x64 data && cd data  && chmod +x gdrive-linux-x64 && ./gdrive-linux-x64 download --recursive {} && rm gdrive-linux-x64".format(
        folder_id_validation)
    download(command)
    return True


if __name__ == "__main__":
  if continue_operation():
    try:
      operation(folder_id_train=sys.argv[1], folder_id_validation=sys.argv[2])
    except ValueError:
      print("Colocar los parametros adecuados")

import os

class changeDir:
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)

  # Change directory with the new path
  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  # Return back to previous directory
  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)
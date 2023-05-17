import os
import traceback

from frontend.settings import BASE_DIR

# BASE_DIR G:\Study\PersonalProjects\frontend

class FileTool(object):
  def __init__(self, path) -> None:
    self.path = os.path.join(BASE_DIR, 'statics', path)

  def create_folder(self, path):
    try:
      os.makedirs(os.path.join(self.path, path), exist_ok=True)
    except:
      print(traceback.format_exc())

  def write_file(self, folder_path, filename, buffer):
    try:
      self.create_folder(folder_path)
      _target = os.path.join(self.path, folder_path, filename)
      with open(_target, 'wb') as destination:
        for chunk in buffer.chunks():
          destination.write(chunk)
      return True
    except OSError:
      print(traceback.format_exc())
      return False
    except:
      print(traceback.format_exc())
      return False
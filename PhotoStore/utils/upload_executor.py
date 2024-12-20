import os

TEMP_PATH = ''


class UploadExecutor(object):
    def __init__(self, filename, storepath, root, binaries, ext_checks=[]) -> None:
        self._filename = filename
        self._storepath = storepath
        self._root = root
        self._ext_checks = ext_checks
        self._binaries = binaries

    def open_file(self):
        path = os.path.join(TEMP_PATH, self._storepath, self._filename)
        return open(path, 'wb')

    def save_temp_path(self):
        with self.open_file() as f:
            f.write(self._binaries)

    def is_vaildate(self):
        pass

    def save(self):
        pass

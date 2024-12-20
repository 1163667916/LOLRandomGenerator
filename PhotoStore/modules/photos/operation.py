from PhotoStore.models import Photos


class BasePhotoOperation(object):
    def __init__(self) -> None:
        self._model = Photos

    def create_and_save(self, *args, **kwargs):
        obj = self._model.objects.create(*args, **kwargs)
        return obj

    def filter(self, *args, **kwargs):
        return self._model.objects.filter(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._model.objects.filter(*args, **kwargs).delete()

    def update(self, *args, **kwargs):
        return self._model.objects.filter(*args, **kwargs).delete()


class PhotoOperation(BasePhotoOperation):
    def __init__(self) -> None:
        super().__init__()

    def handle_upload(self, ):
        pass

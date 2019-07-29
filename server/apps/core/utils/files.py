import uuid
import ntpath
import datetime

from django.utils.deconstruct import deconstructible


def extract_extension(path, is_link=False):
    """Try to extract extension from a file name, file system path or url."""
    path = ntpath.basename(path)
    if is_link:
        for sign in ['?', '&']:
            while sign in path:
                path = path[:path.find(sign)]
    if '.' in path:
        return '.' + path.split('.')[-1]
    return ''


@deconstructible
class UniqueUploadPath(object):
    """Returns a function that is passed to `upload_to` in File/Image field."""
    def __init__(self, base_dir):
        """
        :param base_dir: Base dir for uploading.
        """
        self._base_dir = base_dir

    def __call__(self, _, filename):
        return '{dir}/{date}/{id}{extension}'.format(
            dir=self._base_dir,
            date=datetime.date.today().strftime('%Y%m%d'),
            id=uuid.uuid4().hex,
            extension=extract_extension(filename)
        )

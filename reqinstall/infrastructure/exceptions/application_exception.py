class ApplicationException(Exception):
    def __init__(self, *args, **kwargs):
        super(ApplicationException, self).__init__(*args, **kwargs)

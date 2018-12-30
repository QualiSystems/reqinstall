class ApplicationException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super(ApplicationException, self).__init__(*args, **kwargs)

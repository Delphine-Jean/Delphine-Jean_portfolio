from datetime import datetime

#Abstract Layer object abstract layers
class AbstractModel:

    created: datetime

    def __init__(self, **kwargs):
        """
        goal :
        :param kwargs:
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
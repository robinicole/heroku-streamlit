"""
Base class for a streamlit view
"""
from abc import ABC, abstractmethod


class BaseView(ABC):
    """
    Base class for a streamlit view
    """
    name: str
    @classmethod
    def get_name(cls):
        """
        Getter for the name of the class
        """
        return cls.name

    @abstractmethod
    def display(self):
        """
        Overwrite this method to display
        your page
        """
        raise NotImplementedError

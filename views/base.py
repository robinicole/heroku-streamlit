from abc import ABC, abstractmethod


class BaseView(ABC):
    name: str
    
    @abstractmethod
    def display(self):
        raise NotImplementedError

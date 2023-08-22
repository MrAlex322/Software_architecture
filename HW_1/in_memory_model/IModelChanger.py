from abc import ABC, abstractmethod
from IModelChangeObserver import IModelChangeObserver


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(data: IModelChangersender) -> None:
        pass
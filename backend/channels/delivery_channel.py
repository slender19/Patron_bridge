from abc import ABC, abstractmethod
from typing import Tuple

class DeliveryChannel(ABC):

    @abstractmethod
    def deliver(self, title: str, message: str) -> Tuple[bool, str]:
        
        raise NotImplementedError

from abc import ABC, abstractmethod
from typing import List, Any
from common.message import Message


class Router(ABC):
    """Abstract interface for all StormNet routing algorithms.
    
    Both baseline routers (Module 1: Epidemic, Spray-and-Wait) and the predictive
    optimization router (Module 2: Hankel + DMD + QP) must implement this method.
    """
    @abstractmethod
    def select_next_hops(self, node: Any, message: Message, neighbours: List[Any], now: float) -> List[Any]:
        """Determine which neighbour nodes should receive a copy of message right now.
        
        Args:
            node: The transmitting node holding the message in its buffer.
            message: The Message instance being considered for forwarding.
            neighbours: The current list of active, in-range neighbour nodes.
            now: Current simulation timestamp in seconds.
            
        Returns:
            List of neighbour nodes to forward the message to, or an empty list [] to wait.
        """
        pass


class EpidemicRouter(Router):
    """Baseline 1: Floods the message to all neighbouring nodes that have not seen it yet."""
    def select_next_hops(self, node: Any, message: Message, neighbours: List[Any], now: float) -> List[Any]:
        return [n for n in neighbours if message.id not in n.seen]

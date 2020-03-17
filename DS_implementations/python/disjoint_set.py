from collections import defaultdict
from typing import Generic, TypeVar, DefaultDict, Dict

T = TypeVar('T')


class DisjointSet(Generic[T]):
    """Generic Disjoint Set implementation"""

    def __init__(self):
        self._parents: Dict[T, T] = {}
        self._sizes: DefaultDict[T, int] = defaultdict(lambda: 1)

    def find_root(self, x: T) -> T:
        """
        Find the component in which x belongs in.
        Uses path compression.
        Amortized Time complexity per query ~O(1)
        """
        node, root = None, x
        while root != node:  # using loop instead of recursion due to Python recursion limit
            node, root = root, self._parents.get(root, root)
        while x != root:
            x = self._parents.get(x, x)
            self._parents[x] = root  # path compression
        return root

    def size_of(self, x: T) -> int:
        """
        Find the size of the component that x belongs in
        Time Complexity per query: O(1)
        """
        return self._sizes[self.find_root(x)]

    def merge_components(self, x: T, y: T) -> None:
        """
        Merge the components in which the items x and y belong in
        Amortized Time Complexity per query: ~O(1)
        """
        x, y = self.find_root(x), self.find_root(y)
        if x == y: return  # if both x and y are already in the same component, do thing
        if self.size_of(x) < self.size_of(y):
            x, y = y, x  # swap so that y is always the larger component
        self._parents[y] = x
        self._sizes[x] += self._sizes[y]
        del self._sizes[y]

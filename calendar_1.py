from typing import Optional


class Node():
    def __init__(self, start: int, end: int):
        """
        Initializes a Node instance with start and end times.

        Args:
            start (int): The start time of the time interval.
            end (int): The end time of the time interval.
        """
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self,node: 'Node')-> bool:
        """
        Inserts a new node into the tree, checking for time interval overlaps.

        Args:
            node (Node): The node to be inserted.

        Returns:
            bool: True if insertion is successful (no overlap), False if an overlap is detected.
        """
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)
        elif node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        else:
            return False


class Calendar():
    def __init__(self):
        """
        Initializes an empty calendar.
        """
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        """
        Books a new event in the calendar.

        Args:
            start (int): The start time of the event.
            end (int): The end time of the event.

        Returns:
            bool: True if the event can be added without causing a double booking, False otherwise.
        """
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        return self.root.insert(node=Node(start, end))

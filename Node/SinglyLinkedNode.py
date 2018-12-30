from Node.Node import Node
from Globals import Globals


class SinglyLinkedNode(Node):
    """

    """

    def __init__(self, data, successor):
        Node.__init__(self, data)

        self.__successor = successor

    def __str__(self):
        """

        """
        return \
            "Node: " + "\n" + \
            "Node Data: " + str(self.data) + "\n" + \
            "Successor: " + str(self.successor) + "\n"

    def __eq__(self, other):
        pass

    def __deepcopy__(self, memodict={}):
        """

        """
        return \
            SinglyLinkedNode(
                data=self.data,
                successor=self.successor
            )

    @property
    def successor(self):
        """

        """
        return self.__successor

    @successor.setter
    def successor(self, successor):
        """

        """
        self.__successor = successor


class EmptySinglyLinkedNode(SinglyLinkedNode):
    """

    """

    __singleton = None

    def __init__(self):
        SinglyLinkedNode.__init__(self, None, None)

        if EmptySinglyLinkedNode.__singleton is not None:  # handle multiple client-side calls
            raise Exception(Globals.SINGLETON_EXCEPTION_ERROR)  # raise an exception
        else:  # if this is the first and only call to this method
            EmptySinglyLinkedNode.__singleton = self  #

    def make(self):
        """

        """
        if EmptySinglyLinkedNode.__singleton is None:
            EmptySinglyLinkedNode()

        return EmptySinglyLinkedNode.__singleton

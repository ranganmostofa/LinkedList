from abc import ABCMeta
from Globals import Globals


class Node(metaclass=ABCMeta):
    """
    Abstract Node superclass that implements the idea of a general node object capable of acting as a
    data container
    """

    def __init__(self, data):
        """
        Constructor for the Node class - given the required inputs for all fields and properties,
        initializes said fields and properties for every instance of every concrete subclass that
        inherits this abstract Node superclass
        """
        self.__data = data  # initialize the fields and properties

    def __str__(self):
        """
        Returns a string representation of the data contained in this node
        """
        return \
            "Node: " + "\n" + \
            "Node Data: " + str(self.data) + "\n"  # return the string representation

    def __hash__(self):
        """
        Computes and returns the hash value of the string for any instance of this class
        """
        return hash(str(self))  # return the hash value

    def __eq__(self, other):
        """
        Given a second node, checks if the data contained in this node and the input node are the same
        objects in memory
        """
        # return True if the data contained in both TreeNode objects exist in the same location in memory
        # and False otherwise
        return self.data is other.data

    def same_obj(self, other):
        """
        Given a second node, checks if this node and the input node are the same objects in memory
        """
        # return True if both TreeNode objects exist in the same location in memory and False otherwise
        return self is other

    @property
    def data(self):
        """
        Returns the data contained in this node
        """
        return self.__data  # return the data

    @data.setter
    def data(self, data):
        """
        Given new data, sets the current stored data as the new stored data
        """
        self.__data = data  # set the current stored data as the new stored data


class EmptyNode(Node):
    """
    Abstract class that uses the singleton design pattern to model empty nodes
    """

    __singleton = None  # initialize the singleton instance as a null value

    def __init__(self):
        """
        Virtually private constructor - multiple calls to this procedure from the client-side should
        raise an exception. Use the EmptyNode.make() method instead.
        """
        Node.__init__(self, None)

        if EmptyNode.__singleton is not None:  # handle multiple client-side calls
            raise Exception(Globals.SINGLETON_EXCEPTION_ERROR)  # raise an exception
        else:  # if this is the first and only call to this method
            EmptyNode.__singleton = self  #

    @staticmethod
    def make():
        """

        """
        if EmptyNode.__singleton is None:
            EmptyNode()

        return EmptyNode.__singleton

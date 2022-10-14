"""
file: cast.py
authors: authors of Snake
purpose: This class represents the collection of Actors which appear on the terminal screen
during and after game play.
"""

# class declaration
class Cast:
    """A collection of Actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    # default constructor
    def __init__(self):
        """Constructs a new Actor.
        
        Parameters: none
        Return: none
        """
        # declare the dictionary of Actors
        self._actors = {}
        
    # method to add an actor to a group
    def add_actor(self, group, actor):
        """This method adds an actor to the given group.
        
        Parameters: group (String): The name of the group.
                    actor (Actor): The actor to add.
        Return: nothing
        """
        # if the group doesn't exist, create it, declare list
        if not group in self._actors.keys():
            self._actors[group] = []

        # if the actor is not in the group, add it, append to group list    
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    # method to get a group of actors
    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Parameters: group (String) - The name of the group.
        Returns:    results (List) - All the actors in the requested group.
        """
        # declare empty list variable
        results = []

        # if the group exists in the keys, load the list with the information, return it
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    # method to get all actors, inclusive
    def get_all_actors(self):
        """Gets all of the actors in the cast, return them in a list.
        
        Parameters: none
        Returns:    results (List) - Return all of the actors in the cast in a list.
        """
        # declare empty list in preparation to storing all actors in it
        results = []

        # loop through the cast, put all actors in the results list, then return it
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    # method to get the first actor in a given group
    def get_first_actor(self, group):
        """Gets the first actor in the given group and returns it.
        
        Parameters: group (String) - The name of the group the first element is in.
        Returns:    results (List) - Return the first actor in the passed group.
        """
        # declare empty variable for return information 
        result = None

        # if the group is in the dictionary as a key, load variable with Actor/Cycle 
        # in element 0, return with information
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    # method to get the second actor in a given group
    def get_second_actor(self, group):
        """Gets the second actor in the given group and returns it.
        
        Parameters: group (String) - The name of the group second element is in.
        Returns:    results (List) - Return the second actor in the passed group.
        """
        # declare empty variable for return information
        result = None

        # if the group is in the dictionary as a key, load variable with Actor/Cycle 
        # in element 1, return with information
        if group in self._actors.keys():
            result = self._actors[group][1]
        return result

    # method to remove an actor from a given group
    def remove_actor(self, group, actor):
        """This method removes an actor from the given group.
        
        Parameters: group (String) - The name of the group the actor is in.
                    actor (Actor) - The actor to be removed from the dictionary.
        Returns:    nothing
        """
        if group in self._actors:
            self._actors[group].remove(actor)
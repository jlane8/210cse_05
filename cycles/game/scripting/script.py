"""
file: script.py
author: authors of Snake
purpose: This class acts as a dictionary, containing all actions of the game.
"""

# class declaration
class Script:
    """A collection of actions.

    The responsibility of Script is to keep track of all game actions. It has methods for 
    adding, removing and getting them by a group name, singly or as a group.

    Attributes:
        _actions (dict): A dictionary of actions { key: group_name, value: a list of actions }
    """

    # default constructor
    def __init__(self):
        """Constructs a new Action.
        
        Parameters: none
        Returns: nothing
        """
        self._actions = {}
        
    # method to add an action to the script
    def add_action(self, group, action):
        """Adds an action to the given group.
        
        Parameters: group (String) - The name of the group.
                    action (Action) - The action to add.
        Returns: nothing
        """
        # if group doesn't exist, create a new one
        if not group in self._actions.keys():
            self._actions[group] = []
        
        # if the action doesn't exist in the group's list,
        # add it
        if not action in self._actions[group]:
            self._actions[group].append(action)

    # method to get the actions of a particular group
    def get_actions(self, group):
        """Gets the actions in the given group.
        
        Parameters: group (String) - The name of the group.
        Returns: results (List) - The actions in the group's list.
        """
        # declare empty list in preparation of getting the 
        # group's actions
        results = []
        
        # if the group is in the dictionary keys, get actions
        # and store in results list
        if group in self._actions.keys():
            results = self._actions[group].copy()
        
        # return results
        return results
    
    # method to remove an action from the script's dictionary
    def remove_action(self, group, action):
        """Removes an action from the given group.
        
        Parameters: group (String) - The name of the group.
                    action (Action) - The action to remove.
        Returns: nothing
        """
        # if the group exists in the dictionary, remove
        # the parameter actions
        if group in self._actions:
            self._actions[group].remove(action)
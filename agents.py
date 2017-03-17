# Robin Mehta
# EECS 492 Homework 1

import world
import numpy
from numpy.random import randint

class simple_reflex_agent:
    def __init__(self):
        # Agent has no state, so nothing to do here
        return

    # Given a valid percept (a string), return a valid action (also as a string)
    def choose_action(self, percept):
        ##### Implement this function #####
        if percept == "start":
            return "sense_water"
        if percept == "needs_watering":
            return "water"
        if percept == "watering_succeeded":
            return "sense_weed"
        if percept == "does_not_need_watering":
            return "sense_weed"
        if percept == "needs_weeding":
            return "weed"
        if percept == "does_not_need_weeding":
            return "move"
        if percept == "weeding_succeeded":
            return "move"
        if percept == "move_succeeded":
            return "sense_water"
        if percept == "hit_barrier":
            return "move"

        # Returning an arbitrary action so don't get import errors if function not written
        # You may remove this when you've finished implementing
        return 'water'
        #################################


class state_reflex_agent:
    def __init__(self, worldstate):
        # This agent has a state, so wants to do BFS on the world
        # self.plan is a list of moves for the agent to take through the world
        # self.position is the position in the list
        self.plan, plan_exists = world.BFS(worldstate)
        if not plan_exists:
            raise RuntimeError('Plan does not exist or BFS iteration limit exceeded')
        self.position = 0

    # Given a valid percept (a string), return a valid action (also as a string)
    def choose_action(self, percept):
        if (percept == "start") or (percept == "move_succeeded"):
            return "sense_water"

        if percept == "needs_watering":
            return "water"

        if (percept == "watering_succeeded") or (percept == "does_not_need_watering"):
            return "sense_weed"

        if percept == "needs_weeding":
            return "weed"

        if (percept == "does_not_need_weeding") or (percept == "weeding_succeeded"):

            if self.plan[self.position] == "move_north":
                self.position = self.position + 1
                return "move_north"

            elif self.plan[self.position] == "move_east":
                self.position = self.position + 1
                return "move_east"

            elif self.plan[self.position] == "move_south":
                self.position = self.position + 1
                return "move_south"

            else:
                self.position = self.position + 1

                return "move_west"

        if percept == "hit_barrier":
            return ""

        #################################

class random_reflex_agent:
    def __init__(self):
        # Agent has no state, so nothing to do here
        return

    # Given a valid percept (a string), return a valid action (also as a string)
    def choose_action(self, percept):
        #### Implement this function ####
        if (percept == "start") or (percept == "move_succeeded"):
            return "sense_water"

        if percept == "needs_watering":
            return "water"

        if (percept == "watering_succeeded") or (percept == "does_not_need_watering"):
            return "sense_weed"

        if percept == "needs_weeding":
            return "weed"

        if (percept == "does_not_need_weeding") or (percept == "weeding_succeeded") or (percept == "hit_barrier"):

            randomInt = numpy.random.randint(0, 4)

            if randomInt == 0:
                return "move_north"

            elif randomInt == 1:
                return "move_east"

            elif randomInt == 2:
                return "move_south"

            else:
                return "move_west"

        # Returning an arbitrary action so don't get import errors if function not written
        # You may remove this when you've finished implementing
        return 'water'
        #################################

class better_reflex_agent:
    def __init__(self):
        # Agent cannot see the world in advance
        # However, you may initialize any number of your own state variables here

        self.num_barriers = 0
        self.direction = 0
        self.num_successful_moves = 0

        return

    # Given a valid percept (a string), return a valid action (also as a string)
    def choose_action(self, percept):
        if percept == "start":
            return "sense_water"
        if percept == "needs_watering":
            return "water"
        if percept == "watering_succeeded":
            return "sense_weed"
        if percept == "does_not_need_watering":
            return "sense_weed"
        if percept == "needs_weeding":
            return "weed"
        if percept == "does_not_need_weeding":
            return "move"
        if percept == "weeding_succeeded":
            return "move"
        if percept == "move_succeeded":
            self.num_successful_moves = self.num_successful_moves + 1
            if ((self.num_successful_moves % 4) == 0) and ((self.num_barriers % 4) == 3):
                return "move"
            else:
                return "sense_water"
        if percept == "hit_barrier":
            self.num_barriers = self.num_barriers + 1
            self.direction = self.direction + 1
            self.direction = self.direction % 4
            return "move"

        # Returning an arbitrary action so don't get import errors if function not written
        # You may remove this when you've finished implementing
        return 'water'
        #################################


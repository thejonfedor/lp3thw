# this code is the structure template for
# Gorthons from Planet Percal 25. It's the starting
# point provided by Zed to be expanded on and developed
# by the reader. Use this template if I need a clean-slate
# restart on the exercise.

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self,scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
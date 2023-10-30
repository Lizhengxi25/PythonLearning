class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, game_map):
        self.game_map = game_map
        self.last_scene = self.game_map.next_scene("Death")

    def play(self):
        current_scene = self.game_map.opening_scene()
        while current_scene != self.last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.game_map.next_scene(next_scene_name)
        self.game_map.next_scene("Death")


class Death(Scene):

    def enter(self):
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("CentralCorridor here")
        goal_scene = input("goal scene")
        return goal_scene

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        print("The Bridge")
        goal_scene = input("goal scene")
        return goal_scene

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    Scenes = {
        "Death": Death(),
        "CentralCorridor": CentralCorridor(),
        "TheBridge": TheBridge()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.Scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# a_map = Map("CentralCorridor")
# a_game = Engine(a_map)
# a_game.play()

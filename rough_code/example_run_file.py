from welcome_interface import Welcome_interface
from menu_interface import Menu_interface

class Airport():
    def run_operations(self):
        object1 = Welcome_interface()
        object1.user_interaction_passengers()
        object2 = Menu_interface()
        object2.select_options()


object = Airport()
object.run_operations()
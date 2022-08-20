import inputs
import screens

running = True

inputManager = inputs.InputManager()
screenManager = screens.ScreenManager(inputManager)

currentScreen = "Main Menu"

while running:
    screenManager.clear()
    if currentScreen == "":
        running = False
    else:
       currentScreen = screenManager.runScreen(currentScreen)
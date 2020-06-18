import pyttsx3


def robot_say(robot_clause):
    engine = pyttsx3.init()
    engine.say(robot_clause)
    engine.runAndWait()

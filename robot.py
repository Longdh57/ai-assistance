import helpers
import robot_ear, robot_brain, robot_mouth


while True:
    client_clause = robot_ear.hear_from_customer()

    if "bye" in client_clause:
        helpers.robot_print("Nice to see you. Bye")
        break

    what_robot_thinking = robot_brain.robot_thinking(client_clause)

    robot_mouth.robot_say(what_robot_thinking)
import helpers


def robot_thinking(client_clause):
    if client_clause == "hello":
        robot_brain = "Hello Long"
    else:
        robot_brain = "I can't understand"

    helpers.robot_print(robot_brain)
    return robot_brain

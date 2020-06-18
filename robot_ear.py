import helpers
import speech_recognition


def hear_from_customer():
    robot_ear = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        helpers.robot_print("I'm listening")
        audio = robot_ear.listen(mic)

    try:
        client_clause = robot_ear.recognize_google(audio)
    except:
        client_clause = ""

    helpers.client_print(client_clause)

    return client_clause

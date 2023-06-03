import socket
import json
from threading import Thread


def handle_client(client_socket):
    """
    Handles communication with a client.
    Args:
        client_socket (socket.socket): The client socket object.
    """
    print("Connected to", client_socket.getpeername())
    received_data = client_socket.recv(4096).decode('utf-8')
    data = json.loads(received_data)

    response = {
        "imc": generate_imc(data),
        "imcStatus": get_imc_status(data),
        "bmr": generate_bmr(data),
        "calorieIntake": calculate_calorie_intake(data),
        "nutrients": calculate_nutrients(data)
    }

    response_data = json.dumps(response)
    client_socket.send(response_data.encode('utf-8'))
    client_socket.close()
    print("Connection closed with", client_socket.getpeername())


def generate_imc(data):
    """
    Generates the Body Mass Index (IMC).
    Args:
        data (dict): The user data dictionary.
    Returns:
        float: The calculated IMC.
    """
    height = data['height']
    weight = data['weight']
    imc = weight / (height ** 2)
    return imc


def get_imc_status(data):
    """
    Gets the status corresponding to the calculated IMC.
    Args:
        data (dict): The user data dictionary.
    Returns:
        str: The IMC status.
    """
    imc = generate_imc(data)
    if imc < 18.5:
        return "Underweight"
    elif 18.5 <= imc < 25:
        return "Normal weight"
    elif 25 <= imc < 30:
        return "Overweight"
    elif 30 <= imc < 35:
        return "Obesity Grade 1"
    elif 35 <= imc < 40:
        return "Obesity Grade 2"
    else:
        return "Obesity Grade 3"


def generate_bmr(data):
    """
    Generates the Basal Metabolic Rate (BMR).
    Args:
        data (dict): The user data dictionary.
    Returns:
        float: The calculated BMR.
    """
    height = data['height']
    weight = data['weight']
    gender = data['gender']
    activity_level = data['activityLevel']
    age = data['age']

    if gender.lower() == 'm':
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161

    return bmr


def calculate_calorie_intake(data):
    """
    Calculates the recommended daily calorie.
    Args:
        data (dict): The user data dictionary.
    Returns:
        float: The calculated daily calorie intake.
    """
    bmr = generate_bmr(data)
    activity_level = data['activityLevel']

    calorie_intake = bmr * activity_level

    return calorie_intake


def calculate_nutrients(data):
    """
    Calculates the recommended daily intake of carbohydrates, proteins, and fats.
    Args:
        data (dict): user data dictionary.
    Returns:
        dict: nutrient values.
    """
    weight = data['weight']
    carbohydrates = weight * 3
    proteins = weight * 1
    fats = weight * 0.7

    nutrients = {
        "carbohydrates": carbohydrates,
        "proteins": proteins,
        "fats": fats
    }

    return nutrients


def start_server():
    """
    Starts the server and listens for client connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)
    server_socket.bind(server_address)

    print("Server running on port", server_address[1])

    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == '__main__':
    start_server()

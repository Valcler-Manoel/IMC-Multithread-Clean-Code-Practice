class App:
    """
    Class of the application.
    """

    def __init__(self):
        """
        Initializes the application.
        """
        App.title("The Shape of Us!")
        print()
        print("=> Enter some data to get started: ")
        print()
        App.generate_header()

    @staticmethod
    def padding():
        """
        Adds padding to the output.
        """
        print()
        print()

    @staticmethod
    def generate_header():
        """
        Generates the header for the data input section.
        """
        print("NOTE: Activity level ranges from 1 (Sedentary) to 4 (Very Active)!")
        print("Ex: {:^8s} {:^22s} {:^14s} {:^20s} {:^10s} ".format(
            "1.70", "70.0", "M", "3", "20"))
        print()

    @staticmethod
    def row():
        """
        Prints a row for visual separation.
        """
        print('*' * 81)

    @staticmethod
    def row_table():
        """
        Prints a row dashes for table separation.
        """
        print(f"+{'-' * 25}++{'-' * 25}++{'-' * 25}+")

    @staticmethod
    def title(title):
        """
        Prints the application title.
        Args:
            title (str): Title of the application.
        """
        App.row()
        print('*{:^79s}*'.format(title))
        App.row()

    @staticmethod
    def collect_user_data():
        """
        Collects user data from input.
        Returns:
            list: The collected user data.
        """
        print("{:^16s}".format("Height (m):"), end="")
        print("{:^18s}".format("Weight (Kg):"), end="")
        print("{:^18s}".format("Gender (M/F):"), end="")
        print("{:^18s}".format("Activity Level:"), end="")
        print("{:^16s}".format("Age:"))

        user_data = input("").split(" ")
        print()
        App.row()

        return user_data

    @staticmethod
    def list_user_data(values):
        """
        Converts user data
        Args:
            values (list): User data values.
        Returns:
            list: Cleaned user data list.
        """
        data_list = []
        for value in values:
            if value != "":
                if value.lower() in ["m", "f"]:
                    data_list.append(value)
                else:
                    data_list.append(float(value))
        return data_list

    @staticmethod
    def validate_data(values):
        """
        Validates the user data and ensures all fields are filled.
        Args:
            values (list): User data values.
        Returns:
            list: Validated user data list.
        """
        while True:
            try:
                data_list = App.list_user_data(values)
                user_data = App.generate_dict(data_list)
            except IndexError:
                print()
                print('Please fill in all the data to proceed!'.upper())
                print()
                App.generate_header()
                values = App.collect_user_data()
            except ValueError:
                print()
                print('Invalid value!'.upper())
                print()
                App.generate_header()
                values = App.collect_user_data()
            else:
                data_list = App.list_user_data(values)
                break

        return data_list

    @staticmethod
    def generate_dict(data_list):
        """
        Generates a dictionary from user data.
        Args:
            data_list (list): User data list.

        Returns:
            dict: Generated user data dictionary.
        """
        user_states = ['height', 'weight', 'gender', 'activityLevel', 'age']
        return dict(zip(user_states, data_list))

    @staticmethod
    def print_result(data_list):
        """
        Prints the result data in a formatted table.
        Args:
            data_list (list): Result data list.
        """
        print()
        App.row()
        print('|{:^25s}||{:^25s}||{:^25s}|'.format(
            str(data_list[0][0]), str(data_list[0][1]), str(data_list[0][2])))
        App.row()

    @staticmethod
    def create_table_imc(imc, status):
        """
        Creates and prints the IMC (Body Mass Index) table.
        Args:
            imc (float): Calculated IMC.
            status (str): IMC status.
        """
        content = [
            ['IMC Table', 'Range', 'Status'],
            ['Less than:', '18.5', 'Underweight!'],
            ['Between:', '18.5 and 24.9', 'Normal Weight!'],
            ['Between:', '25.0 and 29.9', 'Overweight!'],
            ['Between:', '30.0 and 34.9', 'Obesity Grade 1!'],
            ['Between:', '35.0 and 39.9', 'Obesity Grade 2!'],
            ['Greater than:', '40.0', 'Obesity Grade 3!'],
        ]

        result = [['YOUR IMC:', str(imc), status]]
        print()
        for row in range(len(content)):
            App.row_table()
            print('|{:^25s}||{:^25s}||{:^25s}|'.format(
                content[row][0], content[row][1], content[row][2]))
            if row == 6:
                App.row_table()
                App.print_result(result)

    @staticmethod
    def create_table_qtd_cal(data_dict):
        """
        Creates and prints the calorie intake table.
        Args:
            data_dict (dict): User data dictionary.
        """
        content = [
            ["Carbohydrates:", data_dict["carbohydrates"], round(
                float(data_dict["carbohydrates"]) / 4.0, 2)],
            ["Proteins:", data_dict["proteins"], round(
                float(data_dict["proteins"]) / 4.0, 2)],
            ["Fats:", data_dict["fats"], round(
                float(data_dict["fats"]) / 9.0, 2)]
        ]

        for row in range(len(content)):
            App.row_table()
            print('|{:^25}||{:^25}||{:^25}|'.format(str(content[row][0]), str(content[row][1]) + " kcal",
                                                    str(content[row][2]) + " g"))
            App.row_table()

    @staticmethod
    def menu(response):
        """
        Displays the application menu and handles user input.
        Args:
            response (dict)
        """
        while True:
            App.padding()
            print("=> Select an option: ")
            print()
            print('{:^16s}{:^18s}{:^18s}{:^18s}{:2s}'.format("1 - IMC", "2 - BMR", "3 - Calorie Intake", "4 - EXIT", ""),
                  end="\t")
            opt = input()
            App.padding()

            if opt == "1":
                App.title("IMC")
                print()
                print("{:^81s}".format(
                    "The Body Mass Index (IMC) is a parameter"))
                print("{:^81s}".format(
                    "used to determine if the weight is appropriate for the individual's height,"))
                print("{:^81s}".format(
                    "which can directly impact their health and quality of life!"))
                App.create_table_imc(response["imc"], response["imcStatus"])

            elif opt == "2":
                App.title("Basal Metabolic Rate (BMR): ")
                print()
                print("{:^81s}".format(
                    "The Basal Metabolic Rate (BMR) is the minimum amount"))
                print("{:^81s}".format(
                    "of energy (calories) required to sustain vital functions"))
                print("{:^81s}".format(
                    "this rate can vary based on sex, weight, height, age, and activity level."))

                result = [['RESULT:', 'YOUR BMR:',
                           str(response['bmr']) + " kcal"]]
                App.print_result(result)

            elif opt == "3":
                nutrients = response["nutrients"]
                App.title("Calorie Intake: ")
                print()
                print("{:^81s}".format(
                    "Calories represent the amount of energy that a given"))
                print("{:^81s}".format(
                    "food provides after being consumed, contributing to essential"))
                print("{:^81s}".format(
                    "bodily functions such as respiration, hormone production, and brain function."))

                print()
                print("{:^81s}".format("You should consume approximately: "))
                print()
                App.create_table_qtd_cal(nutrients)

                result = [['RESULT:', 'YOUR CALORIE INTAKE:',
                           str(response['calorieIntake']) + " kcal"]]
                App.print_result(result)

            elif opt == "4":
                print('{:^79s}'.format("Thank you for using our App!"))
                App.padding()
                App.row()
                break

            else:
                print("Error: Invalid option!")


app = App()
app.__init__()

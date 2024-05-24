def print_menu():
    # write something here to welcome user
    print()


def create_droid(name, skill, battery_level):
    print(f"Congratulations! You have created the following droid:")
    print(f"Name: {name}")
    print(f"Skill: {skill}")
    print(f"Battery Level: {battery_level}")


def droid_info(name, battery_level):
    print(f"Name: {name}")
    print(f"Current battery level: {battery_level}")


# create quick_charge that charges battery 5%
# should print message saying
# your battery was x% and is now y%


def quick_charge(current_level):
    print(f"Your battery level was {current_level}")
    print(f"Your batter level is now {current_level+5}")
    return current_level + 5


def long_charge(num_hours, current_battery_level):
    """Charges the battery 5% for the number of hours specified by
    the user or until it is 100%

    Args:
        num_hours: integer number of hours to charge the battery
        current_battery_level: integer battery charge

    Returns:
        battery level after num_hours of charge. Cannot exceed 100%.

    """

    return None  # replace this line


def perform_task(task, duration, current_battery_level):
    """Performs the task at the cost of 2% battery life per minute.

    Begins by printing
    "{duration} of {task} is being performed. {current_battery_level}% battery remains"

    If the task is completed, print
    "{duration} of {task} is complete. {current_battery_level}% battery remains"

    If the task could not be completed, print
    "{duration} of {task}failed to be completed, battery was depleted"

    Args:
        task: a string that says what the task is
        duration: integer time in minutes that the droid is performing the task

    Returns:
        battery level after task is completed or failed
    """


def main():
    # test code goes here
    print()  # remove this line, just to stop linting errors


if __name__ == "__main__":
    main()

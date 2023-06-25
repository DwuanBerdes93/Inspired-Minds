import random 
import string
import datetime

# Define class
class InnovationCoach():
    def __init__(self):
        self.active_goal = None
        self.goals = []
        self.coaching_session_list = []
  
# Define methods
    def set_active_goal(self, goal):
        self.active_goal = goal

    def add_goal(self, goal):
        self.goals.append(goal)

    def list_goals(self):
        for goal in self.goals:
            print("Goal: " + goal[0])
            print("Description: " + goal[1])
            print("Deadline: ", goal[2])
            print("")

    def clear_goals(self):
        print("Clearing all goals...")
        self.goals.clear()
        print("Goals cleared!")

    def create_coaching_session(self, date, duration):
        # Generate unique ID for every session
        session_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Create a dictionary for the session 
        session = {
            "id": session_id,
            "date": date,
            "duration": duration
        }

        # Append the dictionary to the coaching_session_list
        self.coaching_session_list.append(session)

        print("Coaching session {} successfully created!".format(session_id))

    def list_coaching_sessions(self):
        print("Current coaching sessions:")
        for session in self.coaching_session_list:
            print("ID: " + session['id'])
            print("Date: {}".format(session['date']))
            print("Duration: {}".format(session['duration']))
            print("")

    def clear_coaching_sessions(self):
        print("Clearing all coaching sessions...")
        self.coaching_session_list.clear()
        print("Coaching sessions cleared!")

# Create instance of class
coach = InnovationCoach()

# Set a goal
coach.set_active_goal(("Design a self driving motorcycle",
                        "Design a two wheeled self driving motorcycle with futuristic features",
                        datetime.date(2025, 1, 1)))

# Add more goals
coach.add_goal(("Develop a driverless car",
                "Develop a driverless car to help reduce traffic congestion and increase safety",
                datetime.date(2020, 7, 15)))

coach.add_goal(("Create a drone delivery system",
                "Create a drone delivery system to expedite the delivery of goods",
                datetime.date(2019, 12, 5)))

# List goals
coach.list_goals()

# Clear goals
coach.clear_goals()

# Create a coaching session
coach.create_coaching_session(datetime.date(2019, 5, 17), 2)

# Create another coaching session
coach.create_coaching_session(datetime.date(2019, 6, 7), 1.5)

# List coaching sessions
coach.list_coaching_sessions()

# Clear coaching sessions
coach.clear_coaching_sessions()
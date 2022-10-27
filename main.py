import random


# Create an Environment Class
class myEnvironment:

    def __init__(self):
        self.remaining_steps = 20

    # Function to observe agents current state
    def get_observation(self):
        return [1.0, 2.0, 1.0]

    # Function to observe agents points
    def get_actions(self):
        return [-1, 1]

    # Function to observe agents state and punishments
    def check_is_done(self):
        return self.remaining_steps == 0

    # Track how many steps before a Game Over
    def action(self, int):
        if self.check_is_done():
            raise Exception("Game Over!")
        self.remaining_steps -= 1
        return random.random()


# Create an Agent Class
class myAgent:
    def __init__(self): # Initialise points at 0.0
        self.total_rewards = 0.0

    # Track the Agents current position to check rewards and next move
    def step(self, ob: myEnvironment):
        curr_obs = ob.get_observation()
        print(curr_obs)

        curr_action = ob.get_actions()
        print(curr_action)

        curr_rewards = ob.action(random.choice(curr_action))
        self.total_rewards += curr_rewards

        print("Total Rewards so far = %.3f " % self.total_rewards)


# Main class to run
if __name__ == '__main__':
    # Create instances of myEnvironment and myAgent
    obj = myEnvironment()
    agent = myAgent()
    # Initialise steps to 0
    step_num = 0

    # Run environment with agent within it and track steps
    while not obj.check_is_done():
        step_num += 1
        print("Step - ", step_num)
        agent.step(obj)

    print("Total Reward is %.3f " % agent.total_rewards)

import numpy as np

# Regular 10-arm bandit test bed
#Initialization
UNIT_VARIANCE = 1
#create an array of 10 values sampled from Gaussian(0,1)
actual_rewards = np.random.normal(0,1,10)
steps = 1000

# algorithm
epsilons = [0, 0.1, 0.01]

def initialize_algorithm():
  global sampled_rewards
  global sample_sizes
  global average_reward
  sampled_rewards = np.zeros(10)
  sample_sizes = np.zeros(10)
  average_reward = 0

def get_random_index_of_max_element(np_array):
  indices = np.argwhere(np_array == np.max(np_array)).flatten().tolist()
  random_max = indices[np.random.randint(0,len(indices))]
  return random_max

def update_moving_average(current_average, sample, step_size):
  return current_average + step_size * (sample - current_average)

def get_sample(index):
  return np.random.normal(actual_rewards[index], UNIT_VARIANCE)

def update_sample_rewards(index, reward, step_size):
  sampled_rewards[index] = update_moving_average(sampled_rewards[index], reward, step_size)

def update_sample_sizes(index):
  sample_sizes[index] += 1

for epsilon in epsilons:
  initialize_algorithm()
  for step in range(1, steps+1):
    step_size = 1./float(step)
    i = -1
    if np.random.rand() < 1 - epsilon:
      i = get_random_index_of_max_element(sampled_rewards)
    else:
      i = np.random.randint(0,10)
    reward = get_sample(i)
    update_sample_sizes(i)
    sample_step_size = 1./float(sample_sizes[i])
    update_sample_rewards(i, reward, sample_step_size)
    average_reward = update_moving_average(average_reward, reward, step_size)
  print
  print "With epsilon value: " + str(epsilon)
  print "Sampled reward values: "
  print sampled_rewards
  print "Actual reward values: "
  print actual_rewards
  print "Average Reward: " + str(average_reward)

print
print "###########################################################################"
print
# Exercise 2.5 from Reinforcement Learning book

print "Exercise 2.5"

actual_rewards = [0] * 10
epsilon = 0.1
steps = 10000
sample_step_size = 0.1

def nonstationary_bandit_random_walk():
  return np.random.normal(0, 0.01, 10)

for epsilon in epsilons:
  initialize_algorithm()
  for step in range(1,steps+1):
    step_size = 1./float(step)
    i = -1
    if np.random.rand() < 1 - epsilon:
      i = get_random_index_of_max_element(sampled_rewards)
    else:
      i = np.random.randint(0,10)
    reward = get_sample(i)
    update_sample_sizes(i)
    update_sample_rewards(i, reward, sample_step_size)
    average_reward = update_moving_average(average_reward, reward, step_size)
    actual_rewards += nonstationary_bandit_random_walk()
  print
  print "With epsilon value: " + str(epsilon)
  print "Sampled reward values: "
  print sampled_rewards
  print "Actual reward values: "
  print actual_rewards
  print "Average Reward: " + str(average_reward)
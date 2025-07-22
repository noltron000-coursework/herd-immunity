################
# Logger Class #
################

class Logger(object):
	'''
	Utility class responsible for logging simulation interactions to a file.
	'''

	# TODO:
	# Write a test suite for this class to make sure each method is working as expected.

	# TIP:
	# Write your tests before you solve each function,
	# that way you can test them one by one as you write your class.

	def __init__(self, file_name):
		# TODO:
		# Finish this initialization method.
		# The `file_name` passed should be the full file name of the file
		# that the logs will be written to.
		self.file_name = None

	def log_metadata(
			self,
			virus,
			population_size,
			vaccination_rate,
		):
		'''
		The simulation class should use this method immediately to log
		the specific parameters of the simulation as the first line of the file.
		'''

		# TODO:
		# Finish this method.
		# This line of metadata should be tab-delimited.
		# It should create the text file that we will store all logs in.

		# TIP:
		# Use 'w' mode when you open the file to overwrite the old data with the new.
		# For all other methods, use the 'a' mode to append a new log to the end.

		results_file = open(self.file_name, "w")

		results_file.write("Simulation for virus: {}".format(virus.name))
		results_file.write("More content...!")
		results_file.write("More content...!")
		results_file.write("More content...!")

		results_file.close()

		# NOTE:
		# Make sure to end every line with a '/n' character
		# to ensure that each event logged ends up on a separate line!
		pass

	def log_results(self):
		'''
		Logs the results of the simulation to the file.
		Should include at least three strings:
		- "Simulation ended after {num_turns} turns."
		- "Total Dead: {num_deaths}."
		- "Total Vaccinated: {num_vaccinated}."
		'''

		# TODO:
		# Complete this method.

		# TIP:
		# You will have to add or change parameters for some functions in this project!
		pass

	def log_interaction(
			self,

			# HINT:
			# The `person` parameter should always be sick.
			# Think about whether these `random_person` was sick or healthy,
			# and whether or not they were vaccinated.
			person,
			random_person,

			# HINT:
			# This is just a logger function,
			# we don't have logic to decide whether or not infections happen here.
			did_infect=None,
		):
		'''
		The Simulation object should use this method to log
		every interaction a sick person has during each time step.

		The format of the log should be:
			`"{person.ID} infects {random_person.ID}.\\n"`

		...or the other edge cases:
			`"{person.ID} didn't infect {random_person.ID}
			because {ex. 'vaccinated' or 'already sick'}.\\n"`
		'''

		# TODO:
		# Finish this method.
		# Think about how the booleans that passed (or did not pass) represent all
		# the possible edge cases.
		# Use the values passed along with each person, along with whether they are sick
		# or vaccinated when they interact, to determine exactly what happened
		# during the interaction.
		# Then, create a String, and write to your logfile.
		pass

	def log_infection_survival(self, person, did_die_from_infection):
		'''
		The Simulation object uses this method to log the results of every call of
		a Person object's `.resolve_infection()` method.

		The format of the log should be:
			`"{person.ID} died from infection.\\n"
			or "{person.ID} survived infection.\\n"`
		'''

		# TODO:
		# Finish this method.
		# If the person survives, then `did_die_from_infection` should be `False`.
		# Otherwise, `did_die_from_infection` should be `True`.
		# Append the results of the infection to the logfile.
		pass

	def log_time_step(self, time_step_number):
		'''
		STRETCH CHALLENGE DETAILS:

		If you choose to extend this method,
		the format of the summary statistics logged are up to you.

		At minimum, it should contain:
		- The number of people that were infected during this specific time step.
		- The number of people that died on this specific time step.
		- The total number of people infected in the population
			(including the newly infected).
		- The total number of dead, including those that died during this time step.

		The format of this log should be:
		- `"Time step {time_step_number} ended, beginning {time_step_number + 1}\\n"`
		'''

		# TODO:
		# Finish this method.
		# This method should log when a time step ends, and a new one begins.

		# NOTE:
		# Here is an opportunity for a stretch challenge!
		pass

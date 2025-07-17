import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation:
	'''
	Main class that will run the herd immunity simulation program.
	Expects initialization parameters passed as command line arguments when file is run.

	Simulates the spread of a virus through a given population.
	The percentage of the population that are vaccinated, the size of the population,
	and the amount of initially infected people in a population are all variables
	that can be set when the program is run.
	'''

	def __init__(self, population_size, vaccination_rate, initial_infected, virus):
		'''
		Logger object logger records all events during the simulation.
		Population represents all `Person` objects in the population.
		The `next_person_id` is the next available id for all created `Person` objects,
		and should have a unique `_id` value.
		The vaccination percentage represents the total percentage
		of population vaccinated at the start of the simulation.
		You will need to keep track of the number
		of people currently infected with the disease.
		The total infected people is the running total that have been infected since
		the simulation began, including the currently infected people who died.
		You will also need to keep track of the number of people that have die
		as a result of the infection.

		All arguments will be passed as command-line arguments when the file is run.

		HINT:
		Look in the if `__name__ == "__main__"` function at the bottom.
		'''

		# HINT:
		# This virus property contains a lot of relevant data for later...
		self.virus = virus # `Virus` object

		# TODO:
		# Can you refactor this next line by using Python3's "f-string" format?
		self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, population_size, vaccination_rate, initial_infected)

		# TODO:
		# Create a Logger object and bind it to `self.logger`.
		# Remember to call the appropriate logger method
		# in the corresponding parts of the simulation.
		self.logger = None # Replace with `Logger` object

		# TODO:
		# Call `self._create_population()` and pass in the correct parameters.
		# Store the array that this method will return in the `self.population` attribute.
		self.population = [] # List of `Person` objects

		# TODO:
		# Store each newly infected person's ID in newly_infected attribute.
		# At the end of each time step, call `self._infect_newly_infected()`
		# and then reset `.newly_infected` back to an empty list.
		self.newly_infected = [] # List of `Person` objects

		self.population_size = population_size #  integer number
		self.initial_infected = initial_infected #  integer number
		self.vaccination_rate = vaccination_rate # float number between 0 and 1

		# TODO:
		# Some of these properties might not be needed.
		# These are just some suggestions for you!
		# You can add more or remove all of these, just do
		# what you think is right to organize your solution.
		self.next_person_id = 0 # integer number
		self.current_infected = 0 #  integer number
		self.total_infected = 0 #  integer number
		self.total_dead = 0 #  integer number


	def _create_population(self, initial_infected):
		'''
		This method will create the initial population (a list of `Person` objects)
		consisting of initial infected people,initial healthy non-vaccinated people,
		and initial healthy vaccinated people.
		Be sure to add them all to the population list!

		Args:
			initial_infected (int):
				The number of infected people that the simulation will begin with.
		Returns:
			list:
				A list of `Person` objects.
		'''
		# TODO:
		# Finish this method!
		# This method should be called when the simulation begins,
		# to create the population that will be used.
		# This method should return an array filled with `Person` objects
		# that matches the specifications of the simulation:
		# - The correct number of people in the population.
		# - The correct percentage of people vaccinated.
		# - The correct number of initially infected people.

		# Use the attributes created in the init method to create a population
		# that has the correct intial vaccination percentage and initial infected.
		pass

	def _simulation_should_continue(self):
		'''
		The simulation should only end if the entire population is dead,
		or if the virus has been eradicated (through death and vaccination).

		Returns:
			bool:
				`True` for simulation should continue, `False` if it should end.
		'''
		# TODO:
		# Complete this helper method.
		# Returns a Boolean.
		pass

	def _infect_newly_infected(self):
		'''
		This method should iterate through the list of `._id` stored
		in `self.newly_infected`, and update each `Person` object with the disease.
		'''
		# TODO:
		# Call this method at the end of every time step and infect each `Person`.

		# TODO:
		# Once you have iterated through the entire list of `self.newly_infected`,
		# remember to reset `self.newly_infected` back to an empty list.
		pass

	def run(self):
		'''
		This method should run the simulation until
		all requirements for ending the simulation are met.
		'''
		# TODO:
		# Finish this method.
		# To simplify the logic here, use the helper method
		# `_simulation_should_continue()` to tell us whether or not we should continue
		# the simulation and run at least 1 more `time_step`.

		# TODO:
		# Keep track of the number of time steps that have passed.
		# HINT:
		# You may want to call the logger's `log_time_step()` method
		# at the end of each time step.

		# TODO:
		# Set this variable using a helper...
		time_step_counter = 0

		while self._simulation_should_continue():
			# TODO:
			# for every iteration of this loop, call `self.time_step()`
			# to compute another round of this simulation.
			pass

		# TODO:
		# Can you refactor this next line by using Python3's "f-string" format?
		print('The simulation has ended after {} turns.'.format(time_step_counter))

	def time_step(self):
		'''
		This method should contain all the logic
		for computing one time step-in the simulation.

		This includes:
		1. 100 total interactions with a random person
			for each infected person in the population.
		2. If the person is dead, grab another random person from the population.
			(Since we don't interact with dead people,
			this does not count as an interaction.)
		3. Otherwise call `simulation.interaction(person, random_person)`
			and increment interaction counter by +1.
		4. You can also determine how many die from their infections
			at the end of each call of `self.time_step()`.
		'''

		# TODO:
		# Finish this method.
		# HINT:
		# Newly infected people cannot die in the same step that they were infected in!
		pass

	def interaction(self, person, random_person):
		'''
		This method should be called any time two living people
		are selected for an interaction.
		It assumes that only living people are passed in as parameters.

		Args:
			person1 (person): The initial infected person
			random_person (person): The person that person1 interacts with.
		'''

		# Assert statements are included to make sure
		# that only living people are passed in as params.
		assert person.is_alive == True
		assert random_person.is_alive == True

		# TODO:
		# Finish this method.

		# The possible cases you'll need to cover are listed in the docstring below:
		'''
		`random_person` is vaccinated:
			Nothing happens to random person.

		`random_person` is already infected:
			Nothing happens to random person.

		`random_person` is healthy, but unvaccinated:
			Generate a random number between 0 and 1.

			If that number is smaller than `repro_rate`, `random_person`'s ID should be
			appended to `Simulation` object's `newly_infected` array, so that their
			`.infected` attribute can be changed to True at the end of the time step.
		'''

		# TODO:
		# Call slogger method during this method.
		pass

	# HINT:
	# You may wish to implement new helper methods that you make up yourself,
	# to help organize your thoughts and to help simplify your code elsewhere.

	def print_population(self):
		'''Prints out every person in the population and their current attributes.'''
		# NOTE:
		# This is an example of a method that you could implement, if you find it useful!
		pass

	def get_infected(self):
		'''Gets all the infected people from the population and returns them as a list.'''
		# NOTE:
		# This is an example of a method that you could implement, if you find it useful!
		pass


if __name__ == "__main__":
	params = sys.argv[1:]

	# Virus properties
	virus_name = str(params[0])
	reproduction_rate = float(params[1])
	mortality_rate = float(params[2])

	# Population properties
	population_size = int(params[3])
	vaccination_rate = float(params[4])

	if len(params) == 6:
		initial_infections = int(params[5])
	else:
		initial_infections = 1

	# Create Virus class instance...
	virus = Virus(virus_name, reproduction_rate, mortality_rate)
	# Create Simulation class instance using new virus.
	simulation = Simulation(population_size, vaccination_rate, initial_infections, virus)
	simulation.run()

import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

####################
# Simulation Class #
####################

class Simulation:
	'''
	Main class that will run the herd immunity simulation program.
	Expects initialization parameters passed as command line arguments when file is run.

	Simulates the spread of a virus through a given population.
	The percentage of the population that are vaccinated, the size of the population,
	and the amount of initially infected people in a population are all variables
	that can be set when the program is run.
	'''

	def __init__(
			self,
			population_size: int,
			vaccination_rate: float,
			initial_infected: int,
			virus: Virus,
		):
		'''
		- Logger object logger records all events during the simulation.
		- Population array represents all `Person` objects in the population.
		- The vaccination percentage represents the total percentage of
			the population vaccinated at the start of the simulation.

		-
		The total infected people is the running total that have been infected since
		the simulation began, including the currently infected people who died.
		You will also need to keep track of the number of people that have die
		as a result of the infection.

		All arguments will be passed as command-line arguments when the file is run.

		XXX HINT XXX
		Look in the if `__name__ == "__main__"` function at the bottom.
		'''

		self.population_size = population_size # type: int
		self.vaccination_rate = vaccination_rate # type: float
		self.initial_infected = initial_infected # type: int

		# XXX HINT XXX
		# This virus property contains a lot of relevant data for later...
		self.virus = virus # type: Virus

		# XXX HINT XXX
		# Remember to call the appropriate logger methods
		# in the corresponding parts of the simulation.
		file_name = Logger.generate_file_name(
			virus_name,
			population_size,
			vaccination_rate,
			initial_infected,
		)
		self.logger = Logger(file_name)

		# XXX TODO XXX
		# Call `self.create_population()` and pass in the correct parameters.
		# Store the array that this method will return in the `self.population` attribute.
		self.population = [] # type: list[Person] # FIXME

		# XXX TODO XXX
		# Store each newly infected person in the `newly_infected` attribute.
		# At the end of each time step, call `self.infect_newly_infected()`,
		# and then reset `.newly_infected` back to an empty list.
		self.newly_infected = [] # type: list[Person] # FIXME

		# XXX HINT XXX
		# Some of these properties might not be needed.
		# These are just some suggestions for you!
		# You can add more or remove all of these, just do
		# what you think is right to organize your solution.

		# The `next_person_id` can be the next available id for all
		# created `Person` objects, to help generate unique `_id` values.
		self.next_person_id = 0 # type: int

		# The `current_infected` variable could help you keep track
		# of the number of people currently infected with the disease.
		self.current_infected = 0 # type: int

		# These values could also be helpful.
		self.total_infected = 0 # type: int
		self.total_dead = 0 # type: int

	def create_population(self, initial_infected):
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
		# XXX TODO XXX
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

	def simulation_should_continue(self):
		'''
		The simulation should only end if the entire population is dead,
		or if the virus has been eradicated (through death and vaccination).

		Returns:
			bool:
				`True` for simulation should continue, `False` if it should end.
		'''
		# XXX TODO XXX
		# Complete this helper method.
		# Returns a Boolean.
		pass

	def infect_newly_infected(self):
		'''
		This method should iterate through the list of `._id` stored
		in `self.newly_infected`, and update each `Person` object with the disease.
		'''
		# XXX TODO XXX
		# Call this method at the end of every time step and infect each `Person`.

		# XXX TODO XXX
		# Once you have iterated through the entire list of `self.newly_infected`,
		# remember to reset `self.newly_infected` back to an empty list.
		pass

	def run(self):
		'''
		This method should run the simulation until
		all requirements for ending the simulation are met.
		'''
		# XXX TODO XXX
		# Finish this method.
		# To simplify the logic here, use the helper method
		# `simulation_should_continue()` to tell us whether or not we should continue
		# the simulation and run at least 1 more `time_step`.

		# XXX TODO XXX
		# Keep track of the number of time steps that have passed.
		# XXX HINT XXX
		# You may want to call the logger's `log_time_step()` method
		# at the end of each time step.

		# XXX TODO XXX
		# Set this variable using a helper...
		time_step_counter = 0

		while self.simulation_should_continue():
			# XXX TODO XXX
			# for every iteration of this loop, call `self.time_step()`
			# to compute another round of this simulation.
			pass

		# XXX TODO XXX
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

		# XXX TODO XXX
		# Finish this method.
		# XXX HINT XXX
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

		# XXX TODO XXX
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

		# XXX TODO XXX
		# Call slogger method during this method.
		pass

	# XXX HINT XXX
	# You may wish to implement new helper methods that you make up yourself,
	# to help organize your thoughts and to help simplify your code elsewhere.

	def print_population(self):
		'''Prints out every person in the population and their current attributes.'''
		# XXX NOTE XXX
		# This is an example of a method that you could implement, if you find it useful!
		pass

	def get_infected(self):
		'''Gets all the infected people from the population and returns them as a list.'''
		# XXX NOTE XXX
		# This is an example of a method that you could implement, if you find it useful!
		pass

##################
# CLI Entrypoint #
##################

if __name__ == "__main__":
	params = sys.argv[1:]

	if len(params) < 5:
		# This section should use "Ebola" virus data as a fallback,
		# in case no command-line arguments were provided.

		# XXX TODO XXX
		# Fill in the these None-type variables with the relevant
		# "Ebola" data, which can be found within the `README` file.

		# Ebola Virus properties
		virus_name = "Ebola"
		reproduction_rate = None
		mortality_rate = None

		# Population properties
		population_size = None
		vaccination_rate = None
		initial_infections = None

		# XXX TODO XXX
		# Delete this exception once the above is implemented...
		raise Exception("Bad command line arguments.")

	else:
		# Virus properties
		virus_name = str(params[0])
		reproduction_rate = float(params[1])
		mortality_rate = float(params[2])

		# Population properties
		population_size = int(params[3])
		vaccination_rate = float(params[4])
		initial_infections = 1

		if len(params) > 5:
			initial_infections = int(params[5])

	# Create a new Virus class instance...
	virus = Virus(virus_name, reproduction_rate, mortality_rate)

	# Create a new Simulation class instance, using the new virus.
	simulation = Simulation(population_size, vaccination_rate, initial_infections, virus)

	# Run the simulation!!! This should generate a new log file.
	simulation.run()

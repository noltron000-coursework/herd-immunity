import math, random, sys
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
		Initializes the simulation server.

		- The logger object records all events during the simulation.
		- The population array represents all `Person` objects in the population.
		- The vaccination percentage represents the total percentage of\
			the population vaccinated at the start of the simulation.
		- The total infected people is the running total that have been infected since\
			the simulation began, including the currently infected people who died.
		- You will also need to keep track of the number of people that have die\
			as a result of the infection.

		All arguments will be passed as command-line arguments when the file is run.
		'''

		self.population_size = population_size # type: int
		self.vaccination_rate = vaccination_rate # type: float
		self.initial_infected = initial_infected # type: int
		self.virus = virus # type: Virus

		# Create a logger class to track important events.
		file_name = Logger.generate_file_name(
			virus_name,
			population_size,
			vaccination_rate,
			initial_infected,
		)
		self.logger = Logger(file_name)

		# Generate a population with the correct number of vaccinations and infections.
		self.population = self.create_population() # type: list[Person]

	def create_population(self):
		'''
		1. This method will create the initial population (a list of `Person` objects)\
			based on the given population size.
		2. Then, the method will vaccinate a percentage of them from a virus.
		3. Finally, it will infect a given number of people in the population.\
			If too many people are vaccinated to reach the set number,\
			then as many unvaccinated people as possible are infected.
		4. The method returns the generated list.

		Returns:
			list:
				A list of `Person` objects.
		'''

		# Initialize a list of person objects.
		population: list[Person] = []
		for _id in range(self.population_size):
			person = Person(_id)
			population.append(person)

		# Determine how many people to vaccinate.
		num_vaccinated = self.population_size * self.vaccination_rate
		num_vaccinated = math.floor(num_vaccinated)

		# Vaccinate a random set of the population.
		people_to_vaccinate = random.sample(population, num_vaccinated)
		for person in people_to_vaccinate:
			person.is_vaccinated = True

		# Determine the remaining unvaccinated population.
		unvaccinated_population = [
			person for person in population
			if not person.is_vaccinated
		]

		# Next, determine if we can infect the correct number of people.
		if self.initial_infected > len(unvaccinated_population):
			# We cannot - too many people are vaccinated!
			# The server must adjust the number of initially infected people.
			self.initial_infected = len(unvaccinated_population)

			# XXX TODO XXX
			# Add a log event of this situation.
			# The number of initial infected cannot be reached;
			# there are too many vaccinated people in the population.

		# Infect a random set of the population (that is not vaccinated).
		people_to_infect = random.sample(unvaccinated_population, self.initial_infected)
		for person in people_to_infect:
			person.infection = self.virus

		return population

	def should_continue(self):
		'''
		The simulation should only end if the entire population is dead,
		or if the virus has been eradicated (through death and vaccination).

		Returns:
			bool:
				`True` for simulation should continue, `False` if it should end.
		'''
		# Everyone is dead!
		if len(self.get_alive()) == 0:
			return False

		# No one is infected!
		elif len(self.get_infected()) == 0:
			return False

		# Simulation needs to continue.
		else: return True


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

		# Keeps track of the number of time steps that have passed.
		num_cycles = 0

		# Runs until the simulation completes.
		while self.should_continue():
			num_cycles += 1
			self.time_step()
			self.logger.log_time_step(num_cycles)

		# Call final logger method...
		self.logger.log_results(num_cycles)

	def time_step(self):
		'''
		This method should contain all the logic
		for computing one time step-in the simulation.

		This includes:
		1. Calculate 100 unique random interactions between two people.
		2. Calling `simulation.interaction(person, random_person)` for each interaction.
		3. Resolving who dies, who lives, and who gets sick.
		'''

		MAX_NUM_INTERACTIONS = 100

		sick_population = [
			p for p in self.population
			if p.is_alive and p.infection is not None
		]

		for sick_person in sick_population:
			# Get a list of the people we can have interactions with.
			possible_others = [
				p for p in self.population
				if p._id != sick_person._id and p.is_alive
			]

			# Limit the number of interactions.
			num_interactions = min(
				MAX_NUM_INTERACTIONS,
				len(possible_others),
			)

			# Select random living people from the population.
			random_people = random.sample(possible_others, num_interactions)

			# Make each pair interact.
			for other_person in random_people:
				self.interaction(sick_person, other_person)

		# Resolve who lives, who dies, and resolve dormant infections.
		self.resolve_infections()

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

	def resolve_infections(self):
		deaths = []

		for infected in self.get_infected():
			died = infected.resolve_infection()
			if died: deaths.append(infected)

		# XXX TODO XXX
		# Have to apply infected status to newly infected people.

	def get_alive(self):
		'''Gets everyone in the population that is still alive, and returns them.'''
		return [p for p in self.population if p.is_alive]

	def get_infected(self):
		'''Gets all the infected people from the population and returns them as a list.'''
		return [p for p in self.population if p.is_infected]

##################
# CLI Entrypoint #
##################

if __name__ == "__main__":
	params = sys.argv[1:]

	if len(params) < 5:
		# This section should use "Ebola" virus data as a fallback,
		# in case no command-line arguments were provided.

		# Ebola Virus properties
		virus_name = "Ebola"
		reproduction_rate = 0.25
		mortality_rate = 0.70

		# Default population properties
		population_size = 100000
		vaccination_rate = 0.90
		initial_infections = 10

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

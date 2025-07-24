import math, random, sys
random.seed(42)
from logger import Logger
from person import Person
from population import Population
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
			population: Population,
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

		self.population = population # type: Population
		self.virus = virus # type: Virus

		# Create a logger class to track important events.
		file_name = Logger.generate_file_name(population, virus)
		self.logger = Logger(file_name)

	def should_continue(self):
		'''
		The simulation should only end if the entire population is dead,
		or if the virus has been eradicated (through death and vaccination).

		Returns:
			bool:
				`True` for simulation should continue, `False` if it should end.
		'''
		# Everyone is dead!
		if len(self.population.filter(is_alive=True)) == 0:
			return False

		# No one is infected!
		elif len(self.population.filter(is_infected=True)) == 0:
			return False

		# Simulation needs to continue.
		else: return True


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
			print(f"=== TURN {num_cycles} ===")
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
			p for p in self.population.list
			if p.is_alive and p.infection is not None
		]

		for sick_person in sick_population:
			# Get a list of the people we can have interactions with.
			possible_others = [
				p for p in self.population.list
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

	def interaction(self, person1: Person, person2: Person):
		'''
		This method should be called any time two people are selected for an interaction.

		Args:
			person1 (Person): One of the two people interacting.
			person2 (Person): One of the two people interacting.
		'''

		# Assert statements are included to make sure
		# that only living people are passed in as params.
		assert person1.is_alive == True
		assert person2.is_alive == True

		# Determine if someone getting sick is even possible.
		if person1.infection == person2.infection:
			# Both people are sick (or neither are sick)!
			# Nothing happens in either scenario.
			pass

		# One person must be sick, and the other is not.
		# This may cause an infection...
		else:
			# Determine who is sick, and who is not.
			sick_person: Person
			healthy_person: Person
			if person1.infection != None:
				sick_person = person1
				healthy_person = person2
			else:
				sick_person = person2
				healthy_person = person1

			# Resolve the exposure...
			healthy_person.resolve_exposure(sick_person.infection)

	def resolve_infections(self):
		'''
		This method takes sick people and kills a portion of them.
		Then, it takes newly infected people and makes them sick.
		'''
		new_deaths = []
		new_infections = []

		for infected in self.population.filter(is_dormant=False):
			survives = infected.resolve_infection()
			if not survives: new_deaths.append(infected)

		for infected in self.population.filter(is_dormant=True):
			infected.is_dormant = False
			new_infections.append(infected)

		print(f"   new cases: {len(new_infections)}")
		print(f"  new deaths: {len(new_deaths)}")
		print(f" total alive: {len(self.population.filter(is_alive=True))}")
		print(f"total deaths: {len(self.population.filter(is_alive=False))}")
		print(f"total immune: {len(self.population.filter(is_vaccinated=True))}")
		print()

		# XXX TODO XXX
		# Log the number of deaths and infections somewhere.


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

	# Create new instances, including the root simulation instance.
	virus = Virus(virus_name, reproduction_rate, mortality_rate)
	population = Population(population_size, vaccination_rate, initial_infections, virus)
	simulation = Simulation(population, virus)

	# Run the simulation!!! This should generate a new log file.
	simulation.run()

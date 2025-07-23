import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):
	def __init__(self, population_size, vaccination_rate, virus_name, mortality_rate, infection_rate, initial_infected=1, num_interactions=100):
		# number of (living) people at the start of the simulation.
		self.population_size = population_size

		# a list of each newly infected person from this step (living and to be infected)
		self.newly_infected = []

		# an integer that counts the total number of infected persons (alive and unvaccinated).
		self.currently_infected = []

		# an integer that ensures every Person object has a unique identifier.
		self.next_person_id = 1

		# hard percentage of vaccinated persons in population.
		self.vaccination_rate = vaccination_rate

		# hard value of infected persons in population.
		self.initial_infected = initial_infected

		# hard value of interactions per person
		self.num_interactions = num_interactions

		# The Name of the Virus
		self.virus_name = virus_name

		# The Deadliness of the Virus
		self.mortality_rate = mortality_rate

		# The Contamination of the Virus
		self.infected_rate = infection_rate

		# a list of every person in the entire population (living or dead).
		self.population = self.create_population()

		# the FileName output file
		self.file_name = f"{virus_name}_simulation_pop_{population_size}_vp_{vaccination_rate}_infected_{initial_infected}.txt"

		# creates the log in the output file
		self.logger = Logger(self.file_name)

	def time_step(self):
		sick_population = [
			p for p in self.population
			if p.is_alive and p.is_infected
		]

		for sick_person in sick_population:
			# Get a list of the people we can have interactions with.
			possible_others = [
				p for p in self.population
				if p._id != sick_person._id and p.is_alive
			]

			# Limit the number of interactions.
			num_interactions = min(
				self.num_interactions,
				len(possible_others),
			)

			# Select random living people from the population.
			random_people = random.sample(possible_others, num_interactions)

			# Make each pair interact.
			for other_person in random_people:
				self.interaction(sick_person, other_person)

		# Resolve who lives, who dies, and resolve dormant infections.
		self.resolve_infections()

if __name__ == "__main__":
	params = sys.argv[1:]
	if len(params) == 0:
		print("No parameters input...")
		print("Please input parameters")
		print()
		print("   type: integer, INPUT ≥ 1")
		population_size = int(input("Enter population size: "))


		print()
		print("   type: string")
		virus_name = input("Enter virus name: ")

		print()
		print("   type: float, 0 ≤ INPUT ≤ 1")
		mortality_rate = float(input("Enter mortality rate: "))

		print()
		print("   type: float, 0 ≤ INPUT ≤ 1")
		infection_rate = float(input("Enter infection rate: "))

		print()
		print("   type: float, 0 ≤ INPUT ≤ 1")
		vaccination_rate = float(input("Enter vaccination rate: "))

		print()
		print("default: 1")
		print("   type: integer, INPUT ≥ 1")
		initial_infected = input("Enter initial infected: ")

		if initial_infected == "":
			initial_infected = 1
		else:
			initial_infected = int(initial_infected)

		print()
		print("default: 100")
		print("   type: integer, INPUT ≥ 1")
		num_interactions = input("Enter number of interactions: ")

		if num_interactions == "":
			num_interactions = 100
		else:
			num_interactions = int(num_interactions)

	else:
		population_size = int(params[0])
		vaccination_rate = float(params[1])
		virus_name = str(params[2])
		mortality_rate = float(params[3])
		infection_rate = float(params[4])

		if len(params) >= 6:
			initial_infected = int(params[5])
		else:
			initial_infected = 1

		if len(params) == 7:
			num_interactions = int(params[6])
		else:
			num_interactions = 100

	simulation = Simulation(population_size, vaccination_rate, virus_name, mortality_rate, infection_rate, initial_infected, num_interactions)
	simulation.run()

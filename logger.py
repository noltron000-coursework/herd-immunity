from population import Population
from virus import Virus
from typing import Literal
from person import Person

################
# Logger Class #
################

class Logger(object):
	'''Utility class responsible for logging simulation interactions to a file.'''

	# XXX TODO XXX
	# Write a test suite for this class to make sure each method is working as expected.

	# XXX HINT XXX
	# Try to write your tests before you solve each function,
	# that way you can test them one by one as you write your class.

	@staticmethod
	def generate_file_name(population: Population, virus: Virus):
		'''
		This static method generates a logfile name and returns it,
		based on a few parameters about the simulation (as listed).
		'''

		name = (
			f"sim_{virus.name}_"
			f"pop_{population.size}_"
			f"vac_{population.vaccination_rate}_"
			f"inf_{population.initial_infections}.txt"
		)

		return name.lower()

	def __init__(self, file_name):
		'''
		Initializes a new Logger class instance.
		The `file_name` property that's passed in should be the full name
		of the file that the logs will be written to.
		'''

		self.file_name = file_name # type: str

		print() # Add some space for legibility within the terminal.

		# XXX NOTE XXX
		# Use 'w' mode when you open the file to overwrite the old data with the new.
		# For all other methods, use the 'a' mode to append a new log to the end.
		logfile = open(self.file_name, "w")
		logfile.close()

	def write(self, content: str, verbose = True):
		'''Writes the given content to the logfile.'''
		# Print the given content to console if `verbose = true`.
		if verbose: print(content)

		# XXX NOTE XXX
		# Use 'a' mode to append content to the logfile.
		logfile = open(self.file_name, "a")

		# Write the given content...
		logfile.write(content)
		logfile.write('\n') # This newline helps emulate the behavior of print statements.

		# Close the file - leaving it open can cause problems elsewhere.
		logfile.close()

	def log_metadata(self, population: Population, virus: Virus):
		'''
		The simulation class should use this method immediately to log
		the specific parameters of the simulation as the first line of the file.
		'''

		# XXX TODO XXX
		# The basic header information is pretty bare-bones for now.
		# I can't really think of anything else that would need to go here.
		# Maybe an author field and a creation timestamp?
		content = (
			"====== HERD IMMUNITY SIMULATION ======\n"
			f"Virus Name: {virus.name}\n"
		)
		self.write(content)

		# XXX NOTE XXX
		# We will want to log "Cycle Zero" right away as part of initialization.
		# This shows a summary of some important data cleanly, before anyone dies.
		self.log_cycle(
			num_cycles = 0,
			num_new_infections = population.initial_infections,
			num_newly_immune = 0,
			num_new_deaths = 0,
			total_alive = population.size,
			total_deaths = 0,
			total_immune = population.initial_vaccinations,
		)

	def log_interaction(
			self,
			person1,
			person2,
			scenario: Literal[
				'all-remain-healthy',
				'all-remain-infected',
				'has-vaccination',
				'got-infection',
				'got-lucky',
			]
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

		# Collect the log results string in this variable...
		result: str

		# Determine which scenario applies for the logfile.
		if scenario == 'all-remain-healthy':
			result = (
				f"{person1} and {person2} interacted,"
				" but both are healthy.\n"
			)
		elif scenario == 'all-remain-infected':
			result = (
				f"{person1} and {person2} interacted,"
				" but both are sick already.\n"
			)
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

			# Continue with possible scenarios...
			if scenario == 'has-vaccination':
				result = (
					f"{sick_person} didn't infect {healthy_person}"
					" because they are vaccinated.\n"
				)
			elif scenario == 'got-lucky':
				result = (
					f"{sick_person} didn't infect {healthy_person}"
					" because they got lucky.\n"
				)
			elif scenario == 'got-infection':
				result = (
					f"{sick_person} infected {healthy_person}!"
					" The infection has spread.\n"
				)

		# Finally, write the interaction results to the logfile.
		logfile = open(self.file_name, "a")
		logfile.write(result)
		logfile.close()
		return result

	def log_infection_survival(self, person, did_die_from_infection):
		'''
		The Simulation object uses this method to log the results of every call of
		a Person object's `.resolve_infection()` method.

		The format of the log should be:
			`"{person.ID} died from infection.\\n"
			or "{person.ID} survived infection.\\n"`
		'''

		# XXX TODO XXX
		# Finish this method.
		# If the person survives, then `did_die_from_infection` should be `False`.
		# Otherwise, `did_die_from_infection` should be `True`.
		# Append the results of the infection to the logfile.
		pass

	def log_cycle(
			self,
			num_cycles,
			num_new_infections: int,
			num_newly_immune: int,
			num_new_deaths: int,
			total_alive: int,
			total_immune: int,
			total_deaths: int,
		):
		'''This writes summary statistics to the logfile.'''

		logs = (
			f"------ CYCLE {num_cycles} ------\n"
			f"   new cases: {num_new_infections}\n"
			f"newly immune: {num_newly_immune}\n"
			f"  new deaths: {num_new_deaths}\n"
			f" total alive: {total_alive}\n"
			f"total immune: {total_immune}\n"
			f"total deaths: {total_deaths}\n"
		)
		self.write(logs)

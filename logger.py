'''
	Utility class responsible for logging all interactions of note during the
	simulation.

		_____Attributes______

		file_name: the name of the file that the logger will be writing to.

		_____Methods_____

		__init__(self, file_name):

		write_metadata(self, pop_size, vaccination_rate, virus_name, mortality_rate, infection_rate):
			- Writes the first line of a logfile, which will contain metadata on the parameters for the simulation.

		log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
			- Expects person1 and person2 as person objects.
			- Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
			- Between the values passed with did_infect, person2_vacc, and person2_sick, this method should be able to determine exactly what happened in the interaction and create a String saying so.
			- The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
			- Appends the interaction to logfile.

		log_infection_survival(self, person, did_die_from_infection):
			- Expects person as Person object.
			- Expects bool for did_die_from_infection, with True denoting they died from their infection and False denoting they survived and became immune.
			- The format of the log should be "{person.ID} died from infection" or "{person.ID} survived infection."
			- Appends the results of the infection to the logfile.

		log_time_step(self, time_step_number):
			- Expects time_step_number as an Int.
			- This method should write a log telling us when one time step ends, and the next time step begins.  The format of this log should be:
				"Time step {time_step_number} ended, beginning {time_step_number + 1}..."
			- STRETCH CHALLENGE DETAILS:
				- If you choose to extend this method, the format of the summary statistics logged are up to you.  At minimum, it should contain:
						- The number of people that were infected during this specific time step.
						- The number of people that died on this specific time step.
						- The total number of people infected in the population, including the newly infected
						- The total number of dead, including those that died during this time step.
'''

class Logger(object):

	# TODO:  Finish this initialization method.  The file_name passed should be the full file name of the file that the logs will be written to.
	def __init__(self, file_name):
		self.file_name = file_name

	# TODO: Finish this method.  The simulation class should use this method immediately upon creation, to log the specific parameters of the simulation as the first line of the file. This line of metadata should be tab-delimited (each item separated by a '\t' character).
	# NOTE: Since this is the first method called, it will create the text file that we will store all logs in. Be sure to use 'w' mode when you open the file.
	# For all other methods, we'll want to use the 'a' mode to append our new log to the end, since 'w' overwrites the file.
	# NOTE: Make sure to end every line with a '\n' character to ensure that each event logged ends up on a separate line!
	def write_metadata(self, population_size, vaccination_rate, virus_name, mortality_rate, infection_rate, initial_infected, num_interactions):
		# Open file from the simulation
		with open(self.file_name, "w") as file:
			# Write parameters to first line of file
			file.write(f"{population_size}\t{vaccination_rate}\t{virus_name}\t{mortality_rate}\t{infection_rate}\n")
			file.write("\n=========================\n")
			file.write(f" population_size: {population_size}\n")
			file.write(f"vaccination_rate: {vaccination_rate}\n")
			file.write(f"      virus_name: {virus_name}\n")
			file.write(f"  mortality_rate: {mortality_rate}\n")
			file.write(f"  infection_rate: {infection_rate}\n")
			file.write(f"initial_infected: {initial_infected}\n")
			file.write(f"num_interactions: {num_interactions}\n\n")

		# Close file when done
		file.close()

	# TODO: Finish this method. The Simulation object should use this method to log every interaction a sick individual has during each time step. This method should accomplish this by using the information from person1 (the infected person), person2 (the person randomly chosen for the interaction), and the optional keyword arguments passed into the method. See documentation for more info on the format of the logs that this method should write.
	# NOTE:  You'll need to think about how the booleans passed (or not passed) represent all the possible edge cases!
	# NOTE: Make sure to end every line with a '/n' character to ensure that each event logged ends up on a separate line!
	def log_interaction(self, person1, person2, newly_infected, did_infect=None):
		# Open file from the simulation
		new_infection = False
		for person in newly_infected:
			if person2 == person:
				new_infection = True

		with open(self.file_name, "a") as file:
			if did_infect:
				# person 2 got infected!!!
				file.write("person # " + str(person1.identity) +" infected person # " + str(person2.identity) + "!\n")
			elif person2.vaccinated == True:
				# person 2 was vaccinated. Phew!
				file.write("vaccinated person # " + str(person2.identity) + " is protected\n")
			elif person2.infected != None or new_infection == True:
				# person 2 was already infected ;(
				file.write("person # " + str(person2.identity) + " is already diseased\n")
			else:
				# person 2 lucked out and didn't get infected O_O
				file.write("lucky person # " + str(person2.identity) + " didn't get sick\n")
		file.close()

	def log_person(self, person):
		with open(self.file_name, "a") as file:
			file.write(f"\n------ person # {str(person.identity)} ------\n")
		file.close()


	def log_infection_kickoff(self):
		with open(self.file_name, "a") as file:
			file.write("\n<><><> Computing Deaths <><><>\n\n")
		file.close()

	# TODO: Finish this method.  The Simulation object should use this method to log the results of every call of a Person object's .resolve_infection() method. ISSUE ON GITHUB
	# If the person survives, did_die_from_infection should be False. Otherwise, did_die_from_infection should be True.  See the documentation for more details on the format of the log.
	# NOTE: Make sure to end every line with a '/n' character to ensure that each event logged ends up on a separate line!
	def log_infection_survival(self, person, did_die_from_infection):
		# Open file from the simulation
		with open(self.file_name, "a") as file:
		# Mention whether or not each alive person dies at the end of an interaction cycle.
			if not did_die_from_infection:
				# Person dies
				file.write(f">>> person # {str(person.identity)} has died...rest in peace...\n")
			else:
				# Person lives
				file.write(f">>> person # {str(person.identity)} has survived the infection!\n")
		file.close()


	# TODO: Finish this method.  This method should log when a time step ends, and a new one begins.  See the documentation for more information on the format of the log.
	# NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time step, it also logs a summary of what happened in that time step, including the number of people infected, the number of people dead, etc.  You may want to create a helper class  to compute these statistics for you, as a Logger's job is just to write logs!
	# NOTE: Make sure to end every line with a '/n' character to ensure that each event logged ends up on a separate line!
	def log_time_step(self, time_step_number):
		# Open file from the simulation
		with open(self.file_name, "a") as file:
			# Write that the cycle is complete, and that its starting a new one.
			if time_step_number != 0:
				file.write("\n=========================\n")
				file.write("cycle # " + str(time_step_number) + " has ended...\n")
			file.write("cycle # " + str(time_step_number + 1) + " is starting!\n")
			file.write("=========================\n\n")
		file.close()

	def log_results(self, time_step_number, total_infected, total_deaths, population_size, population):
		with open(self.file_name, "a") as file:
			population_after = population_size - total_deaths
			file.write("\n=========================\n")
			file.write("cycle # " + str(time_step_number) + " has ended...\n")
			file.write("\n~~~~~~~~ RESULTS ~~~~~~~~\n")
			file.write(f" starting population: {population_size}\n")
			file.write(f"finishing population: {population_after}\n")
			file.write(f"  touched by disease: {total_infected}\n")
			file.write(f"    number of deaths: {total_deaths}\n")
			file.write("=========================")
		file.close()

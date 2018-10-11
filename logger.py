'''
	Utility class responsible for logging all interactions of note during the
	simulation.

		_____Attributes______

		file_name: the name of the file that the logger will be writing to.

		_____Methods_____

		__init__(self, file_name):

		write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
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
	def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
		# Open file from the simulation
		with open(self.file_name, "w") as file:
			# Write parameters to first line of file
			file.write("{}\t{}\t{}\t{}\t{}\n").format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)
		# Close file when done
		file.close()

	# TODO: Finish this method. The Simulation object should use this method to log every interaction a sick individual has during each time step. This method should accomplish this by using the information from person1 (the infected person), person2 (the person randomly chosen for the interaction), and the optional keyword arguments passed into the method. See documentation for more info on the format of the logs that this method should write.
	# NOTE:  You'll need to think about how the booleans passed (or not passed) represent all the possible edge cases!
	# NOTE: Make sure to end every line with a '/n' character to ensure that each event logged ends up on a separate line!
	def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
		# Open file from the simulation
		with open(self.file_name, "a") as file:
			if did_infect:
				# person 2 got infected!!!
				file.write(str(person1.identity) +" infected " + str(person2.identity))
			elif person2.vaccination:
				# person 2 was vaccinated. Phew!
				file.write("nothing happened to " + str(person2.identity))
			elif person2.infection:
				# person 2 was already infected ;(
				file.write("nothing happened to " + str(person2.identity))
			else:
				# person 2 lucked out and didn't get infected O_O
				file.write("nothing happened to " + str(person2.identity))
		file.close()

	# TODO: Finish this method.  The Simulation object should use this method to log the results of every call of a Person object's .resolve_infection() method. ISSUE ON GITHUB
	# If the person survives, did_die_from_infection should be False. Otherwise, did_die_from_infection should be True.  See the documentation for more details on the format of the log.
	# NOTE: Make sure to end every line with a '/n' character to ensure that each event logged ends up on a separate line!
	def log_infection_survival(self, person, did_die_from_infection):
		# Open file from the simulation
		with open(self.file_name, "a") as file:
		# Mention whether or not each alive person dies at the end of an interaction cycle.
			if did_die_from_infection:
				# Person dies
				file.write(str(person.identity) +" has died...\n")
			else:
				# Person lives
				file.write(str(person.identity) +" has survived!!!\n")
		file.close()


	# TODO: Finish this method.  This method should log when a time step ends, and a new one begins.  See the documentation for more information on the format of the log.
	# NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time step, it also logs a summary of what happened in that time step, including the number of people infected, the number of people dead, etc.  You may want to create a helper class  to compute these statistics for you, as a Logger's job is just to write logs!
	# NOTE: Make sure to end every line with a '/n' character to ensure that each event logged ends up on a separate line!
	def log_time_step(self, time_step_number):
		# Open file from the simulation
		with open(self.file_name, "a") as file:
			# Write that the cycle is complete, and that its starting a new one.
			file.write("cycle number " + str(time_step_number) + "has ended.\n")
			file.write("cycle number " + str(time_step_number + 1) + "is starting!\n")
		file.close()
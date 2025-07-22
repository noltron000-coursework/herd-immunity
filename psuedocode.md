# Steps

Run Simulation:
`python3 simulation.py`
	instantiate other objects
	create instance of Simulation Object
	create instance of Logger Object
		logger keeps track of newly infected people at the end of each time step, and writes to file.

	call `self.create_population`
		holds a list of person objects
		uses simulation class parameters to create person objects
		forces a certain percent of people to be vaccinated
		forces a certain number of people to be infected
		returns a population list

	call `self.run`
		decides if simulation should continue.
		eventually returns True or False based on helper function":
		call `self.simulation_should_continue`
			returns True if it should continue
			returns False if it should not
				only returns False if entire population is Dead or Uninfected

	call `self.contagiousify()`
		go through `self.newly_infected`, a list of person ID's
		for every person ID in `self.newly_infected`:
			find person object in `self.population`
			sets person's .infected attribute to True
			empty the `self.newly_infected` list when finished

## can a person be infected and vaccinated at the very beginning?

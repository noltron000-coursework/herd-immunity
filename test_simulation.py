import pytest
import simulation

def test_setup():
	sim = simulation.Simulation(population_size=1000, vaccination_rate=0.5, virus_name="Eeksies", mortality_rate=0.5, infection_rate=3/4)
	assert sim.population_size == 1000
	assert sim.vaccination_rate == 0.5
	assert sim.virus_name == "Eeksies"
	assert sim.mortality_rate == 0.5
	assert sim.infected_rate == 0.75
	assert sim.initial_infected == 1
	assert sim.num_interactions == 100
	assert sim.newly_infected == []

def test_population():
	sim = simulation.Simulation(population_size=1002, vaccination_rate=0.5, virus_name="Eeksies", mortality_rate=0.5, infection_rate=3/4, initial_infected=17, num_interactions=97)
	assert len(sim.currently_infected) == 17

	for person in sim.currently_infected:
		assert person.infected =="Eeksies"

	assert len(sim.population) == 1002
	sick_counter = 0

	for person in sim.population:
		assert person.alive == True
		if person.infected == "Eeksies":
			sick_counter += 1

	assert sick_counter == len(sim.currently_infected)

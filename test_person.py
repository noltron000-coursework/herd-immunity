import pytest
import person

def test_person():
	normal_person = person.Person(0,False)
	assert normal_person.alive == True
	assert normal_person.identity == 0
	assert normal_person.vaccinated == False
	assert normal_person.infected == None

	deadly_person = person.Person(1,False,"Deadly Virus")
	assert deadly_person.alive == True
	assert deadly_person.identity == 1
	assert deadly_person.vaccinated == False
	assert deadly_person.infected == "Deadly Virus"


def test_infection():
	normal_person_1 = person.Person(1,False)
	normal_person_2 = person.Person(2,False)
	deadly_person_3 = person.Person(3,False,"Deadly Virus")
	deadly_person_4 = person.Person(4,False,"Deadly Virus")

	assert normal_person_1.resolve_infection(0) == None
	assert normal_person_1.alive == True
	assert normal_person_1.infected == None
	assert normal_person_1.vaccinated == False

	assert normal_person_2.resolve_infection(1) == None
	assert normal_person_2.alive == True
	assert normal_person_2.infected == None
	assert normal_person_2.vaccinated == False

	assert deadly_person_3.resolve_infection(0) == True
	assert deadly_person_3.alive == True
	assert deadly_person_3.infected == "Deadly Virus"
	assert deadly_person_3.vaccinated == True

	assert deadly_person_4.resolve_infection(1) == False
	assert deadly_person_4.alive == False
	assert deadly_person_4.infected == "Deadly Virus"
	assert deadly_person_4.vaccinated == False

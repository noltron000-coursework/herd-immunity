# Project: Herd Immunity Simulation
We're going to create a basic simulation of *Herd Immunity* by modeling how a virus moves
through a population where some (but not all) of a population is vaccinated against this virus.

> #### Nolt's Note
> *This project final was originally created (at least) a couple years before the COVID-19 pandemic.*
> *It's aged quite well; the project is even more fitting to learn with, thanks to some serious retrospective.*

This repository is a draft to help you get started on the project,
and will be updated with more detail as we improve the project and answer questions.

## Project Goals
### Learning Outcomes
By completing this project, you should be able to...
1. Applying functions, scope, conditionals, loops, lists, OOP, and file I/O.
1. Practice reading spec, code comments, and starter code.
1. Practice writing basic tests, and practice running them.

### Primary Objective
Your primary objective is to finish the code in these files to create a working *Herd Immunity* simulation,
which also generates log files of its major events.
As you complete the project, design your program to follow the [rules of the simulation](simulation-rules).

#### Write Unit Tests
As you complete your solution,
we also want you to complete at least 5 of the test functions littered throughout the codebase.
You can also create your own tests (these will count towards the required total).

#### Use Sane Defaults
In order to double check that your simulation works, and spits out the expected results:
- Please use the *Ebola* example data as at least one of your inputs.
	This example data can be found [later in the README](#running-the-program).
- Please do not change the random seed set throughout the project!
	The seed is currently set to 42 at the top of each file.

This will also help you compare your results with your peers!

### Secondary Objective
Your secondary objective is to analyze the data that your simulation generates.
Once you have successfully run a simulation, analyze its log files to answer these questions...
1. What were the inputs you gave the simulation?
	(Population size, percent vaccinated, virus name, mortality rate, reproductive rate)
1. What percentage of the population became infected at some point before the virus burned out?
1. What percentage of the population died from the virus?
1. Out of all interactions sick individuals had during the entire simulation,
	how many total interactions did we see where a vaccination saved a person from potentially becoming infected?

*When you have answered these questions, please put your answers*
*in a file called <kbd>answers.md</kbd> and commit this to your repo.*

### *Optional:* Stretch Challenges
You'll find some of the smaller, individual stretch challenges
contained with the comments of the code on the logger class.
Other stretch challenges include:
- **(Difficulty Level: Easy)** -
	For this project, we give you a data set for Ebola.
	However, you can run this program with data on other viruses as well!
	Run simulations with them, and then upload their logged results files to GitHub.
	- **HINT:**
		You can find some additional virus data [in this article](how-ebola-compares).
		Other than this article, can you find other sources for virus data?
- **(Difficulty Level: Hard)** -
	Extend functionality so that we can test the spread of multiple viruses through a given population at the same time.
- **(Difficulty Level: Medium)** -
	Create a `Visualizer` class that can create visualizations of the virus spreading through the population,
	based on the log files of a simulation.
	- **HINT:**
		You'll want to use *Matplotlib* for visualization stuff,
		because its easy to use and generally awesome at this sort of thing.
	- **HINT:**
		You may also want to consider using a library like *Pandas* for organizing and cleaning your data in
		a more professional way, especially if you want to visualize answers to more complex questions.
	- *Matplotlib* and *Pandas* play very nicely together!

## Getting Started
To download the starter code and earn credit for your project, please follow these instructions *exactly*.
If you skip a step or do them out of order, it may not work correctly,
or you may not earn credit towards your GitHub commit streak.

### Repository Setup
Set up your local clone of this project repo on your computer.

1. [**Clone this repo** from GitHub](github-repo) onto your local computer.
	(Be sure to *clone* it &mdash; do not *fork* it!)
	1. First, open your terminal and navigate into the folder where you keep your projects:
		`cd ~/developer/projects/` (or something similar for your folders).
	1. Then, run this command to *clone* the course repo:
		`git clone https://github.com/remake-school/cs-101-project-herd-immunity-simulation herd-immunity-simulation`
	1. Finally, navigate into the new folder Git just created:
		`cd herd-immunity-simulation`
1. [**Create a new empty repo** on GitHub](github-project) also named `cs-101-project-herd-immunity-simulation`,
	and **do not** initialize it with a new README.
	We need to initialize it **without** a new README to keep the commit tree empty!
1. **Set the `origin` remote's URL** on your local repo to point to your new repo on GitHub:
	`git remote set-url origin https://github.com/<your-github-username>/cs-101-project-herd-immunity-simulation.git`
1. **Push your local repo** onto your *remote* GitHub repo to link your `main` branch to your `origin` remote:
	`git push -u origin main`
1. **Commit your code** to your local repo frequently (each time you've made meaningful progress).
1. **Push your commits** to your remote GitHub repo when you want to publish and backup your code:
	`git push` (the `-u` in the previous command lets you omit `origin main` afterward).

> #### *Cloning* vs *Forking*
> You may either **clone** or **fork** this repository, as either achieves similar results.
> The difference between cloning and forking usually has to do with intention:
> If you **fork** the repository into a new one, usually you intend to merge it back into the original repository.
> If you **clone** the repository into a new one, usually you intend to diverge from the original repository.
>
> On *GitHub*, *forking* will not count towards your commit streak,
> but will neatly and automatically link to the original repository.
> *cloning*, on the other hand, will count towards your commit streak,
> but it will not automatically link the original repository.
>
> Therefore, if you are seeking to complete this challenge project, you'll likely want to *clone* it.
> You will want to *fork* it if you find any errors in the code that you
> or if you want to suggest edits to this <kbd>README.md</kbd> file.

### Running the Program
The program is designed to be run from the command line.
You can even run the script as soon as you clone the repository from GitHub!
(Although it won't do much until you code in some logic, and fill in those empty functions...)

You can run the script by running `python3 simulation.py` in the project's root directory,
followed by these command line arguments, set in the following order:
`{virus name} {reproduction rate} {mortality rate} {population size} {vaccination rate}
{optional: number of people initially infected (default is 1)}`

To get credit for this project, you'll have to run your program with the following input data:

|                              |         |
| ---------------------------- | ------- |
| Virus Name                   | Ebola   |
| Reproduction Rate            | 25%     |
| Mortality Rate               | 70%     |
| Population Size              | 100,000 |
| Vaccination Rate             | 90%     |
| Initial Number of Infections | 10      |

To run your script with this data, you will type: <br />
`python3 simulation.py Ebola 0.25 0.70 100000 0.90 10` <br />
into the terminal.

### How the Program Works
The program consists of 4 classes: `Person`, `Virus`, `Simulation`, and `Logger`.
- `Simulation`: Highest level of abstraction. The main class that runs the entire simulation.
- `Person`: Represents the people that make up the population that the virus is spreading through.
- `Virus`: Models the properties of the virus we wish to simulate.
- `Logger`: A helper class for logging all events that happen in the simulation.

When you run <kbd>simulation.py</kbd> with the corresponding command-line arguments necessary for a simulation,
a `Simulation` class instance is created.
This simulation object then calls the `.run()` method.
This method should continually check if the simulation needs to run another step using
a helper method contained in the class, and then call `.time_step()` if the simulation has not ended yet.
Within the `.time_step()` method, you'll find all the logic necessary for actually simulating everything
&mdash; that is, once you write it.

As is, the files just contain a bunch of method stubs,
as well as numerous comments for explaining what you need to do to get everything working.

> #### *Let's get coding!*
> While there are more details within this <kbd>README</kbd>, you already have enough context to get started!
> You'll find instructions for what you need to do marked within the files themselves.
> Anything that you explicitly need to code should be marked with a comment that starts with `# TODO`.

### Rules
1. A sick person only has a chance at infecting healthy, unvaccinated people they encounter.
1. An infected person cannot infect a vaccinated person.
	This still counts as an interaction.
1. An infected person cannot infect someone that is already infected.
	This still counts as an interaction.
1. At the end of a time step, an infected person will either die of the infection or get better.
	The chance they will die is the percentage chance stored in `mortality_rate`.
1. For simplicity's sake, if the person does not die, we will consider them immune to the virus
	and change `is_vaccinated` to `True` when this happens.
1. Dead people can no longer be infected, either.
	Any time an individual dies, we should also change their `.infected` attribute to False.
1. All state changes for a person should occur at the **end** of a time step,
	after all infected persons have finished all of their interactions.
1. During the interactions, make note of any new individuals infected on this turn.
	After the interactions are over, we will change the .infected attribute of all newly infected individuals to `True`.
1. Resolve the states of all individuals that started the turn infected by determining
	if they die or survive the infection, and change the appropriate attributes.
1. The simulation should output a logfile that
	contains a record of every interaction that occurred during the simulation.
	We will use this logfile to determine final statistics and answer questions about the simulation.

## Tips for Success
First, take a look at each of the files.
Get a feel for the methods and attributes in each.
Feel overwhelmed? Don't panic.
Instead, get out a piece of paper or a whiteboard and try to diagram what needs to happen
and when using each of the objects and methods.
Draw out the data flow.

### Ask for Help
*If you don't understand something, talk to your classmates and ask for help!*

Ask your classmates and teachers for clarification/help/code reviews as needed, or drop in to tutoring hours.
Share your questions and insights in the course Slack channel,
or book some time to get help from Justin and Phyllis, the course teaching assistants.
Collaboration is encouraged, but be sure that you typed in all the code yourself and the final project is your own!

### Make Discourse on Bugs
*Found a bug or a problem? Contact the course instructors or teaching assistants!*

> #### Author's Note
> The template code was written in a cottage on the coast of Ireland with spotty power
> during the strongest hurricane Ireland has seen in 61 years.
> *(Alan's Note: This is 100% true!)*
>
> ***So...* there are probably some bugs in the template code**.

If you think something doesn't make sense, double check with your classmates and/or the instructor.
If you feel the need to modify the template code to make it work another way, that's totally fine!
The template code is there to help you, but it isn't a requirement that you use all of it.

### Write Tests!!!
This is a big project.
There's no way that all the code you write is going to work the first time.

Also, see the paragraph above about all of this being coded by a man on a mountain during a 61-year storm
while fighting off mountain lions with only a soup-ladle to defend himself.

Starting by thinking about your test cases and aiming for good test coverage is a great way
to vaccinate yourself against any pre-existing bugs in the template.
Not sure how to write tests?
Look at the tests for the Super Hero project and utilize some strategies from those tests.

## Detailed Requirements
Your [primary objective](#primary-objective) is to complete the starter code provided to you from the repository!
To help you with that task, we've put together a detailed overview of the functions that you will have to code out.
(This section is totally optional to read, but it may help outline what you want to work on next
&mdash; whether you're just starting on the project, or you're already halfway through.)

Your repository should contain four class files in total...
- <kbd>simulation.py</kbd>
- <kbd>person.py</kbd>
- <kbd>virus.py</kbd>
- <kbd>logger.py</kbd>

### <kbd>simulation.py</kbd>
The simulation class is the highest level of abstraction in the project.
This will contain all of your logic for two people interacting, and whether the virus impacts them.

Complete the logic in the following methods:
- `self.__init__()`:
	Follow the comment instructions to initialize this class.
- `self.create_population()`:
	You'll need to create a population by creating new `Person` classes.
- `self.simulation_should_continue()`:
	Determines whether the simulation should continue based on the state of the population.
	Check this out before each `time_step`.
- `self.infect_newly_infected()`:
	Newly infected people cannot also die from the virus on the same step, so we have to process them seperately.
- `self.run()`:
	This method will create a cycle with a `while` loop until `self.simulation_should_continue()` returns `False`.
- `self.time_step()`:
	This is where the interactions between an infected person and a random person from the population will be called.
	Hopefully, implementing this will help you deconstruct steps in `self.run()` and make it easier to read!
- `self.interaction()`:
	Represents an encounter between an infected person, and a random person.
	This is where a random person may become infected or vaccinated.

### <kbd>person.py</kbd>
Represents a single person in the population.
Complete the following logic in the file:
- `self.did_survive_infection()`:
	Will roll the dice, and determine whether a person survived based on the virus' mortality rate.
- You will also have to **code out atleast 3 tests** in this file.

### <kbd>virus.py</kbd>
Represents a virus which can infect the population.
This class will contain varius data about a virus as well.
- You must **code out atleast 2 tests** within this file.

### <kbd>logger.py</kbd>
This class solely exists to log simulation data into a text file.
As you complete this class, consider which methods you should complete first, and which are less critical for a MVP (minimal viable product).
Complete the following:
- `self.__init__()`:
	This method is incomplete!
	The comments for this one aren't great, so you'll have to figure it out yourself.
- `self.log_metadata()`:
	Creates and logs content for the top of the output data file; this is metadata.
- `self.log_results()`
	Logs a summary of the simulation to the bottom of the data file, after the simulation completes.
- `self.log_interaction()`
	Logs a line in the file, representing a single interaction between two people in the simulation.
- `self.log_infection_survival()`
	Logs a line in the file, representing whether an infected person lives or dies.
- Your project should generate human-readable text and log it to a file every time it runs.
	When you submit your project, **include at least one log file** generated from running your simulation.
	- If you aren't sure what this should look like, refer to <kbd>example_results.txt</kbd>, included in this repo.
	This should help you get started!
	*Note that the file is incomplete, and doesn't include all steps of the simulation.

<!-- References --->
[simulation-rules]: #rules
[github-new]: https://github.com/new
[github-project]: https://github.com/remake-school/cs-101-project-herd-immunity-simulation
[how-ebola-compares]: https://www.theguardian.com/news/datablog/ng-interactive/2014/oct/15/visualised-how-ebola-compares-to-other-infectious-diseases

from rich.console import Console
from rich.panel import Panel
from rich import box
import random
from rich.layout import Layout
from rich import print

console = Console()

#Write title
console.print(Panel.fit("                [bold purple4]Group[/] [slate_blue3]Creator[/] [sky_blue3][white]V1[/][/]                ", subtitle="[white]by[/] [slate_blue3]Isaac [/][purple4]Trost[/]", box=box.ROUNDED, style="sky_blue3")," ")
#<---------------->
def get_people():
	people = []
	console.print("[slate_blue3]Type each persons name. Type [bold]DONE[/] when you're done.[/]")
	people_count = 1
	done = False
	while not done:
		personinput = console.input(prompt=f"\t[purple4][[white]{people_count}.[/]] ").upper().strip()
		if personinput == "DONE":
			if len(people) <= 0:
				console.print("\tThere cant be less than one person!", style="bold italic red")
				continue
			done = True
		elif personinput != "":
			people.append(personinput)
		else:
			console.print("\tInvalid Input", style="bold italic red")
			continue
		people_count += 1
	console.print("\n", end="") #the same as leaving a print empty
	return people
#List which holds all the people
people = get_people()
random.shuffle(people)
#<---------------->
def get_sort_type():
	console.print("[slate_blue3]How would you like to generate your groups?[/]\n\t[sky_blue3][purple4][[white]1.[/]][/] Based on number of people per group\n\t[purple4][[white]2.[/]][/] Based on number of groups[/]")
	valid_choice = False
	choice1 = ["1", "1.", "[1.]", "one"]
	choice2 = ["2", "2.", "[2.]", "two"]
	sort_type = ""
	while not valid_choice:
		valid_choice = True
		choice = str(console.input("[slate_blue3]>: "))
		if choice in choice1:
			sort_type = "people"
		elif choice in choice2:
			sort_type = "group"
		else:
			valid_choice = False
			console.print("Invalid Input.", style="bold italic red")
	return sort_type
sort_type = get_sort_type() #can be either group (by number of groups) or people (by number of people in each group)
#<---------------->
def get_people_per_group(people):
	people_amount = len(people)
	console.print("\n[slate_blue3]How many people do you want in each group?[/]")
	valid_choice = False
	while not valid_choice:
		try:
			people_per_group = int(console.input("[slate_blue3]>: "))
		except:
			console.print("Invalid Input!", style="bold italic red")
			continue
		if people_per_group <= 0:
			console.print("There has to be at least 1 group!", style="bold italic red")
		elif people_per_group > people_amount:
			console.print("There cant be more people in each group than the total number of people!", style="bold italic red")
		else:
			valid_choice = True
	return people_per_group
#<---------------->
def get_groups_amount(people):
	console.print("\n[slate_blue3]How many groups do you want?[/]")
	valid_choice = False
	while not valid_choice:
		valid_choice2 = False
		while not valid_choice2:
			try:
				groups = int(console.input("[slate_blue3]>: "))
				valid_choice2 = True
			except:
				console.print("\tInvalid Input!", style="bold italic red")
		if groups <= 0:
			console.print("You can't have less than one group!", style="bold italic red")
		else:
			valid_choice = True
	return groups
#<---------------->
def generate_group(get_groups_amount, get_people_per_group, people, sort_type):
	if sort_type == "group":
		groups_amount = get_groups_amount(people)
		people_amount = len(people)
		remainer = people_amount % groups_amount
		people_per_group = int(round((people_amount - remainer) / groups_amount))
		groups = {}
		for group in range(0, groups_amount):
			random_people = []
			for loop in range(0, people_per_group):
				random_people.append(people[0])
				people.remove(people[0])
			groups[f"{group}"] = random_people
			people = [i for i in people if i not in random_people]

		if remainer:
			console.print(f"\n[slate_blue3]There are [bold]{remainer} person(s)[/] that could not fit evenly into a group.[/]")
			console.print("[slate_blue3]What would you like to do?[/]")
			console.print("[sky_blue3][purple4]\t[[white]1.[/]][/] Distribute the extra people evenly across the groups\n\t[purple4][[white]2.[/]][/] Put the remaining people into a seperate group[/]")
			choices_for_1 = ["1", "1.", "[1.]", "one"]
			choices_for_2 = ["2", "2.", "[2.]", "two"]
			valid_choice = False
			while not valid_choice:
				valid_choice = True
				choice = str(console.input("[slate_blue3]>: "))
				if choice in choices_for_1:
					cycle = 0
					while people != []:
						if cycle > len(groups)-1:
							cycle = 0
						groups[f"{cycle}"].append(people[0])
						people.remove(people[0])
						cycle += 1
				elif choice in choices_for_2:
					groups[f"{len(groups)}"]= people
				else:
					valid_choice = False
					console.print("Invalid Input.", style="bold italic red")
		return groups
	elif sort_type == "people":
		people_per_group = get_people_per_group(people)
		people_amount = len(people)
		remainer = people_amount % people_per_group
		groups_amount = int(round((people_amount - remainer) / people_per_group))
		groups = {}
		for group in range(0, groups_amount):
			random_people = []
			for i in range(people_per_group, 0, -1):
					random_people.append(people[0])
					people.remove(people[0])
				
			groups[f"{group}"] = random_people
			people = [i for i in people if i not in random_people]

		if remainer:
			console.print(f"\n[slate_blue3]There are [white bold]{remainer} person(s)[/] that could not fit evenly into a group.[/]")
			console.print("[slate_blue3]What would you like to do?[/]")
			console.print("[sky_blue3][purple4]\t[[white]1.[/]][/] Distribute the extra people evenly across the groups\n[purple4]\t[[white]2.[/]][/] Put the remaining people into a seperate group[/]")
			choices_for_1 = ["1", "1.", "[1.]", "one"]
			choices_for_2 = ["2", "2.", "[2.]", "two"]
			valid_choice = False
			while not valid_choice:
				valid_choice = True
				choice = str(console.input("[slate_blue3]>: "))
				if choice in choices_for_1:
					cycle = 0
					while people != []:
						if cycle == len(groups):
							cycle = 0
						groups[f"{cycle}"].append(people[0])
						people.remove(people[0])
						cycle += 1
				elif choice in choices_for_2:
					groups[f"{len(groups)}"] = people
				else:
					valid_choice = False
					console.print("Invalid Input.", style="bold italic red")
		return groups
groups = generate_group(get_groups_amount, get_people_per_group, people, sort_type)
#<---------------->
console.input(prompt="\n[slate_blue3]Press [bold white]ENTER[/] to continue[white]. . .[/]")
console.clear()
#<---------------->

console.print("\n[slate_blue3]Generated Groups[white]:[/]\n")
def print_groups(groups):
	for i in range(0, len(groups)):
		newline = '\n'
		console.print(Panel(f"[sky_blue3]{(newline).join(groups[str(i)])}[/]", title=f"[slate_blue3]Group[/] [white]{i+1}[/]"), style="purple4", width=26)
print_groups(groups)

console.input(prompt="\n[slate_blue3]Press [bold white]ENTER[/] to exit[white]. . .[/]")




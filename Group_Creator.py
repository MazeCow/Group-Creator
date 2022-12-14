from rich.console import Console
from rich.panel import Panel
from rich import box
import random

console = Console()

#Write title
console.print(Panel.fit("                [bold purple4]Group[/] [slate_blue3]Creator[/] [sky_blue3][white]V1[/][/]                ", subtitle="[white]by[/] [slate_blue3]Isaac [/][purple4]Trost[/]", box=box.ROUNDED, style="sky_blue3")," ")

#<---------------->



def get_people():
	people = []
	console.print("\n[slate_blue3]Type each persons name. Type QUIT when you're done.[/]")
	people_count = 1
	done = False
	while not done:
		personinput = console.input(prompt=f"\t[purple4][[white]{people_count}.[/]] ").upper().strip()
		if personinput == "QUIT":
			done = True
		elif personinput != "":
			people.append(personinput)
		else:
			console.print("Invalid Input", style="bold italic red")
		people_count += 1
	print(people)
	return people

#List which holds all the people
people = get_people()

#<---------------->

def get_sort_type():
	console.print("[slate_blue3]How would you like to generate your groups?[/]\n\t[sky_blue3][purple4][[white]1.[/]][/] Based on number of people per group\n\t[purple4][[white]2.[/]][/] Based on number of groups\n[/]")
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
		people_per_group = int(console.input("[slate_blue3]>: "))
		if people_per_group <= 0:
			console.print("There has to be at least 1 group!", style="bold italic red")
		elif people_per_group > people_amount:
			console.print("There cant be more groups than people!", style="bold italic red")
		else:
			valid_choice = True
	
	return people_per_group

#<---------------->

def get_groups_amount(people):
	people_amount = len(people)
	console.print("\n[slate_blue3]How many groups do you want?[/]")
	valid_choice = False
	while not valid_choice:
		valid_choice2 = False
		while not valid_choice2:
			try:
				groups = int(console.input("[slate_blue3]>: "))
				valid_choice2 = True
			except:
				console.print("Invalid Input!", style="bold italic red")
		if groups <= 0:
			console.print("You can't have less than one group!", style="bold italic red")
		else:
			valid_choice = True
	return people_amount

#<---------------->



def generate_group(groups_amount, people_per_group, people, sort_type):
	if sort_type == "group":
		groups_amount = groups_amount(people)
		people_amount = len(people)
		remainer = int(people_amount % groups_amount)
		people_per_group = int(people_amount - remainer) / groups_amount
		groups = {}
		for group in range(0, groups_amount-1):
			random_people = random.choices(people, k = people_per_group)
			groups[f"{group}"] = random_people
			for person in random_people:
				people.remove(person)

		if remainer:
			console.print(f"\n[slate_blue3]There are {remainer} people that could not fit evenly into a group.[/]")
			console.print("[slate_blue3]What would you like to do?[/]")
			console.print("[sky_blue3][purple4][[white]1.[/]][/] Distribute the extra people evenly across the groups\n\t[purple4][[white]2.[/]][/] Put the remaining people into a seperate group\n[/]")
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
					groups.add(f"{len(groups)}", people)
				else:
					valid_choice = False
					console.print("Invalid Input.", style="bold italic red")
		return groups
	elif sort_type == "person":
		people_per_group = people_per_group(people)
		people_amount = len(people)
		remainer = people_amount % people_per_group
		groups = {}
		for group in range(0, len(groups)-1):
			random_people = random.choices(people, k = people_per_group)
			groups.add(f"{group}", random_people)
			for person in random_people:
				people.remove(person)

		if remainer:
			console.print(f"\n[slate_blue3]There are {remainer} people that could not fit evenly into a group.[/]")
			console.print("[slate_blue3]What would you like to do?[/]")
			console.print("[sky_blue3][purple4][[white]1.[/]][/] Distribute the extra people evenly across the groups\n\t[purple4][[white]2.[/]][/] Put the remaining people into a seperate group\n[/]")
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
					groups.add(f"{len(groups)}", people)
				else:
					valid_choice = False
					console.print("Invalid Input.", style="bold italic red")
			return groups

groups = generate_group(get_groups_amount, get_people_per_group, people, sort_type)
print(groups)








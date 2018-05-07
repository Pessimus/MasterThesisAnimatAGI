def get_input():
	
	sensations = {}
	sensations["winter"] = {"[cold]", "[white]"}
	sensations["summer"] = {"[warm]", "[light]"}

	sensations["cat"] = {"[soft]", "[warm]"}
	sensations["dog"] = {"[soft]", "[warm]", "[loud]"}
	sensations["kitten"] = {"[soft]", "[warm]", "[small]"}
	sensations["puppy"] = {"[soft]", "[warm]", "[loud]", "[small]"}
	sensations["bird"] = {"[small]", "[loud]"}
	#sensations["lamp"] = {"light"}

	#sensations["cookie"] = {"sweet", "hard"}
	sensations["berry"] = {"[sweet]", "[soft]"}
	#sensations["lemon"] = {"sour"}
	#sensations["icecream"] = {"sweet", "cold", "soft"}
	sensations["milk"] = {"[white]", "[wet]", "[cold]"}

	sensations["water"] = {"[wet]", "[blue]"}
	sensations["ice"] = {"[cold]", "[hard]", "[blue]"}
	sensations["snow"] = {"[cold]", "[white]", "[soft]"}
	sensations["rain"] = {"[cold]", "[wet]"}
	sensations["sun"] = {"[light]", "[warm]"}

	sensations["night"] = {"[dark]", "[quiet]"}
	sensations["day"] = {"[light]", "[loud]"}

	sensations["green"] = {"[green]"}
	sensations["white"] = {"[white]"}
	sensations["black"] = {"[black]"}
	sensations["red"] = {"[red]"}

	sensations["wet"] = {"[wet]"}
	sensations["cold"] = {"[cold]"}
	sensations["frozen"] = {"[cold]"}

	sensations["leaves"] = {"[green]", "[small]"}
	sensations["tree"] = {"[green]", "[big]"}
	sensations["bush"] = {"[green]"}
	sensations["grass"] = {"[green]"}

	sensations["lake"] = {"[wet]", "[blue]", "[big]"}
	sensations["river"] = {"[wet]", "[blue]"}

	keywords = list(sensations.keys())


	return keywords,sensations

#keywords, key_to_sensations = get_input()
#all_sensations = []
#sensations_to_key = {}
#for key in keywords:
#	s = key_to_sensations[key]
#	for e in s:
#		if not e in all_sensations:
#			all_sensations.append(e) 
#			sensations_to_key[e] = {key}
#		else:
#			sensations_to_key[e].add(key)

#print(keywords)
#print(sensations_to_key["big"])
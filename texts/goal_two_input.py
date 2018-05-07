def get_input():
	
	sensations = {}
	sensations["winter"] = {"cold", "white"}
	sensations["summer"] = {"warm", "light", "green"}

	sensations["cat"] = {"soft", "warm", "small", "sharp"}
	sensations["dog"] = {"soft", "warm", "loud", "big"}
	sensations["kitten"] = {"soft", "warm", "tiny", "sharp"}
	sensations["puppy"] = {"soft", "warm", "loud", "small"}
	sensations["bird"] = {"small", "loud", "tiny"}
	#sensations["lamp"] = {"light"}

	#sensations["cookie"] = {"sweet", "hard"}
	sensations["berry"] = {"sweet", "soft", "tiny", "red"}
	#sensations["lemon"] = {"sour"}
	#sensations["icecream"] = {"sweet", "cold", "soft"}
	sensations["milk"] = {"white", "wet", "cold", "sweet"}

	sensations["water"] = {"wet", "blue", "cold", "warm"}
	sensations["ice"] = {"cold", "hard", "blue", "white"}
	sensations["snow"] = {"cold", "white", "soft"}
	sensations["rain"] = {"cold", "wet"}
	sensations["sun"] = {"light", "warm", "yellow", "red"}

	sensations["night"] = {"dark", "quiet", "black", "cold"}
	sensations["day"] = {"light", "loud", "warm"}

	sensations["green"] = {"green"}
	sensations["white"] = {"white"}
	sensations["black"] = {"black"}

	sensations["wet"] = {"wet"}
	sensations["cold"] = {"cold"}

	sensations["frozen"] = {"cold", "hard"}

	sensations["leaves"] = {"green", "small"}
	sensations["tree"] = {"green", "big"}
	sensations["bush"] = {"green", "small", "soft", "sharp"}
	sensations["grass"] = {"green", "soft", "tiny"}

	sensations["lake"] = {"wet", "blue", "big"}
	sensations["river"] = {"wet", "blue"}

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
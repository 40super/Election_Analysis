print("Hello World")
counties = ["Aaphoe","Denver","Jefferson"]
print(counties) 
#counties.insert(1,"NYC")
#print(counties)
counties.insert(1,"El Paso") 
counties.remove("Aaphoe")
counties.remove("Denver")
counties.append("Denver")
counties.append("Aaphoe")
print(counties)
my_tuple = ()
counties_tuple = ("Aaphoe","Denver","Jefferson")
print(len(counties_tuple))
counties_dict = {}
counties_dict["Aaphoe"] = 422829
counties_dict["Denver"] = 234144
counties_dict["Jefferson"] = 444145
print(counties_dict.items())
print(counties_dict.keys())
voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

#my_votes = (int(input("How many votes you got?")))
#total_vote = (int(input("What was the total vote in the election?")))
#print("Percentage that is your vote: " + str(my_votes/total_vote * 100))

#for county in counties:
 #   print(county)
    
#for i in range(len(counties)):
   # print(counties[i])

print("FOR LOOP TIME \n")  
for voters in counties_dict:
    print(voters)
    
for voters in counties_dict.values():
    print(voters)
    
for county in counties_dict:
    print(counties_dict[county])
    
for keys, value in counties_dict.items():
    print(keys,value)
    
for county_dict in voting_data:
    print(counties_dict)
    
for county, voter in counties_dict.items():
    print(f"{county} county has {voter} voters!")
    
    
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
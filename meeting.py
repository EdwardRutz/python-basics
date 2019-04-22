attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invites = ["Ben", "Dave"]
potential_attendees = attendees + optional_invites
print("There are", len(potential_attendees), "possible attendees currently")

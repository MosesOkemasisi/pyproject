players=["Ronaldo","Messi","Neymar","Mbappe","Salah"]


print ("players in the list:")
for player in players:
    print(player)


    search_player  = input("\nEnter the name of the player to search: ")
    if search_player in players:
        print("player found")
    else:
        print("player not found")

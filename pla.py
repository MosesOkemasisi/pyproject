players=["Ronaldo", "Messi", "Mbappe", "Neymar" "Dembele"]

while True:
    print("\n--- Football Player Management---")
    print("1. Add player")
    print("2. View player")
    print("3. Delete player")
    print("4. Exit")

    choice  =  input("choose an option: ")

    if choice =="1":
        player_name = input("Enter player name: ")
        players.append(player_name)
        print("player added successfully!")

    elif choice =="2":
        if len(players)==0:
            print("No players in the list.")
        else:
         print("\nList of players:")
         for player in players:
               print(player)


    elif choice =="3":
        player_name = input("Enter player name to delete: ")
        if player_name in players:
            players.remove(player_name)
            print("Player deleted successfully")
        else:
            print("Player not found!")


    elif choice =="4":
        print("Exiting the program")
        break

    else:
        print("Invalid choice")


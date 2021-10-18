class Team():
    
    # points = 0

    def __init__(self,name,players,coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        

    def team_has_name(name):
        return name
    
    def team_has_players(players):
        return players

    def team_has_coach(coach):
        return coach    

    def coach_can_be_changed(coach):
        return coach    
    
    def add_player(self,new_player):
        self.players.append(new_player)
        return self.players

    def has_player(self,player):
        for p in self.players:

         if p == player:
            
            return True
        else: 
            return False    

    def team_has_points(points):
        return points
    
    def play_game(self,result):
        if result == True:
            self.points += 3
            
        
             
            
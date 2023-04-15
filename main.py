from fastapi import FastAPI,HTTPException
from models import Team, Competition, Match


fake_teams_db = []
fake_competitions_db = []
fake_matchs_db = []

app = FastAPI()

################ ENDPOINTS FOR TEAMS ################

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teams/")
async def read_teams(skip: int = 0, limit: int = 10):
    return fake_teams_db[skip : skip + limit]

@app.get("/team/{team_name}")
async def read_team(team_name: str):
    team = next(iter([x for x in fake_teams_db if x.name == team_name]), None)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
@app.post("/teams/")
async def create_team(team: Team):
    if not fake_teams_db:
        fake_teams_db.append(team)
    else:
        exists_team = next(iter([x for x in fake_teams_db if x.name == team.name]), None)
        if not exists_team:
            fake_teams_db.append(team)
        else:
            raise HTTPException(status_code=404, detail="Team already Exists, Use put for updating")
    return team

@app.delete("/teams/{team_name}")
def delete_team(team_name: str):
    exists_team = next(iter([x for x in fake_teams_db if x.name == team_name]), None)
    if exists_team:
        fake_teams_db.remove(exists_team)
        return "Team deleted correctly"
    else:
        raise HTTPException(status_code=404, detail="Team doesn't exist")

@app.put("/teams/{team_name}")
def create_or_update_team(team: Team, team_name: str):
    exists_team = next(iter([x for x in fake_teams_db if x["name"] == team_name]), None)
    if exists_team:
        exists_team.update(team.dict())
        return "Team correctly updated"
    else:
        team_dict = team.dict()
        fake_teams_db.append(team_dict)
        return "Team correctly created"

################ ENDPOINTS FOR COMPETITIONS ################

@app.get("/competitions/")
async def read_competition(skip: int = 0, limit: int = 10):
    return fake_competitions_db[skip : skip + limit]

@app.post("/competitions/")
async def create_competition(competition: Competition):
    if not fake_competitions_db:
        fake_competitions_db.append(competition)
    else:
        exists_competition = next(iter([x for x in fake_competitions_db if x.name == competition.name]), None)
        if not exists_competition:
            fake_competitions_db.append(competition)
        else:
            raise HTTPException(status_code=404, detail="Competition already Exists, Use put for updating")
    return competition

@app.delete("/competitions/{competition_name}")
def delete_competition(competition_name: str):
    exists_competition = next(iter([x for x in fake_competitions_db if x.name == competition_name]), None)
    if exists_competition:
        fake_competitions_db.remove(exists_competition)
        return "Competition correctly deleted"
    else:
        raise HTTPException(status_code=404, detail="Competition doesn't exist")

@app.put("/competitions/{competition_name}")
def create_or_update_competition(competition: Competition, competition_name: str):
    exists_competition = next(iter([x for x in fake_competitions_db if x["name"] == competition_name]), None)
    if exists_competition:
        exists_competition.update(competition.dict())
        return "Competition correctly updated"
    else:
        team_dict = competition.dict()
        fake_competitions_db.append(team_dict)
        return "Competition correctly created"

################ ENDPOINTS FOR MATCHES ################

@app.get("/matches/")
async def read_match(skip: int = 0, limit: int = 10):
    return fake_matchs_db[skip : skip + limit]

@app.post("/matches/")
async def create_match(match: Match):
    if not fake_matchs_db:
        fake_matchs_db.append(match)
    else:
        exists_match = next(iter([x for x in fake_matchs_db if x.id == match.id]), None)
        if not exists_match:
            fake_matchs_db.append(match)
        else:
            raise HTTPException(status_code=404, detail="Match already Exists, Use put for updating")
    return match

@app.delete("/matches/{match_id}")
def delete_competition(match_id: int):
    exists_match = next(iter([x for x in fake_matchs_db if x.id == match_id]), None)
    if exists_match:
        fake_matchs_db.remove(exists_match)
        return "Match correctly deleted"
    else:
        raise HTTPException(status_code=404, detail="Match doesn't exist")

@app.put("/matches/{match_id}")
def create_or_update_competition(match: Match, match_id: int):
    exists_match = next(iter([x for x in fake_matchs_db if x["id"] == match_id]), None)
    if exists_match:
        exists_match.update(match.dict())
        return "Match correctly updated"
    else:
        match_dict = match.dict()
        fake_matchs_db.append(match_dict)
        return "Match correctly created"












from match1 import match_career_goals
from match2 import process_user_preferences
from match3 import match_skills
def all_match(items,jobs):
   goals= match_career_goals(items,jobs)
   user= process_user_preferences(items,jobs)
   skills=match_skills(items,jobs)
   return {"goals":goals,"user":user,"skills":skills}
    
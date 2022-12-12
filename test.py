from modules.medal import MedalCabinet

medal = MedalCabinet()

medals = await medal.get_user_medals("zhou_zhou")
msg = ','.join(medals)
print(msg)

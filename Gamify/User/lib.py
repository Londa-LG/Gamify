


def AssignPoints(request):
    mind = request.user.status.challenge_mind.reward
    mind = mind.split(",")
    body = request.user.status.challenge_body.reward
    body = body.split(",")
    skill = request.user.status.challenge_skill.reward
    skill = skill.split(",")
    for atr in mind:
        if atr == "intelligence":
            current = request.user.status
            current.intelligence += 1
            current.save()
        if atr == "strength":
            current = request.user.status
            current.strength += 1
            current.save()
        if atr == "agility":
            current = request.user.status
            current.agility += 1
            current.save()
        if atr == "vitality":
            current = request.user.status
            current.vitality += 1
            current.save()

    for atr in body:
        if atr == "intelligence":
            current = request.user.status
            current.intelligence += 1
            current.save()
        if atr == "strength":
            current = request.user.status
            current.strength += 1
            current.save()
        if atr == "agility":
            current = request.user.status
            current.agility += 1
            current.save()
        if atr == "vitality":
            current = request.user.status
            current.vitality += 1
            current.save()

    for atr in skill:
        if atr == "intelligence":
            current = request.user.status
            current.intelligence += 1
            current.save()
        if atr == "strength":
            current = request.user.status
            current.strength += 1
            current.save()
        if atr == "agility":
            current = request.user.status
            current.agility += 1
            current.save()
        if atr == "vitality":
            current = request.user.status
            current.vitality += 1
            current.save()



def Date():
    td = datetime.date.today()
    return td
def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    current_percent = some_number // 10
    return f"{some_number}% [{current_percent * '%'}{'.' * (10 -current_percent)}]\nStill loading..."


number = int(input())
print(loading_bar((number)))

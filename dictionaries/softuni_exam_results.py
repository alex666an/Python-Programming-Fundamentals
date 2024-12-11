info = input()

results = {}
submission = {}
while info != "exam finished":
    command = info.split("-")
    username = command[0]

    if "banned" in command:
        results.pop(username)
    else:
        language = command[1]
        points = int(command[2])
        results[username] = results.get(username, points)
        submission[language] = submission.get(language, 0)
        if username in results:
            results[username] = max(results[username], points)
        if language in submission:
            submission[language] += 1
    info = input()

print("Results:")
for name, point in results.items():
    print(f"{name} | {point}")

print("Submissions:")
for language_k, times in submission.items():
    print(f"{language_k} - {times}")


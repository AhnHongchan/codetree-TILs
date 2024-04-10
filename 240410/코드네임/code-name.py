class Agent:
    def __init__(self, id, score):
        self.id = id
        self.score = score

lst = []
for _ in range(5):
    x, y = input().split()
    y = int(y)
    agent = Agent(x, y)
    lst.append([agent.id, agent.score])

lst.sort(key = lambda x:x[1])
print(*lst[0])
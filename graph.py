graph = {
    "تهران": ["اصفهان", "قم"],
    "اصفهان": ["تهران", "شیراز"],
    "قم": ["تهران"],
    "شیراز": ["اصفهان"]
}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        city = queue.pop(0)
        if city not in visited:
            visited.append(city)
            queue += graph[city]

    return visited

print(bfs(graph, "تهران"))
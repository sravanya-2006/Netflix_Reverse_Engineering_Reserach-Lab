cache = {}

movie = "Stranger Things"

if movie in cache:
    print("Cache Hit")
else:
    cache[movie] = "Video Data"
    print("Cache Miss")
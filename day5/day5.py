with open("day5/day5.txt") as f:
  file = f.read().split("\n\n")

seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]

maps = [[[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1:]] for i in range(1, 8)]

locs = []

for seed in seeds:
  for map in maps:
    for line in map:
      dest = range(line[0], line[0] + line[2])
      src = range(line[1], line[1] + line[2])
      if seed in src:
        seed = seed + (dest[0] - src[0])
        break

  locs.append(seed)
print(locs)
print(min(locs))
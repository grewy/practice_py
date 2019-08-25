
def bridge_break(reqs):
    reqs.sort()
    ps = 0
    out = 0

    for req in reqs:
        if req[1] >= ps:
            out += 1
            ps = req[0]

    return out


n, m = map(int, raw_input().split())
reqs = []
for _ in range(m):
    st, end = map(int, raw_input().split())
    reqs.append((end, st))

print bridge_break(reqs)

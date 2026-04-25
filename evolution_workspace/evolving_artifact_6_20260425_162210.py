# Evolving Artifact - Generation 6
# Created: 2026-04-25 16:22:10.363424

def compute_pattern():
    """Generate evolving pattern"""
    pattern = []
    base = 3
    for i in range(7):
        pattern.append(base * i)
    return pattern

if __name__ == "__main__":
    print("Pattern:", compute_pattern())
    print("Generation:", 6)

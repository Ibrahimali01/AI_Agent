# Evolving Artifact - Generation 4
# Created: 2026-04-25 16:22:08.356330

def compute_pattern():
    """Generate evolving pattern"""
    pattern = []
    base = 2
    for i in range(3):
        pattern.append(base * i)
    return pattern

if __name__ == "__main__":
    print("Pattern:", compute_pattern())
    print("Generation:", 4)

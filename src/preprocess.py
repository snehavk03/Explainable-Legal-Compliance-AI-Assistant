import re
def split_into_clauses(text):
    clauses = re.split(r'\.\s+', text)
    return [c.strip() for c in clauses if len(c) > 20]
if __name__ == "__main__":
    with open("data/sample_contract.txt","r",encoding="utf-8") as f: text=f.read()
    for i,c in enumerate(split_into_clauses(text),1): print(f"Clause {i}: {c}")
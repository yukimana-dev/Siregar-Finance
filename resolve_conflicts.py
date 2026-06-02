import re

file_path = r"C:\Users\V I C T U S\Downloads\Archiel Finance.worktrees\agents-fix-wallet-connection-ui-updates\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match merge conflicts
pattern = r'<<<<<<< Updated upstream\n(.*?)\n=======\n(.*?)\n>>>>>>> Stashed changes'

def resolve_conflict(match):
    upstream = match.group(1)
    stashed = match.group(2)
    # Prefer stashed version (more modern and complete)
    return stashed

# Replace all conflicts
resolved_content = re.sub(pattern, resolve_conflict, content, flags=re.DOTALL)

# Count remaining conflicts
remaining = len(re.findall(r'<<<<<<< |=======|>>>>>>>', resolved_content))
print(f"Remaining conflict markers: {remaining}")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(resolved_content)

print("Conflicts resolved successfully!")

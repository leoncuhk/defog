#!/usr/bin/env python3
"""Validate defog skill files: frontmatter, naming, cross-references, format claims."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
errors = []


def parse_frontmatter(text, path):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        errors.append(f"{path}: missing frontmatter block")
        return None, ""
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


skill_names = set(os.listdir(SKILLS))

for name in sorted(skill_names):
    path = os.path.join(SKILLS, name, "SKILL.md")
    if not os.path.isfile(path):
        errors.append(f"skills/{name}: missing SKILL.md")
        continue
    text = open(path).read()
    fm, body = parse_frontmatter(text, path)
    if fm is None:
        continue
    if fm.get("name") != name:
        errors.append(f"{path}: frontmatter name '{fm.get('name')}' != directory '{name}'")
    desc = fm.get("description", "")
    if len(desc) < 20:
        errors.append(f"{path}: description too short ({len(desc)} chars)")
    if len(desc) > 500:
        errors.append(f"{path}: description too long ({len(desc)} chars) — descriptions are always-loaded context")
    dmi = fm.get("disable-model-invocation", "false")
    if dmi not in ("true", "false"):
        errors.append(f"{path}: disable-model-invocation must be true/false, got '{dmi}'")
    # Model-invoked skills need trigger phrasing; user-invoked need none.
    if dmi == "false" and "Use when" not in desc:
        errors.append(f"{path}: model-invoked skill description lacks 'Use when' trigger phrasing")
    # Cross-references to other skills must resolve.
    for ref in re.findall(r"`(fog[a-z-]*)`", body):
        if ref not in skill_names and ref != "fog":
            errors.append(f"{path}: references unknown skill `{ref}`")

# README claims that must stay true.
readme = open(os.path.join(ROOT, "README.md")).read()
total = sum(
    len(open(os.path.join(SKILLS, n, "SKILL.md")).read().splitlines())
    for n in skill_names
)
if total >= 239:
    errors.append(
        f"README claim broken: combined skill lines ({total}) no longer smaller than the 239-line monolith"
    )
for n in skill_names:
    if f"skills/{n}/SKILL.md" not in readme:
        errors.append(f"README: skill table missing link to skills/{n}/SKILL.md")

if errors:
    print(f"FAIL — {len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK — {len(skill_names)} skills valid, {total} combined lines")

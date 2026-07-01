#!/usr/bin/env python3
"""bamboo_governor.py — Repository Documentation & Bamboo Memory Tiering Governor.

Enforces canonical folder structure, injects standard header metadata,
appends memory tier (Hot, Warm, Medium, Cool, Cold, Ice) changelogs,
and exports a single-entry structured manifest.
"""
from __future__ import annotations

from datetime import date
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def get_git_timestamps(filepath: Path) -> tuple[str, str]:
    try:
        cmd = ["git", "log", "--follow", "--format=%as", "--", str(filepath)]
        dates = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode().strip().splitlines()
        if not dates:
            today = date.today().isoformat()
            return today, today
        return dates[-1], dates[0]
    except Exception:
        today = date.today().isoformat()
        return today, today

def get_latest_tag() -> str:
    try:
        return subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return "v0.8.0"

def infer_memory_tier(filepath: Path, created_date_str: str | None = None) -> str:
    path_str = str(filepath.relative_to(REPO_ROOT)).lower()
    
    # Check for age-based ice tiering (6 months = 180 days)
    if created_date_str:
        try:
            created_dt = date.fromisoformat(created_date_str)
            age_days = (date.today() - created_dt).days
            if age_days >= 180:
                return "Ice"
        except Exception:
            pass

    if "docs/bamboo" in path_str or "docs/engineering" in path_str:
        return "Hot"
    elif "docs/architecture" in path_str or "why.md" in path_str:
        return "Warm"
    elif "docs/product" in path_str:
        return "Medium"
    elif "docs/notes" in path_str or "docs/research" in path_str or "docs/decision-records" in path_str:
        return "Cool"
    else:
        return "Cold"

def reformat_and_inject(filepath: Path, latest_tag: str) -> dict | None:
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"⚠️ Failed to read {filepath}: {e}")
        return None

    if not content.strip():
        return None

    # Strip existing changelog if present
    if "### 📜 Document Changelog" in content:
        content = content.split("### 📜 Document Changelog")[0].rstrip()
    elif "## 📜 Document Changelog" in content:
        content = content.split("## 📜 Document Changelog")[0].rstrip()

    # Strip trailing horizontal rule and spacing
    lines = content.splitlines()
    while lines and (lines[-1].strip() == "" or lines[-1].strip() == "---"):
        lines.pop()
    content = "\n".join(lines)

    # Strip existing top-level metadata block
    lines = content.splitlines()
    if "Document Metadata:" in content or "**Document Metadata:**" in content:
        new_lines = []
        in_metadata = False
        skipped_metadata = False
        for line in lines:
            if line.strip() == "---" and not skipped_metadata:
                idx = lines.index(line)
                if idx + 1 < len(lines) and ("Document Metadata:" in lines[idx + 1] or "**Document Metadata:**" in lines[idx + 1]):
                    in_metadata = True
                    continue
                elif in_metadata:
                    in_metadata = False
                    skipped_metadata = True
                    continue
            if in_metadata:
                continue
            new_lines.append(line)
        lines = new_lines

    # Find and update the title line
    title_idx = -1
    title_text = filepath.stem.replace("-", " ").title()
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            title_idx = idx
            title_text = line[2:].strip()
            break

    created, updated = get_git_timestamps(filepath)
    version = latest_tag.split("-")[0].replace("v", "")
    memory_tier = infer_memory_tier(filepath, created)

    # Clean the title of existing versions
    title_clean = re.sub(r'\s*-\s*v\d+(\.\d+)*$', '', title_text).strip()
    if title_idx != -1:
        lines[title_idx] = f"# {title_clean} - v{version}"

    # Rebuild top-level Metadata
    metadata_block = [
        "---",
        "**Document Metadata:**",
        f"- **Created:** {created}",
        f"- **Last Updated:** {updated}",
        f"- **Document Version:** v{version}",
        f"- **Operational Freeze Tag:** `{latest_tag}`",
        "---"
    ]

    # Rebuild bottom Changelog
    one_sentence_summary = "Aligned structural doctrine with standard memory tiering."
    if memory_tier == "Hot":
        one_sentence_summary = "Standardized operational guidelines and execution runbooks."
    elif memory_tier == "Medium":
        one_sentence_summary = "Aligned product requirements and specifications."
    elif memory_tier == "Cool":
        one_sentence_summary = "Updated research metrics and observations."
    elif memory_tier == "Cold":
        one_sentence_summary = "Archived historical retro and post-mortem logs."
    elif memory_tier == "Ice":
        one_sentence_summary = "Archived historical conversational notes and frozen metrics."

    changelog_block = [
        "---",
        "### 📜 Document Changelog",
        "",
        "| Version | Date | Freeze Tag | Memory Tier | Summary of Change |",
        "| :--- | :--- | :--- | :--- | :--- |",
        f"| v{version} | {updated} | `{latest_tag}` | **{memory_tier}** | {one_sentence_summary} |"
    ]

    header = lines[:title_idx + 1]
    body = lines[title_idx + 1:]

    updated_lines = header + [""] + metadata_block + [""] + body + [""] + changelog_block
    try:
        filepath.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
        print(f"✅ Governed: {filepath.relative_to(REPO_ROOT)} [{memory_tier}]")
        return {
            "path": str(filepath.relative_to(REPO_ROOT)),
            "title": title_clean,
            "version": f"v{version}",
            "freeze_tag": latest_tag,
            "memory_tier": memory_tier,
            "created": created,
            "updated": updated,
            "summary": one_sentence_summary
        }
    except Exception as e:
        print(f"❌ Failed to write {filepath}: {e}")
        return None

def main() -> int:
    latest_tag = get_latest_tag()
    docs_dir = REPO_ROOT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    manifest_entries = []
    
    # Governs all markdown files in the repository
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if any(part in path.parts for part in [".git", "node_modules", "venv", ".gemini", "bamboo-test"]):
            continue
        entry = reformat_and_inject(path, latest_tag)
        if entry:
            manifest_entries.append(entry)

    # Export BAMBOO_MANIFEST.json
    bamboo_dir = docs_dir / "bamboo"
    bamboo_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = bamboo_dir / "BAMBOO_MANIFEST.json"
    manifest_data = {
        "release_freeze_tag": latest_tag,
        "document_count": len(manifest_entries),
        "documents": manifest_entries
    }
    manifest_path.write_text(json.dumps(manifest_data, indent=2), encoding="utf-8")
    print(f"🚀 Bamboo Manifest exported successfully to {manifest_path.relative_to(REPO_ROOT)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())

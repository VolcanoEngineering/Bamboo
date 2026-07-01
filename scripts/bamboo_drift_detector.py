#!/usr/bin/env python3
"""bamboo_drift_detector.py — Repository Compliance & Context Drift Detector.

Scans the repository's markdown documentation to verify adherence to
the Bamboo Doctrine formatting rules (Created headers, versioned footers, 
and contamination link requirements).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def scan_markdown_compliance() -> tuple[list[str], list[str], list[str]]:
    non_compliant_headers = []
    non_compliant_footers = []
    contamination_violations = []
    
    # Audit all markdown files in the repository
    paths_to_scan = sorted(list(REPO_ROOT.glob("**/*.md")))
    
    for p in paths_to_scan:
        # Ignore common non-project subdirectories
        if any(part in p.parts for part in [".git", "node_modules", "venv", ".gemini", "bamboo-test"]):
            continue
            
        try:
            content = p.read_text(encoding="utf-8")
        except Exception:
            continue
            
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        if not lines:
            continue
            
        # 1. Check Header (first 10 non-empty lines) for Created date
        header_text = "\n".join(lines[:10])
        if not re.search(r"(created|created\s*date)", header_text, re.IGNORECASE):
            non_compliant_headers.append(str(p.relative_to(REPO_ROOT)))
            
        # 2. Check Footer (last 10 non-empty lines) for versioned Last Updated
        footer_text = "\n".join(lines[-10:])
        if not re.search(r"(last updated|updated|version.*v[0-9])", footer_text, re.IGNORECASE):
            non_compliant_footers.append(str(p.relative_to(REPO_ROOT)))
            
        # 3. Check 2026-06-13 Contamination Mandate
        if "2026-06-13" in content:
            if "RECALIBRATION_LOG.md" not in content and "FORENSIC-LEDGER-V2.md" not in content:
                contamination_violations.append(str(p.relative_to(REPO_ROOT)))
                
    return non_compliant_headers, non_compliant_footers, contamination_violations

def main():
    print("🎋 Running Bamboo Drift Detector...")
    
    nc_headers, nc_footers, contamination_violations = scan_markdown_compliance()
    
    all_docs = [p for p in REPO_ROOT.glob("**/*.md") if not any(part in p.parts for part in [".git", "node_modules", "venv", ".gemini", "bamboo-test"])]
    total_audited_docs = len(all_docs)
    
    # Calculate compliance scores
    header_compliance = 1.0 - (len(nc_headers) / max(total_audited_docs, 1))
    footer_compliance = 1.0 - (len(nc_footers) / max(total_audited_docs, 1))
    contamination_compliance = 1.0 - (len(contamination_violations) / max(total_audited_docs, 1))
    
    # Overall Bamboo Drift Score (100 - average compliance %)
    overall_drift_score = round(100.0 * (1.0 - (header_compliance + footer_compliance + contamination_compliance) / 3.0), 2)
    
    # Build lists
    nc_headers_str = "\n".join([f"- [{p.split('/')[-1]}](file://{REPO_ROOT / p})" for p in nc_headers[:20]]) or "*None found.*"
    nc_footers_str = "\n".join([f"- [{p.split('/')[-1]}](file://{REPO_ROOT / p})" for p in nc_footers[:20]]) or "*None found.*"
    contamination_str = "\n".join([f"- [{p.split('/')[-1]}](file://{REPO_ROOT / p})" for p in contamination_violations]) or "*None found.*"
    
    # Generate MD Report
    report_path = REPO_ROOT / "docs" / "bamboo" / "BAMBOO_DRIFT_REPORT.md"
    report_content = f"""# 🎋 Bamboo Drift Compliance & Integrity Report

**Created:** 2026-07-01

## 📊 Compliance Scorecard
*   **Overall Repository Drift Score:** `{overall_drift_score}%` (lower is better, 0% is perfect compliance)
*   **Doc Header Compliance:** `{header_compliance:.2%}`
*   **Doc Footer Compliance:** `{footer_compliance:.2%}`
*   **Contamination Notice Audits:** `{contamination_compliance:.2%}`

---

## ⚠️ Non-Compliant Documents: Headers
*These files do not contain a 'Created Date' block near the top:*
{nc_headers_str}
{f"*...and {len(nc_headers) - 20} more files.*" if len(nc_headers) > 20 else ""}

## ⚠️ Non-Compliant Documents: Footers
*These files do not contain a versioned update footer at the bottom:*
{nc_footers_str}
{f"*...and {len(nc_footers) - 20} more files.*" if len(nc_footers) > 20 else ""}

## ⚠️ Contamination Notice Violations
*These files refer to '2026-06-13' without the required RECALIBRATION_LOG/FORENSIC-LEDGER-V2 reconciliation link:*
{contamination_str}

---

**Last Updated:** 2026-07-01-v0.8.0
"""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content, encoding="utf-8")
    print(f"✅ Saved Bamboo Drift Compliance Report to: {report_path}")
    print(f"🎋 Drift Score: {overall_drift_score}%")

if __name__ == "__main__":
    main()

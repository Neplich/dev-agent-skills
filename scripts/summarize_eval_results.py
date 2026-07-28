#!/usr/bin/env python3
"""汇总各 skill 最新 eval 结论，输出 changelog 的 Skill Eval 汇总表。

按每个 skill 的 evals.json 中 workspace 字段定位 durable comparison.md，
提取 Latest result 结论（PASS / PARTIAL / BLOCKED），按 skill 分组统计。
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_comparison(test_dir, workspace):
    """按 eval workspace 字段定位 comparison.md，兼容 test/{skill}/ 与 test/{skill}/evals/ 两种基准。"""
    for base in (test_dir, os.path.join(test_dir, "evals")):
        candidate = os.path.join(base, workspace, "comparison.md")
        if os.path.isfile(candidate):
            return candidate
    return None


def extract_result(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"Latest [Rr]esult[：:]\s*\**\s*(PASS|PARTIAL|BLOCKED)", text)
    if m:
        return m.group(1)
    m = re.search(r"^##\s*Latest [Rr]esult\s*$([\s\S]{0,400})", text, re.M)
    if m:
        m2 = re.search(r"(PASS|PARTIAL|BLOCKED)", m.group(1))
        if m2:
            return m2.group(1)
    return None


def main():
    rows = []
    total_files = 0
    total_stat = {"PASS": 0, "PARTIAL": 0, "BLOCKED": 0, "UNKNOWN": 0}
    missing = []
    for evals_path in sorted(glob.glob(os.path.join(ROOT, "agents/*/test/*/evals/evals.json"))):
        test_dir = os.path.dirname(os.path.dirname(evals_path))
        rel = os.path.relpath(test_dir, ROOT)
        agent = rel.split(os.sep)[1]
        skill = os.path.basename(test_dir)
        data = json.load(open(evals_path, encoding="utf-8"))
        stat = {"PASS": 0, "PARTIAL": 0, "BLOCKED": 0, "UNKNOWN": 0}
        n = 0
        for ev in data["evals"]:
            comp = find_comparison(test_dir, ev["workspace"])
            if not comp:
                missing.append(f"{agent}/{skill} {ev['id']} ws={ev['workspace']}")
                stat["UNKNOWN"] += 1
            else:
                r = extract_result(comp) or "UNKNOWN"
                stat[r] += 1
            n += 1
        for k in total_stat:
            total_stat[k] += stat[k]
        total_files += n
        parts = [f"{stat[k]} {k}" for k in ("PASS", "PARTIAL", "BLOCKED", "UNKNOWN") if stat[k]]
        rows.append((agent, skill, n, "、".join(parts) if parts else "-"))
    for agent, skill, n, summary in rows:
        print(f"| {agent} | `{skill}` | {n} | {summary} |")
    print(f"\n共 {len(rows)} 个 skill 分组、{total_files} 份 comparison："
          + "、".join(f"{v} {k}" for k, v in total_stat.items() if v))
    if missing:
        print("\n缺 comparison.md:", file=sys.stderr)
        for m in missing:
            print(f"  {m}", file=sys.stderr)


if __name__ == "__main__":
    main()

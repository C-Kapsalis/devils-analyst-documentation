The hook and the scripts
========================

The session hook
----------------

The hook prints one file, ``hooks/core.md``, into the agent's context
at the start of a session. It runs in hosts that support plugin hooks.
It does not run in Claude on the web or Desktop chat, in ChatGPT, or
after ``npx skills add``, which installs the skills only.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File
     - What it does
   * - ``hooks/claude-hooks.json``
     - Claude Code (and the Codex plugin manifest). On the
       ``SessionStart`` event, for ``startup``, ``resume``, ``clear``
       and ``compact``, runs ``cat "${CLAUDE_PLUGIN_ROOT}/hooks/core.md"``
       with a 5-second timeout.
   * - ``hooks/copilot-hooks.json``
     - GitHub Copilot CLI. On ``sessionStart``, prints the same file,
       with a bash command and a PowerShell command. Both exit quietly
       if the file is missing.
   * - ``hooks/core.md``
     - The text the hook prints.

``core.md`` holds three things:

- **A routing table.** It tells the agent to load the matching skill
  before answering any question about marketing data, a marketing
  deliverable or a marketing decision, starting with
  ``devils-analyst:route-question``, and not to answer from memory when
  a skill covers the question. Each row maps a kind of request to one
  of the 16 skills (see :doc:`skills`).
- **The house rules precedence.** Your words in the conversation, then
  house rules, then governed definitions, then the shipped defaults.
- **Seven rules that hold before any skill loads:**

  1. Rates are ratios of summed parts, never averages of rates.
  2. Users, reach, snapshots and percentiles do not add across days or
     groups.
  3. Overlapping columns (attribution windows, ``all_conversions``,
     report levels) are alternatives: pick one and say which.
  4. Two sources meet only after each is aggregated to a shared key.
  5. A before and after is not an effect without a comparison; a
     winner needs significance and power; platform credit is not
     incremental.
  6. Every claim gets an adversary: what else would produce this
     number? Check it before handing over.
  7. Lead with the answer and its number; label unproven causes as
     hypotheses; pair every action with a way to verify it. Do not flag
     what is correct and do not pad.

The scripts
-----------

All the Python scripts use only the standard library.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Script
     - What it does
   * - ``scripts/count.py``
     - Counts the skills, the numbered checks (per audit area and for
       the review), the diagnosis playbooks and the benchmark cases
       from the files. Also checks that every skill description is at most 1,024
       characters, the Agent Skills limit, and exits 1 if one is
       longer.
   * - ``scripts/package.sh``
     - Builds the release zips into ``dist/``: the Claude plugin zip,
       one zip per skill (renamed ``devils-analyst-<skill>``, with a
       description under 200 characters), an archive of all of them,
       and the ChatGPT plugin zip (no hooks). POSIX ``sh``; needs
       ``zip``. A workflow runs it on every ``v*`` tag.
   * - ``scripts/sync-adapters.py``
     - Copies ``AGENTS.md`` into the rules-file adapters (Cursor,
       Cline, Copilot Chat, Kiro, OpenClaw), builds the ChatGPT
       instructions from the compact Windsurf version, and bundles the
       skills into ten ChatGPT knowledge files. ``--check`` exits 1 if
       any copy is out of date.
   * - ``skills/power-bi-definitions/scripts/metric_contract.py``
     - Reads a PBIP or TMDL semantic model and prints its measures,
       tables, warehouse sources and relationships.
       ``--format json|markdown``, ``--out FILE``. Read-only.
   * - ``skills/power-bi-definitions/scripts/devils-analyst-tool``
     - A bash wrapper that runs one of the four Power BI command-line
       tools (``pbip-forge``, ``tmdl-preflight``, ``drift-doctor``,
       ``pbi-plot-styler``) at a pinned release tag through ``uvx``.
       Defaults to ``v1.2.0``; ``DEVILS_ANALYST_TOOLS_VERSION`` picks
       another tag, and ``DEVILS_ANALYST_USE_LOCAL=1`` prefers a copy
       already on the path. Exits 127 with install instructions when it
       cannot run the tool.
   * - ``benchmarks/builder/build_all.py``
     - Builds the benchmark cases: runs each case script, which
       simulates the exports with a fixed seed, computes the true
       answer and writes the case. Pass case names to build only those.
   * - ``benchmarks/report.py``
     - Turns a ``claude plugin eval`` log into a results page with
       overall and per-group tables. ``--no-readme`` leaves the README
       alone.

Run the two repository checks from the repository folder.

bash:

::

    python3 scripts/count.py
    python3 scripts/sync-adapters.py --check

PowerShell:

::

    py -X utf8 scripts\count.py
    py -X utf8 scripts\sync-adapters.py --check

``-X utf8`` matters on Windows: both scripts read the skill files with
the system's default encoding, and some skill files hold characters
that the usual Windows default cannot decode.

A workflow runs the same two commands on every push and pull request.

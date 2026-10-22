Contributing
============

Devil's Analyst is a set of skills written in Markdown, a session hook,
a few standard-library Python scripts and a benchmark. The most useful
contributions, in order:

1. **A case where it is wrong.** A real problem it missed, a correct
   detail it flagged, a number it got wrong, or a decision it called the
   wrong way.
2. **A check proposed upstream.** Something a senior analyst on your
   team knows, that the shipped checks do not cover, and that would
   hold for most teams.
3. **A report from another agent.** Most install routes are untested
   (see :doc:`how-to/install-in-other-agents`). Say whether it
   loaded and whether the analysis followed the method.
4. **A change to an existing check.** A threshold that is out of date,
   a platform setting that moved, a red flag that fires on normal data.
   Cite the source.

Where to talk
-------------

- **Questions, ideas and results** go to
  `GitHub Discussions <https://github.com/C-Kapsalis/devils-analyst/discussions>`_.
  That includes "I installed it in agent X and here is what happened".
- **Wrong answers and bugs** go to
  `GitHub Issues <https://github.com/C-Kapsalis/devils-analyst/issues>`_.
  For a wrong answer, include the export (remove anything private, or
  simulate a version with the same shape), what it said, what it should
  have said, and the host and model you used. A counterexample is worth
  more to the project than a star.
- **These docs** live in a separate repository,
  `devils-analyst-documentation <https://github.com/C-Kapsalis/devils-analyst-documentation>`_.
  Open issues about the pages there.

Never use a client's or an employer's data, names or dashboards, even
anonymized. Simulate them.

Proposing a check upstream
--------------------------

A rule that only fits your team belongs in your own ``house-rules/``
folder (see :doc:`reference/house-rules`). A rule that would save most
teams money belongs in the shipped checks. To propose one:

1. **Write it with the template.** Fill in ``house-rules/TEMPLATE.md``:
   area, check, where to look, the red flag, why it costs money, the
   fix, the source, and you as owner. Name the reference file it would
   go in (in ``skills/audit/references/``, or
   ``skills/review/references/`` for a report check) and the id it
   would take.
2. **Give it a source.** A platform's documentation, a published study,
   a regulation, or an incident you can describe without naming a
   client or an employer. "Everyone knows" is not a source.
3. **Plant the problem in a benchmark case.** See the next section.
4. **Show it fails without the check.** Run your case in both arms and
   paste the summary. A check the model already passes without the
   plugin is still useful documentation, but it does not need to be in
   the shipped checks.
5. **Open a pull request** with the check row, the case and the run
   summary. Expect questions about the decoy: a check that fires on
   normal data costs more trust than it saves.

Adding a benchmark case
-----------------------

Add a script to ``benchmarks/builder/cases/``, following the cases
around it. The ``bx-*`` scripts are the best model. The script should:

- simulate the exports with a fixed seed (``random.Random(<seed>)``),
  with fictional brands and ``.example`` domains;
- plant the problem your check catches, next to at least one decoy that
  looks similar but is normal;
- compute the true answer in code, and ``assert`` that the naive answer
  differs from it;
- write graders that quote the computed numbers: one that passes when
  the problem is found with evidence, one that fails if the decoy is
  flagged, and one for the decision the problem should change.

Then rebuild every case and check that only yours changed.

bash:

::

    python3 benchmarks/builder/build_all.py
    git status --short benchmarks/cases

PowerShell:

::

    py -X utf8 benchmarks/builder/build_all.py
    git status --short benchmarks/cases

Running the benchmark
---------------------

You need Claude Code with ``claude plugin eval``, and Python 3.9 or
later. To run one case, copy it into its own folder and point
``--eval-dir`` at that folder. To run a whole group, filter by name:
``--case 'bx-*'`` is the breadth group.

bash:

::

    claude plugin eval . --eval-dir benchmarks/cases --scaffold --allow-tools Write --model haiku -j 6 --runs 3 --trust-plugin --no-publish | tee benchmarks/eval.log
    python3 benchmarks/report.py benchmarks/eval.log --no-readme

PowerShell (the case scaffolds are bash scripts, so bash must be on the
path, for example from Git for Windows):

::

    claude plugin eval . --eval-dir benchmarks/cases --scaffold --allow-tools Write --model haiku -j 6 --runs 3 --trust-plugin --no-publish | Tee-Object benchmarks/eval.log
    py -X utf8 benchmarks/report.py benchmarks/eval.log --no-readme

The full run above covers all 110 cases in both arms, and the log
prints the API cost of every run and the total. ``--scaffold`` runs
each case's ``scaffold.sh``, which writes the case's files into the
run's folder; read one before you run it. What the results mean, and
what they do not, is in :doc:`explanation/benchmark`.

Before you open a pull request
------------------------------

- Edit ``AGENTS.md`` or ``adapters/windsurf/devils-analyst.md``, not
  the copies, then run ``python3 scripts/sync-adapters.py``.
- Edit the skills in ``skills/``. The ChatGPT knowledge files and the
  release zips are generated from them.
- Run ``claude plugin validate .``.
- Run the two repository checks (see :doc:`reference/hook-and-scripts`
  for the PowerShell form):

  ::

      python3 scripts/count.py
      python3 scripts/sync-adapters.py --check

- If you change a count the README states, update the README from the
  output of ``count.py``.
- If you change a skill, say whether you re-ran the benchmark, on which
  cases, and paste the summary from ``benchmarks/report.py``.
- Write plainly: short sentences, no em dashes, no hype words.

Disagreeing
-----------

If you think a number in the README or on these pages is wrong, say so
in an issue with the log or the case. The maintainer will try to
reproduce it and update the page either way.

License
-------

By contributing you agree that your contributions are licensed under
the project's MIT License (copyright 2026 Christoforos Kapsalis).

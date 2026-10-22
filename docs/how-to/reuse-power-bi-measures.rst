How to reuse Power BI measures
==============================

Goal: make a dashboard or analysis show the same numbers as your Power
BI report, by reusing the measures your semantic model already defines,
and audit those measures before you rely on them. The
``power-bi-definitions`` skill does this.

Before you start
----------------

- Devil's Analyst is installed. See :doc:`../tutorials/first-argument`
  or :doc:`install-in-other-agents`.
- You have one of these, from best to least:

  .. list-table::
     :header-rows: 1

     * - You have
       - What the skill does
     * - A Power BI MCP server added as a connector (one that can run
         DAX queries against a semantic model)
       - Queries the model's own measures by name.
     * - The model saved as PBIP with the TMDL format, on disk or as a
         zip of the ``.SemanticModel`` folder
       - Reads it with the ``metric_contract.py`` script.
     * - Pasted TMDL, or a list of measures and their DAX
       - Reads it directly.
     * - Only a ``.pbix`` file
       - Asks you to open it in Power BI Desktop and use File > Save as
         > Power BI Project, with the TMDL format.

- For the script: Python 3.9 or later. It uses only the standard
  library and never writes to the model. In Claude on the web it needs
  code execution turned on.
- For a live connector: the semantic model's ID (not its name), and a
  tenant setting enabled by a Fabric admin. The skill asks you for
  both.

Steps
-----

1. **Ask for the model's definitions.** Name the model and what you
   want to build. For example:

   ::

       Use our Power BI definitions in ./Sales.SemanticModel to build a
       monthly paid media dashboard on the warehouse.

   With a PBIP folder, the skill runs ``metric_contract.py``. You can
   run it yourself from a copy of the repository to see the same
   output (replace the model path with yours).

   bash:

   ::

       git clone --branch v0.1.0 https://github.com/C-Kapsalis/devils-analyst.git
       python3 devils-analyst/skills/power-bi-definitions/scripts/metric_contract.py ./Sales.SemanticModel --format markdown

   PowerShell:

   ::

       git clone --branch v0.1.0 https://github.com/C-Kapsalis/devils-analyst.git
       py devils-analyst\skills\power-bi-definitions\scripts\metric_contract.py .\Sales.SemanticModel --format markdown

   The output lists every measure (name, format, description, DAX),
   the tables and their visible columns, the warehouse source behind
   each table when the model has one, and the relationships. Add
   ``--out metric-dictionary.md`` to save it; the skill suggests keeping
   it in your project so later dashboards start from it.

2. **Read the flags.** Before building, the skill shows the measures
   your request needs and flags measures with no description, ratios
   that are not ``DIVIDE`` of two base measures, entity counts taken
   from a dimension instead of the fact table, and two measures that
   look like the same business metric with different DAX.

3. **Read the measure audit.** Each measure you reuse is checked
   against the Power BI checks P1 to P14 (see
   :doc:`../reference/checks`), and compared with the agreed formula
   for that metric, not with its name. The checks that most often
   matter:

   - **P1:** a rate built with ``AVERAGE`` or ``AVERAGEX``, instead of
     ``DIVIDE`` of two sums.
   - **P2:** a snapshot, such as list size or open pipeline, summed over
     days.
   - **P4:** a toggle whose default, when nobody selects anything,
     differs from the agreed definition, such as gross instead of net
     revenue.
   - **P5:** Google and Meta claimed revenue added together and divided
     by spend.
   - **P6:** two measures for one KPI with different filters.

   Each measure is classed as correct, differs but defensible (with the
   reason), or wrong (with the number it produces instead). For a wrong
   measure, the skill shows the model's number next to the corrected
   one and proposes corrected DAX. It changes the model only if you
   approve and the connector can write. The model owner decides.

4. **Query or translate.** With a Power BI MCP connector, the skill
   queries the measures by name in DAX and does not re-implement them.
   Without one, it translates the measures to SQL for your warehouse.
   A measure it cannot translate faithfully is left out, or shown
   labeled "Power BI only". It never ships a near miss under the real
   name.

5. **Reconcile one number.** The skill asks for one number you can see
   in your Power BI report, such as a KPI card, with its filters, and
   computes the same. If they differ, it checks in this order: report
   or page filters, Power Query row filters, refresh timing, the time
   zone of the date column, row-level security, then the translation
   itself. The match, or the difference and its cause, goes at the top
   of the dashboard.

Result
------

A dashboard or analysis whose numbers come from your model's own
definitions, with a list of the measures that passed the audit, the
ones that did not, and one number reconciled against Power BI.

If you maintain the model as PBIP in git
----------------------------------------

The skill also documents four open-source command-line tools by the
same author, for models kept as PBIP or TMDL: ``tmdl-preflight``
(lint and mechanical fixes), ``pbip-model-forge`` (build a model from a
spec), ``tmdl-drift-doctor`` (keep client copies in line with a
template) and ``pbi-plot-styler`` (one style for report charts). They
need a local shell and `uv <https://docs.astral.sh/uv/>`_; they do not
run in Claude on the web. The skill pins them to release ``v1.2.0``.

Check that a tool runs. In bash, use the wrapper the skill ships, from
the folder where you cloned the repository in step 1:

::

    T=devils-analyst/skills/power-bi-definitions/scripts/devils-analyst-tool
    $T tmdl-preflight --version

In PowerShell, without Git Bash or WSL, run the tool through ``uvx``
directly:

::

    uvx --from git+https://github.com/C-Kapsalis/tmdl-preflight@v1.2.0 tmdl-preflight --version

Both print ``tmdl-preflight 1.2.0``. If the wrapper exits with code
127, install uv first.

Then lint the model. Checking is read-only:

bash:

::

    $T tmdl-preflight check ./Sales.SemanticModel

PowerShell:

::

    uvx --from git+https://github.com/C-Kapsalis/tmdl-preflight@v1.2.0 tmdl-preflight check .\Sales.SemanticModel

Exit code 0 means clean, 1 means violations, 2 means a usage error.
``tmdl-preflight fix`` edits files: run it only on a folder under git,
or on a copy, so you can undo it. The tools prove that the files pass
their validators. Opening the model in Power BI Desktop is still your
step.

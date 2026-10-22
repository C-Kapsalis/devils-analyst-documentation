The 16 skills
=============

Devil's Analyst v0.1.0 ships 16 skills, one folder each under
``skills/`` in the repository. ``python3 scripts/count.py`` prints
``skills: 16``.

A skill loads when your message matches its description. In Claude
Code, the session hook also tells the agent to load ``route-question``
first for any analysis of marketing data, then the skill that fits the
job (see :doc:`hook-and-scripts`). In the plugin, skill names carry the
``devils-analyst:`` prefix, for example ``devils-analyst:audit``.

The chain
---------

These skills carry one analysis from the question to the answer, in
this order.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Skill
     - Job
     - When it fires
   * - ``route-question``
     - Reads the house rules, lists the data the agent can reach,
       rewrites the question into one precise request (metric,
       conversion action, account, scope, window, grain, report level,
       attribution window), and decides the route: answer, answer
       partly, reframe, onboard, or decline the method.
     - First, before any other Devil's Analyst skill, for any marketing
       or analytics question that needs data.
   * - ``metric-definitions``
     - Gives each metric its formula, the grain it is valid at and the
       trap that makes it lie, plus tested SQL patterns. Reads the house
       rules first.
     - Before computing any marketing metric (CTR, CPA, CAC, ROAS,
       users, reach, retention, LTV and others), or when someone asks
       how a metric is defined or why two numbers disagree.
   * - ``whats-changed``
     - Fixes the comparison, then splits a change into drivers, into
       mix versus rate, and into contributions by segment, and screens
       out noise.
     - When a number went up or down between two periods and you are
       about to explain why.
   * - ``evidence-check``
     - Checks the evidence: sample ratio, significance and power,
       novelty, control groups, seasonality, regression to the mean,
       Simpson's paradox, confounders, incrementality, pull-forward,
       attribution. Writes a verdict with the deciding number.
     - Before saying something worked, won, caused a result, or should
       be scaled, cut or repeated.
   * - ``diagnose``
     - Turns a real movement into a likely cause, the evidence for and
       against it, the next action and how to verify it, using a funnel
       diagnostic, a brand diagnostic and 59 playbooks.
     - After a dashboard or ``whats-changed`` finds a real movement, or
       when someone asks why performance is down or what to do next.
   * - ``marketing-dashboard``
     - Sets which questions a report answers, which definitions and
       comparisons are correct, how to explain what changed, and how to
       end with what to do. Includes a guide to Claude Dashboards.
     - Before analyzing or reporting on marketing data: performance
       reports, dashboards, campaign or channel reviews, client
       reports.

Checking someone else's work
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Skill
     - Job
     - When it fires
   * - ``review``
     - Recomputes every number it can in a report, deck or dashboard,
       checks definitions, charts, comparisons, causal claims and
       recommendations against 44 numbered checks, leaves correct things
       alone, and ranks findings Must fix, Should fix, Nice to have.
     - When someone hands over a report, deck, dashboard or agency
       write-up and asks whether it is right.
   * - ``audit``
     - Maps a whole setup, runs the numbered checks for each area
       present (185 in 12 areas), estimates the money at stake, ranks
       the findings and ends "Fix N first".
     - When someone wants an account, tracking setup, email program,
       CRM or Power BI model checked, not one report.

Decisions and disciplines
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Skill
     - Job
     - When it fires
   * - ``pricing-promotions``
     - Sets the objective, gets contribution margin right, estimates
       elasticity without promotion bias, computes break-even volume,
       nets out pull-forward, and compares sales channels on
       contribution.
     - Price and discount decisions, and promotion read-outs.
   * - ``brand-health``
     - Measures brand health from the data, separates short-term sales
       from long-term equity, checks per segment, and turns the result
       into a decision with a way to verify it.
     - Questions about the brand rather than one campaign: trackers,
       share of search, price premium, extensions, repositioning.
   * - ``channel-audit``
     - Judges a channel or tactic per campaign, creator tier, keyword
       or segment with break-even math on margin, and labels what
       attribution can and cannot prove.
     - Whether a channel or tactic pays and what to change in it: bids,
       Quality Score, display, influencers, SEO, attribution model
       choice, checkout drop-off.
   * - ``product-decisions``
     - Calibrates purchase intent, turns conjoint results into
       willingness to pay per segment, checks scoring matrices, sizes
       markets both ways, and runs NPV and break-even before a go,
       conditional go or no-go.
     - Survey, concept-test, conjoint or business-case numbers behind a
       decision to build, launch, price or kill.
   * - ``marketing-models``
     - Picks the method (NPV and CLV, elasticity, forecasting,
       regression, chi-square, logit, factor and cluster analysis),
       runs it with exact formulas, checks it, and turns it into a
       decision.
     - Questions that need a model, not just a metric: pricing,
       forecasts, drivers, churn, segmentation, customer value.
   * - ``research-design``
     - Chooses the design, the questionnaire, the sample and the
       inference, and says what the data can and cannot support.
     - Planning, reading or relying on customer or market research:
       surveys, focus groups, sample sizes, response rates.
   * - ``hybrid-research``
     - Decides when synthetic respondents are acceptable, reviews the
       instrument, builds personas and prompts, runs a backward pilot,
       and scores recovery against a human benchmark.
     - Research with an AI in the loop: synthetic panels, AI-drafted
       surveys, AI interviews, interview summaries.
   * - ``power-bi-definitions``
     - Reads a Power BI model's measures, relationships and warehouse
       sources, audits the measures, queries them live or translates
       them to SQL, and reconciles one number against Power BI.
     - When the user has a Power BI model, PBIP, TMDL, ``.pbix`` or a
       list of DAX measures, or a number must match what Power BI
       shows.

What every skill does before handing over
-----------------------------------------

Every skill has an adversary table: for each move, what the
adversary asks, the check that settles it, and what to do if it fails.
Then the draft is scored 0 to 100 on clarity, relevance, depth and
insight, and anything under 80 is revised, at most twice. See
:doc:`../explanation/adversary`.

The answer format
-----------------

Analyses follow one shape, from the repository's ``AGENTS.md``:

::

    Answering: [scope line: source, account, scope, conversion action, window vs comparison, grain]
    House rules applied: [ids, or none found]

    **[The answer, with its number.]**

    1. [Finding] · [number] · likely cause (hypothesis until checked) · action · how to verify
    2. ...

    Checked and fine: [...]
    Not checked: [areas with no data]
    Definitions: [metric: formula, source, grain]

At most three findings, unless it is an audit or a review. Audits and
reviews rank their findings and end with what to fix first.

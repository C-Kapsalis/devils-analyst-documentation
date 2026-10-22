Devil's Analyst
===============

Devil's Analyst is the devil's advocate for your marketing data. It is a
set of 16 Agent Skills and a session hook for Claude Code and other AI
agents. When you ask your agent about marketing numbers, a report or a
decision that rests on them, the skills make it ask the questions a
senior analyst asks before anyone moves budget: is this the right
number, from the right source, at the right grain, and what else would
produce it?

These pages describe release
`v0.1.0 <https://github.com/C-Kapsalis/devils-analyst/releases/tag/v0.1.0>`_.

Who it is for
-------------

Marketers, analysts and agencies who already use Claude, or another
agent, with their marketing data. You do not need to be a statistician.
The skills carry the formulas and tell the agent to run the arithmetic
in code; you bring the question, the goal and the margin.

What it needs
-------------

Data. Devil's Analyst argues with numbers, so the agent has to be able
to reach them:

- connectors or MCP servers for your platforms, such as GA4, Google
  Ads, Meta, Search Console, an email platform, a CRM or Shopify;
- a warehouse connection;
- a Power BI model;
- or exported files (CSV or spreadsheet) attached to the conversation.

Devil's Analyst does not ship a connector of its own. It works with the
ones your agent already has. Without data, it tells you which
connection or export would answer your question, instead of guessing.

What it does
------------

- **Routes the question to the data you have.** It lists what the
  agent can reach, rewrites your question into one precise request
  (platform, account, conversion action, period and comparison, grain,
  attribution window) and says up front what can and cannot be
  answered.
- **Defines every number before computing it.** Rates are ratios of
  summed parts. Users and reach do not add across days. Platform
  revenue does not stack across platforms.
- **Explains what changed** by splitting a move into drivers and into
  mix versus rate, and screens out noise.
- **Checks the evidence** before anything is called a win: sample
  ratio, significance and the confidence interval for A/B tests,
  control groups, seasonality, holdouts, promotion pull-forward.
- **Audits a setup or reviews a report** against 229 numbered checks,
  ranks what it finds, and leaves normal patterns (decoys) alone.
- **Attacks its own answer** before handing it over: every skill ends
  with an adversary table. See :doc:`explanation/adversary`.

What it never does
------------------

- **It never invents numbers.** The skills require every figure to
  come from your data, computed in code. If you see a number that did
  not, report it as a bug. If a check needs data the agent cannot see,
  the answer lists it under "Not checked" rather than calling it
  fine.
- **It does not present a cause as proven** when the data cannot prove
  it. Causes are labeled as hypotheses until tested, and each action
  comes with a way to check next month whether it worked.
- **It does not decide your goal or your margin.** The question and the
  decision belong to you. When either is unclear, the skills tell the
  agent to ask.

Where to start
--------------

- New to Devil's Analyst: :doc:`tutorials/first-argument` installs it in
  Claude Code and shows it working, first with no data and then with a
  small fictional export. It takes about ten minutes.
- Using another agent, or Claude on the web: :doc:`how-to/install-in-other-agents`.
- Common jobs: :doc:`how-to/audit-a-ga4-property`,
  :doc:`how-to/check-an-ab-test` and :doc:`how-to/reuse-power-bi-measures`.
- Exactly what it checks: :doc:`reference/skills`,
  :doc:`reference/checks` and :doc:`reference/house-rules`.
- What it can and cannot show: :doc:`explanation/benchmark`.

Source, issues and discussions are on
`GitHub <https://github.com/C-Kapsalis/devils-analyst>`_. Devil's Analyst
is a personal project of Christoforos Kapsalis, released under the MIT
License. It is not affiliated with, or endorsed by, any employer.

.. toctree::
   :maxdepth: 1
   :caption: Tutorial

   tutorials/first-argument

.. toctree::
   :maxdepth: 1
   :caption: How-to guides

   how-to/install-in-other-agents
   how-to/audit-a-ga4-property
   how-to/check-an-ab-test
   how-to/reuse-power-bi-measures

.. toctree::
   :maxdepth: 1
   :caption: Reference

   reference/skills
   reference/checks
   reference/house-rules
   reference/hook-and-scripts

.. toctree::
   :maxdepth: 1
   :caption: Explanation

   explanation/adversary
   explanation/ab-tests
   explanation/benchmark

.. toctree::
   :maxdepth: 1
   :caption: Project

   contributing

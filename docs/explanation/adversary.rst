Why an adversary for every move
===============================

A current model knows most of the marketing judgment around a number.
Ask it about attribution windows or brand search incrementality and you
get a good answer. What it does not do on its own is apply all of that
judgment the same way every time, across the whole chain from the
question to the recommendation. Devil's Analyst writes the questions
down, so they are asked every time, and so your team can read, change
and extend each one.

Where analyses go wrong
-----------------------

Most wrong answers in marketing analytics are not arithmetic errors.
They come from a step nobody challenged:

- the question asked for something the data cannot say;
- a default was filled in without anyone saying so, such as "all
  conversions" instead of purchases;
- a rate was averaged, daily users were summed into monthly users, or
  two platforms' revenue was added together;
- two periods that are not comparable were compared;
- a cause was named when something else would produce the same number:
  a change in mix, the season, a tracking change, regression to the
  mean;
- platform credit was read as sales the spend added;
- an action was recommended with no way to tell next month whether it
  worked.

A correct number can still support the wrong decision. So the
challenge has to happen at each step, not only at the end.

The adversary table
-------------------

Every skill has a table that pairs each of its moves with the
question an adversary would ask, the check that settles it, and what to
do if the check fails. The compact version in ``AGENTS.md`` covers the
whole chain:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Move
     - The adversary asks
   * - Sources
     - Is there a source I did not look for, such as a Power BI model or
       a second account?
   * - Request
     - Which slot did I fill by default without saying so?
   * - Definition
     - Is any rate averaged, any distinct count summed, any revenue
       stacked?
   * - Comparison
     - Is this a fair period, and is the change outside the noise?
   * - Cause
     - What else would produce this number: mix, seasonality, a tracking
       change, a definition change, regression to the mean?
   * - Claim
     - Is this credit, or proven incremental?
   * - Action
     - If they did only this, how would they know next month that it
       worked?

The checks in the skills' own tables are concrete: "every slot in the
scope line has a value and a reason", "sum of contributions equals the
total change", "credit under two attribution models". A failed check
changes the answer: the agent states the default, recomputes, downgrades
the claim to a hypothesis, or proposes a test instead of a cut.

After the table, the skill scores its draft from 0 to 100 on clarity,
relevance, depth and insight. If any score is under 80, it writes the
question that would raise it, answers it from the data and revises, at
most twice.

Why it also leaves things alone
-------------------------------

An adversary that objects to everything is as useless as one that
objects to nothing. Each audit area lists decoys: patterns that look
wrong and are normal. A brand search click-through rate of 40%, Search
Console clicks above GA4 sessions, and Direct at 15% of sessions are
all expected. A check that fires on a decoy costs the reader's trust,
so the skills flag a pattern only when it costs money or corrupts a
decision, and give a healthy area one "checked and fine" line.

What the adversary cannot do
----------------------------

- **It can only check what it can see.** It can tell you a session
  timeout changed in a settings export. It cannot tell you about a
  change nobody exported. A check without its data is reported as "not
  checked", not as fine.
- **It does not own the question or the decision.** The goal, the
  margin and the targets come from you. When either the question or the
  decision is unclear, the skills tell the agent to ask instead of
  assuming.
- **It is the same agent checking its own draft.** The table makes the
  questions consistent; it does not make the answers infallible. The
  one benchmark run so far did not show a measurable gain in answer
  quality. See :doc:`benchmark`.

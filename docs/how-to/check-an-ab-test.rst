How to check an A/B test result
===============================

Goal: find out whether a test result supports rolling out the variant,
using the ``evidence-check`` skill. The skill runs the A/B checks in
order and stops at the first that fails: sample ratio, significance and
the confidence interval, power, novelty, segments. It ends with a
verdict of supported, not supported or inconclusive, and the number
that decides it.

This page uses a fictional homepage test, so you can check the
arithmetic yourself. :doc:`../explanation/ab-tests` explains why the
checks run in this order.

Before you start
----------------

- Devil's Analyst is installed. See :doc:`../tutorials/first-argument`
  or :doc:`install-in-other-agents`.
- You have, for each arm: users and conversions. The planned split and,
  if you set one, the planned minimum detectable effect (MDE) help too.
- If you have them, lift by week and by new versus returning users let
  the skill check for a novelty effect. Without them, that check is
  reported as not checked.

Steps
-----

1. Make a folder with the test setup and the results. These two files
   are fictional.

   bash:

   ::

       mkdir hero-test
       cd hero-test
       cat > experiment_config.json <<'EOF'
       {"test": "homepage hero", "planned_split": {"control": 0.5, "variant": 0.5},
        "alpha": 0.05, "baseline_conversion_rate": 0.03,
        "planned_mde_absolute": 0.005}
       EOF
       cat > ab_results.csv <<'EOF'
       variant,users,conversions
       control,20000,600
       variant,19850,680
       EOF

   PowerShell:

   ::

       mkdir hero-test
       cd hero-test
       @'
       {"test": "homepage hero", "planned_split": {"control": 0.5, "variant": 0.5},
        "alpha": 0.05, "baseline_conversion_rate": 0.03,
        "planned_mde_absolute": 0.005}
       '@ | Set-Content -Path experiment_config.json -Encoding ascii
       @'
       variant,users,conversions
       control,20000,600
       variant,19850,680
       '@ | Set-Content -Path ab_results.csv -Encoding ascii

2. Start your agent in that folder (in Claude Code, run ``claude``) and
   ask:

   ::

       Did the new homepage hero win? Should we roll it out?
       The setup is in experiment_config.json and the results are in ab_results.csv.

3. Check the arithmetic in the answer. The skill computes each check in
   code and keeps a short table of it in the report. For these files,
   the formulas in the skill give:

   .. list-table::
      :header-rows: 1

      * - Check
        - Result
        - What it means
      * - Sample ratio (chi-square against 50/50)
        - 0.56
        - Below 10.8, so the split is as planned. Go on.
      * - Conversion rate
        - control 3.00%, variant 3.43%
        - A lift of 0.43 points, or 14% relative.
      * - Significance (two-proportion z-test)
        - z = 2.41, p = 0.016
        - Below the planned alpha of 0.05.
      * - 95% confidence interval of the difference
        - 0.08 to 0.77 points
        - It excludes zero, so the lift is real at that confidence.
      * - Against the planned MDE
        - 0.43 points against 0.5 planned
        - Significant, but smaller than the effect the test was sized
          for, so likely overstated.

4. Read the verdict. The skill writes it in four lines: the verdict and
   the claim, the deciding number, what the naive read says and why it
   is wrong, and what to do next. For this test, look for:

   - the lift reported with its p-value and its interval, not as "14%"
     alone;
   - a caution that the true lift may be well below 0.43 points, and
     any revenue projection based on the low end of the interval
     (0.08 points), not the point estimate;
   - novelty and segments listed as not checked, because the files
     have no weekly or new versus returning split.

5. See the first check stop the test. Change the variant's users from
   19850 to 18900 in ``ab_results.csv`` and ask again. The chi-square
   for the split becomes 31.1, above 10.8. The skill stops there: the
   assignment or the logging is broken, so the result cannot be
   trusted, whatever its p-value. The verdict should say to find the
   cause before reading the outcome.

Result
------

You have a verdict with the number that decides it, and you can redo
every step of the arithmetic from the table in the answer.

If the change costs money to run, such as a discount or a paid tool,
say so in your question and give the cost. The ``audit`` skill's
experiment checks flag a lift that is tested against zero when the
change has a cost; the lift has to beat the break-even lift, not zero.

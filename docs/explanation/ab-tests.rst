How A/B tests are judged
========================

The ``evidence-check`` skill judges a finished A/B test in a fixed
order and stops at the first check that fails. This page explains the
order and the three ideas people most often mix up: the p-value with
its interval, the minimum detectable effect, and the winner's curse. To
run the checks on your own test, see :doc:`../how-to/check-an-ab-test`.

The order
---------

1. **Sample ratio.** Did each arm get the share of users it was
   planned to get?
2. **Significance.** Is the difference larger than chance would
   produce, and what range of effects does the data allow?
3. **Power.** Was the test big enough to find the effect that matters?
4. **Novelty.** Does the lift last, or does it fade after the first
   weeks?
5. **Segments.** Does the winner hold within the main segments?

The order matters because each check can make the later ones
meaningless. A test whose split is broken cannot be rescued by a good
p-value.

Sample ratio first
------------------

If a test was planned 50/50 and one arm got noticeably fewer users,
something in the assignment or the logging is broken. Whatever broke it
may also be what made one arm convert better.

The skill compares the observed users per arm with the planned split
using a chi-square test. For two arms, a value above 10.8 means the
chance of a split that uneven by accident is under 0.1%. Then the test
is reported as untrustworthy, and the cause has to be found before the
outcome is read.

The p-value and the interval
----------------------------

For conversions per user, the skill runs a two-proportion z-test and
reports two numbers with the lift: the p-value and the 95% confidence
interval of the difference. The lift on its own is not reported.

The p-value says how surprising the result would be if there were no
real difference. The interval says which effects are consistent with
the data. Together they decide the verdict:

- **Significant** (the p-value is below the planned threshold and the
  interval excludes zero): the effect is real at that confidence.
- **Not significant:** inconclusive. It becomes "no effect large enough
  to matter" only when the interval is narrow enough to rule out every
  effect that would matter to the business. The skill never says "no
  effect" on its own, because a small test can miss a real effect.

The minimum detectable effect is for planning
---------------------------------------------

The minimum detectable effect (MDE) is the smallest effect a test of a
given size would reliably detect. It is set before the test, to decide
how many users the test needs. The skill uses it for two things:

- to say whether the test was big enough to find the effect that
  matters;
- for an inconclusive test, to say how many users a real answer would
  need.

The MDE is not a pass mark for the result. A finished test is judged on
its p-value and its interval. A significant lift smaller than the
planned MDE is still significant.

The winner's curse
------------------

A significant lift smaller than the planned MDE is still real, but it
is probably smaller than it looks. When a test is too small for the
effect it found, the results that happen to clear the significance bar
are the ones where chance pushed the estimate up. This is the winner's
curse: among small tests, the winners overstate their effect.

So the skill reports such a result with its interval and a caution, and
projects revenue from the low end of the interval, not from the point
estimate. A forecast built on the point estimate of a barely
significant test tends to disappoint.

Novelty and segments
--------------------

- **Novelty.** A new design can win at first because it is new,
  especially with returning users who notice the change. The skill
  splits the lift by week and by new versus returning users. If the lift
  sits in the first weeks and in returning users and then fades, it
  judges the test on the last stable weeks only.
- **Segments.** A winner should hold within the main segments, such as
  device and new versus returning. Cut a result enough ways and one cut
  will look significant by chance, so a single significant segment out
  of many is not reported as a finding.

The verdict
-----------

The skill writes the verdict as supported, not supported or
inconclusive, with the number that decides it, what the naive read says
and why it is wrong, and what to do next. The arithmetic stays in the
report as a short table, so you can redo it.

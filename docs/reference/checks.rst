The numbered checks
===================

Devil's Analyst v0.1.0 holds 229 numbered checks: 185 audit checks in
12 areas, used by the ``audit`` skill, and 44 review checks, used by the
``review`` skill. The counts on this page are what
``python3 scripts/count.py`` prints. It counts the rows of the check
tables whose first cell is an id such as GA1, U4 or PS12.

Each check is one row of a table in a reference file, so you can read,
change or extend every one, and a finding can name the check that
produced it.

Audit checks
------------

Each audit check has five columns: where to look (a column, a setting,
a report), the red flag, why it costs money, the fix, and a tier for
urgency. Each area's file also lists decoys: patterns that look wrong
but are normal, which the audit leaves alone.

.. list-table::
   :header-rows: 1
   :widths: 30 25 15 30

   * - Area
     - Ids
     - Checks
     - File in ``skills/audit/references/``
   * - Attribution and incrementality
     - A1 to A13
     - 13
     - ``attribution.md``
   * - CRM lifecycle, retention and CLV
     - C1 to C17
     - 17
     - ``crm-lifecycle.md``
   * - Dashboards and reports in use
     - D1 to D14
     - 14
     - ``dashboards.md``
   * - E-commerce and backend revenue against platforms
     - R1 to R10
     - 10
     - ``ecommerce-revenue.md``
   * - Email program and deliverability
     - E1 to E18
     - 18
     - ``email.md``
   * - Experiments and lift studies
     - X1 to X16
     - 16
     - ``experiments.md``
   * - GA4 setup and UTMs
     - GA1 to GA12, U1 to U8
     - 20
     - ``ga4-utm.md``
   * - Meta and other paid social
     - M1 to M11
     - 11
     - ``meta.md``
   * - Paid search (Google Ads, Microsoft Ads)
     - PS1 to PS20
     - 20
     - ``paid-search.md``
   * - Performance Max, Demand Gen, display and video
     - PM1 to PM5, DV1 to DV9
     - 14
     - ``pmax.md``
   * - Power BI models (TMDL, PBIP, a list of DAX measures)
     - P1 to P14
     - 14
     - ``power-bi.md``
   * - Search Console and SEO
     - S1 to S18
     - 18
     - ``search-console.md``

The tiers decide the order of an audit's findings:

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Tier
     - What
     - Group
   * - 1. Measurement integrity
     - Anything that makes later numbers fiction, such as a conversion
       action that mixes sign-ups with sales.
     - Must fix
   * - 2. Hygiene
     - Leaks that waste money every day, such as search-term waste.
     - Must fix if large, else Should fix
   * - 3. Money left on the table
     - Profitable lines starved, such as a budget-capped campaign that
       beats target.
     - Should fix
   * - 4. Fine-tuning
     - Adjustments to a setup that is already right.
     - Nice to have
   * - 5. Causal claims
     - Credit sold as incremental with no test.
     - Should fix, written as "test this"

A tier 1 finding outranks a bigger tier 3 finding, and no performance
is judged on a metric that a tier 1 finding has broken.

Review checks
-------------

The review checklist is in
``skills/review/references/review-checklist.md``. Each check has the
claim that is often wrong, how to spot it, the fix and a default
severity (Must, Should or Nice), which the review raises when the claim
sits in the headline and lowers when it sits in a side table.

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Section
     - Ids
     - Example
   * - A. Numbers and aggregation
     - A1 to A7
     - A ratio rolled up as the average of row ratios.
   * - B. Definitions
     - B1 to B8
     - "Conversions" that are not sales.
   * - C. Comparisons
     - C1 to C7
     - A Search Console "crash" in the last two to three days.
   * - D. Causal claims and tests
     - D1 to D12
     - Attribution credit stated as cause.
   * - E. Actions
     - E1 to E7
     - An action with no way to verify it.
   * - F. The "why" section
     - F1 to F3
     - A "why" written as prose, not computed.

The review ids reuse some letters of the audit ids: review A1 is not
attribution A1. When you cite a check, name the file or the skill with
the id.

Other checks without ids
------------------------

The other skills carry their judgment as worked formulas and adversary
questions rather than numbered rows. Two examples from the repository's
README:

- Pricing: "Is 60% a margin or a markup?", rebuilt from cost lines
  before any break-even.
- Research: sample size scales with 1/E², so halving the margin of
  error needs four times the sample.

``diagnose`` adds 59 playbooks, in
``skills/diagnose/references/playbooks/``, across email, paid search,
Performance Max, SEO, GA4, paid and organic social, customer analytics,
attribution, AI search and product.

To add your own checks, or change a shipped one for your team, see
:doc:`house-rules`.

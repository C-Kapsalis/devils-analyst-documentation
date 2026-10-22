House rules
===========

House rules are what your team knows about its own data that no shipped
check can know: that your revenue of record is finance net revenue,
that campaigns starting ``BR_`` are brand, that your payment page lives
on another domain. You write them down, one rule per file, and the
skills read them before anything else.

Where they live
---------------

A ``house-rules/`` folder at the root of the project or workspace the
agent works in. ``route-question`` and ``metric-definitions`` read
every ``.md`` file in it, except ``README.md``, ``TEMPLATE.md`` and
anything under ``examples/``.

In a chat without files, such as Claude on the web or ChatGPT, add the
rule files to the project's knowledge or paste them into the message.

The plugin's own ``house-rules/`` folder holds only a README, the
template and two fictional examples. Nothing in it is applied to your
data. ``npx skills add`` does not copy it; take the template from the
`repository
<https://github.com/C-Kapsalis/devils-analyst/blob/v0.1.0/house-rules/TEMPLATE.md>`_.

The file format
---------------

Save each rule as ``house-rules/HR-<number>-<short-name>.md``. The
frontmatter has these fields:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Meaning
   * - ``id``
     - Unique within your rules, for example ``HR-014``. Findings cite
       it.
   * - ``area``
     - One of ``paid-search``, ``pmax``, ``meta``, ``ga4-utm``,
       ``search-console``, ``email``, ``crm-lifecycle``,
       ``ecommerce-revenue``, ``experiments``, ``attribution``,
       ``dashboards``, ``power-bi``, or a new area your team uses.
   * - ``overrides``
     - The shipped check or definition this rule replaces, as
       ``<file>:<check id>`` (for example ``audit/ga4-utm:GA2`` or
       ``metric-definitions/catalog:ROAS``), or ``none`` for a new
       check.
   * - ``check``
     - One sentence that says what to check.
   * - ``where_to_look``
     - The column, setting or report, with its exact name.
   * - ``red_flag``
     - The threshold that makes it a finding, as a number or a
       condition two analysts would agree on.
   * - ``why_it_costs_money``
     - What goes wrong in a decision, a budget or a report if nobody
       checks.
   * - ``fix``
     - What to do when the red flag shows, and how to verify the fix.
   * - ``source``
     - Where it comes from: an incident, a platform document, a finance
       policy.
   * - ``owner``
     - Who answers questions about the rule.
   * - ``date``
     - When it was last confirmed true, as ``YYYY-MM-DD``.

Below the frontmatter you can add two or three sentences of context,
the query that tests the red flag, or the incident behind the rule.

Precedence
----------

Highest first:

1. What you say in the conversation.
2. Your house rules.
3. Your governed definitions: a Power BI model, a metric dictionary.
4. The shipped defaults: the skills, their checks and catalogs.

A house rule replaces the shipped check or definition it names in
``overrides``, and any default it contradicts. It cannot make false
arithmetic true. If a rule seems to require averaging rates or summing
daily users, the agent reports the rule's number, shows the correct
number next to it and says why they differ.

How they show up in answers
---------------------------

- The answer lists the rules it applied, under "House rules applied".
- A finding or scope line that a rule changed cites the rule's id, for
  example "per HR-003, revenue is finance net revenue".
- A rule older than its review date, or one that names a column or
  setting that no longer exists, is flagged to its owner, not applied.

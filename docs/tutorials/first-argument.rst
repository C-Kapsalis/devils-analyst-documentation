Tutorial: your first argument with the data
===========================================

In this tutorial you install Devil's Analyst in Claude Code and ask it
one question twice: once with no data connected, and once with a small
fictional ad export. You will see it refuse to guess, then find out
what really moved the number. It takes about ten minutes.

You need Claude Code. Nothing else: no connectors, no Python, no
account with an ad platform. The export in step 4 is fictional.

1. Install the plugin
---------------------

In Claude Code, add the Devil's Analyst marketplace:

::

    /plugin marketplace add C-Kapsalis/devils-analyst

Then install the plugin from it:

::

    /plugin install devils-analyst@devils-analyst

This installs 16 skills and a session hook. The Code tab of the Claude
Desktop app takes the same two commands.

2. Check that it loaded
-----------------------

Start a new session, so the session hook runs, and ask:

::

    Is Devil's Analyst active?

The hook adds a routing table and seven core rules to the start of
every session, so the agent can answer from them. You do not need to
call a skill by name after this. Ask the way you normally would, and
the matching skill loads, starting with ``route-question``.

3. Ask with no data connected
-----------------------------

Still with no connectors and no files, send:

::

    Our ROAS dropped 30% last week, what happened?

The wording differs from run to run, but the ``route-question`` skill
sets what should happen:

- **It looks for data first.** It lists what it can reach: connector
  or MCP tools, a database, a Power BI model, attached files. Here,
  there is nothing.
- **It maps the question to what it needs.** ROAS needs spend and
  revenue, so it needs your ad platforms and a revenue source.
- **It asks for the data instead of answering.** With no source at
  all, the skill's route is "onboard": say what is connected, and
  which connection or export would answer the question.
- **Anything it says about causes is a hypothesis.** If it mentions
  likely suspects, such as a tracking change, a shift in where the
  budget went, or conversions that have not arrived yet, each one
  should be labeled as a hypothesis, not as the answer.

What should not happen: a confident explanation of why ROAS fell, or
any number you did not give it.

4. Give it a small export
-------------------------

Now give it data. Make a new folder, and save this fictional weekly ad
export in it as ``ads_weekly.csv``.

bash:

::

    mkdir roas-tutorial
    cd roas-tutorial
    cat > ads_weekly.csv <<'EOF'
    week_start,platform,campaign,spend,clicks,purchases,purchase_value
    2026-10-05,Google Ads,Brand Search,800,1600,96,9600
    2026-10-05,Google Ads,Generic Search,2000,2500,50,5000
    2026-10-05,Meta,Prospecting,1200,3000,30,3000
    2026-10-12,Google Ads,Brand Search,800,1580,94,9400
    2026-10-12,Google Ads,Generic Search,2000,2480,50,5000
    2026-10-12,Meta,Prospecting,10000,25000,250,25000
    EOF

PowerShell:

::

    mkdir roas-tutorial
    cd roas-tutorial
    @'
    week_start,platform,campaign,spend,clicks,purchases,purchase_value
    2026-10-05,Google Ads,Brand Search,800,1600,96,9600
    2026-10-05,Google Ads,Generic Search,2000,2500,50,5000
    2026-10-05,Meta,Prospecting,1200,3000,30,3000
    2026-10-12,Google Ads,Brand Search,800,1580,94,9400
    2026-10-12,Google Ads,Generic Search,2000,2480,50,5000
    2026-10-12,Meta,Prospecting,10000,25000,250,25000
    '@ | Set-Content -Path ads_weekly.csv -Encoding ascii

Start Claude Code in that folder (run ``claude``) and send:

::

    Our ROAS dropped 30% last week, what happened? The export is ads_weekly.csv.

5. Read what comes back
-----------------------

Before reading the answer, here is the arithmetic, so you can check it.
ROAS is purchase value divided by spend, both summed first:

.. list-table::
   :header-rows: 1

   * - Week starting
     - Spend
     - Purchase value
     - ROAS
   * - 5 October
     - 4,000
     - 17,600
     - 4.40
   * - 12 October
     - 12,800
     - 39,400
     - 3.08

That is a 30% drop. Now each campaign on its own: Brand Search went
from 12.00 to 11.75, Generic Search stayed at 2.50, and Prospecting
stayed at 2.50. No campaign got much worse. What changed is where the
money went: Prospecting spend rose from 1,200 to 10,000, and
Prospecting returns less per unit of spend than Brand Search. The
blended ROAS fell because of mix, not because any campaign got worse.

The answer follows the output format the skills set. Look for these
parts:

- **A scope line** starting "Answering:", naming the source, the
  periods compared (the week of 12 October against the week of
  5 October), the grain and any default it filled in. The export has no
  attribution window column, so that slot should be stated as an
  assumption, or asked about.
- **The answer first, with its number.** ROAS fell from 4.40 to 3.08.
- **A split into mix and rate.** The ``whats-changed`` skill splits a
  change in a ratio into mix (volume moved between campaigns) and rate
  (results changed inside a campaign). Here, mix should carry almost
  all of the drop.
- **At most three findings**, each with a number, a likely cause
  labeled as a hypothesis, an action, and how to check next month
  whether the action worked.
- **Platform claims labeled as claims.** Purchase value here is what
  Google Ads and Meta each report. The skills treat platform revenue
  as a claim that does not add up across platforms, and the export has
  no store revenue to check it against.
- **"Not checked"** for what the export cannot show, such as store
  revenue, whether the extra Prospecting spend added sales that would
  not have happened anyway, and whether last week's conversions are
  complete. Ad platforms keep adding conversions for days after a
  click, so a week that only just ended can look worse than it will.

If the answer blames a campaign's performance, an algorithm change or
creative fatigue as fact, without a number behind it, that is a miss.
Please report it (see :doc:`../contributing`).

Where to go next
----------------

- Install it in Claude on the web, ChatGPT, Codex, OpenCode or another
  agent: :doc:`../how-to/install-in-other-agents`
- Audit a whole setup instead of one number:
  :doc:`../how-to/audit-a-ga4-property`
- Check whether a test really won: :doc:`../how-to/check-an-ab-test`
- Teach it your team's own rules, such as which revenue is the revenue
  of record: :doc:`../reference/house-rules`
- Why every step gets an adversary: :doc:`../explanation/adversary`

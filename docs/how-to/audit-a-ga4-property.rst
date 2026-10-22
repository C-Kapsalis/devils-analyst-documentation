How to audit a GA4 property
===========================

Goal: get a ranked list of what is wrong in a GA4 setup and its UTM
tagging, with the one thing to fix first. The ``audit`` skill does
this with the 20 GA4 and UTM checks (GA1 to GA12, U1 to U8) listed in
:doc:`../reference/checks`.

Before you start
----------------

- Devil's Analyst is installed. See :doc:`../tutorials/first-argument`
  or :doc:`install-in-other-agents`.
- The agent can read your GA4 data, through a GA4 connector or MCP
  server, or as exported files attached to the conversation. An audit
  can only check what it can see. These are the main inputs, and the
  checks that read them:

  .. list-table::
     :header-rows: 1

     * - What to give it
       - Checks that use it
     * - Admin data settings, including data retention
       - GA1
     * - The reporting attribution model, and each key event with its
         conversion count for the last 30 days
       - GA2, GA3, GA4
     * - Engagement rate by day, and the dates key events changed
       - GA5
     * - Enhanced measurement settings and e-commerce funnel events
       - GA6, GA7, GA8
     * - Traffic acquisition and revenue by session source, medium and
         campaign, and your campaign calendar
       - GA9, GA10, U1, U2, U7
     * - Campaign names in your ad platforms, display spend by week,
         and how you tag social, partner and QR code links
       - U3 to U6
     * - AI assistant referral sources
       - U8

- You know your business goal (for example, online purchases) and,
  if possible, your gross margin and your store's own revenue figure.
  The skill asks for any that are missing, then states the assumption
  it used.

Steps
-----

1. In a session with the data available, ask for the audit, and give
   the goal and margin in the same message. For example:

   ::

       Audit our GA4 setup and UTM tagging and tell me what to fix first.
       Our goal is online purchases. Gross margin is about 40%.

   If you attached files, name them in the message.

2. Check the map at the top of the answer. Before any check, the
   ``audit`` skill writes five to eight lines: the sources it found,
   the period covered, spend by channel, the goals, the margin used,
   the revenue it treats as true, and what is missing. If a source or a
   goal is wrong here, correct it now; every finding after it depends
   on the map.

3. Read the findings in order. They come in three groups: **Must
   fix**, **Should fix** and **Nice to have**. Each finding gives what
   the setup does now, why it is wrong (with the computation), the fix,
   and what skipping it costs. Problems that make later numbers wrong,
   such as GA4 silently falling back to last-click attribution, come
   first, ahead of bigger findings from a lower tier. The audit
   lists at most 15 findings and says how many smaller ones it left
   out.

4. Hold each finding to the skill's own rule: no number and no concrete
   case, no finding. A finding should quote a figure from your export
   and name the event, campaign or setting. If one does not, ask:

   ::

       Which rows in the export show finding 3, and what is the number?

5. Check that normal patterns were left alone. These are decoys in GA4
   and should not appear as problems: Direct traffic stable at 10 to
   25% of sessions, ``(not set)`` under about 1%, and GA4 sessions a
   few percent below ad clicks. A healthy area gets one line under
   "Checked and fine".

6. Read the last two lines. "Not checked" lists areas the audit had no
   data for; they are unknown, not fine. The last line names the first
   fix and why, for example "Fix 1 first: ...".

Result
------

You have a ranked list of fixes, each tied to a check id and a number
from your data, and one named first fix.

If a finding depends on something only your team knows, such as a
payment page on another domain that shows up as a referral, write it
down as a house rule so the next audit applies it. See
:doc:`../reference/house-rules`.

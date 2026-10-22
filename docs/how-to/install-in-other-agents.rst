How to install Devil's Analyst in other agents
==============================================

Goal: get the Devil's Analyst skills into the agent you use. For Claude
Code, follow :doc:`../tutorials/first-argument` instead; it uses the
plugin marketplace.

The skills follow the open `Agent Skills <https://agentskills.io>`_
format: one folder per skill, each with a ``SKILL.md`` file and a
``references/`` folder. Every method on this page puts those folders,
or a rules file built from the same method, where your agent looks for
them.

Wherever you install it, the agent needs data to argue with:
connectors or MCP servers for your platforms, a warehouse connection,
a Power BI model, or exported files.

What has been tested
--------------------

.. list-table::
   :header-rows: 1

   * - Install
     - Status for v0.1.0
   * - Claude Code, through the plugin marketplace
     - Tested: installs 16 skills and a session hook.
   * - ``npx skills add`` into OpenCode and Codex
     - Tested: installs the 16 skills.
   * - Zip upload to Claude (web and Desktop chat)
     - Not tested. The zip structure was checked.
   * - ChatGPT (skills, plugin, custom GPT or Project)
     - Not tested.
   * - Codex and GitHub Copilot CLI plugin commands
     - Not tested.
   * - Gemini CLI, Copilot Chat, Cursor, Windsurf, Cline, Kiro,
       OpenClaw and other agents
     - Not tested.

The untested routes copy the file formats of a working multi-agent
plugin, but nobody has confirmed them with Devil's Analyst yet. If you
try one, please open an
`issue <https://github.com/C-Kapsalis/devils-analyst/issues>`_ with the
agent, its version and what happened, working or not.

Any agent that supports Agent Skills, with npx
----------------------------------------------

This needs `Node.js <https://nodejs.org>`_, which provides ``npx``. The
command is the same in bash and PowerShell. Run it from the project you
want the skills in:

::

    npx skills add C-Kapsalis/devils-analyst

It installs the 16 skills into the agents you choose. It does not
install the session hook, so nothing loads the routing table at the
start of a session. Name the job in your message instead: "audit our
GA4 setup", "is this report right?", "did version B win?".

It also does not copy the house rules template. To use house rules,
see :doc:`../reference/house-rules`.

Claude on the web and Desktop chat
----------------------------------

First turn on code execution and file creation in Settings
(Capabilities, in the versions seen so far). Skills do not run without
it. Then pick one of three routes. Menu labels change between app
versions; if one does not match, look for the nearest equivalent.

**a. Add the marketplace.** In Customize > Plugins, choose Add
marketplace, enter ``C-Kapsalis/devils-analyst``, then install
``devils-analyst``.

**b. Upload the plugin.** Download ``devils-analyst-plugin.zip`` from
the `v0.1.0 release
<https://github.com/C-Kapsalis/devils-analyst/releases/tag/v0.1.0>`_
and upload it in Customize > Plugins.

**c. Upload single skills.** Download ``devils-analyst-skills.zip``
from the same release. It holds one zip per skill, such as
``devils-analyst-route-question.zip`` and
``devils-analyst-audit.zip``. Upload the ones you need in Customize >
Skills.

Skills hand work to each other by name, and one reads another's files,
so upload these together:

.. list-table::
   :header-rows: 1

   * - If you upload
     - Also upload
     - Why
   * - any skill
     - ``route-question`` and ``metric-definitions``
     - Every analysis starts with routing and definitions.
   * - ``audit``
     - ``review``
     - The audit's dashboard checks use the review skill's chart
       checks.
   * - ``power-bi-definitions``
     - ``marketing-dashboard``
     - It hands the translated metrics to ``marketing-dashboard`` to
       build the dashboard.

In the single-skill zips each skill is renamed
``devils-analyst-<skill>``, so the relative links between skills do not
resolve; the skill names still do. If you want every cross-reference to
work, use route a or b. The single-skill zips also carry a shorter
description (under 200 characters) than the plugin does, because
Claude's skill upload documents a 200-character limit.

The session hook does not run in chat. Name the job in your message.
For house rules, add your rule files to the project's knowledge or
paste them into the message.

ChatGPT
-------

None of these routes has been tested.

- **Skills.** Open Plugins in the sidebar, then the Skills tab, and
  upload single-skill zips from ``devils-analyst-skills.zip``, starting
  with ``route-question`` and ``metric-definitions``. ChatGPT may scan
  an uploaded skill and mark it "Needs Review". On Enterprise and Edu,
  an admin has to allow skill uploads.
- **Plugin.** ``devils-analyst-chatgpt.zip`` from the release is a
  package for the ChatGPT Plugin Directory: a ``plugin.json`` and the
  skills, with no hooks.
- **Custom GPT or Project.** Use the instructions and the ten knowledge
  files in the repository's
  `adapters/chatgpt/ <https://github.com/C-Kapsalis/devils-analyst/tree/v0.1.0/adapters/chatgpt>`_
  folder. The repository's
  `INSTALL.md <https://github.com/C-Kapsalis/devils-analyst/blob/v0.1.0/INSTALL.md>`_
  has the steps, including which files to add on a free plan, which
  allows five per project.

Codex, GitHub Copilot CLI and Gemini CLI
----------------------------------------

These install the plugin through each agent's own command. The
commands are the same in bash and PowerShell.

Codex:

::

    codex plugin marketplace add C-Kapsalis/devils-analyst
    codex plugin add devils-analyst@devils-analyst

Then run ``codex``, open ``/hooks``, review and trust the session hook,
and start a new thread.

GitHub Copilot CLI:

::

    copilot plugin marketplace add C-Kapsalis/devils-analyst
    copilot plugin install devils-analyst@devils-analyst

This loads the skills and the session hook. There is no slash command
for Copilot CLI, so name the job in your message.

Gemini CLI:

::

    gemini extensions install https://github.com/C-Kapsalis/devils-analyst

This loads ``AGENTS.md`` as always-on context and adds a
``/devils-analyst`` command.

Agents that read a rules file
-----------------------------

These agents read one rules file, a compact version of the method,
rather than the skills. Get a copy of the repository at the release
tag first. The command is the same in bash and PowerShell:

::

    git clone --branch v0.1.0 https://github.com/C-Kapsalis/devils-analyst.git

Then copy the file for your agent into your own project:

.. list-table::
   :header-rows: 1

   * - Agent
     - Copy this file from the repository
     - To
   * - GitHub Copilot Chat
     - ``.github/copilot-instructions.md``
     - the same path in your repository
   * - OpenCode
     - ``AGENTS.md``, and ``.opencode/command/`` for the
       ``/devils-analyst`` command
     - your project root, and ``.opencode/command/``
   * - Cursor
     - ``.cursor/rules/devils-analyst.mdc``
     - ``.cursor/rules/``
   * - Windsurf
     - ``.windsurf/rules/devils-analyst.md``
     - ``.windsurf/rules/``
   * - Cline
     - ``.clinerules/devils-analyst.md``
     - ``.clinerules/``
   * - Kiro
     - ``.kiro/steering/devils-analyst.md``
     - ``~/.kiro/steering/`` for every project, or ``.kiro/steering/``
       for one
   * - OpenClaw
     - ``.openclaw/skills/devils-analyst/``
     - ``~/.openclaw/skills/``
   * - Any other agent
     - ``AGENTS.md``
     - the agent's rules or instructions file

Windsurf caps a rule file at 6,000 characters, so its file is a shorter
version of ``AGENTS.md`` that points to the full skills.

Build the zips yourself
-----------------------

The release zips are built by ``scripts/package.sh``, which a workflow
runs on every ``v*`` tag. To build them from your own copy, run it from
the repository folder. It writes ``dist/`` and needs ``sh`` and
``zip``.

bash:

::

    sh scripts/package.sh

PowerShell (runs the script under WSL):

::

    wsl sh scripts/package.sh

Uninstall
---------

.. list-table::
   :header-rows: 1

   * - Host
     - How
   * - Claude Code
     - ``/plugin remove devils-analyst``
   * - Claude (web, Desktop chat)
     - Customize > Plugins or Customize > Skills, then remove
   * - ChatGPT
     - Remove the skills, the GPT or the project
   * - Codex
     - ``codex plugin remove devils-analyst``
   * - Copilot CLI
     - ``copilot plugin uninstall devils-analyst``
   * - Gemini CLI
     - ``gemini extensions uninstall devils-analyst``
   * - ``npx skills add``, or a copied rules file
     - Delete the installed skill folders or the copied file

Devil's Analyst writes no state outside its own folder, except the
reports you ask it to save.

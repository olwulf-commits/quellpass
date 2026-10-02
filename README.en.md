# QuellPass

[TextPass & QuellPass — Olaf Wulf](https://olwulf-commits.github.io/)

[Deutsch](README.md) · English

QuellPass, developed by Olaf Wulf, researches verifiable questions using an **independent counter-question**, checks against original sources, and an **evidence record**. In the usual article workflow, QuellPass follows an ordinary preliminary search and an article drafted with TextPass: it checks the article’s claims against original sources. If QuellPass is explicitly commissioned before writing, a research report or later article can follow its **evidence review gate**. The plugin is independent of any particular model or search provider.

My goal is to improve the quality of texts significantly using relatively simple methods. After the initial search, TextPass writes the article; QuellPass then checks its claims and sources. Unsupported passages are corrected before a final review of the whole article’s language and structure. People can follow, question, and correct both processes. How well they work in practice has to be demonstrated through actual texts.

I see evaluation as working with what is already there: identifying what holds up, where claims need better evidence, and using those findings to guide further work. “Evaluate” means to assess; the word comes through French from Latin [*valere*](https://www.etymonline.com/word/evaluation), meaning “to be worth.” The German term *evaluieren* means [to assess](https://www.duden.de/rechtschreibung/evaluieren). In formative evaluation, findings inform improvements. QuellPass makes gaps in the evidence visible and helps ground claims in better-supported sources.

This repository contains the **general edition** for Codex, Cursor, Claude Code, and Grok Build. Hermes Agent can also load it as an external skill source. All four use the same [skill](plugins/quellpass/skills/quellpass/SKILL.md) and [research and writing protocol](plugins/quellpass/skills/quellpass/references/protokoll.md). Project-specific integrations are not included.

## Installation and requirements

Codex finds the catalog at `.agents/plugins/marketplace.json`. Cursor can read the portable plugin; `.cursor-plugin/marketplace.json` is also provided for repository import. Claude Code finds its catalog at `.claude-plugin/marketplace.json`. Add the public repository in Claude Code with `claude plugin marketplace add olwulf-commits/quellpass`, then install with `claude plugin install quellpass@quellpass`. This public edition is version 0.3.3. The preceding 0.3.1 edition was installed locally in Codex and checked against the source files; a practical run of 0.3.3 is still pending. The Claude installation route has not been tested here.

For Grok Build, `.grok-plugin/marketplace.json` provides a public repository catalog. After the GitHub update, add it with `grok plugin marketplace add olwulf-commits/quellpass`; the skill becomes active only after a separate install. This catalog has not yet been tested in Grok Build and is not an official xAI directory listing.

To use Hermes Agent, clone this repository and add the absolute path of `plugins/quellpass/skills` inside the clone under `skills.external_dirs` in `~/.hermes/config.yaml`. The complete clone keeps the references at their relative paths. Hermes supports [Grok as a model provider](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md); this does not amount to a Grok Build or grok.com listing. The public 0.3.3 edition has not been tested in Hermes with Grok. See the [Hermes external skills guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md#external-skill-directories).

The two search tracks need genuinely separate contexts if their independence is to be claimed. The complete workflow also requires separate contexts for source verification and the final text cross-check. These four tasks can be assigned to separate subagents in Claude Code, Codex, or Cursor where the environment supports them. Without that separation, a run must not claim an independent cross-check.

The execution environment must provide a web search tool and readable access to original sources. If these requirements are missing, the run must state its limitations.

## Privacy and external search requests

For research, the AI application's search tool sends search terms to the search engines or search services used; opening original sources involves requests to the relevant websites. QuellPass has no MCP servers of its own or fixed search-service integration. The execution environment determines the providers. Personal information and confidential text passages should not be included in external search requests. Olaf Wulf receives no usage data from operation of the plugin. Evidence records may be stored in the user's environment. See the [Privacy Notice](PRIVACY.en.md) for details.

## License

The skill text, README documentation, and reference texts are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The technical package files use the MIT License. See [LICENSE.md](LICENSE.md) for the allocation and license texts. Using the plugin does not place your own research reports or resulting texts under the QuellPass license.

## Contribute

Tests and specific improvement suggestions are welcome through a [GitHub test report](https://github.com/olwulf-commits/quellpass/issues/new/choose). Please include the tool, version, example, and observed result. Successful tests are useful too. I review the feedback and decide which changes enter the official edition.

## Status and limitations

The repository is publicly available with Olaf’s approval. The language and structure research conducted with QuellPass on September 30, 2026 is documented. This does not establish comprehensive testing of the frozen general edition across all supported hosts. Public availability on GitHub is neither an official provider-directory listing nor a guarantee of quality.

# QuellPass

[Deutsch](README.md) · English

QuellPass, developed by Olaf Wulf, researches verifiable questions using an **independent counter-question**, checks against original sources, and an **evidence record**. Once the **evidence review gate** has been passed, a readable research report can be written on request. An article or other draft remains a separate step, based on statements cleared by that review. The plugin is independent of any particular model or search provider.

My goal is to improve the quality of texts significantly using relatively simple methods. QuellPass makes claims and sources open to verification; TextPass then works on language and reading flow. People can follow, question, and correct both processes. How well they work in practice has to be demonstrated through actual texts.

I see evaluation as working with what is already there: identifying what holds up, where claims need better evidence, and using those findings to guide further work. “Evaluate” means to assess; the word comes through French from Latin [*valere*](https://www.etymonline.com/word/evaluation), meaning “to be worth.” The German term *evaluieren* means [to assess](https://www.duden.de/rechtschreibung/evaluieren). In formative evaluation, findings inform improvements. QuellPass makes gaps in the evidence visible and helps ground claims in better-supported sources.

This repository contains the **general edition** for Codex, Cursor, and Claude Code. All three use the same [skill](plugins/quellpass/skills/quellpass/SKILL.md) and [research and writing protocol](plugins/quellpass/skills/quellpass/references/protokoll.md). Project-specific integrations are not included.

## Installation and requirements

Codex finds the catalog at `.agents/plugins/marketplace.json`. Cursor can read the portable plugin; `.cursor-plugin/marketplace.json` is also provided for repository import. Claude Code finds its catalog at `.claude-plugin/marketplace.json`. Add the public repository in Claude Code with `claude plugin marketplace add olwulf-commits/quellpass`, then install with `claude plugin install quellpass@quellpass`. Version 0.3.1 has been installed locally from this repository in Codex and checked against the source files. The Claude installation route has not been tested here.

The two search tracks need genuinely separate contexts if their independence is to be claimed. The complete workflow also requires separate contexts for source verification and the final text cross-check. These four tasks can be assigned to separate subagents in Claude Code, Codex, or Cursor where the environment supports them. Without that separation, a run must not claim an independent cross-check.

The optional local [semantic_feedback.py](plugins/quellpass/scripts/semantic_feedback.py) tool ranks page sections that have already been retrieved. Its command-line interface requires `fastembed` and a locally available embedding model. It does not perform web searches. The execution environment must provide a web search tool and readable access to original sources. If these requirements are missing, the run must state its limitations.

## License

The skill text, README documentation, and reference texts are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The Python tool and technical package files use the MIT License. See [LICENSE.md](LICENSE.md) for the allocation and license texts. Using the plugin does not place your own research reports or resulting texts under the QuellPass license.

## Contribute

Tests and specific improvement suggestions are welcome through a [GitHub test report](https://github.com/olwulf-commits/quellpass/issues/new/choose). Please include the tool, version, example, and observed result. Successful tests are useful too. I review the feedback and decide which changes enter the official edition.

## Status and limitations

The repository is publicly available with Olaf’s approval. The language and structure research conducted with QuellPass on September 30, 2026 is documented. This does not establish comprehensive testing of the frozen general edition across all supported hosts. Public availability on GitHub is neither an official provider-directory listing nor a guarantee of quality.

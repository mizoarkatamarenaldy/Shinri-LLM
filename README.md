# Shinri-LLM
LLM persona psychometrics experiments

A learning project and portfolio piece. It tests whether large language models, when prompted with a personality persona, answer psychometric questionnaires consistently with that persona.

## Status

Phase 0: repository setup. No experiments have been run yet.

## Planned approach

- Data is collected through provider APIs, not chat apps, so memory and app-level system prompts do not affect the results.
- Phase 1: pilot with 2 opposing personas, 10 test questions, 1 low-cost model, 3 repeats.
- Phase 2: measurement with the OEJTS questionnaire and a consistency check.
- Phase 3: add more models, and record model ID, provider, and settings for each run.
- Phase 4: expand to 16 personas if the pilot shows a real difference.
- Phase 5: analysis and write-up.

## Repository structure

- `src/`: shared code
- `experiments/`: one subfolder per instrument or model (starting with `mbti/`)
- `results/`: raw and processed outputs, mirroring `experiments/`

## Setup

Copy `.env.example` to `.env` and fill in your own API keys. The `.env` file is ignored by git and must never be committed.

## License

MIT. See `LICENSE`.

## Author

Mizo Arkatama Renaldy
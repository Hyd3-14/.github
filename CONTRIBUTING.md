# Contributing

Repositories under this account prefer small, reversible changes.

## Issues

- Work starts from an Issue, in principle
- Issue titles carry no prefix such as `[Bug]:` or `[Chore]:`; use a natural title that describes the content
- The kind is expressed with a `type: *` label, not in the title

## Pull Requests

- Include `closes #<issue>` for the corresponding Issue
- Leave the verification steps appropriate to the change in the PR
- Apply at least one `type: *` label
- When adding or updating a workflow, check SHA pinning of actions and minimal permissions

## Labels

Label names are in English; descriptions are in Japanese by default.

- `type: feature`: a new feature or a feature addition
- `type: bug`: a bug fix
- `type: chore`: maintenance, configuration, operational improvement
- `type: docs`: a documentation change
- `type: question`: a question, consultation, or specification check

## Secrets

Never commit tokens, secrets, personal information, or internal information. Topics involving vulnerabilities or secrets are not handled in public Issues; follow the policy in `SECURITY.md`.

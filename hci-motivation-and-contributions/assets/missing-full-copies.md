# Missing full copies and author-access requests

Use this queue only after lawful independent acquisition routes have been tried. A row does not
count as asking the author: record when the concrete request was surfaced in the conversation.
Never record credentials, cookies, session tokens, browser profiles, or copied authentication
material.

| Priority | Exact work | DOI/canonical URL | Why the full source could change the analysis | Routes tried and exact obstacle | Exact author action requested | Request surfaced date | Conversation/workboard locator | Status | Affected stable claim IDs | Claim/rank/chart fallback or narrowing if unavailable | Re-review trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | `OPEN` | | | |

Allowed status values:

- `OPEN`: independent routes remain;
- `NEEDS_AUTHOR_SOURCE_ACCESS`: lawful independent routes are exhausted **and the exact concrete
  request has already been surfaced to the author**;
- `RESOLVED_FULL`: the exact full source was obtained and audited;
- `EXCLUDED`: after the access request, the author declined/could not obtain it and the affected
  claim/rank/chart consequence is recorded, or a documented relevance screen makes it
  non-decision-relevant; or
- `SUPERSEDED`: a verified stronger source makes this copy non-decision-relevant.

`UNASSESSED`, `PARTIAL`, `BROKEN`, and “obtain later” are not terminal statuses. A
`NEEDS_AUTHOR_SOURCE_ACCESS` row requires an actual non-future `YYYY-MM-DD` surfaced date, a stable
session/conversation/workboard locator, affected claim IDs, a fallback/narrowing consequence, and a
specific reopen trigger. Separate multiple affected claim IDs with `||`; every ID must resolve in
`claim-evidence-ledger.csv` before a bounded round can close. Free-form claim descriptions and
placeholder-wrapped locators such as `session:pending` or `workboard.md#TBD` are invalid.
Placeholder values such as `no`, `pending`, or `TBD` cannot satisfy any closure-defining field:
ask now or keep working the independent routes. When the author supplies a file or readies the
authenticated page, verify identity, open and audit it, and update this row to `RESOLVED_FULL`;
receipt alone is not resolution.

Before asking the author to purchase a paper, suggest connecting through their university IP,
library proxy, or university VPN and retrying in the same headed browser. The author connects the
VPN themselves. For a CAPTCHA or institutional login, ask the author to complete it in their own
headed browser and say when the page or download is ready. Do not attempt to bypass the challenge,
inspect VPN configuration, or ask them to transmit authentication material.

# Universal Auctions Group: homepage, buying and selling pages

**Client review build. Not live, and not indexable** (`noindex,nofollow` on every page plus a
blanket `robots.txt`, so this preview cannot compete with universalauctionsgroup.com in search).

Three pages:

| Page | Purpose |
|---|---|
| `index.html` | Homepage signpost. Two-panel buy/sell chooser, short doors into each branch, one register section. No fees, commission or buyer's premium anywhere on it. |
| `buying.html` | Everything a buyer needs. Buyer costs live here and only here. |
| `selling.html` | Everything a seller needs, including administrators and receivers. |

Structure follows the pattern used by Euro Auctions, Wilsons, SDL, Allsop, John Pye and Manheim:
none of them put buyer costs on a homepage, and all of them split buying from selling by page.

Every factual statement is taken from UAG's own published terms and conditions
(universalauctionsgroup.com/terms-and-conditions) and from Adrian's amendment schedule of
5 August 2026. Two yellow flags mark figures that UAG's own terms state inconsistently and which
need confirming before this goes live:

1. **Buyer's premium rate.** Clause 5.1 says 10 to 25%; clause 18.7 says 15 to 20%.
2. **Collection grace period.** Clause 12.5 says 7 days; the amendment schedule says 5.

Design tokens are read from the live site CSS, so this matches the existing site rather than
introducing a new look: Helvetica Neue / Arial weight 400, heading letter-spacing -0.03em,
cyan #53a8c7, square cyan buttons at 1rem/1.3rem padding, sections alternating light, wash and
black. Every class is `uag-` prefixed and every rule is scoped under a `uag-` ancestor, so the CSS
can be pasted into Squarespace Code Blocks without leaking into the theme.

Photo credits and the QA rejections are in `credits.csv` and `credits-rejected.txt`.

# UAG three-page build: notes for the next session

**Published for client review: https://claude.ai/code/artifact/324bad40-da7c-472f-bf26-14be8a31ad12**
(Private until Paul shares it from the page's share menu. Supersedes the older draft-5 artifact
d18b4c1e, which predates Adrian's amendments and still contained three forbidden claims.)

## What is here

| File | Purpose |
|---|---|
| `index.html` | Homepage signpost. Two-panel chooser, short doors, one register section. No fees, commission or buyer's premium anywhere. |
| `buying.html` | Buyer page. All buyer costs live here and only here. |
| `selling.html` | Seller page, including the administrators and receivers section. |
| `uag.css` | Shared stylesheet. Every class `uag-` prefixed, every rule scoped under a `uag-` ancestor, no bare element selectors, so it can go into Squarespace Code Blocks without leaking. |
| `img/` | Seven images, webp plus jpg fallback, 1600px wide, 80 to 380KB each. |
| `credits.csv` | Photo credits with the QA note for each. |
| `credits-rejected.txt` | What was rejected at QA and why. |
| `build_artifact.py` | Combines the three pages into the single-file artifact: inlines the CSS, base64s the images, rewrites internal links to a JS page switcher. Re-run it after editing any page, then republish the same path. |

## Why the structure is what it is

Buyer costs on a buyer page only, and buying split from selling by page, follows the pattern in every
comparable auctioneer we checked: Euro Auctions, Wilsons, SDL, Allsop, John Pye, Manheim. The rule and
the research are in the `feedback_two_sided_site_separation` memory. A seller is never shown the
buyer's economics and a buyer is never shown the seller's.

## Facts

Every factual statement comes from `../service-terms.md`, which was built clause by clause from UAG's
own published terms plus Adrian's 5 Aug amendment schedule. That means this build already avoids the
claims Adrian struck out: no "we check outstanding finance", no "full sale proceeds", no "sold as
seen", no "registration takes no card details", no unqualified "no deposit", no "we arrange collection
UK-wide", no RICS, no on-site cataloguing. The internet surcharge is present, which it was not in any
earlier draft.

**Two yellow flags in the copy are Adrian's to resolve**, both logged in service-terms.md CONFLICTS:
1. Buyer's premium rate. His clause 5.1 says 10 to 25%, his clause 18.7 says 15 to 20%.
2. Collection grace period. His clause 12.5 says 7 days, his amendment note says 5.

## Still to do before this goes near the live site

1. **Confirm the Squarespace plan.** Code Blocks need Business or higher. If UAG is on Personal, the
   paste approach is dead and we rethink delivery.
2. **Get Adrian's nod on the two extra pages as scope.** He approved homepage sections on 30 July, not
   a `/buying` and a `/selling` page.
3. **Split into per-section paste blocks** with the CSS inlined in each, and test on a hidden
   Squarespace page first.
4. **Swap the internal links** once the real URLs exist. See `../missing-pages-plan.md`: the support
   pages the blog amendments assume (buyer fees, viewing, payment and collection, storage, export)
   do not exist yet, so both pages currently link to `/terms-and-conditions` and `/contact`.
5. **Photography.** These are stock. If Paul gets the paid Freepik auction-room set, or UAG supplies
   photographs of real lots, swap them in: real stock beats stock photography on a page like this.
6. **Tell Adrian about his own homepage.** Three forbidden claims are live on it right now (RICS
   surveyors, attending to catalogue, VAT-friendly export), and there is a stray `<h1>` in the contact
   block whose text is literally "H1", currently the only h1 on the page.

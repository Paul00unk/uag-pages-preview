# UAG three-page build: notes for the next session

**Published for client review: https://claude.ai/code/artifact/324bad40-da7c-472f-bf26-14be8a31ad12**
(Private until Paul shares it from the page's share menu. Supersedes the older draft-5 artifact
d18b4c1e, which predates Adrian's amendments and still contained three forbidden claims.)

## What is here

| File | Purpose | Words |
|---|---|---|
| `index.html` | Homepage signpost. Two-panel chooser, short doors, one register section. Carries NEITHER side's economics. | 899 |
| `buying.html` | Buyer page. All buyer costs live here and only here. | 1,982 |
| `why-sell-with-uag.html` | The seller ARGUMENT. No fees, stock stays put, paid before collection, who bids, auction vs dealer vs private sale, the record, who we sell for. | 1,157 |
| `sell-with-us.html` | The seller PROCESS. What we need from you, six steps, what you can sell, valuations and reserves, timing, export. | 1,013 |
| `asset-disposal.html` | Administrators, receivers and liquidators. What you get for the file, why an open auction stands up, how fast we can move, what stays out of the sale. | 1,246 |
| `uag.css` | Shared stylesheet. Every class `uag-` prefixed, every rule scoped under a `uag-` ancestor, no bare element selectors, so it can go into Squarespace Code Blocks without leaking. |
| `img/` | Fifteen images, webp plus jpg fallback. Seven section photos at 1600px; eight category-card photos at 900x562 (16:10), 44 to 104KB each. |
| `credits.csv` | Photo credits with the QA note for each. |
| `credits-rejected.txt` | What was rejected at QA and why. |
| `build_artifact.py` | Combines all five pages into the single-file artifact: inlines the CSS, base64s the images, rewrites internal links to a JS page switcher. Re-run it after editing any page, then republish the same path. |

## Why the structure is what it is

Buyer costs on a buyer page only, and buying split from selling by page, follows the pattern in every
comparable auctioneer we checked: Euro Auctions, Wilsons, SDL, Allsop, John Pye, Manheim. The rule and
the research are in the `feedback_two_sided_site_separation` memory. A seller is never shown the
buyer's economics and a buyer is never shown the seller's.

**Three seller pages, and the reason is conversion, not rank.** Paul's call 6 Aug, and Adrian named
"Why sell with UAG" himself on the 30 July call. The keyword research in
`../seller-keyword-research.md` found effectively no seller search demand in UAG's market:
`sell plant machinery at auction uk` is already tracked at **msv 0, rank 0**, `sell plant and machinery`
and `asset disposal insolvency` return **zero** ideas, and the volume behind generic "selling at
auction" is residential property at £14 to £33 CPC. Sellers arrive from referrals, IP networks,
outbound and Adrian's Facebook ad, so these pages are links you send someone and pages that close them
when they land. The buyer side is where the roughly 2,500 monthly searches are.

I originally recommended three pages partly on ranking grounds. The research killed that argument and
I said so before building. Do not propose further seller pages on SEO grounds.

`selling.html` is retired: it was the single combined seller page, and its content is now split
across the three above.

## The cross-audience rule, and the mistake I made against it

Paul's rule: **the homepage cannot carry the seller information a buyer should not read.** Saying
"sellers pay nothing" reassures a seller and warns a buyer in the same scroll. Full research in the
`feedback_two_sided_site_separation` memory.

**The first version of this build broke it.** The homepage carried the no-fees USP in four places:
a chooser bullet, the seller section heading ("Selling with no fees and no commission"), its lede
("Our sellers pay us nothing") and its first tick, plus a meta description that a buyer sees in
search results. Fixed 5 Aug: the homepage seller door now sells on control, payment timing and reach,
and links to `sell-with-us.html` and `why-sell-with-uag.html` where the economics belong.

**The test to apply, not "which audience is this page for":** does this sentence make the OTHER
audience feel they are the one paying for it? Control, timing and reach pass. Price does not.

Current state, verified by script over all five pages including their meta descriptions:

| Page | Carries seller economics | Carries buyer charges |
|---|---|---|
| Homepage | no | no |
| Buying | no | yes, correctly, and only here |
| Why sell with UAG | yes, correctly | no |
| Sell with us | yes, correctly | no |
| Asset disposal | yes, correctly | no |

## These are sales pages, not guides

Paul, 5 Aug: *"don't say what we don't, avoid saying, this is a sales website pages not a guide"*.
Adrian's 215 amendments demanded the disclaimers, but they were written for the ARTICLES. I had
carried that register across and left 47 defensive sentences here. Now 3, and those are ordinary
helpful sentences rather than disclaimers. Rule and the before/after table:
`feedback_sales_pages_not_guides` memory.

Every operational fact is still true, just stated as what we do. The safety check that matters after
a rewrite like this: removing "we do not inspect" must not leave anything implying we do. Verified by
script that no page claims inspection, grading, appraisal, finance checks or site attendance, and
that the buyer page still makes the buyer's own looking explicit.

## Facts

Every factual statement comes from `../service-terms.md`, which was built clause by clause from UAG's
own published terms plus Adrian's 5 Aug amendment schedule. That means this build already avoids the
claims Adrian struck out: no "we check outstanding finance", no "full sale proceeds", no "sold as
seen", no "registration takes no card details", no unqualified "no deposit", no "we arrange collection
UK-wide", no RICS, no on-site cataloguing. The internet surcharge is present, which it was not in any
earlier draft.

**No prices or rates appear on these pages, by design (Paul, 5 Aug: "leave the pricing aside for
buyers").** The buyer page names the components of a winning bid and says where each rate is stated,
which is the lot's Additional Fees tab, and defers the storage rate, the grace period, the
administration fee, the interest rate and the debt recovery percentage to the auction terms. The one
figure kept is VAT at 20%, because that is the statutory rate rather than a UAG price and it is what a
buyer needs to sanity-check an invoice.

That also keeps the pages maintenance-free if UAG changes a rate, and it keeps our internal queries
out of client-facing copy. **The two questions Adrian still has to answer are tracked in
`../service-terms.md` CONFLICTS, not on the page:**
1. Buyer's premium rate. His clause 5.1 says 10 to 25%, his clause 18.7 says 15 to 20%.
2. Collection grace period. His clause 12.5 says 7 days, his amendment note says 5.

Both need resolving before a `/buyer-fees` page can be written (see `../missing-pages-plan.md`), but
neither blocks these three pages now that no rate is quoted.

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
   The category cards are the first place to swap, because a real UAG lot in a real UAG yard does
   more work there than anywhere else on the site.

## Photography sourcing rules learned on this build

Every image came from Freepik via the Magnific MCP. **No Pexels images are on these pages** — Pexels
was the source for the Batch 1-3 blog covers only, and those are a separate set.

Four QA gates, all of which caught something real (the misses are logged in `credits-rejected.txt`):

1. **`aiGenerated: false` is not trustworthy.** Check the `stock_get` `url` instead: `/free-photo/`
   or `/premium-photo/` is a photograph, anything with `ai-image` is not. Four AI images passed the
   flag on the first round.
2. **The flag does not catch 3D renders either.** "Red delivery vans standing out from a fleet of
   white vans" is CGI, declared as a photo, and only looking at it caught that. Look at every image.
3. **Check it is not already on the site.** The obvious "Group of trucks parked in a row" result is
   byte-for-byte the existing `trucks.webp`, same contributor and same shoot. Compare against `img/`
   before downloading, not after.
4. **Check the setting reads as the UK trade.** Rejected a row of blue MTZ tractors and a set of
   tropical minibuses: both are real photographs of the right category and still wrong for UAG.
6. **Tell Adrian about his own homepage.** Three forbidden claims are live on it right now (RICS
   surveyors, attending to catalogue, VAT-friendly export), and there is a stray `<h1>` in the contact
   block whose text is literally "H1", currently the only h1 on the page.

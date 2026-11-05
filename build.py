from pathlib import Path
from html import escape
from math import cos, sin, radians
import json, re, shutil

ROOT = Path(__file__).parent
SRC = ROOT / 'src'
OUT = ROOT / 'dist'

DOMAIN = 'exchangebitcointohelium.com'
SITE = f'https://{DOMAIN}/'
CN = 'https://changenow.io/currencies/bitcoin/helium-sol'
CN_REL = 'sponsored nofollow noopener noreferrer'  # Variant B: independent site with affiliate links
DOC_HNT = 'https://docs.helium.com/tokens/hnt-token/'
DOC_MIGRATE = 'https://docs.helium.com/wallets/l1-migrate/'
HNT_MINT = 'hntyVP6YFm1Hg25TN9WGLqM12b8TQmcknKrdu1oxWux'
REVIEWED = 'November 5, 2026'
ISO_DATE = '2026-11-05'

TITLE = 'Best Ways to Exchange Bitcoin to Helium (BTC to HNT)'
DESCRIPTION = 'Compare five BTC to HNT exchange services. See why ChangeNOW is our best overall choice and learn how to exchange Bitcoin for Helium step by step.'
OG_DESCRIPTION = 'Compare BTC to HNT exchange services and learn why ChangeNOW is our best overall choice.'
OG_IMAGE = f'{SITE}assets/btc-to-hnt-guide.webp'

ARR = '<span class="arr">→</span>'


def e(t):
    return escape(t, quote=True)


def rich(t):
    """Escape text; render the literal 0x address prefix as code."""
    return re.sub(r'\b0x\b', '<code>0x</code>', e(t))


def link_out(href, text):
    return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{e(text)}</a>'


def cn_link(label, loc, cls='btn btn-dark'):
    return (f'<a class="{cls}" href="{CN}" target="_blank" rel="{CN_REL}" data-cta="{loc}">'
            f'<span>{e(label)}</span></a>')


# ------------------------------------------------------------------ hex art (generated)

def hexpts(cx, cy, s):
    return ' '.join(f'{cx + s * cos(radians(30 + 60 * k)):.1f},{cy + s * sin(radians(30 + 60 * k)):.1f}' for k in range(6))


def hex_tile(stroke, opacity):
    s = 60 / 3 ** 0.5
    h = 3 * s
    cs = [(30, h / 2), (0, 0), (60, 0), (0, h), (60, h)]
    polys = ''.join(f'<polygon points="{hexpts(cx, cy, s)}"/>' for cx, cy in cs)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="60" height="{h:.2f}" viewBox="0 0 60 {h:.2f}">'
            f'<g fill="none" stroke="{stroke}" stroke-opacity="{opacity}" stroke-width="1.2">{polys}</g></svg>\n')


def hex_cluster():
    s = 34
    w = s * 3 ** 0.5
    grid = [
        '. o l o . . .',
        'o l m d l o .',
        '. l d b m l o',
        'o m d m l o .',
        '. o l l o . .',
        '. . o . . . .',
    ]
    fills = {'o': ('none', 0), 'l': ('#474DFF', .12), 'm': ('#474DFF', .34), 'd': ('#474DFF', 1), 'b': ('#F7931A', 1)}
    out = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row.split()):
            if ch == '.':
                continue
            cx = c * w + (w / 2 if r % 2 else 0) + s
            cy = r * 1.5 * s + s
            fill, op = fills[ch]
            out.append(f'<polygon points="{hexpts(cx, cy, s - 1.5)}" fill="{fill}" fill-opacity="{op}" '
                       f'stroke="#474DFF" stroke-opacity=".4" stroke-width="1.4"/>')
    W = int(7 * w + s * 2)
    H = int(6 * 1.5 * s + s * 2)
    return (f'<svg class="hex-art" viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true" focusable="false">'
            + ''.join(out) + '</svg>')


# ------------------------------------------------------------------ content

facts = [
    ('1,000+', 'digital assets on ChangeNOW'),
    ('1M+', 'supported exchange pairs'),
    ('110', 'blockchains supported'),
    ('98%', 'Triumph Rate within a 0.5% deviation or better'),
]

cmp_head = ['Rank', 'Service', 'Best for', 'BTC → HNT', 'Rate options', 'Account for standard swap', 'Support', 'Score']
cmp_rows = [
    ['1', 'ChangeNOW', 'Best overall', 'Available', 'Fixed and floating', 'Not required', '24/7', '9.4/10'],
    ['2', 'SimpleSwap', 'Broad coin coverage', 'Available', 'Fixed and floating', 'Not required', '24/7', '9.0/10'],
    ['3', 'StealthEX', 'Simple wallet-to-wallet flow', 'Confirm live', 'Fixed and floating where offered', 'Not required', 'Customer support available', '8.7/10'],
    ['4', 'ChangeHero', 'Straightforward four-step exchange', 'Available', 'Best Rate and Fixed Rate', 'Not required', '24/7', '8.4/10'],
    ['5', 'Exolix', 'Minimal pair interface', 'Available', 'Check the live offer', 'Not required', '24/7 assistance stated', '8.1/10'],
]

why_cards = [
    ('Direct BTC to HNT route', 'Bitcoin and Helium can be selected as the source and destination assets without using an order book or making an intermediate trade manually.'),
    ('Fixed and floating rates', 'Floating mode follows current market conditions. Fixed mode is intended to preserve the agreed output under the conditions shown for the exchange.'),
    ('Upfront estimate', 'The estimated HNT output and included costs are shown before the user sends the BTC deposit.'),
    ('Broad coverage', 'ChangeNOW lists more than 1,000 digital assets, more than one million exchange pairs and support across 110 blockchains.'),
    ('No upper swap limit', 'ChangeNOW does not publish a maximum amount for standard crypto-to-crypto swaps. The live minimum still depends on the pair, liquidity and network costs.'),
    ('24/7 support', 'Support is available around the clock, including assistance with complex transaction issues.'),
]

reviews = [
    {
        'id': 'review-changenow', 'rank': 1, 'award': '#1 · Best Overall', 'name': 'ChangeNOW', 'featured': True,
        'paras': [
            'ChangeNOW is our top BTC-to-HNT choice for users who want a direct exchange with a clear estimate and a choice between fixed and floating rates. The standard flow does not require account registration: select BTC and HNT, confirm the HNT payout network, enter a compatible receiving address, review the estimate and send the Bitcoin deposit.',
            'The service stands out for the combination of route coverage and execution options. It supports more than 1,000 assets, more than one million pairs and 110 blockchains. ChangeNOW also publishes a 98% Triumph Rate, meaning swaps over the measured period were completed at a better rate than estimated or within a deviation of less than 0.5%.',
            'Users should still treat the displayed amount as an estimate when choosing a floating rate. Bitcoin confirmation time, market movement and liquidity can change the result. Fixed mode is the better fit when output certainty matters more than following the live market.',
        ],
        'facts': [('Rate modes', 'Fixed and floating'), ('Account', 'Not required for a standard swap'), ('Asset coverage', '1,000+ digital assets'),
                  ('Upper swap limit', 'None published'), ('Support', '24/7'), ('Our score', '9.4/10')],
        'best': 'Most users who want a balanced mix of simplicity, rate choice, broad coverage and support.',
        'consider': 'The average exchange time is not a guarantee for a specific BTC-to-HNT transaction.',
        'cta': 'Exchange BTC to HNT on ChangeNOW',
    },
    {
        'id': 'review-simpleswap', 'rank': 2, 'award': '#2 · Best for Broad Coin Coverage', 'name': 'SimpleSwap',
        'paras': [
            'SimpleSwap is a strong alternative for users who value broad asset coverage. Its official BTC-to-HNT page displayed a direct cross-chain route from Bitcoin to HNT on Solana during our review and states that a standard swap does not require sign-up.',
            'The interface provides fixed and floating rate options and does not require users to create an account for a standard swap. Its broad coverage makes SimpleSwap particularly useful when a user expects to exchange less common assets before or after the BTC-to-HNT transaction.',
            'ChangeNOW ranks higher in this comparison because we found its combination of exchange flow, published operational metrics, broad blockchain coverage and support evidence stronger for this specific route. A live quote comparison may still favor either provider at a particular moment.',
        ],
        'facts': [('Rate modes', 'Fixed and floating'), ('Account', 'Not required for a standard swap'),
                  ('Asset coverage', '1,000+ coins and tokens stated on the reviewed pair page'), ('Support', '24/7'), ('Our score', '9.0/10')],
        'best': 'Users who prioritize the widest possible asset catalogue.',
        'consider': 'Always compare the final HNT estimate for the same BTC amount immediately before exchanging.',
    },
    {
        'id': 'review-stealthex', 'rank': 3, 'award': '#3 · Best for a Minimal Wallet-to-Wallet Flow', 'name': 'StealthEX',
        'paras': [
            'StealthEX supports Bitcoin and Helium and uses a straightforward exchange process: choose the currencies, enter the receiving wallet address, send the deposit and wait for the payout. Its public pages state that fixed and floating options may be available and that no account is required for a standard exchange. Confirm the direct BTC-to-HNT route and the payout network in the live form before sending funds.',
            'The service emphasizes wallet-to-wallet swaps and lists more than 2,000 coins and tokens. This makes it a credible alternative for users who want a simple interface with relatively broad coin support.',
            'It ranks below ChangeNOW and SimpleSwap because its public pair page makes several broad marketing claims that users should verify against the live offer and current terms. We give more weight to a clearly presented estimate, documented service metrics and a balanced explanation of transaction conditions.',
        ],
        'facts': [('BTC → HNT route', 'Confirm in the live form before sending funds'), ('Rate modes', 'Fixed and floating where offered'),
                  ('Account', 'Not required for a standard swap'), ('Asset coverage', '2,000+ coins and tokens stated'), ('Our score', '8.7/10')],
        'best': 'Users who want a minimal pair-focused interface.',
        'consider': 'Do not rely on general privacy or speed claims; read the live exchange terms for the specific transaction.',
    },
    {
        'id': 'review-changehero', 'rank': 4, 'award': '#4 · Best for a Guided Four-Step Swap', 'name': 'ChangeHero',
        'paras': [
            'ChangeHero displayed an active BTC-to-HNT route and organizes the exchange into four clear steps: enter the amount, provide the HNT address, confirm the transaction and receive the payout. It offers a Best Rate mode and a Fixed Rate mode and does not require an account for a standard exchange.',
            'The service states support for more than 300 cryptocurrencies and provides round-the-clock assistance. Its focused interface can work well for users who prefer a guided process over a feature-heavy platform.',
            'ChangeHero ranks fourth because its supported-asset catalogue is smaller than the leading services in this comparison. Its official page also states percentage-based fee ceilings for its two rate modes, but the most useful comparison remains the final HNT output offered for the same BTC amount.',
        ],
        'facts': [('Rate modes', 'Best Rate and Fixed Rate'), ('Account', 'Not required for a standard swap'),
                  ('Asset coverage', '300+ cryptocurrencies stated'), ('Support', '24/7'), ('Our score', '8.4/10')],
        'best': 'Users who prefer a guided four-step exchange.',
        'consider': 'Compare the final expected output rather than a headline fee percentage alone.',
    },
    {
        'id': 'review-exolix', 'rank': 5, 'award': '#5 · Best for a Simple Pair Page', 'name': 'Exolix',
        'paras': [
            'Exolix displayed a dedicated BTC-to-HNT pair page with a minimal exchange interface during our review. The page explains the wallet, amount and deposit stages and shows the expected output before the user sends Bitcoin. Confirm that the route is active and that the HNT payout network is Solana in the live form before sending funds.',
            'This uncluttered format may appeal to users who already understand cross-chain exchanges and do not need much guidance. Exolix also states that account creation is not required for its standard exchange flow.',
            'It ranks fifth because the public information available for a route-level comparison is less detailed than the documentation offered by the higher-ranked services. Users should confirm the rate type, minimum amount, expected processing time and support conditions in the live form before sending BTC.',
        ],
        'facts': [('BTC → HNT route', 'Available during review; confirm in the live form before sending funds'), ('Account', 'Not required for a standard swap'),
                  ('Quote', 'Shown in the live exchange flow'), ('Our score', '8.1/10')],
        'best': 'Experienced users who want a minimal exchange page.',
        'consider': 'Verify all transaction conditions in the live form because public route-level details are limited.',
    },
]

criteria = [
    ('Pair availability', 20, 'Whether a direct BTC-to-HNT route was available during review'),
    ('Quote and cost transparency', 20, 'Whether the estimated HNT output and included costs were visible before deposit'),
    ('Exchange speed', 15, 'Published timing, clarity of conditions and dependence on network confirmations'),
    ('Ease of use', 15, 'Number of steps, form clarity and whether an account was required for a standard swap'),
    ('Rate options', 10, 'Availability and explanation of fixed and floating modes'),
    ('Limits and coverage', 10, 'Live minimum, maximum policy, asset catalogue and blockchain coverage'),
    ('Support and reputation', 10, 'Support availability, public documentation and review evidence'),
]

compare_steps = [
    'Open each service within the same 10–15 minute window.',
    'Enter the same BTC amount on every service.',
    'Select the same rate type where possible.',
    'Record the estimated HNT output before sending funds.',
    'Check whether network and service costs are already included.',
    'Compare the live minimum and expected completion conditions.',
    'Recheck the wallet address and final estimate before choosing a provider.',
]

howto = [
    ('Select Bitcoin and Helium', 'Open the BTC-to-HNT exchange page. Choose Bitcoin as the asset you send and Helium as the asset you receive. Enter the BTC amount. The form will display the live minimum, HNT payout network and estimated output. Do not continue until the selected network matches your receiving wallet.'),
    ('Choose a rate mode', 'Use floating mode if you want the exchange to follow current market conditions. Choose fixed mode when it is available and receiving the agreed amount matters more than tracking short-term market movement. Read the conditions shown in the live form.'),
    ('Enter a Solana address that supports HNT', 'Paste the destination address from a wallet that supports HNT on Solana. Compare the first and last characters with the original address. Do not enter a Bitcoin address, an Ethereum 0x address or a legacy address from the former Helium L1. If you have an old Helium wallet, complete the official migration process before using it to receive current HNT.'),
    ('Review, send BTC and track the exchange', 'Confirm the pair, amount, rate mode, HNT network and receiving address. Send the required Bitcoin amount to the generated BTC deposit address. Keep the exchange ID and follow the status until the HNT payout reaches your wallet on the selected network.'),
]

vs_rows = [
    ('Network', 'Bitcoin blockchain', 'Solana blockchain'),
    ('Asset type', 'Native coin', 'Helium Network protocol token on Solana'),
    ('Address type', 'Native Bitcoin address', 'Solana address from a wallet that supports HNT'),
    ('Asset role in this exchange', 'Deposit asset', 'Payout asset'),
    ('Main user check', 'Correct BTC deposit address and amount', 'Correct HNT receiving address'),
    ('Reversibility', 'Blockchain transfers are irreversible', 'Blockchain transfers are irreversible'),
]

rate_cards = [
    ('Exchange rate', 'The BTC-to-HNT rate shows how much Helium you can receive for a given amount of Bitcoin. It changes with market prices, liquidity and the selected rate mode.'),
    ('Included costs', 'ChangeNOW states that all costs are built into the estimate shown before the swap, with no additional charge added after the exchange. Compare final HNT output rather than a headline fee alone.'),
    ('Processing time', 'ChangeNOW publishes an overall average exchange time of about one minute, but a BTC-to-HNT swap can take longer because it starts after the required Bitcoin confirmations and depends on network and liquidity conditions.'),
]

safety_items = [
    'Confirm that BTC is the deposit asset and HNT is the payout asset.',
    'Confirm the exact HNT payout network shown in the live exchange form.',
    'Use a wallet that supports HNT on that exact network and that you control.',
    'Confirm that the form shows HNT on Solana.',
    'Use a Solana address from a wallet that can display HNT; do not use a Bitcoin, Ethereum or legacy Helium L1 address.',
    'Keep a small amount of SOL available if the receiving wallet will later need to send HNT or interact on Solana.',
    'Copy the receiving address instead of typing it manually.',
    'Compare the first and last characters after pasting the address.',
    'Review the live minimum and estimated HNT output.',
    'Check whether you selected a fixed or floating rate.',
    'Send exactly the amount requested by the exchange form.',
    'Save the exchange ID until the HNT payout arrives.',
    'Consider a smaller test exchange when the transaction size justifies it.',
    'Contact support through the service’s official domain only.',
]

faq = [
    ('What is the best way to exchange Bitcoin for Helium?',
     'ChangeNOW is our best overall choice for exchanging BTC to HNT. It offers a direct route, fixed and floating rate modes, an upfront estimate, no required account for a standard swap and 24/7 support. The best live quote can still change, so compare the final HNT output immediately before sending Bitcoin.'),
    ('Can I exchange BTC to HNT without creating an account?',
     'Yes. ChangeNOW and the other services in this comparison state that account registration is not required for a standard BTC-to-HNT exchange. This does not mean a transaction can never be reviewed. Providers may apply risk-based checks under their terms, policies and legal obligations.'),
    ('How long does a BTC to HNT exchange take?',
     'The exact time depends on Bitcoin confirmations, HNT payout-network processing, liquidity and network congestion. ChangeNOW publishes an overall average exchange time of about one minute, but BTC-to-HNT transactions can take longer. Delivery is usually expected within one hour, although this is not a guarantee for every swap.'),
    ('What is the minimum BTC to HNT exchange amount?',
     'The minimum is dynamic because it depends on network costs, liquidity and the live exchange conditions. ChangeNOW states that minimums can be as low as the equivalent of $2, but users should rely on the current minimum displayed in the BTC-to-HNT form.'),
    ('What network is Helium HNT on?',
     'HNT operates on the Solana blockchain. The Helium Network migrated from its original purpose-built blockchain to Solana on April 18, 2023. The ChangeNOW route reviewed for this page is explicitly labeled HNT (SOLANA).'),
    ('What fees apply when converting Bitcoin to Helium?',
     'Costs depend on network conditions, liquidity, the exchange amount and rate mode. ChangeNOW says its costs are included in the estimate shown before the swap. To compare providers fairly, enter the same BTC amount and compare the final estimated HNT output rather than looking only at a headline fee.'),
    ('Should I choose a fixed or floating BTC-to-HNT rate?',
     'Choose fixed mode when receiving the agreed output is the priority and the live conditions are acceptable. Choose floating mode when you prefer the transaction to follow the market during processing. A floating result can differ from the initial estimate, while fixed mode may show a different starting quote.'),
    ('What happens if I enter the wrong HNT address or network?',
     'The payout may be sent to an incompatible destination and can be impossible to recover. Check that the wallet supports HNT on the exact network selected in the form, paste the address carefully and compare its first and last characters before starting the exchange. Contact support immediately if you notice an error, but recovery cannot be guaranteed.'),
    ('Which wallet can receive HNT?',
     'Use a wallet that supports Solana tokens and can display HNT. Copy the Solana receiving address directly from your wallet. Do not use a native Bitcoin address, an Ethereum 0x address or an unmigrated address from the old Helium blockchain.'),
    ('Which network will I receive HNT on?',
     'Use the network shown in the live exchange form as the authoritative answer. The ChangeNOW BTC-to-HNT page reviewed for this page shows HNT on Solana. Confirm this immediately before entering the receiving address because network availability and asset labels can change.'),
    ('Can I use an old Helium wallet address?',
     'Do not enter a legacy Helium L1 address without first completing the official migration process. Helium provides an L1 migration tool that maps or seeds old wallets for use on Solana. Follow the current official Helium instructions, then copy the Solana address from the migrated wallet.'),
    ('Can I cancel the exchange after sending Bitcoin?',
     'Usually not. Once the Bitcoin deposit has been broadcast and confirmed, the blockchain transfer cannot be reversed. Review the pair, amount, rate mode and receiving address before sending funds.'),
    ('Can I exchange Helium back to Bitcoin later?',
     'Yes, when the reverse HNT-to-BTC route is available. You will need a Bitcoin-compatible receiving address and enough HNT to meet the current minimum. Rates, liquidity and network conditions will be recalculated for the new transaction.'),
]

nav = [('#comparison', 'Comparison'), ('#reviews', 'Reviews'), ('#methodology', 'Methodology'),
       ('#how-to', 'How to Exchange'), ('#faq', 'FAQ')]

# ------------------------------------------------------------------ JSON-LD

graph = {
    '@context': 'https://schema.org',
    '@graph': [
        {'@type': 'WebPage', '@id': f'{SITE}#webpage', 'url': SITE, 'name': TITLE, 'description': DESCRIPTION,
         'inLanguage': 'en-US', 'datePublished': ISO_DATE, 'dateModified': ISO_DATE,
         'breadcrumb': {'@id': f'{SITE}#breadcrumbs'}},
        {'@type': 'ItemList', '@id': f'{SITE}#ranking', 'name': 'Best services for exchanging Bitcoin to Helium',
         'itemListOrder': 'https://schema.org/ItemListOrderAscending', 'numberOfItems': len(reviews),
         'itemListElement': [{'@type': 'ListItem', 'position': r['rank'], 'name': r['name'], 'url': f"{SITE}#{r['id']}"}
                             for r in reviews]},
        {'@type': 'FAQPage', '@id': f'{SITE}#faq',
         'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]},
        {'@type': 'BreadcrumbList', '@id': f'{SITE}#breadcrumbs',
         'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE},
                             {'@type': 'ListItem', 'position': 2, 'name': 'BTC to HNT Exchange', 'item': SITE}]},
    ],
}
jsonld = json.dumps(graph, ensure_ascii=False).replace('<', '\\u003c')

# ------------------------------------------------------------------ HTML parts


def arrows(t):
    return e(t).replace('→', ARR)


def fact_cells():
    return ''.join(f'<li><span class="hexdot" aria-hidden="true"></span><b>{e(v)}</b><span>{e(l)}</span></li>' for v, l in facts)


def cmp_head_html():
    out = []
    for i, h in enumerate(cmp_head):
        cls = 's1' if i == 0 else 's2' if i == 1 else ''
        out.append(f'<th scope="col" class="{cls}">{arrows(h)}</th>')
    return ''.join(out)


def cmp_body():
    out = []
    for r in cmp_rows:
        top = r[0] == '1'
        cells = [f'<td class="c-rank s1">{e(r[0])}</td>']
        badge = '<span class="pick">Best Overall</span>' if top else ''
        cells.append(f'<th scope="row" class="c-opt s2"><strong>{e(r[1])}</strong>{badge}</th>')
        for i, v in enumerate(r[2:], start=2):
            if i == len(r) - 1:
                cells.append(f'<td class="c-score"><span>{e(v)}</span></td>')
            else:
                cells.append(f'<td>{e(v)}</td>')
        out.append(f'<tr class="{"top" if top else ""}">{"".join(cells)}</tr>')
    return '\n'.join(out)


def review_card(r):
    facts_html = ''.join(f'<div><dt>{arrows(k)}</dt><dd>{e(v)}</dd></div>' for k, v in r['facts'])
    paras = ''.join(f'<p>{e(p)}</p>' for p in r['paras'])
    cta = f'<div class="rev-cta">{cn_link(r["cta"], "review", "btn btn-purple")}</div>' if r.get('cta') else ''
    feat = ' featured' if r.get('featured') else ''
    return f'''<article class="rev{feat}" id="{r['id']}">
  <div class="rev-head">
    <span class="rank-badge" aria-hidden="true"><b>{r['rank']}</b></span>
    <div><p class="award">{e(r['award'])}</p><h3>{e(r['name'])}</h3></div>
  </div>
  <div class="rev-body">
    {paras}
    <dl class="facts">{facts_html}</dl>
    <div class="notes">
      <div class="note-ok"><h4>Best for</h4><p>{e(r['best'])}</p></div>
      <div class="note-warn"><h4>Consideration</h4><p>{e(r['consider'])}</p></div>
    </div>
    {cta}
  </div>
</article>'''


def faq_items():
    out = []
    for i, (q, a) in enumerate(faq, start=1):
        out.append(f'''<div class="faq-item">
  <h3><button class="faq-q" type="button" id="faq-q{i}" aria-expanded="{'true' if i == 1 else 'false'}" aria-controls="faq-a{i}">{e(q)}</button></h3>
  <div class="faq-a" id="faq-a{i}" role="region" aria-labelledby="faq-q{i}"><p>{e(a)}</p></div>
</div>''')
    return '\n'.join(out)


why_html = ''.join(
    f'<div class="wcard"><span class="hexnum" aria-hidden="true"><b>{i}</b></span><h3>{e(t)}</h3><p>{e(b)}</p></div>'
    for i, (t, b) in enumerate(why_cards, start=1))
rate_html = ''.join(
    f'<div class="rcard"><span class="hexnum" aria-hidden="true"><b>{i}</b></span><h3>{e(t)}</h3><p>{e(b)}</p></div>'
    for i, (t, b) in enumerate(rate_cards, start=1))


def hex_meter(w):
    n = w // 5
    return ''.join('<i class="on"></i>' if k < n else '<i></i>' for k in range(5))


meter = ''.join(
    f'<li><span class="w-name">{e(n)}</span><span class="hexmeter" aria-hidden="true">{hex_meter(w)}</span><b>{w}%</b></li>'
    for n, w, _ in criteria)
crit_rows = ''.join(f'<tr><th scope="row">{e(n)}</th><td>{w}%</td><td>{e(d)}</td></tr>' for n, w, d in criteria)
vs_body = ''.join(f'<tr><th scope="row">{e(a)}</th><td>{rich(b)}</td><td>{rich(c)}</td></tr>' for a, b, c in vs_rows)
steps_html = ''.join(
    f'<li><span class="tl-num" aria-hidden="true"><b>{i}</b></span><div class="tl-card"><h3>{e(t)}</h3><p>{rich(b)}</p></div></li>'
    for i, (t, b) in enumerate(howto, start=1))
safety_html = ''.join(f'<li>{e(s)}</li>' for s in safety_items)

kickers = {
    'comparison-h': 'Comparison', 'why-h': 'Our verdict', 'reviews-h': 'Ranking', 'meth-h': 'Methodology',
    'how-h': 'Step by step', 'vs-h': 'Two networks', 'rates-h': 'Rates and timing', 'safety-h': 'Stay safe', 'faq-h': 'FAQ',
}

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESCRIPTION}">
<link rel="canonical" href="{SITE}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#F4F3FF">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{OG_DESCRIPTION}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{OG_DESCRIPTION}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preload" href="/fonts/sora-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/" aria-label="BTC to HNT Guide, home"><span class="logo-mark" aria-hidden="true"></span><span>BTC {ARR} HNT Guide</span></a>
    <nav class="nav-desktop" aria-label="Primary">{''.join(f'<a href="{h}">{t}</a>' for h, t in nav)}</nav>
    <div class="header-actions">
      {cn_link('Exchange BTC to HNT', 'header', 'btn btn-dark btn-sm')}
      <details class="menu">
        <summary aria-label="Open menu"><span class="burger" aria-hidden="true"></span></summary>
        <nav aria-label="Mobile">{''.join(f'<a href="{h}">{t}</a>' for h, t in nav)}</nav>
      </details>
    </div>
  </div>
</header>

<main id="main">

<section class="hero" aria-labelledby="h1">
  {hex_cluster()}
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="label"><i aria-hidden="true"></i>Independently scored using a published methodology</p>
      <h1 id="h1">Best Ways to Exchange Bitcoin to <span class="h-hnt">Helium</span> (BTC to HNT)</h1>
      <p class="lead"><a href="{CN}" target="_blank" rel="{CN_REL}" data-cta="hero">ChangeNOW is our best overall choice</a> for exchanging Bitcoin to Helium. It combines a direct three-step swap flow with fixed and floating rate options, upfront pricing, broad asset coverage and 24/7 support. Among the five services reviewed, it offers the strongest overall balance of route availability, transparency, speed and ease of use.</p>
      <ul class="chips">
        <li>Best overall score: 9.4/10</li>
        <li>Fixed and floating rates</li>
        <li>No account required for a standard swap</li>
        <li>24/7 human support</li>
      </ul>
      <div class="hero-actions">
        {cn_link('Exchange BTC to HNT on ChangeNOW', 'hero', 'btn btn-dark btn-lg hero-cta')}
        <a class="btn btn-light btn-lg" href="#comparison">See the comparison</a>
      </div>
      <p class="micro">Last reviewed: {REVIEWED}. Pair availability, minimum amounts and estimates can change. Check the live exchange form before sending funds.</p>
    </div>
    <a class="xcard" href="{CN}" target="_blank" rel="{CN_REL}" data-cta="hero" aria-label="Open the live ChangeNOW BTC to HNT exchange form">
      <span class="xcard-title">BTC to HNT exchange</span>
      <span class="xfield">
        <span class="xtext"><small>You send</small><b>BTC — Bitcoin</b></span>
        <span class="coin coin-btc" aria-hidden="true"><b>BTC</b></span>
      </span>
      <span class="xmid"><span class="swap" aria-hidden="true">↓</span><span>Live estimate available on ChangeNOW</span></span>
      <span class="xfield">
        <span class="xtext"><small>You receive</small><b>HNT — Helium</b></span>
        <span class="coin coin-hnt" aria-hidden="true"><b>HNT</b></span>
      </span>
      <span class="modes"><span>Floating rate</span><span class="dot" aria-hidden="true">·</span><span>Fixed rate available</span></span>
      <span class="btn btn-dark btn-block"><span>Check the live BTC/HNT rate</span></span>
      <span class="xnote">All costs are included in the estimate shown before the swap. Network and market conditions can affect the final result in floating-rate mode.</span>
    </a>
  </div>
</section>

<section class="strip-sec" aria-label="ChangeNOW figures">
  <div class="wrap">
    <ul class="strip">{fact_cells()}</ul>
    <p class="strip-note">ChangeNOW product figures. The Triumph Rate describes swaps completed at a better rate than estimated or with a deviation below 0.5%; it is not a promise that every swap will match its estimate.</p>
  </div>
</section>

<section class="sec" id="comparison" aria-labelledby="comparison-h">
  <div class="wrap">
    <div class="text-block">
      <h2 id="comparison-h">BTC to HNT Exchange Services Compared</h2>
      <p>We compared five services that support Bitcoin and Helium and checked whether a direct Bitcoin-to-Helium route was available. Each service was evaluated using the same weighted criteria: pair availability, quote transparency, exchange speed, ease of use, rate options, limits, coverage, support and public reputation. ChangeNOW currently identifies the destination as HNT on Solana. Route availability and the network can change, so confirm both in the live form before you send funds.</p>
      <p>Quotes change continuously, so we do not publish a static BTC/HNT rate in this table. Open the live form and compare the amount of HNT offered for the same BTC input immediately before starting an exchange.</p>
    </div>
    <div class="table-card" data-track="comparison">
      <div class="table-scroll" tabindex="0" role="region" aria-label="BTC to HNT exchange services comparison table">
        <table class="cmp">
          <caption class="sr">BTC to HNT exchange services compared</caption>
          <thead><tr>{cmp_head_html()}</tr></thead>
          <tbody>
{cmp_body()}
          </tbody>
        </table>
      </div>
    </div>
    <p class="table-note">“Account not required” does not mean that a transaction can never be reviewed. Exchange services may apply risk-based checks under their terms and policies. Availability and conditions can vary by transaction and jurisdiction.</p>
    <div class="verdict">
      <p><strong>Our verdict:</strong> ChangeNOW ranks first because it combines an available direct route, two rate modes, a clear three-step flow, no upper swap limit, broad multi-chain coverage and 24/7 support in one service.</p>
      {cn_link('Open ChangeNOW BTC to HNT Exchange', 'comparison', 'btn btn-orange')}
    </div>
  </div>
</section>

<section class="sec sec-dark" id="why-changenow" aria-labelledby="why-h">
  <div class="wrap">
    <div class="why-grid">
      <div class="why-text">
        <h2 id="why-h">Why ChangeNOW Is Our Best Overall BTC to HNT Exchange</h2>
        <p>ChangeNOW earned the highest score in our comparison because it performs well across the full exchange journey rather than winning on a single feature. The BTC-to-HNT route is presented in a clear form, users can choose between fixed and floating rates when both are available, and the expected output is shown before the deposit is sent.</p>
        <p>A standard exchange does not require an account. The process has three main stages: select the pair, amount and HNT network; enter a receiving address compatible with that network; then send Bitcoin to the generated deposit address. ChangeNOW states that all costs are built into the displayed rate, so there are no additional charges added after the swap.</p>
      </div>
      <div class="why-cards">{why_html}</div>
    </div>
    <div class="consider">
      <h3>What to consider</h3>
      <p>The one-minute figure published by ChangeNOW is an overall average, not a guaranteed completion time for every BTC-to-HNT transaction. Bitcoin confirmations, payout-network processing, liquidity and network congestion can extend the exchange. ChangeNOW says delivery is usually expected within one hour, but the live status page is the correct source for an active transaction.</p>
      {cn_link('Check the Current BTC to HNT Estimate', 'comparison', 'btn btn-orange')}
    </div>
  </div>
</section>

<section class="sec" id="reviews" aria-labelledby="reviews-h">
  <div class="wrap">
    <div class="text-block">
      <h2 id="reviews-h">The 5 Best Services for Exchanging Bitcoin to Helium</h2>
      <p>The services below support Bitcoin and Helium, but direct-route availability and the payout network can change. Rankings reflect the weighted methodology published further down the page, not a claim that one service will offer the highest live quote at every moment. Confirm every live form before sending funds.</p>
    </div>
    <div class="revs">{''.join(review_card(r) for r in reviews)}</div>
  </div>
</section>

<section class="sec sec-lav" id="methodology" aria-labelledby="meth-h" data-track="methodology">
  <div class="wrap">
    <div class="meth-top">
      <div class="meth-text">
        <h2 id="meth-h">How We Compared BTC to HNT Exchange Services</h2>
        <p>We reviewed services that support Bitcoin and Helium on {REVIEWED} and confirmed a direct BTC-to-HNT route where stated in the ranking. Every service was assessed using the same seven criteria. We prioritized the complete user journey rather than selecting a winner from a single headline fee or marketing claim.</p>
        <p>Live crypto quotes change from minute to minute. A fair price check uses the same BTC input, the same rate type and a narrow time window. Because a static quote would become outdated quickly, this page explains how to repeat the comparison immediately before exchanging.</p>
      </div>
      <div class="weights">
        <p class="weights-title">Scoring weights</p>
        <ul class="wlist">{meter}</ul>
        <p class="weights-key"><span class="hexkey" aria-hidden="true"></span> each hexagon = 5% of the total score</p>
      </div>
    </div>
    <div class="table-card">
      <div class="table-scroll" tabindex="0" role="region" aria-label="Comparison criteria table">
        <table class="crit">
          <caption class="sr">Comparison criteria, weights and evaluation method</caption>
          <thead><tr><th scope="col">Criterion</th><th scope="col">Weight</th><th scope="col">How it was evaluated</th></tr></thead>
          <tbody>{crit_rows}</tbody>
        </table>
      </div>
    </div>
    <div class="meth-bottom">
      <div class="meth-col">
        <h3>How to compare live quotes yourself</h3>
        <ol class="num-list">{''.join(f'<li>{e(s)}</li>' for s in compare_steps)}</ol>
      </div>
      <div class="meth-col">
        <h3>Limitations</h3>
        <p>Our review used publicly available service information and route-level forms. We did not send a real deposit through every provider. A displayed estimate is not the same as a completed-transaction result, particularly in floating-rate mode.</p>
        <h3>Why ChangeNOW won</h3>
        <p>ChangeNOW achieved the strongest combined score. It did not need to be the top service in every individual category. Its first-place result came from offering the direct route, two rate modes, an upfront estimate, broad coverage, no published upper swap limit, a simple three-step process and 24/7 support in one product.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="how-to" aria-labelledby="how-h">
  <div class="wrap how-grid">
    <div class="how-main">
      <h2 id="how-h">How to Exchange Bitcoin for Helium on ChangeNOW</h2>
      <p class="intro">The standard BTC-to-HNT flow has three main exchange stages, plus a final address, network and amount check before you start. You need a Bitcoin wallet with enough BTC for the deposit and a wallet that supports HNT on Solana. The reviewed ChangeNOW pair page labels the destination as “HNT (SOLANA).” Confirm the network again before every exchange and use a Solana address, not an old Helium L1 address.</p>
      <ol class="timeline">{steps_html}</ol>
      <p class="alert alert-warn"><strong>Important:</strong> A crypto exchange cannot normally be cancelled after you send the deposit. Blockchain transfers are irreversible, so verify the asset, network and address before sending BTC. HNT sent to an incompatible network or address may be permanently lost.</p>
    </div>
    <aside class="how-side" aria-label="Open the live exchange form">
      <div class="side-card">
        <h3>Ready to exchange?</h3>
        <p>Open the live ChangeNOW form to check the current minimum, estimate and rate modes.</p>
        {cn_link('Start BTC to HNT Exchange', 'how_to', 'btn btn-orange btn-block')}
      </div>
    </aside>
  </div>
</section>

<section class="sec sec-white" aria-labelledby="vs-h">
  <div class="wrap">
    <div class="vs-grid">
      <div class="vs-text">
        <h2 id="vs-h">What Changes When You Exchange BTC for HNT?</h2>
        <p>BTC is the native asset of the Bitcoin network. HNT is the native cryptocurrency and protocol token of the Helium Network, and it now operates as a token on Solana. Exchanging BTC for HNT is a cross-chain exchange: the service receives BTC on Bitcoin and sends HNT to the Solana address supplied by the user.</p>
        <h3>Why is HNT on Solana?</h3>
        <p>The Helium Network migrated from its purpose-built blockchain to Solana on April 18, 2023. Current HNT is therefore received and transferred on Solana. The official HNT mint address published by Helium is <code class="mint">{HNT_MINT}</code>. This is an informational reference only: copy your receiving address from your own supported wallet rather than interacting with a token contract manually. See the {link_out(DOC_HNT, 'official Helium HNT documentation')}.</p>
        <p>This operation is an exchange, not a native Bitcoin transfer and not a bridge that converts BTC into a wrapped version of Bitcoin. ChangeNOW receives BTC on the Bitcoin network and sends a separate HNT payout on Solana. Never send HNT to a Bitcoin address, Ethereum <code>0x</code> address or unmigrated legacy Helium L1 address.</p>
        <h3>What should owners of an old Helium wallet do?</h3>
        <p>Wallets created before the Solana migration may need to be migrated or seeded using Helium’s official L1 migration tools. This page does not provide its own migration instructions: follow the {link_out(DOC_MIGRATE, 'official Helium L1 migration documentation')} and finish the migration before entering a receiving address in an exchange form.</p>
      </div>
      <div class="table-card vs-table">
        <div class="table-scroll" tabindex="0" role="region" aria-label="Bitcoin and Helium comparison table">
          <table class="vs">
            <caption class="sr">Bitcoin and Helium compared</caption>
            <thead><tr><th scope="col">Feature</th><th scope="col"><span class="dot-btc" aria-hidden="true"></span>Bitcoin (BTC)</th><th scope="col"><span class="dot-hnt" aria-hidden="true"></span>Helium (HNT)</th></tr></thead>
            <tbody>{vs_body}</tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="rates-h">
  <div class="wrap">
    <div class="text-block"><h2 id="rates-h">BTC to HNT Rates, Fees and Exchange Time</h2></div>
    <div class="rcards">{rate_html}</div>
    <div class="rates-text">
      <div>
        <h3>Fixed rate or floating rate?</h3>
        <p>A floating rate follows the market while the exchange is processed, so the final HNT amount can differ from the initial estimate. A fixed rate is designed to preserve the agreed output when the exchange conditions are met. Fixed mode may use a different estimate because the provider takes on short-term rate risk.</p>
        <p>Choose based on your priority: potential market movement in floating mode or greater output certainty in fixed mode. Always read the live terms before sending BTC.</p>
      </div>
      <div>
        <h3>Is there a minimum or maximum amount?</h3>
        <p>The live minimum changes with the pair, network costs and liquidity. ChangeNOW says minimum amounts can be as low as the equivalent of $2, but the BTC-to-HNT form is the authoritative source for the current transaction. ChangeNOW does not publish an upper limit for standard crypto-to-crypto swaps.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-pad-sm" aria-labelledby="safety-h">
  <div class="wrap">
    <div class="safety">
      <h2 id="safety-h">BTC to HNT Safety Checklist</h2>
      <p class="safety-intro">Complete these checks before sending Bitcoin. Most address and network mistakes cannot be reversed.</p>
      <ul class="checklist">{safety_html}</ul>
      <p class="alert alert-dark">Never send funds based on an address received through an unsolicited message, social-media reply or search advertisement. Start from the official exchange page and verify the domain.</p>
    </div>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-h" data-track="faq">
  <div class="wrap faq-wrap">
    <h2 id="faq-h">Frequently Asked Questions</h2>
    <div class="faq">
{faq_items()}
    </div>
  </div>
</section>

<section class="sec-final" aria-labelledby="final-h">
  <div class="wrap">
    <div class="final">
      <div class="final-left">
        <p class="label label-light"><i aria-hidden="true"></i>Our #1 BTC to HNT choice</p>
        <h2 id="final-h">Exchange Bitcoin to Helium with ChangeNOW</h2>
        <p>ChangeNOW ranks first in our comparison for its direct BTC-to-HNT route, fixed and floating rate options, upfront estimate, simple exchange flow and 24/7 support. Open the live form to check the current minimum and expected HNT output before sending funds.</p>
      </div>
      <div class="final-right">
        {cn_link('Check the Live BTC to HNT Rate', 'final', 'btn btn-orange btn-lg')}
        <p>Crypto prices and estimates can change. Verify the address, rate mode and expected output before confirming the exchange.</p>
      </div>
    </div>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <p class="foot-h">About</p>
      <p><strong>BTC {ARR} HNT Guide</strong><br>A focused comparison resource for users researching how to exchange Bitcoin for Helium.</p>
    </div>
    <div>
      <p class="foot-h">Page links</p>
      <ul class="foot-links">{''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in nav)}</ul>
    </div>
    <div>
      <p class="foot-h">Disclosures</p>
      <p>Rankings are based on the published methodology and information available on the review date. Availability, estimates, limits and service terms can change.</p>
      <p>Cryptocurrency transactions involve price, network, liquidity and operational risks. This page provides general information and is not financial, investment, legal or tax advice. Blockchain transfers are irreversible. Verify all transaction details independently.</p>
      <p><strong>Affiliate disclosure:</strong> We may earn a commission when you use links on this page. This does not change the price you pay. Rankings are based on the methodology and data described above.</p>
    </div>
  </div>
  <div class="wrap copy">© 2026 BTC {ARR} HNT Guide. All rights reserved.</div>
</footer>

<div class="sticky-cta" id="sticky-cta" aria-hidden="true">
  <span>Best overall: ChangeNOW</span>
  <a class="btn btn-orange btn-sm" href="{CN}" target="_blank" rel="{CN_REL}" data-cta="mobile_sticky" tabindex="-1"><span>Exchange BTC to HNT</span></a>
</div>

<script src="/assets/app.js" defer></script>
</body>
</html>
'''

for hid, label in kickers.items():
    tag = f'<h2 id="{hid}">'
    assert tag in html, hid
    html = html.replace(tag, f'<p class="kicker" aria-hidden="true">{label}</p>{tag}', 1)

# ------------------------------------------------------------------ write

OUT.mkdir(exist_ok=True)
(OUT / 'assets').mkdir(exist_ok=True)
(OUT / 'fonts').mkdir(exist_ok=True)
for f in ('style.css', 'app.js'):
    shutil.copy2(SRC / f, OUT / 'assets' / f)
shutil.copy2(SRC / 'assets' / 'btc-to-hnt-guide.webp', OUT / 'assets' / 'btc-to-hnt-guide.webp')
(OUT / 'assets' / 'hex-light.svg').write_text(hex_tile('#474DFF', '.16'))
(OUT / 'assets' / 'hex-dark.svg').write_text(hex_tile('#FFFFFF', '.16'))
for f in (SRC / 'fonts').iterdir():
    shutil.copy2(f, OUT / 'fonts' / f.name)
(OUT / 'index.html').write_text(html)
(OUT / 'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#F4F3FF"/><polygon points="32,6 54,19 54,45 32,58 10,45 10,19" fill="#474DFF"/><polygon points="32,22 44,29 44,43 32,50 20,43 20,29" fill="#F7931A"/></svg>\n')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f'  <url>\n    <loc>{SITE}</loc>\n    <lastmod>{ISO_DATE}</lastmod>\n  </url>\n</urlset>\n')
print('built', OUT / 'index.html', len(html), 'bytes')

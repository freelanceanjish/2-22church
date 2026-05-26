// ============================================================
//  2:22 CHURCH, BLOG POSTS DATA FILE
//  ============================================================
//  HOW TO ADD A NEW POST:
//  1. Copy the template block at the bottom of this file
//  2. Paste it at the TOP of the posts array (so newest shows first)
//  3. Fill in all the fields
//  4. Save the file and push to GitHub, your post is live!
//
//  HOW TO DELETE A POST:
//  Simply remove the entire { ... } block for that post.
//
//  CATEGORIES (use one of these exactly):
//  "Teaching" | "Baptism" | "Service" | "Giving" | "Community"
//  | "Prayer" | "Testimony" | "Leadership" | "Reflection"
// ============================================================

const POSTS = [
  {
    id: "the-seed-and-the-shadow",
    title: "The Seed and the Shadow",
    date: "26 May 2026",
    category: "Teaching",
    image: "bg-blog.jpg",
    excerpt: "Nations wage wars, churches write cheques, and theologians draft endless justifications — all in the name of a covenant whose finest detail has been quietly overlooked. That detail is a single word: Seed. A word the Apostle Paul identified as the singular key that unlocks every promise God ever made to Abraham.",
    content: `
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --ink: #1a1714;
    --ink-mid: #3d3830;
    --ink-soft: #7a7268;
    --ink-faint: #b5ae9f;
    --parchment: #f9f5ed;
    --parchment-mid: #f0e9d8;
    --parchment-dark: #e2d9c5;
    --gold: #8b6914;
    --gold-light: #c9a84c;
    --rule: #d4cbb5;
    --serif: 'EB Garamond', Georgia, serif;
    --display: 'Cormorant Garamond', Georgia, serif;
    --sans: 'DM Sans', system-ui, sans-serif;
  }

  html { scroll-behavior: smooth; }

  body {
    background-color: var(--parchment);
    color: var(--ink);
    font-family: var(--serif);
    font-size: 20px;
    line-height: 1.85;
    min-height: 100vh;
  }

  /* ── Masthead ── */
  .masthead {
    background: var(--ink);
    color: var(--parchment-mid);
    text-align: center;
    padding: 4rem 2rem 3.5rem;
    position: relative;
    overflow: hidden;
  }

  .masthead::before {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 39px,
      rgba(255,255,255,0.03) 39px,
      rgba(255,255,255,0.03) 40px
    );
    pointer-events: none;
  }

  .masthead-kicker {
    font-family: var(--sans);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--gold-light);
    margin-bottom: 1.5rem;
  }

  .masthead h1 {
    font-family: var(--display);
    font-weight: 300;
    font-size: clamp(2.8rem, 7vw, 5.5rem);
    line-height: 1.1;
    color: var(--parchment);
    letter-spacing: -0.01em;
    margin-bottom: 0.4rem;
  }

  .masthead h1 em {
    font-style: italic;
    color: var(--gold-light);
  }

  .masthead-sub {
    font-family: var(--display);
    font-weight: 300;
    font-style: italic;
    font-size: clamp(1.1rem, 2.5vw, 1.5rem);
    color: var(--ink-faint);
    margin-top: 1rem;
    margin-bottom: 2.5rem;
  }

  .masthead-rule {
    width: 60px;
    height: 1px;
    background: var(--gold);
    margin: 0 auto;
  }

  /* ── Layout ── */
  .article-wrap {
    max-width: 720px;
    margin: 0 auto;
    padding: 4rem 2rem 6rem;
  }

  /* ── Drop cap & opening ── */
  .opening {
    font-size: 1.15em;
    color: var(--ink-mid);
    border-left: 3px solid var(--gold);
    padding-left: 1.5rem;
    margin-bottom: 3rem;
    font-style: italic;
  }

  /* ── Body prose ── */
  p {
    margin-bottom: 1.6rem;
    color: var(--ink-mid);
  }

  p:first-of-type::first-letter {
    font-family: var(--display);
    font-size: 4.2rem;
    font-weight: 400;
    line-height: 0.8;
    float: left;
    margin: 0.12em 0.1em -0.05em 0;
    color: var(--ink);
  }

  /* ── Section headings ── */
  .section {
    margin-top: 3.5rem;
    margin-bottom: 2rem;
  }

  .section-num {
    font-family: var(--sans);
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    display: block;
    margin-bottom: 0.5rem;
  }

  .section h2 {
    font-family: var(--display);
    font-weight: 400;
    font-size: clamp(1.6rem, 3.5vw, 2.2rem);
    line-height: 1.2;
    color: var(--ink);
    letter-spacing: -0.01em;
  }

  .section h2 em {
    font-style: italic;
    color: var(--ink-soft);
  }

  /* ── Scripture blocks ── */
  .scripture {
    background: var(--parchment-dark);
    border-left: 3px solid var(--gold);
    padding: 1rem 1.5rem;
    margin: 1.8rem 0;
    border-radius: 0 4px 4px 0;
  }

  .scripture p {
    font-style: italic;
    font-size: 0.95em;
    color: var(--ink);
    margin-bottom: 0.3rem;
  }

  .scripture p:last-child { margin-bottom: 0; }

  .scripture-ref {
    font-family: var(--sans);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--gold);
    display: block;
    margin-top: 0.6rem;
  }

  /* ── Pull quote ── */
  .pullquote {
    text-align: center;
    padding: 2.5rem 1rem;
    margin: 3rem -1rem;
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
  }

  .pullquote p {
    font-family: var(--display);
    font-size: clamp(1.4rem, 3vw, 1.9rem);
    font-weight: 300;
    font-style: italic;
    line-height: 1.4;
    color: var(--ink);
    margin: 0;
  }

  .pullquote p::before { content: '\201C'; color: var(--gold-light); }
  .pullquote p::after  { content: '\201D'; color: var(--gold-light); }

  /* ── Key terms inline ── */
  .term {
    font-style: italic;
    color: var(--ink);
  }

  /* ── Irony callout ── */
  .irony-box {
    background: var(--ink);
    color: var(--parchment-mid);
    padding: 1.8rem 2rem;
    margin: 2.5rem 0;
    border-radius: 6px;
  }

  .irony-box .irony-label {
    font-family: var(--sans);
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--gold-light);
    margin-bottom: 0.8rem;
    display: block;
  }

  .irony-box p {
    color: var(--parchment-mid);
    font-size: 0.95em;
    margin-bottom: 0;
  }

  /* ── Sub-points ── */
  .point {
    padding: 1.2rem 0 1.2rem 1.5rem;
    border-left: 1px solid var(--rule);
    margin: 1.2rem 0;
  }

  .point-label {
    font-family: var(--sans);
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--gold);
    display: block;
    margin-bottom: 0.4rem;
  }

  .point p {
    margin-bottom: 0;
    font-size: 0.95em;
  }

  /* ── Divider ── */
  .divider {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 3rem 0;
  }

  .divider::before,
  .divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--rule);
  }

  .divider-mark {
    color: var(--gold);
    font-size: 1.1rem;
    font-family: var(--display);
  }

  /* ── Conclusion ── */
  .conclusion {
    background: var(--parchment-dark);
    border: 1px solid var(--rule);
    border-radius: 6px;
    padding: 2.5rem;
    margin-top: 3.5rem;
  }

  .conclusion-label {
    font-family: var(--sans);
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 1.2rem;
    display: block;
  }

  .conclusion h3 {
    font-family: var(--display);
    font-weight: 400;
    font-size: 1.6rem;
    margin-bottom: 1rem;
    color: var(--ink);
  }

  .conclusion p {
    font-size: 0.95em;
  }

  .three-truths {
    margin: 1.5rem 0 0;
    list-style: none;
    counter-reset: truths;
  }

  .three-truths li {
    counter-increment: truths;
    display: flex;
    gap: 1rem;
    margin-bottom: 0.8rem;
    font-size: 0.95em;
    color: var(--ink-mid);
  }

  .three-truths li::before {
    content: counter(truths);
    font-family: var(--display);
    font-size: 1.4rem;
    color: var(--gold);
    line-height: 1;
    flex-shrink: 0;
    width: 1.4rem;
  }

  /* ── Footer ── */
  footer {
    text-align: center;
    padding: 2rem;
    font-family: var(--sans);
    font-size: 12px;
    letter-spacing: 0.1em;
    color: var(--ink-faint);
    border-top: 1px solid var(--rule);
  }

  @media (max-width: 600px) {
    .article-wrap { padding: 2.5rem 1.25rem 4rem; }
    .pullquote { margin: 2rem 0; }
    .masthead { padding: 2.5rem 1.25rem 2rem; }
  }
</style>
<p class="opening">
    The people fighting for the "dirt" are using the name of a man who refused to settle for it — because he was looking at the stars.
  </p>

  <p>There is a remarkable irony at the centre of modern biblical debate. Nations wage wars, churches write cheques, and theologians draft endless justifications — all in the name of a covenant whose finest detail has been quietly overlooked. That detail is a single word. A word the Apostle Paul identified as the singular key that unlocks every promise God ever made to Abraham. The word is <span class="term">Seed</span>.</p>

  <p>Paul's statement in Galatians 3:16 is not tentative. It is surgical: <em>"Now the promises were made to Abraham and to his offspring. It does not say, 'And to offsprings,' referring to many, but referring to one, 'And to your offspring,' who is Christ."</em> Paul is not offering an interpretation. He is announcing a legal fact. The covenant was made to a specific, singular recipient: Yeshua — the Christ. Everything else flows from this.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="section">
    <span class="section-num">Part I</span>
    <h2>The Covenant Reread: <em>The Seed is a Person</em></h2>
  </div>

  <p>Once Paul's key is applied, the Genesis covenant passages transform entirely. What appeared to be a series of ethnic land-grants to a biological lineage reveals itself as something far more precise — a royal deed, issued to a specific King, who had not yet arrived.</p>

  <div class="scripture">
    <p>"To your offspring I will give this land." — "Blessing I will bless you, and multiplying I will multiply your offspring as the stars of the heaven and as the sand which is on the seashore; and your offspring shall possess the gate of his enemies."</p>
    <span class="scripture-ref">Genesis 12:7 · 22:17</span>
  </div>

  <p>Notice the tension built into these verses from the beginning. In one breath the offspring is compared to the dust — countable grains — and in the next, to the stars of heaven. Abraham himself understood this tension. The Letter to the Hebrews tells us plainly that he was <em>"looking forward to the city that has foundations, whose designer and builder is God."</em> He was not anchoring his hope to a parcel of land between the Nile and the Euphrates. He was looking past the dirt, toward something celestial.</p>

  <div class="irony-box">
    <span class="irony-label">The Central Irony</span>
    <p>If the Seed is singular and eternal, then "forever" only makes sense when the recipient is a Person who transcends time. A biological population dies, scatters, and ends. A King who rises from the dead does not. The promise requires an immortal recipient — and only one candidate qualifies.</p>
  </div>

  <p>The word translated "forever" — <em>olam</em> — carries the weight of perpetuity. It is the same word applied to God's own covenant relationship. For such a promise to hold, the recipient must be capable of enduring forever. This is not a description of any ethnic group. It is a description of Yeshua alone.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="section">
    <span class="section-num">Part II</span>
    <h2>Union with the Seed: <em>One Body, One Inheritance</em></h2>
  </div>

  <p>If the promise belongs to Yeshua, the natural question follows: what of his followers? The New Testament answers this with a concept of breathtaking depth — the union of the believer with Christ. This is not metaphor or devotional warmth. It is presented by the Apostles as a legal and ontological reality.</p>

  <p>When Yeshua appeared to the persecutor Saul on the Damascus road, he did not ask, <em>"Why are you persecuting my followers?"</em> He asked: <em>"Why are you persecuting Me?"</em> (Acts 9:4). The people Saul was imprisoning and killing were not separate from Yeshua. Their pain was His pain. Their bodies were, in some inexpressible way, His body.</p>

  <p>Paul builds this logic into a formal doctrine. In 1 Corinthians 12, he writes that the Church <em>is</em> the body of Christ — not merely resembles it, not is spiritually close to it, but <em>is</em> it. Each believer is a member, as a hand or eye is a member of a living body. There is only one body. There is only one Seed.</p>

  <div class="pullquote">
    <p>A branch has no independent right to the soil. It draws life only because it remains attached to the Vine. The moment it severs itself from the root, it ceases to carry the promise.</p>
  </div>

  <p>The most explicit statement comes in Galatians 3:27–29: <em>"For as many of you as were baptized into Christ have put on Christ… And if you are Christ's, then you are Abraham's offspring, heirs according to promise."</em> Paul has collapsed the distance entirely. There is no second route to Abraham's covenant. There is no alternative track, no DNA-based bypass. The only path into the Seed is through the Seed himself.</p>

  <p>This transforms the nature of inheritance. Believers do not inherit the land because of their genealogy. They inherit it because they are legally part of the Person who owns it — clothed in Him, as Paul says, like a garment grants entry into the King's court.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="section">
    <span class="section-num">Part III</span>
    <h2>The Redefinition of Israel: <em>Nation of Faith, Not Flesh</em></h2>
  </div>

  <p>With the identity of the Seed established, the New Testament proceeds to methodically redefine the word <span class="term">Israel</span> itself. This is not a fringe theological maneuver. It is the explicit, sustained argument of Yeshua and all of his Apostles.</p>

  <div class="point">
    <span class="point-label">Romans 9:6–8</span>
    <p>Paul announces the governing principle: <em>"For they are not all Israel who are descended from Israel."</em> The name "Israel" is not coextensive with a genetic population. Something more is required. That something is faith — participation in the promise through union with the Seed.</p>
  </div>

  <div class="point">
    <span class="point-label">Romans 2:28–29</span>
    <p>Paul presses further: a true Jew is one <em>inwardly</em>, and true circumcision is of the heart, by the Spirit. By this measure, a Gentile who belongs to Yeshua is more authentically "Jewish" before God than a biological descendant who walks in lawlessness.</p>
  </div>

  <div class="point">
    <span class="point-label">1 Peter 2:9</span>
    <p>Peter seals the argument by taking the titles once reserved exclusively for the physical nation — <em>"chosen race, royal priesthood, holy nation, a people for his own possession"</em> — and transferring them wholesale to the community of believers.</p>
  </div>

  <p>This transfer is not additive. Peter is not creating a second Israel running parallel to the first. He is announcing that the substance has arrived and the shadow is passing away. The "holy nation" God was always building was never a country with borders and a flag. It was a global, spiritual kingdom gathered from every tongue, tribe, and people — defined not by soil or bloodline, but by faith in and union with the Seed.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="section">
    <span class="section-num">Part IV</span>
    <h2>The Shadow Mistaken for the Substance: <em>1948 and the Dispensationalist Claim</em></h2>
  </div>

  <p>Against this background, the dominant modern Christian justification for the political state established in 1948 presents a significant theological collision. Millions of believers, shaped by a relatively recent doctrinal framework known as Dispensationalism, read passages like Ezekiel 37 — the vision of dry bones assembled into a nation — and conclude that the return of Jewish populations to the land of Canaan is a direct fulfillment of God's promise to gather "His people."</p>

  <p>The argument is intuitive at first glance. A people scattered for two thousand years return to the same geographical coordinates. The same language is revived. The same name is restored. Surely this is the hand of God keeping his covenant with the physical descendants of Abraham?</p>

  <p>But this reading stands or falls on a prior question: <em>who is the Seed?</em> If Paul is correct — and the New Testament treats him as speaking under divine authority — then the covenant was never made to a biological population in the first place. It was made to a single Person. Any claim to the covenant's blessings that bypasses that Person is, in legal terms, a claim made outside the contract.</p>

  <div class="irony-box">
    <span class="irony-label">The Theological Collision</span>
    <p>Those who use these verses to justify 1948 are claiming the blessings of the Seed for people who, in many cases, explicitly reject the Seed himself. They are treating Yeshua as incidental to a covenant in which, according to Paul, he is the sole named heir. This is not a minor interpretive difference. It is a fundamental inversion of the New Covenant.</p>
  </div>

  <p>Furthermore, the "gathering" language of the prophets, read through Paul's lens, points not to an airport in Tel Aviv but to the gathering of souls from every nation into the Body of Christ. The "nation" being assembled is not a geopolitical entity; it is the one new man that Yeshua came to create — Jew and Gentile together, the dividing wall demolished, reconciled in one body (Ephesians 2:14–15).</p>

  <p>Yeshua himself drew the distinction plainly in Matthew 21, when he told the religious custodians of the physical nation: <em>"The kingdom of God will be taken away from you and given to a people producing its fruits."</em> He did not say it would be paused for two millennia and then handed back to a secular state. He announced a transfer — to a new people defined by fruitfulness, not ancestry.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="section">
    <span class="section-num">Part V</span>
    <h2>One Tree, No Second Track: <em>The Apostolic Rejection of Parallelism</em></h2>
  </div>

  <p>Perhaps the deepest problem with the modern Christian Zionist framework is the "dual-track" it implies — the notion that God maintains two simultaneous, parallel plans: one for a secular ethnic nation and one for a spiritual Church. The New Testament does not merely fail to support this idea. It systematically dismantles it.</p>

  <p>Paul's image in Romans 11 is a single olive tree. Not two trees. There is one trunk, one root, one source of nourishment. Some natural branches have been broken off; wild branches have been grafted in. But there is only ever one tree. If you are not attached to the root — to the Seed — you are not part of the covenant, regardless of what your genealogy says.</p>

  <p>Dispensationalism, which took formal shape around the 1830s, effectively attempts to reconstruct the very dividing wall that Paul says Yeshua destroyed at the cross. It creates a category of divine favoritism based on ethnicity — precisely the kind of partiality that Acts 10:34 declares God does not show, and that Galatians 3:28 declares the Gospel has ended: <em>"There is neither Jew nor Greek… for you are all one in Christ Jesus."</em></p>

  <p>Paul makes the consequence explicit in Galatians 4, using the allegory of Hagar and Sarah. The earthly Jerusalem — characterized by bondage to flesh and political power — corresponds to Hagar and her son of the flesh. The heavenly Jerusalem — the city Abraham was always seeking — corresponds to Sarah and the son of promise. Paul's conclusion is unambiguous: <em>"Cast out the slave woman and her son, for the son of the slave woman shall not inherit with the son of the free woman."</em></p>

  <p>The ultimate irony is that the very entity many churches are funding today is, by Paul's own typology, the son of the flesh. While the Israel of God — the body of those who are in the Seed — is the son of the promise.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="section">
    <span class="section-num">Part VI</span>
    <h2>The Temple and the Body: <em>Chasing the Shadow into Stone</em></h2>
  </div>

  <p>The contradiction sharpens when we turn to the movement for a Third Temple in Jerusalem. Here, certain segments of American Christianity have not merely endorsed a political state — they have begun funding the reconstruction of a religious institution whose entire purpose was to point forward to Yeshua, and which Yeshua himself declared superseded.</p>

  <p>Paul warns in Colossians 2:17 that the rituals, sabbaths, temples, and festivals of the old order are <span class="term">a shadow of things to come, but the substance belongs to Christ.</span> The shadow was real and necessary — it was given by God to teach a people to recognize the shape of the One who was coming. But when the substance arrives, to keep pursuing the shadow is not faithfulness. It is a refusal to look up.</p>

  <p>The Letter to the Hebrews extends this with surgical precision. The old covenant — which included the temple, its priesthood, and its sacrificial system — is declared <em>"obsolete and growing old"</em> (Hebrews 8:13). The author's word for "obsolete" is not gentle. It means rendered void, displaced, set aside. And the reason it has been displaced is that the <em>once-for-all</em> sacrifice of Yeshua has accomplished what ten thousand animal sacrifices could only gesture toward.</p>

  <p>For American churches to fund the breeding of red heifers, the reconstruction of temple vessels, and the revival of a priesthood is — from within their own scriptures — to financially support a return to a system that the New Testament declares terminated by the death of the Seed himself. They are, in effect, writing cheques to the shadow, while standing with their backs turned to the Light that cast it.</p>

  <div class="divider"><span class="divider-mark">✦</span></div>

  <div class="conclusion">
    <span class="conclusion-label">Conclusion</span>
    <h3>Stars, Not Dirt</h3>

    <p>Abraham was shown two things: the dust of the earth and the stars of the sky. He was told his Seed would be like both. But Abraham himself chose to look upward. He <em>"went out, not knowing where he was going,"</em> because he was <em>"looking forward to the city that has foundations, whose designer and builder is God."</em> He never received the land. He never built a house on it. He died a stranger and pilgrim — and the New Testament celebrates this not as his failure, but as his greatest act of faith.</p>

    <p>The covenant was always about the stars, not the dirt. It was always about an eternal King, not a temporary population. It was always pointing toward the day when the Heavenly Jerusalem — the City of the Living God — would descend, and the meek would inherit not one sliver of contested land, but the whole renewed earth.</p>

    <p>Those who invoke Abraham's name to justify earthly conquest in his name have, with great sincerity and great confusion, missed the very point Abraham himself never missed. They are fighting over the shadow. Abraham was walking toward the Substance.</p>

    <ul class="three-truths">
      <li>Israel-the-State is a secular political entity — it is not, and cannot be, a party to a covenant made with the singular Seed who it rejects.</li>
      <li>Israel-the-People are those who are in the Seed: the body of Christ, drawn from every nation, defined by faith and not by flesh.</li>
      <li>The Land is the whole earth, to be inherited not by military conquest but by the arrival of the Heavenly Jerusalem — when the Seed, seated at the right hand of the Father, returns to claim what was always His.</li>
    </ul>
  </div>
    `
  },
  {
    id: "autopsy-of-a-soul",
    title: "Autopsy of a Soul",
    date: "7 May 2026",
    category: "Testimony",
    image: "autopsy_of_soul.svg",
    excerpt: "I was saved in 2009. I was sincere. But salvation is not a transaction that ends the moment you say yes to it. In the darkest hour, in the driest period, in the deepest bottom, God was designing something. He calls it an autopsy of the soul.",
    image: "autopsy_of_soul.svg",
    content: `
<p>I was saved in 2009. I was sincere. I remember the hunger of those early years, the desire to know the Lord, to follow Him, to be close to Him. That was real. I do not doubt it. But salvation is not a transaction that ends the moment you say yes to it. Who said once saved, always saved? That is not scriptural. Faith is a living thing, held in close cooperation with God, and it demands everything you have, including the parts of yourself you have not yet had the courage to look at. We are always in the Lord's factory, always being built into the character of Yeshua, which means we are always being exposed to our own darkness, not as punishment, but as the necessary work of a God who loves us too much to leave us as we are.</p>

<p>When I left my parents' home and stepped into the world as my own man, I thought I was ready. Then in 2013 I started working, and something shifted. The soul, unguarded, finds its distractions. Solomon knew this. A man of wisdom and devotion, and yet his heart was drawn away by the women he loved, women whose gods were not his God. I found myself on a similar road, not in the same measure, but on the same road. I moved through multiple relationships before marriage, each one a search for rest and alignment, for someone who would finally settle the weight I had been carrying. Some of these women had no interest in my faith. Others wore the mask of belief just long enough for me to lose my footing, and by the time I understood what had happened, it was already too late.</p>

<p>God warned Samson. He warns all of us. But the warnings are easier to hear than to heed when the heart is pulling in a different direction. Those relationships left shadows on my soul, patterns of thinking and relating that I had not chosen but had absorbed, wounds that I carried forward without knowing their shape. Their personalities pressed into mine, and mine into theirs, and the man who came out the other side was carrying more than he knew.</p>

<p>Then I found my wife. A woman with an extraordinary testimony of her own, someone who had genuinely encountered the Saviour and whose faith was not borrowed or performed. I loved her and I married her, and I meant every word of what I said. But I brought all of it into that marriage with me, the scars, the patterns, the undealt wounds from years of searching in the wrong places. I had sincere intent to serve the Lord, and I did serve Him, in India and outside India, giving what I had. But man, oh man. How deep is the soul of a man. Only the Spirit of God can reach those rooms, and He does not rush. He waits until we are still enough to let Him in.</p>

<p>When the COVID lockdown came, my wife and I spent that year in my homeland with my parents. It was the first time in a long while that I had been forced to slow down. Then, four years ago, we moved to Belgium together, and I began what felt like the real chapter, a foreign country, a fresh start, a life being built from the ground up. I worked. I struggled with authority as I always had. I changed roles and companies and environments, always telling myself the problem was around me rather than within me.</p>

<p>In June 2024, my first daughter was born, and something in me shifted with her arrival in a way I had not expected. Then in October of that same year, my employer told me to leave. I found another position, but there too I met heavy rejection from authority, confusion at every level, and eventually I was asked to step down and enter performance training. I had seen it coming, and instead of humbling myself and receiving it, I walked away. Since that day, nothing has opened. No door, no favour, no ground to stand on.</p>

<p>What followed was a kind of stripping I had never imagined for myself. I had to leave the apartment we had made into a home. I sold my daughter's things, the furniture we had gathered, and the car. I packed what remained and flew back to my homeland, back to the house I had once left with great confidence in God. I moved back in with my parents, who are unbelievers, and I had no choice in the matter and nowhere else to turn.</p>

<p>My father, the man who once burned my Bible, cursed the name of Jesus, and tore up my notes while I watched, became the one putting groceries on our table. God gave a contract to my unbelieving father just to keep me alive, and I sat across from him at meals while he questioned my faith, and I had no answer that felt honest. There was nowhere else to go, and I have come to understand that this was precisely the point. The Lord was not punishing me. In the darkest hour, in the driest period, in the unanswered prayers and the unopened doors and the deepest bottom, He was designing something. He was taking me to a separate room to operate. His love separates us from everything that is noise, and quietly, without asking our permission, begins the work.</p>

<blockquote>"O God, You have rejected us and broken our defenses; You have been angry. O, restore us.", Psalm 60:1</blockquote>

<p>That verse became mine. He had broken every defense I had built, every wall of pride, every strategy, every plan I had made for my own life. Not because He had abandoned me, but because He was answering a prayer deeper than the ones I had been praying. He was restoring me.</p>

<blockquote>"It is good for me that I have been afflicted, that I may learn Your statutes.", Psalm 119:71</blockquote>

<p>I did not understand this verse when I first read it. A man saying it is good that he suffered? But I understand it now. The affliction was the lesson. The emptiness was the curriculum. The shame was the classroom. I could not have learned what God needed to teach me in any other school.</p>

<p>There, in that enforced stillness, I finally stopped running long enough to perform an autopsy on my own soul. What I found was not easy to name. Procrastination. Authority issues. A dual and confused mind that could never quite settle. A heart of lust tied to masturbation and pornography, carried quietly for years behind a different public face. Arrogance, anger, and jealousy. And underneath everything, my deepest trap: a subtle and dangerous pride that had convinced me, for most of my adult life, that I knew more than my seniors. I was never truly at peace with those above me. What I called principle and righteous conviction was, most of the time, my ego, and it had been costing me everything.</p>

<p>The breaking point that cracked me open was my daughter. Seeing her being drawn toward the idols my parents keep in their house broke something in me that nothing else had reached, and I cried out to the Lord for rescue. It felt at first as though nothing was changing, but God was already moving beneath everything I could see.</p>

<p>My wife and I humbled ourselves and moved to her parents' house for the final months of her pregnancy. Our marriage had been fracturing under the weight of my pride and her arrogance, with no real submission between us and a great deal of fighting. But God settled us in that season. She gave up her branded clothes and the modern way of living she had grown used to, and she began stitching her own clothes, embracing modesty, and serving her mother-in-law in the kitchen. I watched a woman I had genuinely wounded choose humility when she had every reason not to, and it undid something deep in me.</p>

<p>As for me, I placed myself under my strict and authoritative father-in-law, without conditions and without argument. I water his garden, clean his car, and serve him in whatever way he needs. I have opened my heart to the people the world tends to pass over, the delivery boy, the waiter, the shopkeeper, the cleaner, people I once moved past without a second thought who now feel, genuinely, like brothers. I am finally paying my obligations and taking responsibility for the things I had been avoiding for years.</p>

<p>God used two books as particular instruments to show me what had been hiding in my heart. The first was <em>Introduction to the Devout Life</em> by Francis de Sales, and the second was <em>A Tale of Three Kings</em> by Gene Edwards. Together they showed me plainly that I had been acting like a rebel king while calling it righteousness. The image of David refusing to raise his hand against Saul, even when Saul was clearly wrong, even when David had every justification, stayed with me for weeks. I had spent years raising my hand against every Saul in my life and telling myself that was discernment. God wanted a servant's heart from me, and I had been trying to offer Him a throne.</p>

<blockquote>"Whoever wants to become great among you must be your servant, and whoever wants to be first must be your slave.", Matthew 20:26-27</blockquote>

<p>It is not finished. I recently found myself speaking angrily to my father when he would not listen to my instructions about my daughter, and the old man in me rose up with that familiar heat. But this time I did not justify it. My own rebellion broke my heart, and I went back to God with nothing to offer except the honest confession that I had gone astray again.</p>

<p>I am living in dryness, in a situation the world would call shameful, with no title, no platform, and no visible proof that any of this is producing anything. But for the first time in as long as I can remember, my mind is not at war with itself. I am waiting on the Lord. I am finding, in the middle of these empty places, a peace I was always running too fast to receive.</p>

<p>Was David spared from his darkest chapter? Was Moses exempt from the wilderness? Was this a one-day job for either of them? It was a lifetime of progress, stumbling, restoration, and being used again. And those shameless acts, those failures recorded without apology, became the Scriptures of the Lord, for His glory and for the comfort of every broken man and woman who came after them.</p>

<p>What shame then is there in sharing mine? Does this make me a hypocrite? Or does it make me a poor man crying the only thing he knows to cry: Son of David, have mercy on me.</p>

<p>I know there are many reading this who are blaming God for the outcome of their lives. Many who are doubting whether He sees them at all. Many who have cried out and heard nothing back, and have started to wonder if anything is there to hear them. I was all of those people at different points in this journey.</p>

<p>I am not writing this because I have arrived somewhere. I am writing it from the middle of the desert, with soil on my hands from a garden I did not plant, in a house that is not mine, learning things I should have learned years ago. But I am writing it because what God has done in this season, quietly and without announcement, is real. He did not leave. He was working in the breaking. In the darkest hour, in the driest period, in the most humbling corner of a man's life, He gets to design something beautiful. He calls it an autopsy of the soul.</p>

<p>May this small piece of my story lift you, wherever you are. If He can do it here, He can do it where you are.</p>

<blockquote>"The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise.", Psalm 51:17</blockquote>

    `
  },
  {
    id: "the-word-judges-history-not-the-other-way-around",
    title: "The Word Judges History. Not the Other Way Around.",
    date: "21 May 2026",
    category: "Teaching",
    excerpt: "On Scripturalism, the authority of God\u2019s Word, and why the Church has it backwards. When external data becomes the measuring rod by which Scripture is tested, something catastrophic has occurred. The creature has been handed the gavel meant for the Creator.",
    image: "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgdmlld0JveD0iMCAwIDY4MCA4MjAiIHJvbGU9ImltZyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8dGl0bGU+VGhlIFdvcmQgSnVkZ2VzIEhpc3Rvcnk8L3RpdGxlPgogIDxkZXNjPkEgYmFsYW5jZSBzY2FsZSBvbiBkYXJrIGJhY2tncm91bmQ6IG9uIHRoZSBsZWZ0IHBhbiBzaXRzIGEgc2luZ2xlIG9wZW4gYm9vayB3ZWlnaGluZyBpdCBkb3duLCBvbiB0aGUgcmlnaHQgcGFuIHNpdHMgYSBzY3JvbGwgb2YgaGlzdG9yeSwgcmFpc2VkIHVwLjwvZGVzYz4KICA8cmVjdCB3aWR0aD0iNjgwIiBoZWlnaHQ9IjgyMCIgZmlsbD0iIzBlMGUwZSIvPgogIDxsaW5lIHgxPSIzMDAiIHkxPSIxMDAiIHgyPSIzODAiIHkyPSIxMDAiIHN0cm9rZT0iI2UwZDljZSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIi8+CiAgPGxpbmUgeDE9IjM0MCIgeTE9IjEwMCIgeDI9IjM0MCIgeTI9IjE4MCIgc3Ryb2tlPSIjZTBkOWNlIiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9Im5vbmUiLz4KICA8Y2lyY2xlIGN4PSIzNDAiIGN5PSIxODAiIHI9IjYiIGZpbGw9IiNjOWE5NmUiLz4KICA8bGluZSB4MT0iMTQwIiB5MT0iMjMwIiB4Mj0iNTQwIiB5Mj0iMTMwIiBzdHJva2U9IiNlMGQ5Y2UiIHN0cm9rZS13aWR0aD0iMi41IiBmaWxsPSJub25lIi8+CiAgPGxpbmUgeDE9IjE0MCIgeTE9IjIzMCIgeDI9IjEyMCIgeTI9IjM4MCIgc3Ryb2tlPSIjNTU1IiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiLz4KICA8bGluZSB4MT0iMTQwIiB5MT0iMjMwIiB4Mj0iMTYwIiB5Mj0iMzgwIiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIvPgogIDxsaW5lIHgxPSIxMDAiIHkxPSIzODUiIHgyPSIxODAiIHkyPSIzODUiIHN0cm9rZT0iI2UwZDljZSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHJlY3QgeD0iMTA4IiB5PSIzNDAiIHdpZHRoPSI2NCIgaGVpZ2h0PSI0NCIgcng9IjIiIGZpbGw9IiMyMjIiLz4KICA8cmVjdCB4PSIxMDgiIHk9IjM0MCIgd2lkdGg9IjY0IiBoZWlnaHQ9IjQ0IiByeD0iMiIgc3Ryb2tlPSIjYzlhOTZlIiBzdHJva2Utd2lkdGg9IjEuNSIgZmlsbD0ibm9uZSIvPgogIDxsaW5lIHgxPSIxNDAiIHkxPSIzNDAiIHgyPSIxNDAiIHkyPSIzODQiIHN0cm9rZT0iI2UwZDljZSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPGxpbmUgeDE9IjExNiIgeTE9IjM1MCIgeDI9IjEzNiIgeTI9IjM1MCIgc3Ryb2tlPSIjNTU1IiBzdHJva2Utd2lkdGg9IjAuNiIvPgogIDxsaW5lIHgxPSIxMTYiIHkxPSIzNTciIHgyPSIxMzYiIHkyPSIzNTciIHN0cm9rZT0iIzU1NSIgc3Ryb2tlLXdpZHRoPSIwLjYiLz4KICA8bGluZSB4MT0iMTE2IiB5MT0iMzY0IiB4Mj0iMTM2IiB5Mj0iMzY0IiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMC42Ii8+CiAgPGxpbmUgeDE9IjExNiIgeTE9IjM3MSIgeDI9IjEzNiIgeTI9IjM3MSIgc3Ryb2tlPSIjNTU1IiBzdHJva2Utd2lkdGg9IjAuNiIvPgogIDxsaW5lIHgxPSIxNDQiIHkxPSIzNTAiIHgyPSIxNjQiIHkyPSIzNTAiIHN0cm9rZT0iIzU1NSIgc3Ryb2tlLXdpZHRoPSIwLjYiLz4KICA8bGluZSB4MT0iMTQ0IiB5MT0iMzU3IiB4Mj0iMTY0IiB5Mj0iMzU3IiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMC42Ii8+CiAgPGxpbmUgeDE9IjE0NCIgeTE9IjM2NCIgeDI9IjE2NCIgeTI9IjM2NCIgc3Ryb2tlPSIjNTU1IiBzdHJva2Utd2lkdGg9IjAuNiIvPgogIDxsaW5lIHgxPSIxNDQiIHkxPSIzNzEiIHgyPSIxNjQiIHkyPSIzNzEiIHN0cm9rZT0iIzU1NSIgc3Ryb2tlLXdpZHRoPSIwLjYiLz4KICA8ZWxsaXBzZSBjeD0iMTQwIiBjeT0iMzk1IiByeD0iNDUiIHJ5PSI1IiBmaWxsPSIjMDAwMDAwNTUiLz4KICA8bGluZSB4MT0iNTQwIiB5MT0iMTMwIiB4Mj0iNDgwIiB5Mj0iMjYwIiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIvPgogIDxsaW5lIHgxPSI1NDAiIHkxPSIxMzAiIHgyPSI2MDAiIHkyPSIyNjAiIHN0cm9rZT0iIzU1NSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIi8+CiAgPGxpbmUgeDE9IjQ2MCIgeTE9IjI2NSIgeDI9IjYyMCIgeTI9IjI2NSIgc3Ryb2tlPSIjZTBkOWNlIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cmVjdCB4PSI0NjIiIHk9IjIxMCIgd2lkdGg9IjE1NiIgaGVpZ2h0PSI1NSIgcng9IjQiIGZpbGw9IiMxZTFlMWUiLz4KICA8cmVjdCB4PSI0NjIiIHk9IjIxMCIgd2lkdGg9IjE1NiIgaGVpZ2h0PSI1NSIgcng9IjQiIHN0cm9rZT0iI2UwZDljZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIi8+CiAgPGVsbGlwc2UgY3g9IjQ2OCIgY3k9IjIzNyIgcng9IjgiIHJ5PSIyNyIgZmlsbD0iIzFlMWUxZSIgc3Ryb2tlPSIjZTBkOWNlIiBzdHJva2Utd2lkdGg9IjEiLz4KICA8ZWxsaXBzZSBjeD0iNjEyIiBjeT0iMjM3IiByeD0iOCIgcnk9IjI3IiBmaWxsPSIjMWUxZTFlIiBzdHJva2U9IiNlMGQ5Y2UiIHN0cm9rZS13aWR0aD0iMSIvPgogIDxsaW5lIHgxPSI0ODIiIHkxPSIyMjUiIHgyPSI1OTgiIHkyPSIyMjUiIHN0cm9rZT0iIzU1NSIgc3Ryb2tlLXdpZHRoPSIwLjYiLz4KICA8bGluZSB4MT0iNDgyIiB5MT0iMjMzIiB4Mj0iNTk4IiB5Mj0iMjMzIiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMC42Ii8+CiAgPGxpbmUgeDE9IjQ4MiIgeTE9IjI0MSIgeDI9IjU5OCIgeTI9IjI0MSIgc3Ryb2tlPSIjNTU1IiBzdHJva2Utd2lkdGg9IjAuNiIvPgogIDxsaW5lIHgxPSI0ODIiIHkxPSIyNDkiIHgyPSI1OTgiIHkyPSIyNDkiIHN0cm9rZT0iIzU1NSIgc3Ryb2tlLXdpZHRoPSIwLjYiLz4KICA8bGluZSB4MT0iNDgyIiB5MT0iMjU3IiB4Mj0iNTkwIiB5Mj0iMjU3IiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMC42Ii8+Cjwvc3ZnPg==",
    link: "scripturalism.html"
  },
  {
    id: "were-the-apostles-confused-or-did-translators-bias-the-text",
    title: "Were the Apostles Confused or Did Translators Bias the Text?",
    date: "19 May 2026",
    category: "Teaching",
    excerpt: "A sharp paradox runs through your Bible: in one verse Jesus is seemingly called God, and in the very next chapter the same Jesus calls the Father 'my God'. Were the Apostles contradictory writers — or did later translators insert their own theological biases into the text?",
    image: "apostles_vs_translators.svg",
    content: `
<p>For centuries, mainstream theology has presented a highly complex, multi-personal view of the Godhead. We are told that Jesus is "God the Son," a co-equal, co-eternal member of a Trinity who came down, took on human flesh, and died for humanity.</p>

<p>Yet, when you open a Bible and read the actual text, an unavoidable paradox emerges. In one verse, Jesus is seemingly labelled with the Greek word for God (<em>Theos</em>). In the very next chapter, the exact same Jesus looks up to heaven and speaks of the Father as "my God" (Revelation 3:12).</p>

<p>This leaves readers with a sharp choice: were the Apostles deeply confused and contradictory writers, or did later translators insert their own theological biases into the text?</p>

<p>When we strip away modern church filters and examine the raw scriptural evidence, the answer becomes undeniably clear: the Apostles were completely consistent. The confusion belongs entirely to modern translations.</p>

<h2>1. The Real Paul vs. The Translated Paul</h2>

<p>The Apostle Paul is frequently used to champion the idea of a literal incarnation. Modern English Bibles translate Titus 2:13 to announce: <em>"…the appearing of the glory of our great God and Savior Jesus Christ."</em></p>

<p>To a casual reader, this looks like Paul is explicitly calling Jesus "our great God." But forcing this interpretation pushes Paul into a direct, logical contradiction with his other letters. Writing to Timothy, Paul lays down an ironclad, unyielding definition of the Supreme Creator:</p>

<blockquote>"Now to the King eternal, immortal, invisible, the only God…" — 1 Timothy 1:17</blockquote>

<blockquote>"…who alone possesses immortality and dwells in unapproachable light, whom no man has seen or can see." — 1 Timothy 6:16</blockquote>

<p>The logic is simple. If God alone possesses inherent immortality, then Jesus — who genuinely died on a Roman cross — cannot be that self-existent God. If God is a being whom no man can see, but thousands of people physically touched and ate with Jesus, then Jesus cannot be identical to that invisible God.</p>

<p>Paul was not a confused writer. The Greek grammar of Titus 2:13 easily allows for two separate entities: <em>"…the appearing of the glory of our great God, and [the appearing] of our Savior Jesus Christ."</em> Translators choose to merge them to fit later church formulas, creating an artificial contradiction.</p>

<h2>2. The Internal Clash in the Writings of John</h2>

<p>A similar translation issue occurs in the letters of John. Standard translations of 1 John 5:20 end with a dramatic claim regarding Jesus: <em>"…and we are in him who is true, in his Son Jesus Christ. He is the true God and eternal life."</em></p>

<p>By rendering the Greek pronoun <em>houtos</em> as "He" and pointing it to Jesus, translators create a direct clash with the Gospel of John. In John 17:3, Jesus explicitly prays to the Father and defines reality:</p>

<blockquote>"And this is eternal life, that they know you, the only true God, and Jesus Christ whom you have sent." — John 17:3</blockquote>

<p>Jesus cannot name the Father as the only true God while John simultaneously claims Jesus is the true God. The original Greek pronoun <em>houtos</em> literally means "This One." In biblical Greek, it routinely points back to the main subject of the paragraph, not just the nearest word. When read correctly, 1 John 5:20 means: <em>"…we are in Him who is true [the Father], by means of His Son Jesus Christ. This One [the Father] is the true God."</em> By resolving the pronoun correctly, the contradiction vanishes entirely.</p>

<h2>3. The Unchanging Apostolic Formula</h2>

<p>If you read the opening greetings of the actual letters of the Apostles, they never merge God and Jesus into a single Trinitarian entity. They consistently maintain a clear hierarchy:</p>

<blockquote>"Grace to you and peace from God our Father and the Lord Jesus Christ." — Romans 1:7</blockquote>

<blockquote>"James, a servant of God and of the Lord Jesus Christ…" — James 1:1</blockquote>

<p>The text refuses to use the late, post-biblical phrases coined by 4th and 5th-century church councils, such as "God the Son" or "God the Holy Spirit." Instead, the ultimate Apostolic summary is found in 1 Corinthians 8:6:</p>

<blockquote>"…yet for us there is one God, the Father, from whom are all things… and one Lord, Jesus Christ, through whom are all things…" — 1 Corinthians 8:6</blockquote>

<p>One God. The Father. One Lord. Jesus Christ. Two persons, named separately, in the same breath — exactly as every apostolic letter consistently states.</p>

<h2>The Victory Reclaimed</h2>

<p>Saying an immortal, unchangeable God came down and pretended to die is foreign to the very definition of God. It reduces the crucifixion to a scripted illusion. If a being cannot fail, the moral triumph of staying faithful unto death loses all its substance.</p>

<p>The Apostles did not teach a confusing Greek philosophical paradox. They taught a beautifully uniform Hebrew truth: the Father is the sole, invisible, immortal source of all existence. Jesus was a real mortal man who achieved absolute victory over temptation and death through pure obedience. Because of that victory, God highly exalted him and granted him a seat at His right hand.</p>

<blockquote>"God has made this Jesus, whom you crucified, both Lord and Christ." — Acts 2:36</blockquote>

<p>The Apostles were not confused. It is time to stop letting biased translations make them sound like they were.</p>
    `
  },
  {
    id: "let-jesus-speak-for-himself",
    title: "Let Jesus Speak For Himself",
    date: "11 May 2026",
    category: "Teaching",
    image: "let_jesus_speak.jpg",
    excerpt: "Centuries of councils have spoken about Jesus at great length. But remarkably little time is spent simply listening to what Jesus said about himself — in plain, unambiguous language. His own words. On the record. Then you decide.",
    content: `
<style>
.ljs-lead{font-family:'Cormorant Garamond',serif;font-size:1.25rem;font-style:italic;color:var(--gold);line-height:1.65;margin-bottom:1.8rem;border-left:2px solid var(--gold);padding-left:1.4rem;}
.ljs-divider{display:flex;align-items:center;gap:1rem;margin:2.5rem 0;}
.ljs-divider::before,.ljs-divider::after{content:'';flex:1;height:0.5px;background:var(--border);}
.ljs-divider span{font-family:'Cormorant Garamond',serif;font-size:0.75rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--text-muted);}
.ljs-card{background:var(--surface);border:0.5px solid var(--border);border-left:3px solid #8b1a1a;margin-bottom:1.6rem;padding:1.8rem 2rem 1.5rem;transition:background 0.2s;}
.ljs-card:hover{background:var(--surface-light);}
.ljs-label{font-size:0.65rem;letter-spacing:0.22em;text-transform:uppercase;color:#c0392b;margin-bottom:0.75rem;}
.ljs-verse{font-family:'Cormorant Garamond',serif;font-size:1.25rem;font-style:italic;color:var(--text-primary);line-height:1.7;margin-bottom:0.75rem;}
.ljs-verse strong{font-style:normal;font-weight:600;color:#e07060;background:rgba(139,26,26,0.15);padding:0 2px;}
.ljs-note{font-size:0.85rem;color:var(--text-muted);border-top:0.5px solid var(--border);padding-top:0.9rem;margin-top:0.75rem;line-height:1.75;}
.ljs-question{background:var(--deep-mid);border:0.5px solid var(--border);padding:3rem 2rem;margin:3rem 0;text-align:center;}
.ljs-q-eyebrow{font-size:0.65rem;letter-spacing:0.25em;text-transform:uppercase;color:var(--gold);margin-bottom:1.2rem;}
.ljs-q-text{font-family:'Cormorant Garamond',serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:300;color:var(--text-primary);line-height:1.3;margin-bottom:0.75rem;}
.ljs-q-sub{font-size:0.88rem;font-style:italic;color:var(--text-muted);max-width:480px;margin:0 auto 2rem;}
.ljs-buttons{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;}
.ljs-btn{font-family:'DM Sans',sans-serif;font-size:0.68rem;letter-spacing:0.2em;text-transform:uppercase;padding:0.75rem 1.8rem;border:0.5px solid;cursor:pointer;background:transparent;transition:all 0.2s;border-radius:2px;}
.ljs-btn-yes{border-color:var(--gold);color:var(--gold);}
.ljs-btn-yes:hover{background:rgba(91,141,184,0.15);}
.ljs-btn-no{border-color:rgba(139,26,26,0.5);color:#8b4a4a;}
.ljs-btn-no:hover{background:rgba(139,26,26,0.1);color:#c07060;border-color:#c07060;}
.ljs-resp{display:none;max-width:520px;margin:1.8rem auto 0;padding:1.4rem 1.8rem;border:0.5px solid;font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-style:italic;line-height:1.75;text-align:left;}
.ljs-resp.yes{border-color:var(--gold);color:var(--gold-light);}
.ljs-resp.no{border-color:#c0392b;color:#e07060;}
.ljs-closing{margin:2.5rem 0 1rem;padding:2rem 0;border-top:0.5px solid var(--border);}
.ljs-closing p{font-family:'Cormorant Garamond',serif;font-size:1.15rem;font-style:italic;color:var(--text-secondary);margin-bottom:1rem;line-height:1.8;}
.ljs-closing strong{font-style:normal;color:var(--text-primary);}
</style>

<p class="ljs-lead">"Before we debate what Jesus is — let us ask Jesus what he said about himself. Then we can ask each other: do you agree with him?"</p>

<p>Centuries of councils, creeds, and controversies have spoken <em>about</em> Jesus at great length. But remarkably little time is spent simply listening to what Jesus said <em>about himself</em> — in plain, unambiguous language, recorded by those who walked with him.</p>

<p>Below are his own words. No commentary. No theological framing. Just the man himself, speaking directly about who he is, who sent him, and who is greater than him.</p>

<div class="ljs-divider"><span>The Words of Jesus</span></div>

<div class="ljs-card">
  <div class="ljs-label">John 17:3</div>
  <div class="ljs-verse">"This is eternal life — that they know you, <strong>the only true God</strong>, and Jesus Christ <strong>whom you have sent.</strong>"</div>
  <div class="ljs-note">Jesus himself names the Father as the only true God. He names himself as the one sent — two distinct roles, spoken by Jesus in the same breath.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 14:28</div>
  <div class="ljs-verse">"You heard me say I am going away and I am coming back to you. If you loved me, you would be glad that I am going to the Father, for <strong>the Father is greater than I.</strong>"</div>
  <div class="ljs-note">Not equal. Not co-equal. Jesus says it simply and directly: the Father is greater. This is not humility rhetoric — it is a statement about rank and origin.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 20:17</div>
  <div class="ljs-verse">"Do not hold on to me… Go instead to my brothers and tell them: I am ascending to <strong>my Father and your Father, to my God and your God.</strong>"</div>
  <div class="ljs-note">After resurrection — glorified, exalted — Jesus still calls the Father <em>my God</em>. The relationship does not dissolve into equality. It remains: Son and Father. Worshipper and God.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 5:19</div>
  <div class="ljs-verse">"Very truly I tell you, <strong>the Son can do nothing by himself</strong>; he can do only what he sees his Father doing, because whatever the Father does the Son also does."</div>
  <div class="ljs-note">An independent co-equal divine person can act independently. Jesus says the Son cannot. His authority is derived, not inherent.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 5:30</div>
  <div class="ljs-verse">"By myself <strong>I can do nothing</strong>; I judge only as I hear, and my judgment is just, for I seek not to please myself but <strong>him who sent me.</strong>"</div>
  <div class="ljs-note">The one who sent and the one sent are not the same person. Jesus consistently returns to this: he is the messenger, the Father is the source.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 7:16</div>
  <div class="ljs-verse">"My teaching <strong>is not my own.</strong> It comes from <strong>him who sent me.</strong>"</div>
  <div class="ljs-note">His doctrine is not self-originated. The one who is the eternal co-equal Word of God would need no external source for teaching. Jesus traces everything back to the Father.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">Mark 10:18</div>
  <div class="ljs-verse">"Why do you call me good? <strong>No one is good — except God alone.</strong>"</div>
  <div class="ljs-note">Jesus deflects the title of absolute goodness away from himself and toward God. He does not say "yes, I am good, I am God." He redirects. God alone holds that position.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">Matthew 24:36</div>
  <div class="ljs-verse">"About that day or hour <strong>no one knows</strong>, not even the angels in heaven, <strong>nor the Son</strong>, but only the Father."</div>
  <div class="ljs-note">An omniscient co-equal God knows all things — including the hour. Jesus says the Son does not know it. His knowledge, like his authority, is given — not inherent.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 6:57</div>
  <div class="ljs-verse">"Just as <strong>the living Father sent me</strong> and I live <strong>because of the Father</strong>, so the one who feeds on me will live because of me."</div>
  <div class="ljs-note">Jesus lives because of the Father. His life is sourced in God. He is not self-existent. He is the Son — dependent, derived, given life from the living Father.</div>
</div>

<div class="ljs-card">
  <div class="ljs-label">John 14:10</div>
  <div class="ljs-verse">"The words I say to you <strong>I do not speak on my own authority.</strong> Rather, it is the Father, living in me, who is doing his work."</div>
  <div class="ljs-note">The Father dwelling in Jesus — not Jesus being the Father. Two distinct persons, one working through the other. The source is always the Father.</div>
</div>

<div class="ljs-question">
  <div class="ljs-q-eyebrow">Now, a question for the room</div>
  <div class="ljs-q-text">Do you agree with what Jesus said about himself?</div>
  <div class="ljs-q-sub">He called the Father the only true God. He called himself the one sent. He said the Father is greater. These are his words — not ours.</div>
  <div class="ljs-buttons">
    <button class="ljs-btn ljs-btn-yes" onclick="ljsRespond('yes')">Yes — I take him at his word</button>
    <button class="ljs-btn ljs-btn-no" onclick="ljsRespond('no')">No — I believe he meant something else</button>
  </div>
  <div id="ljs-resp-yes" class="ljs-resp yes" style="display:none;"></div>
  <div id="ljs-resp-no" class="ljs-resp no" style="display:none;"></div>
</div>

<div class="ljs-closing">
  <p>Jesus never once said <strong>"I am the Father."</strong><br>He never said <strong>"I am co-equal with God."</strong><br>He never said <strong>"Worship me as the Most High."</strong></p>
  <p>He said: <strong>"The Father is greater than I."</strong><br>He said: <strong>"My God and your God."</strong><br>He said: <strong>"The only true God — whom you have sent me."</strong></p>
  <p>The simplest act of faith is to believe the man at his word.</p>
</div>
    `
  },
  {
    id: "agencies-of-god-how-the-almighty-speaks-acts-and-appears",
    title: "The Agencies of God: How the Almighty Speaks, Acts and Appears",
    date: "5 May 2026",
    category: "Teaching",
    excerpt: "No man has seen God at any time. Yet Abraham spoke with visitors. Moses encountered a burning bush. Jacob wrestled until dawn. How do we reconcile these accounts? The answer lies in one of the most ancient and consistently applied principles in Scripture: divine agency.",
    image: "agencies_of_god.svg",
    content: `
<p>Here is something that puzzled me for a long time. The Bible says clearly that no one has ever seen God. And yet Abraham sat down and had a meal with three visitors. Moses spoke face to face with someone at a burning bush. Jacob wrestled a man through the entire night. How do we make sense of this?</p>

<p>The answer has been there all along. It is called divine agency. And once you see it, you cannot unsee it.</p>

<p>In the ancient world, particularly in Hebrew culture, there was a legal principle called <em>shaliah</em>. It was simple: a man's authorised messenger is as the man himself. When a fully trusted representative speaks in your name, he carries your full authority. He does not just deliver your message. He is you, legally speaking.</p>

<p>God applied this same principle throughout the Bible. He sent authorised agents, angels and his Word, to communicate with human beings. And when those agents spoke, the text records it as God speaking. Not because the agent is God, but because the agent is fully carrying God's name and authority.</p>

<p>Look at Exodus 23. God tells Israel to follow a certain angel through the wilderness. Then He says: "My name is in him." That is the language of authorised representation. This angel does not just know God's name. He carries it. To obey him is to obey God. To resist him is to resist God.</p>

<p>Now go back to the burning bush. Read it slowly. The angel of the Lord appears in the fire. Three verses later, God is calling Moses by name from the same bush. Then it is the Lord who speaks. The text moves between the agent and God without explanation, because in the framework of divine agency there is no contradiction. Moses is not talking to two beings. He is talking to one authorised representative of the Most High, who speaks in the full name and authority of the One who sent him.</p>

<p>The same pattern shows up when Abraham receives three visitors at Mamre. The text opens by saying the Lord appeared to him. Then we see three men standing there. Two of them later go to Sodom. But the third stays and speaks with Abraham, and the conversation is recorded as the Lord speaking directly. Abraham understood exactly what he was in the presence of. He bowed to the ground and served them food.</p>

<p>Then there is Jacob. He wrestled a man all night at the Jabbok river. At the end of it, Jacob named the place Peniel, which means the face of God, and said: I have seen God face to face and survived. The prophet Hosea later explains that Jacob wrestled with an angel. Both statements are true at the same time. The angel carried God's full presence, God's name, and God's authority. To encounter the agent was to encounter the One who sent him.</p>

<p>The glory cloud that led Israel through the desert, the pillar of fire at night, the Kavod that descended on the Tabernacle so powerfully that Moses could not enter: all of these were God's presence extended into the physical world through an authorised form. Real. Objective. Powerful. But not the Eternal Father in His unveiled essence.</p>

<p>And this is where it all leads. The apostle Paul wrote that Jesus is the image of the invisible God, the firstborn over all creation. John wrote that no one has ever seen God, and then said the Son has made Him known. The Son is the final and complete divine agent, the one who carried the Name not just in spiritual authority but in human flesh, in a body that could be touched and heard and seen.</p>

<p>But here is what must be said plainly. The Father remained the Father throughout all of this. He never became the Son. He never shared His throne with a co-equal person. He sent His agents, including finally His Son, to make Himself known to human beings. And when His Son had completed everything He was sent to do, the Father spoke His verdict over all of history:</p>

<blockquote>"God has made this Jesus, whom you crucified, both Lord and Christ." — Acts 2:36</blockquote>

<p>The Father made Him Lord. It is the Father's declaration, the Father's gift, to the glory of the Father. This is not a Trinity. This is one God who chose to reveal Himself through many agencies across many centuries, and then finally through His beloved Son, whom He has appointed Lord over all nations.</p>

<p>One God. Many agents. One appointed Son. That is the story the whole Bible is telling.</p>
    `
  },
  {
    id: "just-reasonable-mind-devout-life-francis-de-sales",
    title: "Partiality in Love: Self and Neighbours",
    date: "28 April 2026",
    category: "Reflection",
    excerpt: "Reason is the defining mark of man, writes Francis de Sales, yet truly reasonable people are rare. Self-love is the reason why. Chapter 36 names the small daily dishonesties we commit without noticing, and offers one discipline to correct them.",
    image: "partiality_in_love_self_neighbours.svg",
    content: `
<p><em>Introduction to the Devout Life</em>, Francis de Sales. Part Three, Chapter 36: <strong>That We Must Be Just and Reasonable.</strong></p>

<h2>Reason is rare</h2>

<p>Francis de Sales opens the chapter plainly: <em>"Reason is the special characteristic of man, and yet it is a rare thing to find really reasonable men."</em> The cause, he says, is self-love. Self-love hinders reason and beguiles us, quietly, without our noticing, into all manner of trifling but dangerous acts of injustice and untruth.</p>

<p>He reaches for an image from the Song of Songs: these small corruptions are like the little foxes that spoil the vines. Because they are trifling, people pay no attention to them. Because they are numerous, they do infinite harm.</p>

<h2>The small dishonesties we overlook in ourselves</h2>

<p>Francis then gives a list. Read it slowly, each line is a mirror:</p>

<p>We find fault with our neighbour readily for small matters, while we pass over great things in ourselves. We strive to sell dear and buy cheap. We are eager to deal out strict justice to others, while seeking indulgence for ourselves. We expect a good construction to be put on all we say, but we are sensitive and critical as to our neighbour's words. We want him to give us what we want, while it would be more reasonable to let him keep what is his. We are vexed with him because he will not accommodate us, while perhaps he has better reason to be vexed with us for wanting to disturb him.</p>

<p>If we have formed a dislike for someone, particularly a subordinate, everything they do appears wrong. We thwart them. We look coldly on them. We never stop to ask whether our judgement is just or merely convenient.</p>

<h2>These things seem unimportant, but they are not</h2>

<p>Francis is careful to note that these small dishonesties do not usually require restitution. We have, after all, only taken what the strict letter of the law permits. But he is clear: <em>they are sins against right and charity. They are trickery. And they greatly need correction.</em> No one, he adds, ever truly loses by being generous, noble-hearted and courteous.</p>

<h2>The remedy: put yourself in your neighbour's place</h2>

<p>The counsel Francis gives is simple and direct. Be just and fair in all you do. And then one practical discipline: <em>always put yourself in your neighbour's place, and put him into yours, and then you will judge fairly.</em></p>

<p>Sell as you would buy. Buy as you would sell. Examine your dealings with your neighbour and ask honestly: is my heart right towards him, as I would wish his to be towards me, if positions were reversed? Francis calls this <strong>the true test of reason.</strong></p>

<p>He closes with the Emperor Trajan, who was criticised for making himself too accessible to his subjects. Trajan replied: <em>"Does it not behove me to be such an emperor towards my subjects as I should myself wish to find, were I a subject?"</em> The Emperor applied to his throne the same discipline Francis applies to every ordinary transaction, reverse the positions and see if it still seems fair.</p>

<h2>The Golden Rule</h2>

<p>The entire chapter is an exposition of what the Messiah called the summary of the Law and the Prophets:</p>

<blockquote>"So in everything, do to others what you would have them do to you, for this sums up the Law and the Prophets.", Matthew 7:12</blockquote>

<blockquote>"The commandments are summed up in this one command: Love your neighbour as yourself. Love does no harm to a neighbour. Therefore love is the fulfilment of the law.", Romans 13:9–10</blockquote>

<blockquote>"Whoever claims to love God yet hates a brother or sister is a liar. For whoever does not love their brother and sister, whom they have seen, cannot love God, whom they have not seen.", 1 John 4:20</blockquote>

<p>Chapter 36 is not about the dramatic sins. It is about the little foxes, the double standard, the convenient judgement, the small advantage quietly taken. The test is the same one placed before every disciple: reverse the positions, and see if it still seems fair.</p>

<div style="margin:3rem 0;padding:1.6rem 1.8rem;background:rgba(201,168,76,0.06);border:0.5px solid rgba(201,168,76,0.2);border-left:2px solid rgba(201,168,76,0.5);">
  <p style="font-size:0.75rem;letter-spacing:0.14em;text-transform:uppercase;color:#C9A84C;margin-bottom:0.75rem;">Editorial Note</p>
  <p style="font-size:0.88rem;color:#A8A090;line-height:1.85;">2:22 Church does not endorse Catholicism, its institutional practices, or any Trinitarian doctrine. The writings of Francis de Sales are cited solely because they contain God-inspired reflection, pure in intent, useful for the edification and uplifting of those who desire to be true disciples of Jesus the Messiah, known in Hebrew as <strong style="color:#F0EAD6;">Yeshua</strong> (יֵשׁוּעַ), rendered in Greek as <strong style="color:#F0EAD6;">Iēsous</strong> (Ἰησοῦς), from which the name Jesus is derived. We test all things by Scripture alone.</p>
</div>
    `
  },
  {
    id: "was-jesus-god-a-biblical-examination",
    title: "Was Jesus God? A Biblical Examination",
    date: "22 April 2026",
    category: "Teaching",
    excerpt: "I do not belong to any denomination, nor am I introducing any cult. What follows is a thorough, verse-by-verse examination of what Scripture actually says about the nature of Jesus Christ, and why the Trinitarian position cannot stand on the plain testimony of the Bible.",
    image: "Is_Jesus_GoD.jpg",
    content: `
<p>I want to ask you something simple. When you open any letter Paul wrote, what does the first line say about God and Jesus?</p>

<p>Romans 1:7: "Grace and peace to you from God our Father and from the Lord Jesus Christ." Two persons. God our Father. And the Lord Jesus Christ. Not one person called God who is also Jesus. Two persons, named separately, in the same sentence.</p>

<p>Read every single apostolic letter. The pattern never breaks. God is the Father. Jesus is the Son. They are distinct. The Father sends the Son. The Son prays to the Father. The Father raises the Son. The Son sits at the right hand of the Father. No apostle ever wrote that Jesus is the Father. Not once.</p>

<p>So where does the idea come from that Jesus is God in the sense of being the Eternal Father?</p>

<p>It comes from a handful of verses that seem, on first reading, to say something different. Let us look at the most common ones honestly.</p>

<p>John 1:1 says the Word was God. This has been used for centuries to argue that Jesus is fully God in the same sense as the Father. But read the same verse carefully. "The Word was with God." With God. If the Word is God in the same sense as the Father, how can the Word be with God at the same time? The answer is that the Word carries divine nature and divine authority, as the Father's chief agent, without being identical to the Father. John 1:18 then answers its own question: no one has ever seen God, but the Son has made Him known. The Son reveals the Father. He is not the Father.</p>

<p>Thomas called Jesus "my Lord and my God" in John 20:28. This is a title of honour and worship, not a statement that Jesus is the Eternal Father. The same title was used of kings and masters throughout the ancient world. Thomas was not delivering a systematic theology lecture. He was overwhelmed by what he was seeing. And Jesus did not say to him: correct, I am the Eternal Father. He said: blessed are those who believe without seeing.</p>

<p>Isaiah 9:6 calls the coming child Mighty God and Everlasting Father. These are throne names and governmental titles, the way ancient kings were given names that described their authority and mission. They describe what the Messiah would carry out and represent, not a claim that he is literally the Eternal Father of creation.</p>

<p>Now look at what Scripture says directly about who made Jesus Lord.</p>

<blockquote>"God has made this Jesus, whom you crucified, both Lord and Christ." — Acts 2:36</blockquote>

<p>The Father made Him Lord. This is Peter at Pentecost, speaking under the full power of the Spirit. The Lordship of Jesus was conferred by the Father, not self-possessed from eternity. It was the Father's act of exaltation after the resurrection.</p>

<blockquote>"Therefore God also has highly exalted Him and given Him the name which is above every name." — Philippians 2:9</blockquote>

<p>God gave Him the name. God exalted Him. The Son received what the Father gave. This is not the language of two co-equal persons in a Trinity. This is the language of a Father honouring His Son.</p>

<p>And why does any of this matter? Because if Jesus is the Father, then who was He praying to in Gethsemane? Who raised Him from the dead? Who does He sit beside right now? The Trinitarian answer requires increasingly complex explanations that the apostles themselves never gave.</p>

<p>The simpler reading, the one every apostolic letter assumes without argument, is this: there is one God, the Father. And there is one Lord, Jesus Christ, His Son, through whom all things were made and through whom we are saved. These are not the same person. They are Father and Son. And that relationship is not a limitation. It is the very shape of the gospel.</p>

<blockquote>"For there is one God and one Mediator between God and men, the Man Christ Jesus, who gave Himself a ransom for all." — 1 Timothy 2:5-6</blockquote>

<p>One God. One Mediator. The Man Christ Jesus. That is the apostolic testimony, stated plainly, needing no Trinity to hold it together.</p>
    `
  },
];

// ============================================================
//  TEMPLATE, Copy this block to add a new post
//  Paste it at the TOP of the POSTS array above (after the [)
// ============================================================
//
//  {
//    id: "short-url-friendly-title",         // no spaces, use hyphens
//    title: "Your Full Blog Title Here",
//    date: "21 April 2026",
//    category: "Teaching",                   // see category list at top
//    excerpt: "One or two sentence summary shown on blog listing page.",
//    image: "",                              // paste an image URL or leave ""
//    content: `
//      <p>Your first paragraph here.</p>
//
//      <h2>A Section Heading</h2>
//
//      <p>More content here.</p>
//
//      <blockquote>"A scripture verse here.", Reference</blockquote>
//
//      <p>Closing thoughts.</p>
//    `
//  },
//
// ============================================================

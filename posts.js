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
    id: "let-jesus-speak-for-himself",
    title: "Let Jesus Speak For Himself",
    date: "11 May 2026",
    category: "Teaching",
    image: "Is_Jesus_GoD.jpg",
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
  <div id="ljs-resp-yes" class="ljs-resp yes">
    Then we are agreed. The Father is the only true God. Jesus is His Son — sent, begotten, exalted. And the Spirit of God is God Himself going forth. One God. One truth. Let him who has ears hear.
  </div>
  <div id="ljs-resp-no" class="ljs-resp no">
    Then the debate is no longer between us and theologians. It is between you and Jesus. He is on the record. The question now is — whose interpretation do you trust more: the councils of men, or the words of the man himself?
  </div>
</div>

<div class="ljs-closing">
  <p>Jesus never once said <strong>"I am the Father."</strong><br>He never said <strong>"I am co-equal with God."</strong><br>He never said <strong>"Worship me as the Most High."</strong></p>
  <p>He said: <strong>"The Father is greater than I."</strong><br>He said: <strong>"My God and your God."</strong><br>He said: <strong>"The only true God — whom you have sent me."</strong></p>
  <p>The simplest act of faith is to believe the man at his word.</p>
</div>

<script>
function ljsRespond(choice) {
  document.getElementById('ljs-resp-yes').style.display = 'none';
  document.getElementById('ljs-resp-no').style.display = 'none';
  var box = document.getElementById('ljs-resp-' + choice);
  box.style.display = 'block';
  box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
</script>
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
  {
    id: "what-does-it-mean-to-be-the-church",
    title: "What Does It Mean to Be the Church?",
    date: "14 July 2025",
    category: "Teaching",
    excerpt: "We have inherited a word, 'church', that has been buried under centuries of stone, steeple, and institution. But the New Testament paints a picture that looks very different.",
    image: "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=900&q=80",
    content: `
<p>We have inherited a word, "church", that has been buried under centuries of stone, steeple, and institution. When most people hear it, they picture a building: a pointed roof, stained glass, rows of pews. But the New Testament paints a picture that looks very different.</p>

<p>The Greek word is <em>ekklesia</em>, meaning "the called-out ones," an assembly of people. Not a place. Not an organisation. People. Living, breathing, Spirit-filled people gathered in the name of Jesus Christ.</p>

<h2>The Early Church Had No Buildings</h2>

<p>For the first three centuries of Christian history, there were no church buildings. Believers met in homes, in courtyards, by riversides, in hired halls. The "church at Corinth" was not a building in Corinth, it was the community of believers living in that city. Paul wrote letters to people, not to addresses.</p>

<blockquote>"Where two or three gather in my name, there am I with them.", Matthew 18:20</blockquote>

<p>Jesus did not say "where a grand building stands" or "where an institution is registered." He said <em>where two or three gather</em>. The threshold is remarkably low. The promise is remarkably high.</p>

<h2>What This Means for Us</h2>

<p>At 2:22 Church, we take this seriously, not as a theological novelty but as a return to something ancient. When we gather in someone's living room, when we meet in the park on a Sunday morning, when we share a meal and open the Word together around a kitchen table, that is the church. Fully. Not a second-rate version of church.</p>

<p>This does not mean we are disorganised or lacking in depth. The apostles' teaching, fellowship, breaking of bread, and prayer (Acts 2:42) can happen anywhere the people of God choose to meet. What it does mean is that we refuse to confuse the container with the contents.</p>

<h2>You Are the Church</h2>

<p>Perhaps the most important implication of all this is personal. You, if you have been born again by the Spirit of God, if you are following Jesus, <em>you are the church</em>. Not a member of it in the sense of a club. Not a customer attending a service. You are a living stone in a spiritual house (1 Peter 2:5).</p>

<p>That means your daily life is not separate from your church life. How you treat your neighbour, how you serve the poor, how you speak truth in your workplace, all of this is the church being the church in the world. The gathering on Sunday (or whenever your community meets) is the equipping and encouragement. The rest of the week is the mission.</p>

<p>We are not waiting to build something. We already are something. Let us live like it.</p>
    `
  },
  {
    id: "baptism-in-jesus-name",
    title: "Baptism in Jesus' Name, What the Apostles Actually Did",
    date: "7 July 2025",
    category: "Baptism",
    excerpt: "A close look at Acts and the early church practice of baptism, and why the outward act must follow genuine inward transformation.",
    image: "https://images.unsplash.com/photo-1476234251651-f353703a034d?w=800&q=80",
    content: `
<p>Few topics in Christian history have generated as much debate as baptism. Who should be baptised? When? How much water? What words should be spoken? Behind all these questions lies a more important one: what is baptism actually <em>for</em>?</p>

<p>At 2:22 Church, we follow the pattern of the early apostles. When Peter preached on the day of Pentecost and the crowd asked "What shall we do?" his answer was clear:</p>

<blockquote>"Repent and be baptised, every one of you, in the name of Jesus Christ for the forgiveness of your sins. And you will receive the gift of the Holy Spirit.", Acts 2:38</blockquote>

<h2>The Apostolic Pattern</h2>

<p>Throughout the book of Acts, every recorded baptism is performed in the name of Jesus Christ. The Samaritans were baptised in the name of the Lord Jesus (Acts 8:16). Cornelius and his household were baptised in the name of Jesus Christ (Acts 10:48). The disciples at Ephesus were baptised in the name of the Lord Jesus (Acts 19:5).</p>

<p>This is not a minor detail. The apostles who had walked with Jesus, who had received his final instructions, who had been filled with the Holy Spirit at Pentecost, these men consistently baptised in the name of Jesus. We follow their example.</p>

<h2>Baptism Cannot Save You Alone</h2>

<p>This is where we must be clear and honest. Baptism is a powerful, meaningful, public declaration of a transformed life. But the water itself does not save. The act itself does not save. What saves is genuine repentance, genuine faith in Jesus Christ, and the new birth from above by the Holy Spirit.</p>

<p>Baptism is the outward sign of an inward reality. If the inward reality is not there, if there has been no genuine turning from sin, no real trust in Jesus, no experience of spiritual renewal, then baptism is just getting wet. Meaningful ceremony, no spiritual transaction.</p>

<h2>The New Birth First</h2>

<p>Jesus told Nicodemus that no one can see the kingdom of God unless they are born again (John 3:3). This new birth is not baptism. It is what baptism declares. The order matters: transformation, then testimony. New life within, then public declaration without.</p>

<p>We baptise people when they have genuinely encountered Jesus Christ and want to declare it to the world. We do not rush people toward water as if the water will finish what the Spirit has not yet started.</p>
    `
  },
  {
    id: "we-live-by-practice-not-preaching",
    title: "We Live by Practice, Not by Preaching",
    date: "30 June 2025",
    category: "Service",
    excerpt: "What happens when a community decides that the measure of faith is not what they say on Sunday, but what they do the other six days of the week?",
    image: "https://images.unsplash.com/photo-1609234656432-603831d5cbee?w=800&q=80",
    content: `
<p>There is a kind of Christianity that is very good at talking about itself. It produces excellent sermons, polished worship sets, and beautifully designed programmes. What it sometimes struggles to produce is changed lives and served communities.</p>

<p>We want to be a different kind of community. Not better, we have no ground for pride, but different in this one specific way: <em>we measure ourselves by what we do, not what we say.</em></p>

<h2>The Letter of James</h2>

<p>James, the brother of Jesus, was blunt about this. "What good is it, my brothers and sisters, if someone claims to have faith but has no deeds? Can such faith save them?" (James 2:14). He goes on to paint a vivid picture of a brother or sister who is cold and hungry, and the believer who says "Go in peace, keep warm and well fed" but does nothing about their physical needs. Faith without works, James concludes, is dead.</p>

<p>This is not salvation by works. It is the recognition that genuine faith produces genuine fruit, and that fruit is visible in how we treat people, especially the vulnerable.</p>

<h2>What This Looks Like for Us</h2>

<p>In our community, service is not a programme. There is no "service ministry" with a sign-up sheet. Instead, we try to cultivate a culture where every person is alert to need and equipped to meet it, in their own neighbourhood, workplace, family, and friendship circle.</p>

<p>When someone in our gathering loses their job, others quietly find ways to help. When a single mother needs childcare, people step up. When a neighbour is sick, someone brings food. Not because we organised a rota. Because we are trying to follow Jesus, who himself came not to be served but to serve.</p>

<h2>The Testimony of a Lived Life</h2>

<p>Peter writes that we should live such good lives among people that even those who speak against us may see our good deeds and glorify God (1 Peter 2:12). The most powerful apologetic, the most compelling argument for the truth of the gospel, is a community of people whose lives have been visibly transformed and who are visibly laying those lives down for others.</p>

<p>Preach by all means. Teach by all means. But let your life preach louder than your words.</p>
    `
  },
  {
    id: "why-we-dont-take-a-tithe",
    title: "Why We Don't Take a Tithe",
    date: "23 June 2025",
    category: "Giving",
    excerpt: "Generosity that flows from love looks very different from an obligation. Here is why we abandoned the 10% mandate, and what replaced it.",
    image: "",
    content: `
<p>The tithe, the instruction to give one tenth of one's income to the church, is deeply embedded in many Christian traditions. It is taught from pulpits, printed on giving envelopes, and often framed as a non-negotiable spiritual discipline. We understand where it comes from. We respectfully disagree with how it is typically applied.</p>

<h2>The Old Covenant Context</h2>

<p>The tithe in the Old Testament was a specific instruction to the nation of Israel, functioning partly as a tax system to support the Levitical priesthood and the Temple, institutions that no longer exist in the same form. The New Testament does not repeat the tithe as a command to the church. What it does say, consistently and beautifully, is something more demanding and more freeing: give as you have decided in your heart, not reluctantly or under compulsion, for God loves a cheerful giver (2 Corinthians 9:7).</p>

<h2>The Problem with Mandated Giving</h2>

<p>When giving becomes a rule, two things tend to happen. First, people who give the 10% feel they have fulfilled their obligation, and stop thinking beyond it. Second, people who cannot give 10% (because they are poor, because they are struggling) carry guilt they were never meant to carry. Neither outcome reflects the generosity of the kingdom.</p>

<h2>What We Do Instead</h2>

<p>We encourage every person in our community to prayerfully ask: what cause can I support that builds the kingdom of God? That might mean buying groceries for a struggling family. It might mean helping someone with rent. It might mean funding a child's education, or supporting a believer who is working in a difficult place. It might mean giving financially to support the practical needs of our gatherings.</p>

<p>We do not pass offering plates. We do not publish giving targets. We do not tell you what percentage to give. We trust the Spirit to lead generous people toward genuine need, and we have seen, again and again, that this works.</p>
    `
  },
  {
    id: "meeting-in-a-park-changed-everything",
    title: "Meeting in a Park Changed Everything",
    date: "16 June 2025",
    category: "Community",
    excerpt: "Our first outdoor gathering had no sound system, no order of service, and no offering plate. It was the most alive gathering we had experienced.",
    image: "https://images.unsplash.com/photo-1529070538774-1843cb3265df?w=800&q=80",
    content: `
<p>It was a cool Saturday morning. We had no venue booked, no chairs to arrange, no sound system to set up, and no order of service printed. What we had was a patch of grass under some trees, a few blankets, a thermos of tea, and about fourteen people who wanted to spend time with God and with each other.</p>

<p>I will be honest: I was nervous. It felt too simple. Too informal. Not enough like what I had been taught church should look like.</p>

<h2>What Happened</h2>

<p>Someone opened with a prayer. Someone else read a passage from Luke. A third person said "that verse you just read, can I share something about it?" And for the next two hours, something extraordinary and completely ordinary happened at the same time: people talked about Jesus. Honestly. Personally. Without a microphone or a programme or a professional to manage the flow.</p>

<p>A woman shared how a verse had kept her going through a very dark month. A young man asked a question he said he had never felt safe asking in a "normal church." An older believer answered it with gentleness and experience. We prayed for each other by name. We shared the bread and the cup together on the grass.</p>

<h2>What It Taught Us</h2>

<p>That morning reorganised something in me. I had been unconsciously equating "good church" with production value, with the quality of the sound, the polish of the worship, the length and structure of the sermon. The park stripped all of that away and left only the thing that actually matters: the presence of Jesus among his gathered people.</p>

<p>We still meet in halls and homes. We still value good teaching and meaningful worship. But that morning under the trees reminded us what we are actually doing and why. We are not producing a religious experience. We are being a family. And families can meet anywhere.</p>
    `
  }
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

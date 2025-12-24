
Bennett Cohen
·
maintouch (S23)
·
5mo ago

Founders Guide to SEO/GEO Part 1: Technical SEO (100% Free Tools, Advice, and Prompts)
I commented on a few bookface posts about SEO/GEO last month and had 20+ founders message me to talk about it.

There are a million and one ~SEO experts~ in the world. Each one has their own strategies that totally can work. The problem is that almost every founder I talked to said that they were overwhelmed with the sheer amount of information out there.

This is part one of my three part Founder’s Guide to SEO. It’s best for B2B SaaS founders.

Why listen to me? I’ve been building SEO tools for a few years at my family’s 200 customer marketing agency. Every dinner conversation for the last 25 years in my fam has been about this. I’m pretty sure my parents told me SEO bedtime stories.

My goal: you walk away with actionable things you can do today to improve visibility.

Remember, SEO is holistic. There is no singular silver bullet. Things can rank with some of these not optimized. Build good habits. Do them day in and day out. Get your basic blocking and tackling in place.

Shit takes time.

uploaded image

Btw, I’m not really here to convince you seo/geo is important. If it isn’t for you biz, this post won’t be helpful. I won’t be upset if you stop here.

What is Technical SEO
Technical SEO is everything you do in your HTML and site architecture to help search engines and LLMs understand what your site is about more easily.

A lot it is total b.s. and won’t impact rankings in a meaningful way. Most of it is set-it-and-forget-it. Fix the basics once, and you're 80% there.

We’re about to walk through the following:

Website Metadata
Structured Markup (aka JSONLD aka Schema)
Speed, Sitemap, and Search Console
Technical SEO Audits
A technical SEO audit is a report that scans your site and tells you everything that's "wrong" with it. Every major SEO tool (Ahrefs, SEMrush, Moz) has free audit features.

Many many many errors don’t matter and won’t impact rankings in a meaningful way. It’s actually more commonly used as a sales tool. Marketing agencies try to poach customers from another agency. They run audits on prospects’ sites, send it to them, and say “hey, your current agency isn’t fixing XYZ. Come talk to us and we’ll fix it for you.”

Ex:

uploaded image

In reality, most of it doesn’t matter in B2B SaaS SEO. With that in mind, let’s talk about the things that I’ve seen matter.

Website Metadata
When search engines and LLMs crawl your site, they look at your HTML.

The easiest thing for them to read and understand are HTML tags that appear on every page. The big three that matter here are Title Tags, H1s, and Meta Descriptions (see note below).

This means we can improve rankability by optimizing those tags in our site.

Let’s skip the small talk. Here’s what I’d do:

uploaded image

How to Fix Website Metadata for Free
There are quite a few tools ( I actually built one of these a bit ago ) where you drop a script tag in, and it dynamically updates these tags with optimized versions on page load. This works for SEO because there is a delay in Google crawl jobs where javascript is rendered. Vercel actually wrote a blog about this indexing delay.

However, because LLMs do not directly execute javascript, they won’t see these changes. This means you need to change the values manually if you want them to. Sure, they still reference some search index somewhere which might take that into account, so still could be valuable.

uploaded image

Here’s how to do it for free.

Get all URLs from `your-marketing-site.com/sitemap.xml `

For each page, grab the text/content, and pass to a prompt like below. Any LLM will do it fine for the most part.

task
- You are an expert SEO copywriter working for {{companyName}}
- Your task is to write a perfectly SEO optimized H1, title tag, and meta description.
- The title tag is between 50 and 60 characters, and is usually closely related to the H1 tag below
- The metadata description between 150 and 155 characters and describes what the content is about, per the rules below.
/task

rules
**H1 Tag**
- Contain a primary keyword variant
- For landing pages, you can keep the marketing speak if you really want to
- For blogs, it's just the blog title
- Example: "Best AI Presentation Makers of 2025 (with example outputs)"
- Example: "Browserbase Features, Reviews, and Alternatives"

**Title Tag**
- Max = 60 characters
- Do not match H1 exactly
- Contain a primary keyword variant
- Title tag may not contain em dashes
- Put {{companyName}} at the end after a pipe
- Example: "Best AI Presentation Makers of 2025 (with example outputs) | Plus"
- Example: "Browserbase Review and Alternatives | {{companyName}}"

**Meta Description**
- Max = 155 characters
- Include primary keyword
- Use active voice and have CTAs
- NOTE: not technically a ranking factor on Google, but matters for GEO and is shown across google pages anyway
- Example: "The best AI presentation makers for PowerPoint, Google Slides, and other presentation apps. In-depth reviews with real examples and user reviews"
- Example: "Browserbase review 2025: Features, pricing, pros & cons of this headless browser platform. Compare alternatives and see if it's right for you."
/rules

schema
{
    "h1": string;
    "title": string;
    "description": string;
}
/schema

page_content
{{content}}
/page_content
Update these values in Webflow, Framer, Next.js, etc. Note: for CMS collections, you’ll want to use their field template syntax.
Resubmit your sitemap to Google Search Console.
You might be asking yourself if there is an API that lets you automate this in Webflow/Framer. Unfortunately, no. Sorry fellas.

Bang my line if you want a full code snippet for this. Happy to drop a gist

Structured Markup (aka JSONLD aka Schema)
This is somehow the hottest thing in the GEO space right now.

I believe it when people say it’s important, but it’s been around for at least a decade, and every good marketing agency worth their salt would have put this in your site.

It’s another script tag with company specific info in structured json format. The original use is so Google can show rich text snippets for products, reviews, listings, etc.

Here’s an example:

uploaded image

Good news is that it’s super easy to fix. Because it’s really just more metadata, my point above about why you may not want to dynamically render it stands.

What Types of Structured Markup Should I Use?
There are ~800 different schemas you can put in your website, but most of them don’t matter. The best performing sites seem to use these seven most frequently.

uploaded image

How to Add Structured Markup/Schema/JSONLD for Free
Because schema has been around forever, LLMs know how to generate it!

Here’s how I’d do it for free:

Get all URLs from `your-marketing-site.com/sitemap.xml `

For each page, fetch the text/content. Based on the table above, ask an LLM to generate JSON in that format ← it will know how to do it.

Validate that the LLM generated these correctly. You can use https://validator.schema.org/ or https://search.google.com/test/rich-results. If you want to get fancy, create zod/pydantic types and validate that way.

uploaded image

Put each of these in a script tag on each page at the end of the HTML head. script type="application/ld+json"PUT YOUR JSON HERE/script

Resubmit your sitemap to Google Search Console.

Speed, Sitemap, and Search Console/Indexing
Page Speed
Page speed is a confirmed ranking factor, so your site should be quick. Use whatever tool you want for this. I just use https://pagespeed.web.dev/

It also just sucks to have people bounce because your animations take forever.

Site Architecture / Sitemap
Put every important page within three clicks of the home page. It’s not gonna nuke your SEO but the closer to the root, the better.

your-marketing-site.com/resouces/blogs/case-studies/dev-tools/resend ❌
your-marketing-site.com/customers/resend ✅
Put important pages in your header and footer, but don’t overdo it.

One cool thing you can do is link to featured blogs from your header and footer. We’ve seen this “link juice” bump strong articles.

Note: It’s better to make your blog a subfolder (your-marketing-site.com/blog) instead of a subdomain (blog.your-marketing-site.com). It’s not a deal-breaker per Google, but it’s historically better for SEO so you share domain authority (which we’ll talk about what this rlly means next time).

Search Console / Indexing
People often forget to check that Google is actually indexing pages! You can check if a page is indexed and rankable by google by searching site:{{URL}} in google directly. If it appears, you’re good! If not, you should request indexing.

uploaded image

It’s fairly simple to request indexing on Google. Just paste the URL into the search at the top of your Google Search Console dashboard, and click request indexing!

Monitor how long it takes for pages to get picked up by Google. We call this your “crawl budget.” On average it can be a measure for how much the page rank overlords like your site.

uploaded image

To be accurate, there is a lot of controversy here in the SEO community on whether this actually does anything or is just a tool from Google to appease us, but worth doing to see how quickly you get indexed.

Random Cool Thing I’ve Seen
One incredibly interesting thing we’ve seen is that sites where the product is the home page, like chatgpt, lovable, bolt, etc are absolutely freaaaaking ripppping in SEO against incumbents.

Google publicly says this isn’t a ranking factor, but some leaked documents shared they do use it. Even if an anecdote, if you’re building a self-serve or consumer SaaS tool, I’d highly recommend copying this pattern. It’s also just a good UX.

You’ve got this!
My dad (who i learned everything from) always says that SEO is like buying a house. You need to pay your mortgage every month, and over time you build equity.

It just doesn’t happen over night, and that’s okay.

Don’t let agencies or companies overcomplicate this stuff.

Don’t overthink GEO. Many of the strategies are the same. Adjust to the new strategies that have a lot of data behind them.

Get your basic blocking and tackling in order, consistently do it, and good things will come.

I really hope people get some value from this…trying to build up a collection of simple OSS resources so would love some feedback.

Of course, if you wanna go deeper on SEO / organic marketing, shoot me a message on bookface, text 202-734-0491 or email bennett@maintouch.com

Godspeed,

Bennett



AvatarAvatar
Pete Koomen and 87 others
40 comments
6.6K views

Write a comment...

Ethan Blackburn
Telophase (S23)
·
5 months ago

Never considered the impact of LLMs not rendering js on my site. Definitely need to go check the impact. Some serious alpha in this post

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

it’s p weird actually. that vercel article goes so in depth into how googlebot works. it’s fascinating technically tbh

Upvote

(1)
Reply
Reply Privately

Caelean Barnes
Gauge (S24)
·
5 months ago

Bennett CohenBennett Cohen fantastic post! A few things I’ll add that we’ve seen across top performing pages:

Make sure you’re using your h2/h3s correctly alongside your h1.
Include trust signals on your page. Who is the author? Why are they qualified to speak on this topic?
Write the post in first person.
Include pro/cons and FAQ sections. Structure these as well.
Here’s an example of the top-performing post in the HRIS space (extremely competitive, Rippling, Deel, etc): https://peoplemanagingpeople.com/tools/best-global-hris/

The above page is quite literally a pay-to-pay post, yet does incredibly well with LLMs (and Google).

You can see organizations like Rippling are writing their own versions as well: https://www.rippling.com/blog/top-global-hris-systems

If anyone is interested in learning more/improving leads from ChatGPT, always happy to chat! My calendar is here.

Upvote

(3)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

That’s on the content side which i’ll cover in another post, but also that’s also p standard SEO advice. Ex: “trust signals” are just EEAT, which has been a standard strategy forever. Anyway, i’ll cover it more in a next part of this series ! would love to get access to your stuff

Upvote
Reply
Reply Privately

Caelean Barnes
Gauge (S24)
·
5 months ago

Yep, a lot of the basics overlap heavily here 🙂 and happy to share more! Feel free to grab something here.

Upvote

(1)
Reply
Reply Privately

Suchintan Singh
Skyvern (S23)
·
5 months ago

Definitely the Taylor Swift of SEO

Upvote

(7)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

that’s what they say

Upvote
Reply
Reply Privately

Jake Johnson
Bolto (S23)
·
5 months ago

I’m curious how much your SEO playbook impacts AEO. I’m seeing plenty of people say GPT is soon to be the number one search engine and Google even has smart search built into regular search. Do you tackle this as well?

Upvote
Reply
Reply Privately

Caelean Barnes
Gauge (S24)
·
5 months ago

Hey Jake! This is exactly what we’re working on with GaugeGauge. Would love to share how we can help if you’re interested! My calendar is here.

Upvote

(1)
Reply
Reply Privately

Omri Mor
Routable (S17)
·
5 months ago

Thanks Bennett CohenBennett Cohen 💪💪💪

Going to jam with our growth team tomorrow.

Upvote

(1)
Reply
Reply Privately

Keenan D. Williams
Formerly REZI (W17)
·
5 months ago

Critical intel and loved the context deep dive + reference material. Thx Bennett.

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

yessir!

Upvote
Reply
Reply Privately

Sidharth Choraria
Infinity (W24)
·
5 months ago

Great post !
found few mistakes we were doing.

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

Thanks Sidharth ChorariaSidharth Choraria ! Appreciate it. shoot me a text if u ever have any qs

Upvote
Reply
Reply Privately

Sam Jung
Formerly Archon (W25)
·
5 months ago

loved the post, found lots of advice we weren’t following 🙏

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

thanks sam appreciate the note!

Upvote
Reply
Reply Privately

Spencer Levitt
Coast (S21)
·
5 months ago

Awesome post. Super helpful read + wonder if we’ll see LLMs render JS / how much does behavior change with grounding systems handling dynamic web content that requires js exeuction?

Upvote

(1)
Reply
Reply Privately

Joseph Besgen
The LLM Data Company (X25)
·
5 months ago

This is super insightful and such a great post!

I’m curious if the advice changes for AEO/GEO for getting your info in a future model’s pre-training corpus vs ranking highly during model web search tool calls?

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

I think trying to get into the corpus is much less relevant b/c it’s even more of a black box. at least with web search tool calling we at least know there is some search index that can be influenced moving forward

Upvote
Reply
Reply Privately

Sepand Dyanatkar
OnDeck AI (S25)
·
5 months ago

Thanks! Gonna do your tag and meta description optimization before we launch. I’ll ping back here if we get any intel from our customers actually finding us that way

Curious if anyone has gotten to the point of having GEO metrics/results 👀

Upvote

(1)
Reply
Reply Privately

Caelean Barnes
Gauge (S24)
·
5 months ago

Hey Sepand! We’re building a platform to improve your GEO presence in a data-driven way. This includes concrete metrics and results — would love to share more if you’re interested! https://cal.com/caelean/30

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

nice man! stuff takes a while so good to build that equity early.

i’ve used a bunch of the GEO data providers and they all seem solid. I don’t really have a dog in that fight and it seems like they all are doing well!

woah just checked your site. u have so many super cool seo/content things u could do. That’s awesome. excited for ya

Upvote

(1)
Reply
Reply Privately

Brad Brenner
Joon Health (W22)
·
5 months ago

Dope post, much needed 🙏

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

thanks brad. been a sec since we talked so I appreciate the note

Upvote
Reply
Reply Privately

Di Qi
Formerly Lantern (W24)
·
5 months ago

This is excellent! Can’t wait for Part 2

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

thx di :) trying to be actually valuable LOL

Upvote
Reply
Reply Privately

Mrinal Singh
Bolto (S23)
·
5 months ago

This is solid and practical advice - the home buying analogy is true. Good post. I’m curious about your thoughts on AEO as well? Just DM’d you

Upvote

(1)
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

ya I mean in general I think so much of the aeo/geo space overlaps with SEO. there are a lot of cool observational studies coming out about where each llm sources info from. super hard to spot optimize for them especially b/c it’s way more volatile than google.

from everything ive seen, if you’re generally doing well in seo and you’re true b2b where there is less organic competition compared to b2c, you tend to do well on ai platforms

so many anecdotes in either direction so who knows?

most people would benefit from getting the basics in order first. You can’t go zero to #1 in a day anyway

Upvote

(1)
Reply
Reply Privately

Jamil Bou Kheir
Firezone (W22)
·
2 months ago

Great overview! Super helpful.

Upvote
Reply
Reply Privately

Michael Wang
ROGER (W21)
·
5 months ago

wow thanks Bennett CohenBennett Cohen

Upvote
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

for sure! hope helpful. part 2 coming out tonight :)

Upvote
Reply
Reply Privately

Sandilya Miduthuri
Siftly (W22)
·
5 months ago

Bennett CohenBennett Cohen.

Really enjoyed this post. Lots of solid takeaways here.

Quick question I’ve been thinking about: if you had to actually score a page based on these best practices, how would you weight each one? Like, which ones are deal-breakers for you, and which ones are more “nice to have” depending on the situation?

Upvote
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

yo! didn’t see this. No clue how to score them. Google doesn’t release the weights on each of these as ranking factors and a lot is situational.

I tried to simplify all the noise into action items so id say just do the stuff listed if u have time.

Upvote

(1)
Reply
Reply Privately

Shahul ES
Vibrant Labs (W24)
·
5 months ago

This is great, thank you. Are you planning to share this blog in public? I would like to share it with a team member.

Upvote
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

hey i wasn’t planning on sharing it publicly with quite as much detail, but if u text me I can share a slightly stripped version ?

Upvote

(1)
Reply
Reply Privately

Cooper Newby
Bluecrew (S15)
·
5 months ago

https://basehub.com/ check out this headless CMS for AI first automation. Been very impressed by ease of setup and AI first integration / MCP / Claude code. Still pretty new, but really great so far. Going to see if I can add this logic to the agents in basehub

Upvote
Reply
Reply Privately

Chris Le
Pax (S24)
·
5 months ago

This is gold, thanks Bennett!

Upvote
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

thanks!

Upvote
Reply
Reply Privately

Daniel Ho
Apten (S24)
·
5 months ago

crazy amounts of value in here - thanks for sharing!

Upvote
Reply
Reply Privately

Bennett Cohen
OP
maintouch (S23)
·
5 months ago

yessir thx dude

Upvote
Reply
Reply PrivatelyMany marketing agencies make SEO feel like a black box. Every founder I talk to about this is overwhelmed by the sheer amount of info out there, and most of it is a load of bs.

Look, three things matter: technical seo (last post), backlinks, and content.

This post is all about how to get backlinks.

TLDR: get more high quality backlinks → signals to google you’re a valuable site → easier to rank (both seo and geo)

Why listen to me? I’ve been building SEO tools for years at my family’s 200 customer marketing agency. My dad used to make me do manual backlink outreach as punishment when I was a kid ;)

Remember, SEO is holistic. There is no singular silver bullet. Things can rank without everything optimized. Build good habits. Repeat them every month. Shit takes time.

Let’s get into it.

uploaded image

Definitions:

Backlink: a link from one website to another website. When Site A links to Site B, that's a backlink for Site B because it links back to the site we care about.
Authority: a measure of the overall SEO strength of a website. That’s it.
Each SEO tool calls it something different. Moz calls it Domain Authority (DA). Semrush calls is Authority Score (AS). Ahrefs calls it Domain Rating. It’s all the same.

One level deeper, it’s a measure of how good a website’s backlinks are.

Why do backlinks matter?
Search engines view backlinks as votes of confidence in a site, because why would you link to a site that isn’t valuable? The more quality backlinks a site has, the more trustworthy and authoritative it appears.

Quick aside: if you’ve ever seen the term “keyword difficulty (KD),” this is directly correlated to the authority of the top rankings sites for a given keyword. The stronger the ranking sites are, the harder it will be to rank.

Backlink nuances
Nothing comes easy in this world. All life is suffering. We’re all gonna die in the end.

sorry, got distracted.

Not all backlinks are created equal. Some things to look out for:

Follow vs. Nofollow Backlinks
When someone links to you, they can either give you a "follow" link (which passes SEO juice) or a "nofollow" link (which doesn't). Most social media links are nofollow. Most editorial links from blogs and news sites are follow. You want follow links, but don't stress too much about it tbh. Google has said they treat some nofollow links as hints anyway.

uploaded image

Link Equity
Think of this as the SEO power that gets passed from one site to another through a link. A link from the New York Times passes way more equity than a link from your cousin's blog about cats. The stronger the linking site's authority, the more equity flows to you.

uploaded image

Relevance and Quality
Back in the day, you probably could get a bunch of super shitty backlinks from scam websites and see your authority boom. Doesn’t really work like that now.

In most cases, you’d rather have 10 links from high-authority, legit sites in your industry than 100 dog-shit links. Seeing a common trend? People do something hacky → google figures out how to block it → rinse and repeat.

Anchor Text
This is the clickable text in the link. "Click here" tells Google nothing. "Best project management software" tells Google exactly what your site is about. Don't overthink it, but don't waste the opportunity either.

Let’s pause for a sec
The section above might make you feel like you have to control very aspect of a backlink, but that’s not possible naturally.

Keep in mind that SEO is holistic. You’re not gonna optimize every link. You can’t fix every single thing. It’s just not worth your time.

How NOT to get backlinks
1. Private Blog Networks
If you’re smart, you might look at this and think you could spin up a bunch of sites and just create backlinks to your own site. Good idea, right? Unfortunately, no. They call this a Private Blog Network (PBN) and it’s been mostly eradicated by Google. At best you’ll waste time and get no benefit. At worst, you’ll get penalized and de-indexed by the page rank overlords.

uploaded image

2. Backlink Exchange Network
This idea has floated around bookface quite a few times. On a small scale, I think it’s totally fine, especially if it’s actually relevant to your business.

If ppl want me to make an official one that won’t screw people, i’d be down but feel like there r some options out there.

Here are a few gotchas with it:

Make sure you’re getting backlinks from sites that are actually relevant to your industry. Some examples could be:

AI infra tool links to application layer companies
Vertical AI tool links to other vertical AI tools in the space
Use a snake exchange if possible so you don’t have reciprocal backlinks. That way it can’t be tracked.

uploaded image

I talk about this a bit below, but instead of just pure backlinks on a page, try to write a high value guest blog.

Dis u?

uploaded image

HOW DO I GET BACKLINKS?
I’ll go into each one below, but for lazy people, here’s the overview:

uploaded image

Method 1: Directory Submissions
If you’re a SaaS or AI tool, the easiest way to get solid backlinks is to submit your company to a bunch of directories of SaaS tools. Stuff like theresanaiforthat dot com
These aren’t the highest quality, but still good esp if you vet by their authority.
I have a running list of ~100 directories that are free. Pasting here is annoying to read but if people are still reading this deep into a post, just text me and I’ll give to u for free.

Method 2: PR or Link Building Agency/Broker
You pay an agency to get you spots in publications or get backlinks. These agencies fluctuate like crazy.
Good PR agencies have relationships with journalists and know how to pitch stories. They'll get you in Forbes, TechCrunch, your industry publications, podcasts, etc.
Many agencies that advertise link building are garbage. They'll promise you the moon and deliver a blog post on "EntrepreneurInsights247.net" that nobody reads.
Method 3: Reach out to Blogs

Find articles where your competitors are mentioned and ask to be included too.
The process:
Google "best [your category] tools 2025"
Find listicles that mention your competitors (Zapier does a lot of these)
Reach out to the author with a personalized email
Explain why your tool deserves a spot
Here’s an email template that I’ve seen work:

uploaded image

SANITY CHECK: Skip the ones that are obviously paid placements (Forbes, Wired, etc.) unless you have a massive budget. Focus on industry blogs, smaller publications, and independent reviewers.
Pro tip: Offer to update them on new features, provide quotes for future articles, or connect them with your customers for case studies. You might still have to pay, and that’s okay if they are high quality. Also, if the page is ranking well, you’ll get the added benefit of being featured there.
Method 4: Guest Posting
Write content for other people's blogs in exchange for a backlink.
Don't just blast "GUEST POST OPPORTUNITY???" emails to random blogs. Instead, find companies that complement yours (not compete) and propose content that helps both audiences.
Example: Let's say I run an AI-native organic marketing agency. I might write a guest post for a LinkedIn automation tool that talks about how to combine content marketing + outbound campaigns. Their audience learns something useful, my agency gets exposure, everyone wins.
The content has to actually be good. No thin, promotional garbage. Write something you'd be proud to put on your own blog.
So for a YC network, it’s better to do it like this instead of just pure backlink listings because context and relevance matters.

Red flag: If someone is actively soliciting guest posts from random people, their site probably isn't worth your time.

FAQ

How long does it take to see results from backlinks? Don't expect miracles overnight. Google takes 2-6 months to fully recognize and pass authority from new backlinks. I've seen people get upset at week 3 and start buying sketchy links. Don't be that person. Good things take time.
Should I disavow bad backlinks pointing to my site? Only if they're obviously spammy (like porn sites linking to your B2B SaaS). Google's gotten pretty good at ignoring shitty links automatically.
How many backlinks do I need to rank? Wrong question. It's not about quantity. I've seen sites with 10 killer backlinks outrank sites with 1,000 garbage ones. Quality beats quantity every time. Also, how many times do I have to say that SEO is holistic.
My competitor has way more backlinks than me. Am I screwed? Nope. SEO isn't just about backlinks. Get technical SEO and content in order as well.
Some closing thoughts

My dad always says that SEO is like buying a house. Pay your mortgage every month and build equity over time.

Do the small stuff consistently (directories, outreach, guest blogs) and good backlinks will start happening naturally. People discover your stuff and link without you asking.

As always, I hope people get real value from this….hoping this collection of free resources can help people out.

Of course, if you wanna go deeper on how to get backlinks or just talk SEO/GEO/organic marketing, happy to help. Shoot me a message on bookface, text 202-734-0491 or email bennett@maintouch.com

Godspeed,ounder’s Guide to SEO/GEO Part 3: How to Write Blogs that Rank
Alright, alright, alright, this is part three of a series. Part 1: Technical SEO and Part 2: Backlinks here.

There are so many SEO experts. Many are good. Many are bad.

I’ve now spoken to 172 founders about it. Most are confused on how to find ideas and write blogs.

I want to solve this for you.

Why listen to me? I spent years building SEO tools at my family’s 200 customer marketing agency. I hate to say it, but it literally runs in the family.

My goal: you walk away knowing how to come up with ideas and write quality blog content.

Remember, SEO is holistic. There is no silver bullet. Things can rank without perfect optimization. Focus on building strong habits. Do them week in and week out.

Shit takes time.

uploaded image

Let’s get some terminology straight
Before we go any further, let’s get some quick vocab in place:

uploaded image

Think about topics instead of keywords
We call search terms “keywords” in the SEO world or “prompts” in the AI search world, but in reality, you should be thinking about a grouping of prompts or keywords.

I call them topics.

A topic is made up of tons of keyword variants that have very similar search results. Both google’s page rank algorithm

LLMs are smart enough to identify that two keywords are similar. Later in this blog, I talk about some cool ML stuff I do around this with clustering algorithms.
Now, using these four words, your content strategy should stack-rank topics based on volume, keyword difficulty, and relevance to drive qualified traffic to your site.

Pretty simple, right?

uploaded image

Great, the goal has been set. Enough talk.

Let’s get down to bidness.

Method #1: Bottom of Funnel Content
Bottom-of-funnel (BoFu) content just means writing about topics that a potential customer who is very close to a purchase decision might look up.

So let’s say someone needs to build a slide deck. They’ve heard of all those AI tools for it, so they look up “best ai powerpoint maker” . Or maybe they already have heard of some of them and they look up something more direct like “gamma ai review”

uploaded image

You, as an AI powerpoint maker platform, want to write content about each of these to own the narrative about topics that are very close to someone purchasing.

BoFu content usually means listicles, competitor reviews, pricing guides, or head to head comparisons. We’ve all seen them before:

uploaded image

The point of this strategy is to recognize that these types of searches are generally lower volume, but VERY HIGH INTENT. Our goal is to drive quality traffic, not just traffic.

Just to get ahead of this, here are some questions I’ve heard in my calls:

“I don’t want to talk badly about competitors.”
You actually don’t have to. It’s about showing up in the conversation when someone is close to a purchase point.
“I don’t want to acknowledge competitors”
If you’re in a space that’s sufficiently large, SEO is a channel for you. Why not own the narrative? Competitors will do it.
“I already have a landing page comparing competitors. Why write a blog?”
Landing pages tend to have way less text, so it will be hard for it to rank. I’ve been seeing blogs do appreciably better ranking for BoFu terms because they can contain way more relevant, compelling content.
“My competitors are doing tons of this. How can I even rank here?”
Write the most up to date, quality content. Because everyone's doing this, having a good backlink strategy allows you to juice up these pieces of content by demonstrating authority and credibility to these specific pages which helps make sure the content you post here shows up higher. Ping me if you want to talk about that.
Method #2: Fill competitor keyword gaps
If you haven’t invested in SEO, but competitors have, great news!! We can find gaps! Let’s freaking go.

The rationale is pretty clear: if a competitor has invested marketing budget to rank on a topic, and that topic is also relevant to you, you should write content to try to rank for it too.

uploaded image

Here’s how you find these gaps very simply:

Go to the keyword gap page of any SEO tool (SEMRush, Ahrefs, etc)
Put in your url and competitor’s url
Apply these filters: competitor rank in top 10, keyword difficulty < 50%, exclude keywords containing their name.
Click “missing”
This will leave you with a list like this (for an example GPU platform like thunder compute).

uploaded image

Now, we can go through each of these keywords, decide which are relevant, and create a list of 10-30 topics that are most relevant to us. We can then stack rank them by search volume, intent, relevance, and keyword difficulty to decide what to prioritize.

Each of these becomes a piece of content you should write about.

Random technical callout: one thing I do is pull all the search results for hundreds of thousands of keywords and create a similarity function based on results so we can run a classical ML clustering algorithm on them to identify topics….blog post for another time.

This is how you fill gaps and start to rank for things that competitors have invested in.

uploaded image

Method #3: Double down where you’re already ranking
If you’ve already invested in SEO, you’re likely ranking for a broad set of keywords. It’s easier to go from page 4 to page 1 than it is to go from not ranking to page 4.

It’s time to double down.

uploaded image

Here’s how you find what content to write about based on things you’re already ranking for:

Go to the organic results page of any SEO tool (SEMRush, Ahrefs, etc)
Apply filters: ranking 3 to 40, keyword difficulty < 50%, exclude keywords containing your name.
Go through the list of keywords (remember think about topic clusters).
For each one, look at the page that ranks and decide if that page’s content is the most relevant to the keyword.
If it is the most relevant, you’ll want to add a few hundred words to that page specifically about this new topic that wasn’t covered well.
If it’s not the most relevant, you should write a net new blog post about this!
The core idea here is that if we are already ranking for a topic, Google has clearly valued something about our site or that piece of content.

It’s our job to decide whether we should update an existing blog OR splinter off and write a new blog.

Let’s go through an example. Suppose you’re an accounts payable platform with a blog post titled “Accounts Payable Best Practices”

You rank 12th for “invoice approval workflow”
It briefly mentions approvals and it’s relevant, so add content to that blog that goes a bit deeper.
You rank 30th for “automated invoice processing”
The intent of this keyword is much more looking for a feature (not educational), so we splinter off and create a more transaction oriented blog, and link the two.
If Google already ranks you for a topic, decide whether to expand existing content or spin off a new post so you build on what Google already trusts.

Method #4: Find the hidden long tail
Long tail searches are those that are, well, on the long tail of search volume. Very specific keywords that have lower search volume. They also are literally longer.

uploaded image

If you can write content that matches these exact long tail queries someone might search up or ask an LLM, you’ll rank very highly b/c your content will be the most relevant.

Now, the search volume estimate data from all the SEO data tools is a steaming pile of sh*t once you get to the lower volumes, so DO NOT TRUST IT.

Our job is to find what long tail keywords people might be searching up.

One interesting method that works well if you’re not even sure what people are looking up is to dump sales calls to an LLM and ask it to find relevant searches related to those calls. Then you can take them to an SEO tool or agency, and stack rank topics based on volume, relevance, and keyword difficulty. This is what I do.

This is a very hot thing with GEO companies. Most just ask an LLM to come up with a bunch of long tail questions someone might ask, and then they try to include specific answers to these in the content. No scary monsters there.

What makes good content?
Look, there are a million ways to write a piece of content that ranks. Don’t let anybody tell you otherwise. If you’re new to SEO and want some very clear guidelines to point to, here you go: 8 blogs per month, 1500-2K words, 3-7 images, 5-15 internal links, 3-5 external links, at least 7-12 H2 sections + plenty of H3s, only one H1. Make sure you include some references across your page about who you (author or company) are and why you have experience, expertise, authority, and trust (called EEAT in the biz). In a world of infinite content, stand out.

Anecdotally, I’ve found it worth the effort to have an FAQ and TLDR section, write in first person where it makes sense, and add structured markup to the head of the blog. Make sure your technical SEO is optimized per my previous post on it.

I’ll save intrasite linking for another post, but those internal links should point to other relevant blogs and also point back up to conversion focused landing pages.

How is AI search different than SEO
From all the data I’ve seen for SaaS companies, good SEO content is good GEO.

ChatGPT uses google under the hood, and the citation statistics are converging toward Google rankings. This doesn’t mean for every single keyword/prompt, because there’s an infinite long tail and variance is much higher.

But, in the long run, I’ve yet to see a company with strong SEO do poorly on AI Search.

One interesting human behavior thing is that queries tend to be much higher intent (closer to the bottom of funnel), which is why you’ll see all the GEO companies push you to write that style content.

My take: LLMs search the internet when looking for sources to cite. So if you do a good job at ranking high in the places that LLMs are scraping, then you will likely show up there.

Just a reminder that with any data “experiments” in marketing, make sure to ask sample size and methodology, time horizon, and metrics.

AI Slop or Not? Which way western man?
I wish there were some hack that you can do to print out a bunch of content that ranks immediately.

Spoiler alert, there isn’t. (If you have figured something like this out that is also readable, lmk)

In a world where everyone can make a bunch of blogs from a single for loop, volume isn’t really a competitive advantage. Sure, sometimes AI content ranks, but sometimes it doesn’t. Hallucinations suck. Btw, page dwell time does improve rankings!

So as you’re writing this content, ask yourself:

Is this adding anything to the internet?
Would you actually spend time reading it?
Don’t print out pure AI slop, plz.

My closing thoughts
My dad always says that SEO is like buying a house. Pay your mortgage every month and build equity over time.

Let’s get the basics right. Own the narrative about competitors, find gaps where you’re not ranking, double down on areas where you are, try to find the hidden long tail. Do this month after month.

While you’re at it, optimize your technical SEO and build quality backlinks. There’s quite a bit I didn’t talk about with cannibalization, splintering, and content refreshes, but let’s save that for another day.

As always, I really hope people get free value from this. Nothing hidden.

I’ve been helping ~30 companies with SEO/GEO so if you’re thinking about it as a growth strategy or just want me to do all of this for you, just email me bennett@maintouch.com or text 202-734-0491 and I can give you some advice.

But seriously, I just gave you the formula above. That’s it.

Godspeed,

Bennett

p.s. im doing a webinar today on how to get your first 100 customers from SEO/GEO for vertical AI companies. We have 65 sign ups if anyone else wants to join: https://maintouch.com/vertical-ai-webinar


What Publishing 500+ Pages Taught Me About SEO & AEO (Seed/Series A Edition)
After exiting Mailwarm, I launched 7aeo to tackle AEO (answer engine optimization) / GEO wave.

Here are my learnings after publishing 500+ pages over the past 10 months.

Disclaimer: This is simply my experience, not the truth.

Here are my learnings to go from 0 to 1 in AEO and SEO with a recent domain (require some tweaks for more historical websites and lot of existing pages):

1. The scope of AEO

AEO includes every surface where answers are generated:\

Google AI surfaces (AI Overviews, AI-expanded People Also Ask, AI-rewritten featured snippets)\
LLM answers (ChatGPT, Claude, Gemini, Perplexity…)
Winning AEO happens in two ways:

(a) being mentioned in an AI answer

(b) being cited as a source under the answer

You want both.

2. Search is becoming personalized

People don’t type keywords, they prompt their exact situation.

Your content must solve contextual problems, not chase static queries.

3. Content is key

Content is your foundation.

No content = no mentions, no citations, no authority.

But make it buyer-level, niche, and actionable, not broad filler.

4. AI content works (when supervised)

We see strong results across companies.

Google openly says AI-generated content is allowed.

We see strong results across companies.

The key: guide it, read it, correct it, narrow it.

Unguided AI drifts, guided AI performs.

5. Always add Schema Markups

Schema = structured metadata describing what your page is (Article, FAQPage, Product, HowTo, Review, Organization…)

Schema helps LLMs + search engines:

• parse your information

• classify your content type

• extract clean answers

It’s a machine-interpretation layer.

6. Always add FAQs

LLMs digest Q&A structure perfectly.

Google also uses FAQs to trigger AI expansions and rich snippet formats.

7. Backlinks matter, but with nuances

High-quality backlinks (PR, partnerships, trusted sites) help you:

• win more competitive keyword intents

• win more competitive AI prompts

• raise your “authority category”

But:

• avoid low-quality backlink purchase

• avoid spammy marketplaces

• avoid obvious link schemes

A better plan:

Dominate niche prompts/searches instead of fighting giants in ultra-competitive queries.

Backlinks lift you into a stronger category. but do not prevent you from winning AEO mentions without them.

8. Add catchy main image to each page

Google surfaces images heavily in standard results, Google Images, but also within Google Overviews sources.

A good illustration can expand reach and clicks. AI illustration work well.

9. Add an LLMS.txt

LLMS.txt tells LLM crawlers what they can/cannot ingest.

No strong proof it’s useful yet., but it’s free, harmless, and takes 5 minutes.

Website builders generally assist to add it.

10. Don’t fear most technical SEO errors: except the real ones

The ones that matter are:

• important 404s

• wrong canonical tags

• missing/duplicate meta titles

• duplicate competing pages

• crawl loops

• slow loading speed

• broken hreflang

• broken or wrong sitemaps / robots.txt

Make sure your pages are well indexed on Search Console.

Other fixings won’t do much difference.

11. Reddit matters, but don’t automate it

Reddit is cited by LLMs because it’s human, raw, contextual.

Bots get banned fast. Full automation takes lot of handling time and is at risk, better do it manually with brand/topics alerts triggers.

Use your real persona:

• answer when relevant

• mention your brand naturally

• avoid links (ban risk)

Human replies > bot farms.

12. Long-tail is your oxygen if you’re not the leader

Eventually you aim for “best tool to do X.”

But you start with:

• “best tool to do X for Y”

• “best tool to do X for Y and Z” (hyper-niche)

Low volume + low difficulty = compounding authority.

13. Segment your service into hubs (features, verticals, use cases)

LLMs understand a product better when its content is spread across clear sub-segments:

• features

• verticals

• use cases

• customer types

Do not describe your service in one generic page.

Split it.

One page per angle, one problem per page.

This helps LLMs perceive the full scope of what you do and pick the right part of your product for each user prompt.

14. Do tops, comparisons, and year-based articles

“Top tools for X”

“X vs Y vs Z”

“Best tools for X in 2025”

Search engines love them, users click them, LLMs cite them.

15. Cover your gaps (keyword & answer gaps)

Competitors talk about things you don’t.

Fill them to manifest your expertise to search engines and LLM.

Show that you cover your entire domain.

16. Talk about others

Write Y vs Z even if Y and Z are your competitors or other services addressing the same target.

LLMs may not mention your brand but will cite you as a source, bringing discovery and authority.

17. Don’t underestimate your blog

Your blog isn’t decoration.

It’s a distribution machine.

Each page is a door to your product.

Build daily. Spread everywhere.

18. Post a glossary

One definition = one page.

Glossaries dominate “what is / define / explain / difference” queries and prompts.

19. Watch your slugs.

Clean, short, timeless.

Don’t include the year, even if the title has it.

You’ll update the page later.

20. Get good UX, don’t over-optimize

A solid UX matters more than fancy tricks:

• clean H-tags

• clear structure

• fast load

Google sees structure. LLMs do too.

21. Strengthen your internal linking

Internal links help both search engines and LLMs map your domain.

Link every page to your main themes, link between related subtopics, and link upward to your core pages.

This reinforces your topical authority and guides models toward the right piece of content when generating answers.

22. Execution tracking and adjustment

Track monthly (clicks, conversions, mentions, new queries).

Same input does not give the same output across websites.

Adjust continuously your contents, explore topics, cover main topics, go for long-tail situations.

23. SERPs change fast, AI answers even faster

Being number 1 or cited today is temporary,.

Your website must move too: new content, updates, new links, refreshed structure.

24. Trust the process but not blindly

You should see clicks, leads, mentions.

But there’s no “GPT Search Console” (yet).

AEO is measured indirectly through AI-search tools and your traffic patterns.

25. Consistency compounds

Consistency is the multiplier.

Every page, every mention, every update compounds your authority.

This is a compounding game, not a linear one.


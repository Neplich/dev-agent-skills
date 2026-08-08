---
name: competitive-brief
description: "Produce competitor positioning briefs or sales battlecards from current sourced research, including messaging, gaps, opportunities, threats, and recent developments. Use after pm-agent routes competitive research."
visibility: internal
argument-hint: "<competitor or market segment>"
---

# Competitive Brief

> If you see unfamiliar placeholders or need to check which tools are connected, verify the available tools first.

Research competitors and generate a structured competitive analysis comparing positioning, messaging, content strategy, and market presence.

For battlecard mode, produce one complete page per competitor with these
explicit sections: Quick Overview, Their Pitch, Our Position, Strengths,
Weaknesses, Objection Handling, Landmines to Set, Landmines to Defuse, Win/Loss
Themes, Discovery Questions, Talk Track, and POC Guidance. Do not replace this
page contract with a generic comparison narrative.

## Trigger

User runs `/competitive-brief` or asks for a competitive analysis, competitor research, or market comparison.

## Inputs

Gather the following from the user:

1. **Competitor name(s)** — one or more competitors to analyze (required)

2. **Your company/product context** (optional but recommended):
   - What you sell and to whom
   - Your positioning or value proposition
   - Key differentiators you want to highlight

3. **Focus areas** (optional — if not specified, cover all):
   - Messaging and positioning
   - Product and feature comparison
   - Content and thought leadership strategy
   - Recent announcements and news
   - Pricing and packaging (if publicly available)
   - Market presence and audience

## Research Process

When the user supplies dated research notes or an exported source packet, read
those materials first and preserve their source/capture boundaries. Use web
search only to fill an explicitly requested gap. If live search is unavailable,
complete the artifact from the supplied packet and mark unsupported claims as
assumptions or follow-up research instead of inventing current facts.

For each competitor, research using web search:

1. **Company website** — homepage messaging, product pages, about page, pricing page
2. **Recent news** — press releases, funding announcements, product launches, partnerships (last 6 months)
3. **Content strategy** — blog topics, resource types, social media presence, webinars, podcasts
4. **Review sites and comparisons** — third-party comparisons, analyst mentions, customer review themes
5. **Job postings** — hiring signals that indicate strategic direction (optional)

### Research Sources

Gather intelligence from these categories of sources:

#### Primary Sources (Direct from Competitor)
- **Website**: homepage, product pages, pricing, about page, careers
- **Blog and resource center**: content themes, publishing frequency, depth
- **Social media profiles**: messaging, engagement, content strategy
- **Product demos and free trials**: UX, features, onboarding experience
- **Webinars and events**: topics, speakers, audience engagement
- **Press releases and newsroom**: announcements, partnerships, milestones
- **Job postings**: hiring signals that reveal strategic priorities (e.g., hiring for a new product line or market)

#### Secondary Sources (Third-Party)
- **Review sites**: G2, Capterra, TrustRadius, Product Hunt — customer sentiment themes
- **Analyst reports**: Gartner, Forrester, IDC — market positioning and category placement
- **News coverage**: TechCrunch, industry publications — funding, partnerships, narrative
- **Social listening**: mentions, sentiment, share of voice across social platforms
- **SEO tools**: keyword rankings, organic traffic estimates, content gaps
- **Financial filings**: revenue, growth rate, investment areas (for public companies)
- **Community forums**: community forums (e.g. Reddit, Discourse), industry chat groups (e.g. Slack communities) — user sentiment

### Research Cadence
- **Deep competitive analysis**: quarterly (full research across all sources)
- **Competitive monitoring**: monthly (scan for new announcements, content, messaging changes)
- **Real-time alerts**: ongoing (set up alerts for competitor brand mentions, press, job postings)

## Competitive Brief Structure

### 1. Executive Summary
- 2-3 sentence overview of the competitive landscape
- Key takeaway: your biggest opportunity and biggest threat

### 2. Competitor Profiles

For each competitor:

#### Company Overview
- What they do (one-sentence positioning)
- Target audience
- Company size/stage indicators (funding, employee count if available)
- Key recent developments

#### Messaging Analysis
- Primary tagline or headline
- Core value proposition
- Key messaging themes (3-5)
- Tone and voice characterization
- How they describe the problem they solve

#### Product/Solution Positioning
- How they categorize their product
- Key features they emphasize
- Claimed differentiators
- Pricing approach (if publicly available)

#### Content Strategy
- Blog frequency and topics
- Content types produced (ebooks, webinars, case studies, tools)
- Social media presence and engagement approach
- Thought leadership themes
- SEO strategy observations (what terms they appear to target)

#### Strengths
- What they do well
- Where their messaging resonates
- Competitive advantages

#### Weaknesses
- Gaps in their messaging or positioning
- Areas where they are vulnerable
- Customer complaints or criticism themes (from reviews)

### 3. Messaging Comparison Matrix

| Dimension | Your Company | Competitor A | Competitor B |
|-----------|-------------|--------------|--------------|
| Primary tagline | ... | ... | ... |
| Target buyer | ... | ... | ... |
| Key differentiator | ... | ... | ... |
| Tone/voice | ... | ... | ... |
| Core value prop | ... | ... | ... |

(Include user's company only if they provided their positioning context)

### 4. Content Gap Analysis
- Topics your competitors cover that you do not (or vice versa)
- Content formats they use that you could adopt
- Keywords or themes they own vs. opportunities they have missed

### 5. Opportunities
- Positioning gaps you can exploit
- Messaging angles your competitors have not claimed
- Audience segments they are underserving
- Content or channel opportunities

### 6. Threats
- Areas where competitors are strong and you are vulnerable
- Trends that favor their positioning
- Recent moves that could shift the market

### 7. Recommended Actions
- 3-5 specific, actionable recommendations based on the analysis
- Quick wins (things you can act on this week)
- Strategic moves (longer-term positioning or content investments)

## Battlecard Mode

当 pm-agent 以 `battlecard` 信号路由初始请求时，直接产出单页 battlecard 产物，不做完整 brief；基于已有研究或现场补充检索，覆盖每家竞品：

- **Quick Overview**：他们做什么、目标客户、定价模型摘要、近期关键动态
- **Their Pitch**：自我描述、主要口号、声称的 top 3 差异点
- **Strengths（如实）**：真正有竞争力的地方、客户好评点、领先的能力
- **Weaknesses**：一致的客户抱怨、技术限制、能力缺口
- **Objection Handling**：预期会听到的反对话术与建议回应
- **Landmines to Set**：引导客户早期暴露其痛点的提问
- **Landmines to Defuse**：竞品可能引导客户问你的问题与应对
- **Win/Loss Themes**：赢单与丢单的常见原因、偏好各自的客户类型

无法确认的信息标记为假设或需验证，不编造确定结论；标注研究日期。

## Output

在 Battlecard Mode（pm-agent 以 `battlecard` 信号路由的初始请求）下，只输出单页 battlecard 产物，不再输出完整 brief，也不询问是否创建 battlecard。其他请求输出完整 competitive brief。无论哪种模式，都注明研究日期，让用户知道数据的时效性。

After the brief, ask:

"Would you like me to:
- Create a battlecard for your sales team based on this analysis?
- Draft messaging that exploits the positioning gaps identified?
- Dive deeper into any specific competitor?
- Set up a competitive monitoring plan?"

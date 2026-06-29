---
layout: default
title: "Insight Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 29 条内容中筛选出 12 条重要资讯。

---

1. [GLM 5.2 开源模型在网络安全测试中超越 Claude](#item-1) ⭐️ 8.0/10
2. [1960-2026 年历史内存价格可视化](#item-2) ⭐️ 8.0/10
3. [探索纽约公共图书馆巴托尔夫收藏的 5000 份历史菜单](#item-3) ⭐️ 8.0/10
4. [用 Claude Code 分析 MRI：一次个人实验](#item-4) ⭐️ 8.0/10
5. [布朗大学教授谴责大规模 AI 作弊](#item-5) ⭐️ 8.0/10
6. [《儿童在线安全法案》要求强制年龄验证](#item-6) ⭐️ 8.0/10
7. [Jon Udell：主张用'agent in the loop'取代'human in the loop'](#item-7) ⭐️ 8.0/10
8. [谷歌因算力不足限制 Meta 使用 Gemini](#item-8) ⭐️ 8.0/10
9. [LibrePods：开源解放 AirPods 功能](#item-9) ⭐️ 7.0/10
10. [Codex 中排除敏感文件的问题仍未解决](#item-10) ⭐️ 7.0/10
11. [浏览器 Ctrl+S 快捷键阻塞波兰语变音符号输入](#item-11) ⭐️ 7.0/10
12. [可编辑权重的交互式最小化 Transformer](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GLM 5.2 开源模型在网络安全测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

Z.ai 发布的 GLM 5.2（7530 亿参数开源模型）在 Semgrep 的网络安全基准测试中表现优于 Claude Code，检测率达到 41%，而 Claude Code 为 32%，每发现一个漏洞的成本仅 0.17 美元。 这一结果凸显了开源 AI 模型在网络安全等专业领域的快速进步，可能为闭源模型提供经济高效的替代方案，并挑战了闭源模型更优越的假设。 GLM 5.2 支持百万 token 上下文窗口，专为长周期智能体工作流设计，但社区成员指出，运行完整的 7530 亿参数模型需要大量硬件资源，如多个高端 GPU。

hackernews · jms703 · 6月28日 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: GLM 5.2 是 Z.ai 最新的旗舰模型，接替 GLM 5.1。它是一个开源大语言模型，可在 Hugging Face 和 Ollama 等平台获取。Semgrep 基准测试评估模型在代码中查找网络安全漏洞的能力，并比较性能和成本效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ollama.com/library/glm-5.2">GLM - 5 . 2 is Z. ai ’s flagship model for the era of long-horizon tasks.</a></li>
<li><a href="https://openrouter.ai/z-ai/glm-5.2">GLM 5 . 2 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：部分用户称赞 GLM 5.2 是日常编程的经济高效实用模型，但也有用户指出基准比较存在缺陷，因为 Claude Code 是智能体工具而非纯语言模型。还有关于硬件需求以及与其他开源模型（如 DeepSeek V4 Pro 和 MiMo 2.5 Pro）的比较讨论。

**标签**: `#GLM`, `#AI benchmarks`, `#Open models`, `#Cybersecurity`, `#Machine Learning`

---

<a id="item-2"></a>
## [1960-2026 年历史内存价格可视化](https://dam.stanford.edu/memory-prices.html) ⭐️ 8.0/10

该数据集提供了内存价格趋势的独特长期视角，对于理解硬件经济学、行业周期以及 AI 需求推动近期价格飙升的影响至关重要。 价格未进行通胀调整，早期数据（1990 年前）基于不现实的每 GB 定价，因为当时存储容量以 MB 或 KB 计。该数据集延续了现已归档并恢复的 jcmit.com 的工作。

hackernews · vga1 · 6月28日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=48710092)

**背景**: 内存价格历史上呈指数级下降，但近期 AI 需求引发了超级周期，价格飙升。例如，2026 年 DRAM 价格预计同比上涨 125%，NAND 闪存上涨 234%。该可视化捕捉了这些长期趋势和繁荣-萧条模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dam.stanford.edu/memory-prices.html">Memory Prices | DAM</a></li>
<li><a href="https://newsletter.semianalysis.com/p/memory-mania-how-a-once-in-four-decades">Memory Mania: How a Once-in-Four-Decades Shortage Is Fueling ...</a></li>
<li><a href="https://www.cnbc.com/2026/03/11/memory-stocks-ai-chips-demand.html">The memory stock cycle of boom-bust-repeat is over ... - CNBC</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了过去 20 年明显的价格周期，将其归因于制程节点、晶圆厂扩张和 AI 需求。一些人指出通胀调整会使早期价格更高，而另一些人批评现代软件臃肿。还有人担忧数据集的长期保存。

**标签**: `#memory`, `#hardware`, `#pricing`, `#historical data`

---

<a id="item-3"></a>
## [探索纽约公共图书馆巴托尔夫收藏的 5000 份历史菜单](https://pudding.cool/2026/06/menu-story/) ⭐️ 8.0/10

《布丁》发布了一个数据可视化项目，分析了纽约公共图书馆巴托尔夫收藏的 5000 份菜单（1880-1920 年），揭示了当时的烹饪趋势和餐饮文化。 该项目将数字人文与数据可视化相结合，为历史饮食文化和社会史提供了一个独特的窗口，并使普通大众也能接触这些内容。 巴托尔夫收藏最初约有 25,000 份菜单，现在纽约公共图书馆在线提供近 19,000 份数字化条目。该可视化专注于 19 世纪末至 20 世纪初的 5,000 份菜单子集。

hackernews · xbryanx · 6月28日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=48707763)

**背景**: 纽约公共图书馆的巴托尔夫菜单收藏由弗兰克·E·巴托尔夫整理，她毕生致力于收集餐馆和活动的菜单。该收藏涵盖 1850 年代至 1920 年代，是研究饮食历史和社会变迁的丰富资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digitalcollections.nypl.org/collections/the-buttolph-collection-of-menus">The Buttolph collection of menus - NYPL Digital Collections</a></li>
<li><a href="https://www.thehistoryblog.com/archives/40485">Browse 18,000 historic menus in the New York Public Library – The History Blog</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了相关趣闻，例如德国用啤酒垫记录啤酒消费的传统，这在法律上被视为文件。还有人指出，菜单随时间变化不大，但早期常见“煮”类菜肴。

**标签**: `#data-visualization`, `#digital-humanities`, `#history`, `#culture`

---

<a id="item-4"></a>
## [用 Claude Code 分析 MRI：一次个人实验](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

一位用户利用 Anthropic 的 AI 编码工具 Claude Code，对其肩部 MRI 扫描结果进行二次分析，并将过程与结果公开发布。 此事凸显了 AI 与医疗领域日益密切的交集——通用 AI 工具正被用于关键医疗任务，引发了关于信任、可靠性以及专业领域验证必要性的紧迫讨论。 Claude Code 主要设计为编码助手，可读取代码库并执行命令，并非用于医学影像分析。该用户的分析基于有限的二维切片而非完整的三维 MRI 数据集，放射科医生指出这是局限性。

hackernews · engmarketer · 6月28日 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude Code 是 Anthropic 开发的 AI 编码代理，帮助开发者构建功能、修复漏洞并在文件和工具间自动化任务。它并未针对医学影像解读进行训练或验证。通用 AI 模型在医疗中的应用充满争议，因其存在误诊风险且缺乏监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 讨论中的放射科医生指出，由于训练数据不足以及三维扫描的复杂性，AI 模型在医学影像上通常表现不佳。一位放射科医生分享了自己曾被误诊的经历，强调了其中的高风险。总体观点谨慎，许多人同意 AI 可作为补充工具，但不应单独信赖。

**标签**: `#AI`, `#healthcare`, `#MRI`, `#Claude Code`, `#trust`

---

<a id="item-5"></a>
## [布朗大学教授谴责大规模 AI 作弊](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 8.0/10

布朗大学一名教授报告称学生在考试中大规模使用 AI，引发了关于学术诚信的校内辩论，并促使有人呼吁采用手写考试和对抗性课程设计。 这一事件凸显了生成式 AI 对传统评估方式的深远挑战，可能迫使全球大学重新设计考试，并重新思考分数对雇主的信号价值。 该教授的研究背景是博弈论，一些评论者指出，使用 LLM 对学生来说是博弈论上的最优选择。提出的解决方案包括现场手写考试、一对一面试，以及尽量减少 AI 使用益处的对抗性课程设计。

hackernews · geox · 6月28日 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48708991)

**背景**: 像 ChatGPT 这样的生成式 AI 工具可以快速生成看似合理的答案，使得传统的带回家考试容易受到隐蔽作弊的影响。对抗性课程设计是一种新兴的教育框架，通过安排课程和评估（例如监考考试和口头检查）来降低 AI 辅助的效果。这种方法将考试诚信重新定义为教师与 AI 辅助学生之间持续的军备竞赛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/10.1145/3769694.3771130">Adversarial Thinking as a Professional Disposition for Computing Education</a></li>
<li><a href="https://www.learntechlib.org/p/2129054/">Adversarial Instructional Design: An AI-Resilient Assessment Framework ...</a></li>

</ul>
</details>

**社区讨论**: 评论显示了分歧：一些人主张回归手写、现场考试以及法学院使用的安全考试环境，而另一些人则质疑分数本身的价值，认为教授不应为公司做免费筛选。一个值得注意的观点是，教授自身的博弈论专业知识表明，学生理性地选择使用 AI，部分责任应归咎于评估设计本身。

**标签**: `#AI`, `#education`, `#academic integrity`, `#cheating`, `#assessment`

---

<a id="item-6"></a>
## [《儿童在线安全法案》要求强制年龄验证](https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online) ⭐️ 8.0/10

美国两党提出的《儿童在线安全法案》(KIDS Act)要求网站和在线服务在允许用户访问前验证其年龄。该立法旨在保护未成年人，但引发了严重的隐私和言论自由担忧。 如果该法案通过，将要求众多平台进行年龄验证，可能重塑互联网访问方式，影响数十亿用户。批评者认为这可能削弱匿名性、抑制言论自由，并导致危害隐私的数据收集行为。 法案全文可在 Congress.gov 上查看（H.R. 7757）。发起人包括共和党议员 Brett Guthrie 和民主党议员 Frank Pallone。电子前哨基金会（EFF）反对该法案，认为其违反第一修正案且现有年龄验证技术效果不佳。

hackernews · bilsbie · 6月28日 11:56 · [社区讨论](https://news.ycombinator.com/item?id=48706560)

**背景**: 年龄验证是指在线确认用户年龄的方法，例如扫描身份证、检查信用卡或自拍分析。但这些方法通常损害隐私或容易被绕过。隐私倡导者警告说，强制性年龄验证可能创建用户信息的中央数据库，增加安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Age_verification">Age verification - Wikipedia</a></li>
<li><a href="https://www.newamerica.org/insights/exploring-privacy-preserving-age-verification/">Exploring Privacy-Preserving Age Verification: A Close Look at Zero ...</a></li>
<li><a href="https://www.cs.columbia.edu/~smb/papers/age-verify.pdf">PDF Privacy-Preserving Age Verification—and Its Limitations</a></li>

</ul>
</details>

**社区讨论**: 评论中表达了怀疑：有人质疑社交媒体对心理健康影响的研究，有人怀疑有特殊利益集团在游说。还有人担心强制年龄验证与早前保护个人信息的建议相矛盾。不过，也有评论者支持任何保护在线身份的措施。

**标签**: `#privacy`, `#age verification`, `#legislation`, `#internet regulation`, `#EFF`

---

<a id="item-7"></a>
## [Jon Udell：主张用'agent in the loop'取代'human in the loop'](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell 主张将'human in the loop'重新定义为'agent in the loop'，认为人类应保持控制权，而 AI 代理在软件开发中提供协助。 这一转变强调人类的主导地位而非机器的权威，反驳了 AI 削弱人类角色的说法。它可能影响开发者对与 AI 代理协作的理解，促进透明度和可审查性。 Udell 警告不要出现不可审查的代理生成的拉取请求（PR），主张代理辅助流程应保持人类监督。该概念与现有框架（如 HULA——人在回路的 LLM 代理框架）一致，但扭转了叙事方向。

rss · Simon Willison · 6月28日 21:57

**背景**: 'human in the loop' 一词通常描述需要人类验证的 AI 决策系统，暗含人类在主循环之外。Udell 的替代说法'agent in the loop'将人类置于中心操作者地位，邀请代理作为协作伙伴而非替代者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2411.12924">[2411.12924] Human-In-the-Loop Software Development Agents</a></li>
<li><a href="https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html">Humans and Agents in Software Engineering Loops</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#human-agent collaboration`, `#Jon Udell`

---

<a id="item-8"></a>
## [谷歌因算力不足限制 Meta 使用 Gemini](https://www.ft.com/content/c5d52f72-71ef-40bc-bad3-61afdba8b378) ⭐️ 8.0/10

谷歌自 2026 年 3 月起限制 Meta 对其 Gemini AI 模型的使用，理由是算力不足，无法满足 Meta 购买的容量，导致 Meta 内部 AI 项目延迟，并促使 Meta 加速自研模型。 这揭示了影响大型科技公司的现实 AI 算力瓶颈，凸显 AI 基础设施的供需失衡，迫使 Meta 减少对第三方模型的依赖，可能重塑 AI 生态的竞争格局。 该限制截至 2026 年 4 月仍然有效，Meta 已通过鼓励员工更高效使用 AI tokens，并优先采用 2026 年 4 月发布的 Muse Spark 模型作为回应——这是 Meta 超级智能实验室的首个模型。

telegram · zaihuapd · 6月28日 07:38

**背景**: Gemini 是 Google DeepMind 开发的多模态大语言模型系列，于 2023 年 12 月发布，通过云 API 使用。AI tokens 是模型处理的文本单位，按使用量计量和计费，类似于数据套餐。Meta 此前依赖 Gemini 进行部分 AI 工作负载，现正自建数据中心和模型以减少依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>
<li><a href="https://www.pivotpointsecurity.com/ai-tokens-how-they-impact-usage-costs/">AI Tokens and How They Impact Usage Costs—Explained</a></li>
<li><a href="https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/">Meta debuts the Muse Spark model in a 'ground-up... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#AI`, `#compute capacity`, `#Google`, `#Meta`, `#Gemini`

---

<a id="item-9"></a>
## [LibrePods：开源解放 AirPods 功能](https://github.com/librepods-org/librepods) ⭐️ 7.0/10

LibrePods 是一个开源项目，通过逆向工程苹果的专有协议，将 AirPods 的耳部检测、噪声控制模式和电池状态等功能带到 Android、Linux 等非苹果设备上。 它打破了苹果对 AirPods 的生态系统锁定，让用户能够在任何平台上使用高端耳塞。这可能会迫使苹果开放其协议，否则可能失去看重跨平台兼容性的用户。 该项目实现了 AirPods 与苹果设备之间的专有数据交换协议，支持自适应通透模式、头部手势和对话感知等功能。代码托管在 GitHub 上，通过配套应用使用。

hackernews · rbanffy · 6月28日 18:48 · [社区讨论](https://news.ycombinator.com/item?id=48710232)

**背景**: AirPods 是蓝牙耳塞，在非苹果设备上可作为标准耳机使用，但自动耳部检测和噪声控制等高级功能被锁定在苹果生态系统中。LibrePods 逆向工程了私有通信协议来解锁这些功能。苹果历来保护其生态系统，未来的更新可能会试图阻止此类努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/librepods-org/librepods">GitHub - librepods -org/ librepods : AirPods liberated from...</a></li>
<li><a href="https://www.theverge.com/news/824953/librepods-apple-airpods-wireless-headphones-android-linux">AirPods ’ best features come to Android and Linux with... | The Verge</a></li>
<li><a href="https://github.com/kavishdevar/librepods">kavishdevar/librepods: AirPods liberated from Apple 's ecosystem.</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍赞赏这一技术成就，但对苹果可能通过更新进行封堵表示怀疑。一些用户指出，尽管这个破解令人印象深刻，但购买 AirPods 仍然支持苹果的封闭生态。还有人希望类似地解放其他苹果功能，如 AirDrop。

**标签**: `#reverse-engineering`, `#airpods`, `#bluetooth`, `#open-source`

---

<a id="item-10"></a>
## [Codex 中排除敏感文件的问题仍未解决](https://github.com/openai/codex/issues/2847) ⭐️ 7.0/10

GitHub 上的一个问题（codex/issues/2847）仍然开放，讨论如何防止 OpenAI Codex 访问敏感文件。社区提出了如文件权限和沙箱等解决方案，但官方尚未实现该功能。 该问题突显了 AI 编程助手的一个关键安全担忧：意外泄露 API 密钥或凭据等敏感数据。如果没有适当的保护措施，用户在使用 Codex 等工具时可能面临暴露机密的风险，从而削弱对 AI 辅助开发的信任。 该问题建议实施敏感文件的黑名单，但评论者认为，LLM 的不确定性使得这种执行不可靠。技术细节包括目前的工作方案是通过更改文件权限（如 chmod）或在未挂载敏感文件的容器中运行 Codex。

hackernews · pikseladam · 6月28日 12:27 · [社区讨论](https://news.ycombinator.com/item?id=48706714)

**背景**: OpenAI Codex 是一个可以自动化软件工程任务的 AI 编程代理。然而，如果敏感文件对该进程可读，它可能会无意中访问并上传这些文件。沙箱是一种安全技术，用于隔离运行中的程序以防止未授权访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sandbox_(computer_security)">Sandbox (computer security) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：一些人认为如果用户正确沙箱环境（例如通过 chmod 或容器），该功能是不必要的；而另一些人坚持采用选择加入的方法，让代理只访问明确允许的文件。一位 NVIDIA 工程师分享了他们的开源工具'rumpelpod'，用于远程安全开发容器。

**标签**: `#AI safety`, `#Codex`, `#security`, `#coding assistants`, `#sandboxing`

---

<a id="item-11"></a>
## [浏览器 Ctrl+S 快捷键阻塞波兰语变音符号输入](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/) ⭐️ 7.0/10

Ares Luna 在 2015 年的一篇文章揭示，浏览器键盘快捷键（如 Ctrl+S）会无意中阻止波兰用户输入某些变音符号（如'ś'），因为浏览器在字符插入前就捕获了按键组合。 这突显了非英语用户长期存在的可用性问题：浏览器键盘事件处理优先考虑快捷键而非本地输入，影响数百万波兰语使用者及其他类似的语言群体。 问题发生的原因是浏览器在 keydown 事件到达网页之前就拦截了 Ctrl+S（及其他快捷键），从而阻止字符组合；文章还指出，波兰字母'ł'在 Unicode 规范化下表现不同，分解后保持不变。

hackernews · colinprince · 6月28日 12:44 · [社区讨论](https://news.ycombinator.com/item?id=48706814)

**背景**: 波兰语使用拉丁字母及九个变音符号（ą, ć, ę, ł, ń, ó, ś, ź, ż）来表示额外发音。这些字符通过 AltGr 或 Compose 等修饰键输入，产生的按键组合可能被浏览器误认为快捷键。浏览器键盘事件（keydown、keyup）在字符输入前触发，开发者常依赖 event.key 或 event.code，但系统级快捷键可以抢先拦截。文章的文化分析将这一问题与波兰的西方倾向以及波兰字母 S 在民族认同中的历史角色联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent">KeyboardEvent - Web APIs - MDN Web Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polish_alphabet">Polish alphabet - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key">KeyboardEvent: key property - Web APIs | MDN</a></li>

</ul>
</details>

**社区讨论**: 评论者指出其他应用程序也有类似冲突，例如新的 Copilot 365 拦截“Ć”。一条技术评论指出浏览器缺乏检查按键组合的简单 API，且文章展示的代码修复仅适用于 Windows。另一位贡献者提到，在 Unicode 规范化形式 C（规范分解）下，9 个波兰字母中有 8 个会分解，但'ł'保持不变，这导致 SQLite 的 unicode61 分词器出现问题。

**标签**: `#Polish`, `#keyboard shortcuts`, `#browser bugs`, `#Unicode`, `#web development`

---

<a id="item-12"></a>
## [可编辑权重的交互式最小化 Transformer](https://www.reddit.com/r/MachineLearning/comments/1uhw7fu/i_shrank_a_transformer_until_every_number_fitted/) ⭐️ 7.0/10

一个交互式网页可视化了一个最小化的 Transformer，其权重可编辑，用户能够实时探索从嵌入到概率的前向传播过程。 该工具使 Transformer 的内部机制对学习者变得直观，弥合了高级 API 与底层矩阵运算之间的鸿沟，且无需任何配置。 该 Transformer 使用 6 个词的词汇表、3 维嵌入、单注意力头、单块和因果掩码。所有权重和词向量均可编辑，预测结果实时更新。

reddit · r/MachineLearning · /u/DanielMoGo · 6月28日 12:35

**背景**: Transformer 是一种使用自注意力机制处理序列的神经网络架构，其中 Query（Q）、Key（K）和 Value（V）矩阵计算注意力分数。因果掩码防止令牌关注未来位置，确保自回归预测。该交互式演示以最小规模可视化了这些概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)">Attention (machine learning) - Wikipedia</a></li>
<li><a href="https://discuss.huggingface.co/t/difference-between-attention-mask-and-causal-mask/104922">Difference Between Attention Mask and Causal Mask - ...</a></li>

</ul>
</details>

**标签**: `#transformer`, `#LLM`, `#education`, `#visualization`, `#interactive`

---
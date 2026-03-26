# Part 1: 传统量化基础（Days 1-15）

> **学习目标**：建立量化投资的理论认知框架，理解为什么因子能够解释和预测收益。

---

## Day 1-3: 有效市场假说与行为金融学

### Day 1: 有效市场假说的三个层次

#### 什么是有效市场假说（EMH）

Eugene Fama在1970年提出的有效市场假说（Efficient Market Hypothesis）是量化投资的理论基石。它的核心观点是：**资产价格已经反映了所有可获得的信息**。

#### 市场有效性三层次

```mermaid
graph TB
    subgraph EMH["有效市场假说 EMH"]
        A["强式有效<br/>Strong-Form"] --> B["半强式有效<br/>Semi-Strong"]
        B --> C["弱式有效<br/>Weak-Form"]
    end

    A --- A1["包含内幕信息"]
    A --- A2["无法获得超额收益"]

    B --- B1["包含公开信息"]
    B --- B2["基本面分析无效"]

    C --- C1["包含历史价格"]
    C --- C2["技术分析无效"]

    style A fill:#ffebee,stroke:#c62828
    style B fill:#fff3e0,stroke:#ef6c00
    style C fill:#e8f5e9,stroke:#2e7d32
```

**信息集包含关系**：

```
强式有效信息集 ⊃ 半强式有效信息集 ⊃ 弱式有效信息集
├─ 内幕信息
├─ 公开信息（财报、宏观数据、新闻）
├─ 历史价格和成交量
└─ 其他私有信息
```

| 层次 | 信息范围 | 无效策略 | 实证证据 |
|------|----------|----------|----------|
| **弱式** | 历史价格 | 技术分析 | 短期动量、长期反转 |
| **半强式** | 公开信息 | 基本面分析 | PEAD、价值/动量因子 |
| **强式** | 所有信息 | 任何策略 | 内幕交易可获利 |

#### 价格对新信息的反应模式

```mermaid
xychart-beta
    title "价格对新信息的反应模式"
    x-axis ["T-3", "T-2", "T-1", "T(事件日)", "T+1", "T+2", "T+3"]
    y-axis "累计超额收益(%)" -5 --> 10

    line "有效市场( instantly )" [0, 0, 0, 0, 5, 5, 5]
    line "过度反应( reversal )" [0, 0, 0, 0, 7, 5, 3]
    line "反应不足( momentum )" [0, 0, 0, 0, 2, 3.5, 5]
    line "延迟反应( slow info )" [0, 0, 0, 0, 2, 4, 5]
```

**解读**：
- **有效市场**：价格立即调整到新信息水平
- **反应不足**：信息逐步反映，产生动量效应
- **过度反应**：价格超调后反转
- **延迟反应**：信息扩散缓慢

---

### Day 2: 市场异象与因子投资的起源

#### 什么是市场异象（Anomalies）

市场异象是指**与市场有效性假说不一致的、系统性的收益模式**。它们是因子投资的起点。

#### 经典市场异象对比

```mermaid
quadrantChart
    title 市场异象：收益 vs 风险
    x-axis 低风险 --> 高风险
    y-axis 低收益 --> 高收益
    quadrant-1 高收益+高风险: 值得研究
    quadrant-2 高收益+低风险: 理想因子
    quadrant-3 低收益+低风险: 债券型
    quadrant-4 低收益+高风险: 价值陷阱

    "价值因子": [0.6, 0.55]
    "动量因子": [0.8, 0.75]
    "质量因子": [0.3, 0.5]
    "低波动因子": [0.2, 0.45]
    "规模因子": [0.7, 0.4]
    "市场指数": [0.5, 0.5]
```

#### 异象的生命周期

```mermaid
graph LR
    A["学术发现"] --> B["策略验证"]
    B --> C["市场认知"]
    C --> D["资金涌入"]
    D --> E["套利压缩"]
    E --> F["异象衰减"]
    F --> G["新异象出现"]
    G --> A

    style A fill:#e1f5ff
    style D fill:#fff3e0
    style E fill:#ffebee
    style G fill:#e8f5e9
```

**各阶段特征**：

| 阶段 | 时间 | 特征 | 策略 |
|------|------|------|------|
| 发现期 | 0-2年 | 超额收益高，容量有限 | 积极建仓 |
| 成长期 | 2-5年 | 收益稳定，资金进入 | 适度配置 |
| 成熟期 | 5-10年 | 收益压缩，竞争激烈 | 降低权重 |
| 衰退期 | 10年+ | 几乎失效，或仅熊市有效 | 择机使用 |

---

### Day 3: 行为金融学——理解市场非理性的钥匙

#### 核心认知偏差图谱

```mermaid
mindmap
  root((行为偏差))
    过度自信
      频繁交易
      分散化不足
      择时错误
    处置效应
      过早卖出盈利股
      过久持有亏损股
      导致动量延续
    锚定效应
      买入成本锚定
      历史价格锚定
      调整不足
    损失厌恶
      风险厌恶不对称
      偏好彩票型股票
      低波动异象
    羊群效应
      追涨杀跌
      泡沫与崩溃
      反转信号
    代表性偏差
      过度外推趋势
      忽视基础概率
      成长/价值偏差
```

#### 有限套利机制

```mermaid
graph TB
    subgraph "套利限制因素"
        A["基本面风险"] --> A1["价值陷阱"]
        A --> A2["黑天鹅事件"]

        B["噪音交易者风险"] --> B1["价格更偏离"]
        B --> B2["被迫平仓"]

        C["实施成本"] --> C1["交易成本"]
        C --> C2["做空限制"]

        D["委托代理问题"] --> D1["短期考核"]
        D --> D2["赎回压力"]
    end

    style A fill:#ffebee
    style B fill:#fff3e0
    style C fill:#e8f5e9
    style D fill:#e1f5ff
```

---

## Day 4-6: 风险与收益的关系

### Day 5: CAPM模型与Beta

#### CAPM模型结构

```mermaid
graph LR
    subgraph "CAPM 资本资产定价模型"
        A["无风险利率<br/>R_f"] --> E["预期收益<br/>E[R_i]"]
        B["市场风险溢价<br/>E[R_m] - R_f"] --> M["×"]
        C["Beta系数<br/>β_i"] --> M
        M --> E
    end

    style A fill:#e8f5e9
    style B fill:#fff3e0
    style C fill:#e1f5ff
    style E fill:#f3e5f5
    style M fill:#ffebee
```

**公式**：`E[R_i] = R_f + β_i × (E[R_m] - R_f)`

#### Beta值的含义

```mermaid
xychart-beta
    title "不同Beta值股票的收益特征"
    x-axis ["市场-20%", "市场-10%", "市场0%", "市场+10%", "市场+20%"]
    y-axis "股票收益(%)" -30 --> 40

    line "β=0 (无风险)" [2, 2, 2, 2, 2]
    line "β=0.5 (防御)" [-8, -3, 2, 7, 12]
    line "β=1.0 (市场)" [-20, -10, 0, 10, 20]
    line "β=1.5 (激进)" [-28, -13, 2, 17, 32]
    line "β=2.0 (高杠杆)" [-38, -18, 2, 22, 42]
```

**Beta解释**：
- **β < 0.5**：防御型，波动小于市场
- **β = 1.0**：与市场同波动
- **β > 1.5**：进攻型，波动大于市场
- **β < 0**：与市场反向（极少见）

---

## Day 7-10: 套利定价理论（APT）

### APT多因子结构

```mermaid
graph TB
    subgraph "APT 套利定价模型"
        R["资产收益 R_i"] --> Sum["+"]

        R_f["无风险利率<br/>R_f"] --> Sum

        F1["因子1收益<br/>F_1"] --> B1["× β_i1"]
        F2["因子2收益<br/>F_2"] --> B2["× β_i2"]
        F3["因子3收益<br/>F_3"] --> B3["× β_i3"]

        B1 --> Sum
        B2 --> Sum
        B3 --> Sum

        Sum --> E["预期收益<br/>E[R_i]"]
        Sum --> Residual["+ 残差 ε_i"]
    end

    style R_f fill:#e8f5e9
    style F1 fill:#e1f5ff
    style F2 fill:#fff3e0
    style F3 fill:#f3e5f5
    style E fill:#ffebee
```

**对比**：

| 维度 | CAPM | APT |
|------|------|-----|
| 因子数量 | 1个（市场） | 多个（宏观/统计） |
| 理论基础 | 均值-方差优化 | 无套利条件 |
| 市场组合 | 必需 | 不需要 |
| 因子选择 | 固定 | 灵活 |

---

## Day 11-15: Fama-French框架

### Fama-French三因子模型

```mermaid
graph LR
    subgraph "FF3 三因子模型"
        R["股票超额收益<br/>R_i - R_f"] --> Sum["+"]

        MKT["市场因子<br/>RM-RF"] --> B1["× β"]
        SMB["规模因子<br/>Small - Big"] --> B2["× s"]
        HML["价值因子<br/>High - Low"] --> B3["× h"]

        B1 --> Sum
        B2 --> Sum
        B3 --> Sum

        Sum --> Alpha["+ Alpha α_i"]
    end

    style MKT fill:#e8f5e9
    style SMB fill:#e1f5ff
    style HML fill:#fff3e0
    style Alpha fill:#ffebee
```

### 五因子模型扩展

```mermaid
graph TB
    subgraph "FF5 五因子模型"
        direction LR

        F1["市场因子<br/>MKT"]
        F2["规模因子<br/>SMB"]
        F3["价值因子<br/>HML"]
        F4["盈利因子<br/>RMW<br/>(Robust - Weak)"]
        F5["投资因子<br/>CMA<br/>(Conservative - Aggressive)"]

        F1 --- FF["多因子定价"]
        F2 --- FF
        F3 --- FF
        F4 --- FF
        F5 --- FF

        FF --> R["股票预期收益"]
    end

    style F1 fill:#e8f5e9
    style F2 fill:#e1f5ff
    style F3 fill:#fff3e0
    style F4 fill:#f3e5f5
    style F5 fill:#fce4ec
```

### 因子收益历史表现（1990-2020）

```mermaid
xychart-beta
    title "Fama-French因子年化收益"
    x-axis ["MKT-RF", "SMB", "HML", "RMW", "CMA", "MOM"]
    y-axis "年化收益(%)" -2 --> 8
    bar [6.5, 2.2, 3.4, 3.2, 2.8, 6.8]

    line "零线" [0, 0, 0, 0, 0, 0]
```

---

## Part 1 知识图谱

```mermaid
mindmap
  root((Part 1<br/>理论基础))
    有效市场假说
      弱式有效
      半强式有效
      强式有效
      Grossman-Stiglitz悖论
    行为金融学
      认知偏差
      有限套利
      市场异象
    资产定价模型
      CAPM
        Beta系数
        SML线
      APT
        多因子结构
        无套利
    Fama-French
      三因子模型
      五因子模型
      因子构建方法
      实证检验
```

---

## Part 1 总结

通过这15天的学习，你应该建立了以下认知框架：

### 核心理论

1. **市场不是完全有效的**，存在可预测的因子收益
2. **收益来自承担风险和发现错误定价**
3. **多因子模型比单因子模型更能解释收益差异**
4. **因子收益可能是风险补偿，也可能是行为偏差的结果**

### 关键概念回顾

| 概念 | 核心要点 | 公式/关键值 |
|------|----------|-------------|
| **EMH** | 三层次：弱/半强/强 | 信息集逐步扩大 |
| **CAPM** | 单因子定价 | E[R] = R_f + β(R_m - R_f) |
| **APT** | 多因子无套利 | E[R] = R_f + Σβ_j × RP_j |
| **FF3** | 市场+规模+价值 | SMB, HML构建 |
| **FF5** | 加入盈利+投资 | RMW, CMA |

准备好进入Part 2，深入探索经典因子了吗？

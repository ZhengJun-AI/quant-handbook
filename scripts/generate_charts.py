#!/usr/bin/env python3
"""
量化因子手册图表生成脚本
生成高质量的图表供手册使用

使用方法:
    python generate_charts.py

依赖:
    pip install matplotlib numpy pandas seaborn
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import os

# 设置中文字体 - 使用系统可用字体
plt.rcParams['font.family'] = ['Hiragino Sans GB', 'Heiti TC', 'Songti SC', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 设置样式
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8-darkgrid')

# 创建输出目录
OUTPUT_DIR = "../images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_factor_cumulative_returns():
    """生成因子累积收益曲线图"""
    print("生成: 因子累积收益曲线...")

    # 模拟数据 (1990-2020)
    years = np.arange(1990, 2021)
    n_years = len(years)

    # 生成累积收益数据 (从1开始)
    np.random.seed(42)
    market = np.cumprod(1 + np.random.normal(0.08, 0.16, n_years))
    value = np.cumprod(1 + np.random.normal(0.034, 0.12, n_years))
    momentum = np.cumprod(1 + np.random.normal(0.065, 0.18, n_years))
    quality = np.cumprod(1 + np.random.normal(0.032, 0.08, n_years))
    low_vol = np.cumprod(1 + np.random.normal(0.028, 0.11, n_years))
    size = np.cumprod(1 + np.random.normal(0.022, 0.10, n_years))

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(years, market, label='Market Index', linewidth=2.5, color='gray', alpha=0.7)
    ax.plot(years, value, label='Value Factor (HML)', linewidth=2.5, color='#2E7D32')
    ax.plot(years, momentum, label='Momentum Factor (MOM)', linewidth=2.5, color='#C62828')
    ax.plot(years, quality, label='Quality Factor (RMW)', linewidth=2.5, color='#1565C0')
    ax.plot(years, low_vol, label='Low Volatility (BAB)', linewidth=2.5, color='#F57C00')
    ax.plot(years, size, label='Size Factor (SMB)', linewidth=2.5, color='#6A1B9A')

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Cumulative Return (Multiple)', fontsize=12)
    ax.set_title('Classic Factor Cumulative Returns Comparison (1990-2020)', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/factor_cumulative_returns.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {OUTPUT_DIR}/factor_cumulative_returns.png")


def generate_factor_correlation_heatmap():
    """生成因子相关性热力图"""
    print("生成: 因子相关性热力图...")

    # 因子名称
    factors = ['Value\nHML', 'Size\nSMB', 'Momentum\nMOM', 'Quality\nRMW', 'Low Vol\nBAB']

    # 相关性矩阵
    corr_matrix = np.array([
        [1.00, 0.20, -0.30, 0.10, 0.30],
        [0.20, 1.00, 0.10, -0.10, -0.30],
        [-0.30, 0.10, 1.00, 0.20, -0.40],
        [0.10, -0.10, 0.20, 1.00, 0.30],
        [0.30, -0.30, -0.40, 0.30, 1.00]
    ])

    fig, ax = plt.subplots(figsize=(8, 7))

    # 使用seaborn绘制热力图
    sns.heatmap(corr_matrix,
                annot=True,
                fmt='.2f',
                cmap='RdYlBu_r',
                center=0,
                square=True,
                xticklabels=factors,
                yticklabels=factors,
                cbar_kws={'label': 'Correlation Coefficient'},
                ax=ax,
                vmin=-0.5, vmax=0.5)

    ax.set_title('Classic Factor Correlation Matrix', fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/factor_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {OUTPUT_DIR}/factor_correlation_heatmap.png")


def generate_risk_return_scatter():
    """生成风险收益散点图"""
    print("生成: 风险收益散点图...")

    # 因子数据 (年化收益, 波动率)
    factors = {
        'Value Factor': (3.4, 12.0, '#2E7D32'),
        'Size Factor': (2.2, 10.0, '#6A1B9A'),
        'Momentum Factor': (6.5, 18.0, '#C62828'),
        'Quality Factor': (3.2, 8.0, '#1565C0'),
        'Low Vol Factor': (2.8, 11.0, '#F57C00'),
        'Market Index': (6.0, 16.0, 'gray')
    }

    fig, ax = plt.subplots(figsize=(10, 8))

    for name, (ret, vol, color) in factors.items():
        ax.scatter(vol, ret, s=400, c=color, alpha=0.7, edgecolors='black', linewidth=2)
        ax.annotate(name, (vol, ret), xytext=(5, 5), textcoords='offset points',
                   fontsize=11, fontweight='bold')

    # 添加有效前沿线 (示意)
    x = np.linspace(8, 20, 100)
    y = 0.5 * x - 2  # 简化的线性关系
    ax.plot(x, y, 'k--', alpha=0.5, label='Theoretical Efficient Frontier')

    ax.set_xlabel('Annualized Volatility (%)', fontsize=12)
    ax.set_ylabel('Annualized Excess Return (%)', fontsize=12)
    ax.set_title('Factor Risk-Return Profile (1990-2020)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/risk_return_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {OUTPUT_DIR}/risk_return_scatter.png")


def generate_monthly_returns_distribution():
    """生成月度收益分布图"""
    print("生成: 月度收益分布图...")

    np.random.seed(42)

    # 生成月度收益数据
    n_months = 360  # 30年
    momentum_returns = np.random.normal(0.0054, 0.052, n_months)
    value_returns = np.random.normal(0.0028, 0.035, n_months)
    market_returns = np.random.normal(0.005, 0.046, n_months)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 动量因子
    axes[0, 0].hist(momentum_returns, bins=50, color='#C62828', alpha=0.7, edgecolor='black')
    axes[0, 0].axvline(0, color='black', linestyle='--', linewidth=2)
    axes[0, 0].axvline(np.mean(momentum_returns), color='red', linestyle='-', linewidth=2, label='Mean')
    axes[0, 0].set_title('Momentum Factor Monthly Return Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Monthly Return')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 价值因子
    axes[0, 1].hist(value_returns, bins=50, color='#2E7D32', alpha=0.7, edgecolor='black')
    axes[0, 1].axvline(0, color='black', linestyle='--', linewidth=2)
    axes[0, 1].axvline(np.mean(value_returns), color='green', linestyle='-', linewidth=2, label='Mean')
    axes[0, 1].set_title('Value Factor Monthly Return Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Monthly Return')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # 市场指数
    axes[1, 0].hist(market_returns, bins=50, color='gray', alpha=0.7, edgecolor='black')
    axes[1, 0].axvline(0, color='black', linestyle='--', linewidth=2)
    axes[1, 0].axvline(np.mean(market_returns), color='blue', linestyle='-', linewidth=2, label='Mean')
    axes[1, 0].set_title('Market Index Monthly Return Distribution', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Monthly Return')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # 箱线图对比
    data_to_plot = [momentum_returns, value_returns, market_returns]
    labels = ['Momentum', 'Value', 'Market']
    bp = axes[1, 1].boxplot(data_to_plot, labels=labels, patch_artist=True)
    colors = ['#C62828', '#2E7D32', 'gray']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    axes[1, 1].axhline(0, color='black', linestyle='--', linewidth=1)
    axes[1, 1].set_title('Factor Return Box Plot Comparison', fontsize=12, fontweight='bold')
    axes[1, 1].set_ylabel('Monthly Return')
    axes[1, 1].grid(True, alpha=0.3)

    plt.suptitle('Factor Monthly Return Distribution Characteristics', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/monthly_returns_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {OUTPUT_DIR}/monthly_returns_distribution.png")


def generate_drawdown_chart():
    """生成回撤分析图"""
    print("生成: 回撤分析图...")

    np.random.seed(42)

    # 生成价格序列
    n_days = 252 * 20  # 20年
    dates = pd.date_range('2000-01-01', periods=n_days, freq='D')

    # 模拟不同因子的价格序列
    market = 100 * np.cumprod(1 + np.random.normal(0.0003, 0.01, n_days))
    momentum = 100 * np.cumprod(1 + np.random.normal(0.0005, 0.012, n_days))
    value = 100 * np.cumprod(1 + np.random.normal(0.0002, 0.008, n_days))

    # 计算回撤
    def calculate_drawdown(price_series):
        peak = np.maximum.accumulate(price_series)
        drawdown = (price_series - peak) / peak * 100
        return drawdown

    dd_market = calculate_drawdown(market)
    dd_momentum = calculate_drawdown(momentum)
    dd_value = calculate_drawdown(value)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [2, 1]})

    # 净值曲线
    ax1.plot(dates, market, label='Market Index', linewidth=1.5, color='gray', alpha=0.7)
    ax1.plot(dates, momentum, label='Momentum Factor', linewidth=1.5, color='#C62828')
    ax1.plot(dates, value, label='Value Factor', linewidth=1.5, color='#2E7D32')
    ax1.set_ylabel('Net Value', fontsize=12)
    ax1.set_title('Factor Net Value & Drawdown Analysis (2000-2020)', fontsize=14, fontweight='bold')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')

    # 回撤曲线
    ax2.fill_between(dates, dd_market, 0, alpha=0.3, color='gray', label='Market DD')
    ax2.fill_between(dates, dd_momentum, 0, alpha=0.5, color='#C62828', label='Momentum DD')
    ax2.fill_between(dates, dd_value, 0, alpha=0.5, color='#2E7D32', label='Value DD')
    ax2.set_ylabel('Drawdown (%)', fontsize=12)
    ax2.set_xlabel('Year', fontsize=12)
    ax2.legend(loc='lower left')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/drawdown_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {OUTPUT_DIR}/drawdown_analysis.png")


def generate_factor_timing_illustration():
    """生成因子择时示意图"""
    print("生成: 因子择时示意图...")

    # 模拟市场环境
    months = np.arange(1, 25)

    # 模拟不同市场环境下的因子表现
    value_performance = [2, 1, -1, -2, -1, 1, 3, 4, 3, 1, -1, -2,
                        -1, 1, 2, 3, 2, 0, -2, -3, -2, 0, 2, 3]
    momentum_performance = [3, 4, 3, 1, -2, -3, -2, 0, 2, 4, 5, 4,
                           2, 0, -2, -3, -1, 2, 4, 5, 3, 1, -1, -2]

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.plot(months, value_performance, label='Value Factor', linewidth=2.5, color='#2E7D32', marker='o', markersize=6)
    ax.plot(months, momentum_performance, label='Momentum Factor', linewidth=2.5, color='#C62828', marker='s', markersize=6)
    ax.axhline(0, color='black', linestyle='--', linewidth=1)

    # 添加市场环境标注
    ax.axvspan(1, 6, alpha=0.1, color='red', label='Bear Market')
    ax.axvspan(7, 14, alpha=0.1, color='green')
    ax.axvspan(15, 20, alpha=0.1, color='red')
    ax.axvspan(21, 24, alpha=0.1, color='green')

    # 添加文本标注
    ax.text(3.5, 5.5, 'Bear\n→ Value Wins', fontsize=10, ha='center', color='#2E7D32', fontweight='bold')
    ax.text(10.5, 5.5, 'Bull\n→ Momentum Wins', fontsize=10, ha='center', color='#C62828', fontweight='bold')
    ax.text(17.5, 5.5, 'Choppy\n→ Value Wins', fontsize=10, ha='center', color='#2E7D32', fontweight='bold')

    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Relative Return', fontsize=12)
    ax.set_title('Factor Timing Illustration: Factor Rotation in Different Market Conditions', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xticks(months)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/factor_timing_illustration.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {OUTPUT_DIR}/factor_timing_illustration.png")


def main():
    """主函数：生成所有图表"""
    print("="*60)
    print("Quantitative Factor Handbook Chart Generator")
    print("="*60)
    print()

    try:
        generate_factor_cumulative_returns()
        generate_factor_correlation_heatmap()
        generate_risk_return_scatter()
        generate_monthly_returns_distribution()
        generate_drawdown_chart()
        generate_factor_timing_illustration()

        print()
        print("="*60)
        print("All charts generated successfully!")
        print(f"Output directory: {OUTPUT_DIR}/")
        print("="*60)

        # 列出生成的文件
        print("\nGenerated files:")
        for f in sorted(os.listdir(OUTPUT_DIR)):
            if f.endswith('.png'):
                print(f"  - {f}")

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

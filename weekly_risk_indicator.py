import pandas as pd

input_excel = "portfolio_nav.xlsx"  # 由数据库导出
input_daily_excel = "自营资金投资台账20220826.xlsx"  # 台账
output_excel = "weekly_risk_indicator.xlsx"  # 输出

# 通过顺序把台账和数据库对应
sheet_list = {"泰铼金泰2号": "泰铼开源尊享1号", "泰铼信泰3号A": "泰铼开源尊享2号",
              "橡木启明": "橡木", "致远22号": "致远", "时代复兴微观一号": "时代复兴", "致远CTA精选5号": "富善",
              "珺容翔宇CTA2号": "珺容", "白鹭鼓浪屿量化多策略一号": "白鹭", "安进四号": "安诚数盈",
              "思勰投资子张十号": "思勰", "时间序列量化对冲1号": "时间序列", "旭诺CTA三号": "旭诺",
              "衍合量化市场中性1号": "衍合", "无隅鲲鹏一号": "无隅", "图灵谷雨中性一号": "图灵",
              "殊馥馥源套利1号": "殊馥开源臻选", "聊塑投资期权1号": "聊塑投资套利7号"}
mark_list = [0.05, 0.1, 0.15, 0.20, 0.25]
res_indicator = {"滚动周收益": [], "historical_VaR": []}
# res_indicator = {"historical_VaR":[]}

# 读取数据库列名
df = pd.read_excel(input_excel)
stocks_names = df.columns.to_list()
stocks_names = stocks_names[1:]
for x in stocks_names:
    if x not in sheet_list:
        stocks_names.remove(x)
# print(stocks_names)

# 根据数据库列名进行对应处理
for i in range(len(stocks_names)):
    df_stock1 = df[stocks_names[i]]
    # 去除NaN
    df_stock1 = df_stock1.dropna()  # 去除数据库列中的空值

    # 获取去NaN后的起始和结束位置
    s_index = df_stock1.index[0]
    e_index = df_stock1.index[-1]

    # 获取去掉前面建仓部分的1后的起始位置
    for j in range(s_index, e_index + 1):
        if df_stock1[j] != float(1.0):
            s_index = j
            break

    # 补上部分没有前面1的基金情况
    df_stock1[s_index - 1] = 1

    # 计算收益率并升序排列：历史周收益
    historical_theta = []
    for k in range(s_index, e_index + 1):
        historical_theta.append(df_stock1[k] / df_stock1[k - 1] - 1)
    historical_theta.sort()

    # 获取滚动周收益率theta
    # 根据数据库列名读取对应台账表格
    df_daily = pd.read_excel(input_daily_excel, sheet_name=sheet_list[stocks_names[i]])
    size = df_daily["日涨跌幅"].size
    today_theta = 1
    for k in range(1, 6):
        today_theta = today_theta * (1 + df_daily["日涨跌幅"][size - k])
    today_theta -= 1
    res_indicator["滚动周收益"].append(today_theta)

    # 生成his_var_indicator
    his_var_indicator_assign = False

    for k in range(0, 5):
        index = round(mark_list[k] * len(historical_theta))
        if today_theta < historical_theta[index]:
            res_indicator["historical_VaR"].append(5 - k)
            his_var_indicator_assign = True
            break

    # 如果前面没有添加值说明没有触发预警，所以加0
    if not his_var_indicator_assign:
        res_indicator["historical_VaR"].append(0)

# 输出为excel表格
# index_list = stocks_names
# print(index_list)
# print(res_indicator["historical_VaR"])
df_indicator = pd.DataFrame(res_indicator, index=stocks_names)
df_indicator.to_excel(output_excel)

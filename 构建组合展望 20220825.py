{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pymssql'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-5b4a901daaf3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msqlalchemy\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mcreate_engine\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpymssql\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msqlite3\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pymssql'"
     ]
    }
   ],
   "source": [
    "from sqlalchemy import create_engine\n",
    "import pymssql\n",
    "import pandas as pd\n",
    "import sqlite3\n",
    "import pandas as pd\n",
    "import xlsxwriter\n",
    "from pandas import read_excel\n",
    "import time\n",
    "from dateutil.parser import parse\n",
    "from functools import reduce\n",
    "import datetime\n",
    "from datetime import datetime,date,timedelta\n",
    "import warnings\n",
    "import calendar\n",
    "c = calendar.Calendar(firstweekday=calendar.SUNDAY)\n",
    "warnings.filterwarnings('ignore')\n",
    "from WindPy import w\n",
    "if w.isconnected()!=1:\n",
    "    w.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_fund_nav=pd.read_csv('all_fund_nav.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_fund_nav['统计日期']=[datetime.strptime(i,'%Y-%m-%d').date() for i in all_fund_nav['统计日期']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df_outside=pd.read_excel(\"C:/Users/Yin Hui/Desktop/导入净值new.xlsx\", None)\n",
    "df_outside=df_outside['Sheet1']\n",
    "df_outside['统计日期']=[i.date() for i in df_outside['统计日期']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_fund_nav=all_fund_nav.append(df_outside)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_fund_nav.to_csv('all_fund_nav.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "组合成分= pd.read_excel(r\"C:\\Users\\Yin Hui\\Desktop\\自营组合展望.xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>组合投资</th>\n",
       "      <th>Unnamed: 1</th>\n",
       "      <th>参考产品</th>\n",
       "      <th>代码</th>\n",
       "      <th>规模</th>\n",
       "      <th>预期收益</th>\n",
       "      <th>预期收益(费后）</th>\n",
       "      <th>预期波动</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>泰铼开源尊享1号</td>\n",
       "      <td>泰铼</td>\n",
       "      <td>泰铼金泰2号</td>\n",
       "      <td>504562</td>\n",
       "      <td>30000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>泰铼开源尊享2号</td>\n",
       "      <td>泰铼</td>\n",
       "      <td>泰铼信泰3号A</td>\n",
       "      <td>439678</td>\n",
       "      <td>33000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>橡木启明</td>\n",
       "      <td>橡木</td>\n",
       "      <td>橡木启明</td>\n",
       "      <td>500667</td>\n",
       "      <td>1000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>致远22号</td>\n",
       "      <td>致诚卓远</td>\n",
       "      <td>致远22号</td>\n",
       "      <td>291379</td>\n",
       "      <td>5000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>时代复兴开源微观八号</td>\n",
       "      <td>时代复兴</td>\n",
       "      <td>时代复兴微观一号</td>\n",
       "      <td>316470</td>\n",
       "      <td>1000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>富善投资开源歆享1号</td>\n",
       "      <td>富善</td>\n",
       "      <td>致远CTA精选5号</td>\n",
       "      <td>691375</td>\n",
       "      <td>16000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>珺容开源量化臻选1号</td>\n",
       "      <td>珺容</td>\n",
       "      <td>珺容翔宇CTA2号</td>\n",
       "      <td>442675</td>\n",
       "      <td>10000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>白鹭鼓浪屿量化多策略十号</td>\n",
       "      <td>白鹭</td>\n",
       "      <td>白鹭鼓浪屿量化多策略一号</td>\n",
       "      <td>435913</td>\n",
       "      <td>10000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>安诚数盈开源安进1号</td>\n",
       "      <td>安诚数盈</td>\n",
       "      <td>安诚数盈锐利1号</td>\n",
       "      <td>安诚数盈锐利1号</td>\n",
       "      <td>10000000</td>\n",
       "      <td>0.10</td>\n",
       "      <td>0.08</td>\n",
       "      <td>0.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>思想三十九号</td>\n",
       "      <td>思勰</td>\n",
       "      <td>思勰投资子张十号</td>\n",
       "      <td>472397</td>\n",
       "      <td>5000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>时间序列开源臻选多策略套利</td>\n",
       "      <td>时间序列</td>\n",
       "      <td>时间序列量化对冲1号</td>\n",
       "      <td>533724</td>\n",
       "      <td>10000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>旭诺CTA三号</td>\n",
       "      <td>旭诺</td>\n",
       "      <td>旭诺CTA三号</td>\n",
       "      <td>425503</td>\n",
       "      <td>10000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>衍合开源量化市场中性1号</td>\n",
       "      <td>衍合</td>\n",
       "      <td>衍合量化市场中性1号</td>\n",
       "      <td>495036</td>\n",
       "      <td>30000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>无隅开源500一号</td>\n",
       "      <td>无隅</td>\n",
       "      <td>无隅鲲鹏一号</td>\n",
       "      <td>374140</td>\n",
       "      <td>15000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>图灵开源时间海臻选1号</td>\n",
       "      <td>图灵</td>\n",
       "      <td>图灵谷雨中性一号</td>\n",
       "      <td>565495</td>\n",
       "      <td>30000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>殊馥开源臻选一号</td>\n",
       "      <td>殊馥</td>\n",
       "      <td>殊馥馥源套利1号</td>\n",
       "      <td>422488</td>\n",
       "      <td>30000000</td>\n",
       "      <td>-0.02</td>\n",
       "      <td>-0.02</td>\n",
       "      <td>0.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>聊塑投资套利7号</td>\n",
       "      <td>聊塑</td>\n",
       "      <td>聊塑投资期权1号</td>\n",
       "      <td>433868</td>\n",
       "      <td>5000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             组合投资 Unnamed: 1          参考产品        代码        规模  预期收益  \\\n",
       "0        泰铼开源尊享1号         泰铼        泰铼金泰2号    504562  30000000   NaN   \n",
       "1        泰铼开源尊享2号         泰铼       泰铼信泰3号A    439678  33000000   NaN   \n",
       "2            橡木启明         橡木          橡木启明    500667   1000000   NaN   \n",
       "3           致远22号       致诚卓远         致远22号    291379   5000000   NaN   \n",
       "4      时代复兴开源微观八号       时代复兴      时代复兴微观一号    316470   1000000   NaN   \n",
       "5      富善投资开源歆享1号         富善     致远CTA精选5号    691375  16000000   NaN   \n",
       "6      珺容开源量化臻选1号         珺容     珺容翔宇CTA2号    442675  10000000   NaN   \n",
       "7    白鹭鼓浪屿量化多策略十号         白鹭  白鹭鼓浪屿量化多策略一号    435913  10000000   NaN   \n",
       "8      安诚数盈开源安进1号       安诚数盈      安诚数盈锐利1号  安诚数盈锐利1号  10000000  0.10   \n",
       "9          思想三十九号         思勰      思勰投资子张十号    472397   5000000   NaN   \n",
       "10  时间序列开源臻选多策略套利       时间序列    时间序列量化对冲1号    533724  10000000   NaN   \n",
       "11        旭诺CTA三号         旭诺       旭诺CTA三号    425503  10000000   NaN   \n",
       "12   衍合开源量化市场中性1号         衍合    衍合量化市场中性1号    495036  30000000   NaN   \n",
       "13      无隅开源500一号         无隅        无隅鲲鹏一号    374140  15000000   NaN   \n",
       "14    图灵开源时间海臻选1号         图灵      图灵谷雨中性一号    565495  30000000   NaN   \n",
       "15       殊馥开源臻选一号         殊馥      殊馥馥源套利1号    422488  30000000 -0.02   \n",
       "16       聊塑投资套利7号         聊塑      聊塑投资期权1号    433868   5000000   NaN   \n",
       "\n",
       "    预期收益(费后）  预期波动  \n",
       "0        NaN   NaN  \n",
       "1        NaN   NaN  \n",
       "2        NaN   NaN  \n",
       "3        NaN   NaN  \n",
       "4        NaN   NaN  \n",
       "5        NaN   NaN  \n",
       "6        NaN   NaN  \n",
       "7        NaN   NaN  \n",
       "8       0.08  0.10  \n",
       "9        NaN   NaN  \n",
       "10       NaN   NaN  \n",
       "11       NaN   NaN  \n",
       "12       NaN   NaN  \n",
       "13       NaN   NaN  \n",
       "14       NaN   NaN  \n",
       "15     -0.02  0.01  \n",
       "16       NaN   NaN  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "组合成分"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def get_trade_date(start_date,end_date,period='W'):\n",
    "    data=w.tdays(start_date,end_date,period=period)\n",
    "    trade_dates=data.Data[0]\n",
    "    trade_dates=[i.date() for i in trade_dates]\n",
    "    return trade_dates\n",
    "\n",
    "def get_all_date(start_date,end_date):\n",
    "    data=w.tdays(start_date, end_date, \"Days=Alldays\")\n",
    "    all_dates=data.Data[0]\n",
    "    all_dates=[i.date() for i in all_dates]\n",
    "    return all_dates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_week_date=get_trade_date('2005-05-04','',period='W')\n",
    "all_date=get_all_date('2005-05-04','')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_funds=[]\n",
    "for i in range(len(组合成分)):\n",
    "    #print(i)\n",
    "    mask=all_fund_nav['基金ID']==组合成分['代码'][i]\n",
    "    fund_info=all_fund_nav[mask][['基金简称','统计日期','复权累计净值']].dropna()\n",
    "    #print(fund_info)\n",
    "    fund_data_=pd.DataFrame(index=all_date,columns=[组合成分['参考产品'][i]])\n",
    "        #把净值填充进有所有日期的表中\n",
    "    fund_data_[组合成分['参考产品'][i]].loc[fund_info['统计日期']]=fund_info['复权累计净值'].tolist()\n",
    "    fund_data_=fund_data_.fillna(method='ffill')\n",
    "        #按照周度筛选出数据\n",
    "    fund_data_=fund_data_.loc[all_week_date]\n",
    "    \n",
    "    #fund_data_=pd.DataFrame(index=all_week_date,columns=[组合成分['参考产品'][i]])\n",
    "    #for j in all_week_date:\n",
    "        #if j in fund_info['统计日期'].tolist():\n",
    "            #fund_data_.loc[j][组合成分['参考产品'][i]]=fund_info[fund_info.统计日期==j].iloc[0][2]\n",
    "    fund_data_=fund_data_.reset_index()\n",
    "    #fund_data_['日期']=[datetime.strptime(i,'%Y-%m-%d') for i in fund_data_.index]\n",
    "    #fund_data_=fund_data_.sort_values(by=['日期'],ascending=False)\n",
    "    #print(fund_data_)\n",
    "    #fund_info=fund_data_\n",
    "    #fund_data_after_fee_=高水位法(fund_data_.iloc[:,1],费率)\n",
    "    \n",
    "    all_funds.append(fund_data_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_funds_merge=reduce(lambda left,right: pd.merge(left,right,on='index',how='outer'),all_funds)\n",
    "all_funds_merge['index']=[datetime.strptime(str(i),'%Y-%m-%d') for i in all_funds_merge['index']]\n",
    "all_funds_merge=all_funds_merge.sort_values(by=['index'],axis=0,ascending=True, inplace=False)\n",
    "all_funds_merge=all_funds_merge.set_index('index',drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>泰铼金泰2号</th>\n",
       "      <th>泰铼信泰3号A</th>\n",
       "      <th>橡木启明</th>\n",
       "      <th>致远22号</th>\n",
       "      <th>时代复兴微观一号</th>\n",
       "      <th>致远CTA精选5号</th>\n",
       "      <th>珺容翔宇CTA2号</th>\n",
       "      <th>白鹭鼓浪屿量化多策略一号</th>\n",
       "      <th>安诚数盈锐利1号</th>\n",
       "      <th>思勰投资子张十号</th>\n",
       "      <th>时间序列量化对冲1号</th>\n",
       "      <th>旭诺CTA三号</th>\n",
       "      <th>衍合量化市场中性1号</th>\n",
       "      <th>无隅鲲鹏一号</th>\n",
       "      <th>图灵谷雨中性一号</th>\n",
       "      <th>殊馥馥源套利1号</th>\n",
       "      <th>聊塑投资期权1号</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>index</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2005-05-13</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2005-05-20</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2005-05-27</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2005-06-03</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2005-06-10</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-07-29</th>\n",
       "      <td>1.3432</td>\n",
       "      <td>1.392277</td>\n",
       "      <td>1.064</td>\n",
       "      <td>2.035318</td>\n",
       "      <td>1.451113</td>\n",
       "      <td>1.029</td>\n",
       "      <td>1.738875</td>\n",
       "      <td>1.503316</td>\n",
       "      <td>1.698233</td>\n",
       "      <td>1.2108</td>\n",
       "      <td>1.172314</td>\n",
       "      <td>2.1457</td>\n",
       "      <td>1.127946</td>\n",
       "      <td>2.154513</td>\n",
       "      <td>1.088</td>\n",
       "      <td>1.342457</td>\n",
       "      <td>1.5469</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-08-05</th>\n",
       "      <td>1.3198</td>\n",
       "      <td>1.387182</td>\n",
       "      <td>1.056</td>\n",
       "      <td>2.035318</td>\n",
       "      <td>1.457236</td>\n",
       "      <td>1.027</td>\n",
       "      <td>1.729576</td>\n",
       "      <td>1.483177</td>\n",
       "      <td>1.640632</td>\n",
       "      <td>1.2080</td>\n",
       "      <td>1.172314</td>\n",
       "      <td>2.0661</td>\n",
       "      <td>1.117118</td>\n",
       "      <td>2.133539</td>\n",
       "      <td>1.088</td>\n",
       "      <td>1.342457</td>\n",
       "      <td>1.5480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-08-12</th>\n",
       "      <td>1.3709</td>\n",
       "      <td>1.418000</td>\n",
       "      <td>1.069</td>\n",
       "      <td>2.037079</td>\n",
       "      <td>1.456011</td>\n",
       "      <td>1.038</td>\n",
       "      <td>1.742067</td>\n",
       "      <td>1.493839</td>\n",
       "      <td>1.671569</td>\n",
       "      <td>1.2154</td>\n",
       "      <td>1.170224</td>\n",
       "      <td>2.0743</td>\n",
       "      <td>1.119056</td>\n",
       "      <td>2.193925</td>\n",
       "      <td>1.084</td>\n",
       "      <td>1.342457</td>\n",
       "      <td>1.5473</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-08-19</th>\n",
       "      <td>1.3765</td>\n",
       "      <td>1.424587</td>\n",
       "      <td>0.953</td>\n",
       "      <td>2.033558</td>\n",
       "      <td>1.457236</td>\n",
       "      <td>1.030</td>\n",
       "      <td>1.681139</td>\n",
       "      <td>1.485546</td>\n",
       "      <td>1.617271</td>\n",
       "      <td>1.2128</td>\n",
       "      <td>1.170224</td>\n",
       "      <td>2.0168</td>\n",
       "      <td>1.121221</td>\n",
       "      <td>2.203835</td>\n",
       "      <td>1.089</td>\n",
       "      <td>1.341787</td>\n",
       "      <td>1.5477</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-08-26</th>\n",
       "      <td>1.3765</td>\n",
       "      <td>1.424587</td>\n",
       "      <td>0.953</td>\n",
       "      <td>2.033558</td>\n",
       "      <td>1.457236</td>\n",
       "      <td>1.050</td>\n",
       "      <td>1.681139</td>\n",
       "      <td>1.485546</td>\n",
       "      <td>1.617271</td>\n",
       "      <td>1.2128</td>\n",
       "      <td>1.170224</td>\n",
       "      <td>2.0168</td>\n",
       "      <td>1.121221</td>\n",
       "      <td>2.203835</td>\n",
       "      <td>1.089</td>\n",
       "      <td>1.341787</td>\n",
       "      <td>1.5477</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>883 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            泰铼金泰2号   泰铼信泰3号A   橡木启明     致远22号  时代复兴微观一号  致远CTA精选5号  珺容翔宇CTA2号  \\\n",
       "index                                                                           \n",
       "2005-05-13     NaN       NaN    NaN       NaN       NaN        NaN        NaN   \n",
       "2005-05-20     NaN       NaN    NaN       NaN       NaN        NaN        NaN   \n",
       "2005-05-27     NaN       NaN    NaN       NaN       NaN        NaN        NaN   \n",
       "2005-06-03     NaN       NaN    NaN       NaN       NaN        NaN        NaN   \n",
       "2005-06-10     NaN       NaN    NaN       NaN       NaN        NaN        NaN   \n",
       "...            ...       ...    ...       ...       ...        ...        ...   \n",
       "2022-07-29  1.3432  1.392277  1.064  2.035318  1.451113      1.029   1.738875   \n",
       "2022-08-05  1.3198  1.387182  1.056  2.035318  1.457236      1.027   1.729576   \n",
       "2022-08-12  1.3709  1.418000  1.069  2.037079  1.456011      1.038   1.742067   \n",
       "2022-08-19  1.3765  1.424587  0.953  2.033558  1.457236      1.030   1.681139   \n",
       "2022-08-26  1.3765  1.424587  0.953  2.033558  1.457236      1.050   1.681139   \n",
       "\n",
       "            白鹭鼓浪屿量化多策略一号  安诚数盈锐利1号  思勰投资子张十号  时间序列量化对冲1号  旭诺CTA三号  衍合量化市场中性1号  \\\n",
       "index                                                                           \n",
       "2005-05-13           NaN       NaN       NaN         NaN      NaN         NaN   \n",
       "2005-05-20           NaN       NaN       NaN         NaN      NaN         NaN   \n",
       "2005-05-27           NaN       NaN       NaN         NaN      NaN         NaN   \n",
       "2005-06-03           NaN       NaN       NaN         NaN      NaN         NaN   \n",
       "2005-06-10           NaN       NaN       NaN         NaN      NaN         NaN   \n",
       "...                  ...       ...       ...         ...      ...         ...   \n",
       "2022-07-29      1.503316  1.698233    1.2108    1.172314   2.1457    1.127946   \n",
       "2022-08-05      1.483177  1.640632    1.2080    1.172314   2.0661    1.117118   \n",
       "2022-08-12      1.493839  1.671569    1.2154    1.170224   2.0743    1.119056   \n",
       "2022-08-19      1.485546  1.617271    1.2128    1.170224   2.0168    1.121221   \n",
       "2022-08-26      1.485546  1.617271    1.2128    1.170224   2.0168    1.121221   \n",
       "\n",
       "              无隅鲲鹏一号  图灵谷雨中性一号  殊馥馥源套利1号  聊塑投资期权1号  \n",
       "index                                               \n",
       "2005-05-13       NaN       NaN       NaN       NaN  \n",
       "2005-05-20       NaN       NaN       NaN       NaN  \n",
       "2005-05-27       NaN       NaN       NaN       NaN  \n",
       "2005-06-03       NaN       NaN       NaN       NaN  \n",
       "2005-06-10       NaN       NaN       NaN       NaN  \n",
       "...              ...       ...       ...       ...  \n",
       "2022-07-29  2.154513     1.088  1.342457    1.5469  \n",
       "2022-08-05  2.133539     1.088  1.342457    1.5480  \n",
       "2022-08-12  2.193925     1.084  1.342457    1.5473  \n",
       "2022-08-19  2.203835     1.089  1.341787    1.5477  \n",
       "2022-08-26  2.203835     1.089  1.341787    1.5477  \n",
       "\n",
       "[883 rows x 17 columns]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_funds_merge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_funds_merge.to_excel('portfolio_nav.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_fund_return=np.array((all_funds_merge/all_funds_merge.shift()).sub(1).mean()*52*0.8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "all_fund_weekly_return=(all_funds_merge/all_funds_merge.shift()).sub(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "port_weight=np.array(组合成分['规模']/组合成分['规模'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "port_return=all_fund_return*port_weight.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "port_return=np.sum(all_fund_return*port_weight)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.09691383365205"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "port_return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "port_std=np.dot(port_weight.T,np.dot(all_fund_weekly_return.cov()*52,port_weight))**0.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0447061825800149"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "port_std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.1677948788983294"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "port_return/port_std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

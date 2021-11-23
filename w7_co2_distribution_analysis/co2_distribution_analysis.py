import pandas as pd
#from pyecharts import Map
from pyecharts import options as opts
from pyecharts.charts import Sankey
from pyecharts.charts import ThemeRiver


class Analytics:
    def __init__(self):
        self.dictionary = {'Beijing': "北京",
                           'Tianjin': "天津",
                           'Hebei': "河北",
                           'Shanxi': "山西",
                           'InnerMongolia': "内蒙古",
                           'Liaoning': "辽宁",
                           'Jilin': "吉林",
                           'Heilongjiang': "黑龙江",
                           'Shanghai': "上海",
                           'Jiangsu': "江苏",
                           'Zhejiang': "浙江",
                           'Anhui': "安徽",
                           'Fujian': "福建",
                           'Jiangxi': "江西",
                           'Shandong': "山东",
                           'Henan': "河南",
                           'Hubei': "湖北",
                           'Hunan': "湖南",
                           'Guangdong': "广东",
                           'Guangxi': "广西",
                           'Hainan': "海南",
                           'Chongqing': "重庆",
                           'Sichuan': "四川",
                           'Guizhou': "贵州",
                           'Yunnan': "云南",
                           'Shaanxi': "陕西",
                           'Gansu': "甘肃",
                           'Qinghai': "青海",
                           'Ningxia': "宁夏",
                           'Xinjiang': "新疆"}

    def analyze_area(self, year, category):
        '''
        :param year: 年份
        :param category: 燃料种类
        :return:
        '''
        analyze_area_df = pd.read_excel(
            "./co2_demo/Province sectoral CO2 emissions " + str(year) + ".xlsx",
            sheet_name="Sum", index_col=[0])
        analyze_area_eng_name = list(analyze_area_df.index)[0:30]
        analyze_area_chi_name = []
        for i in analyze_area_eng_name:
            analyze_area_chi_name.append(self.dictionary[i])
        analyze_area_data = list(analyze_area_df[category])[0:30]
        return dict(zip(analyze_area_chi_name, analyze_area_data))

    def analyze_fuel_distribution(self, year, area):
        analyze_fuel_distribution_df = pd.read_excel(
            "./co2_demo/Province sectoral CO2 emissions " + str(year) + ".xlsx",
            sheet_name=area, index_col=[0])
        industry = list(analyze_fuel_distribution_df.index)[3:]
        fuel_type = list(analyze_fuel_distribution_df.columns)[:-4]
        node_list = []
        links = []
        for i in industry:
            for j in fuel_type:
                if analyze_fuel_distribution_df.loc[i, j] != 0:
                    node_list.append(i)
                    node_list.append(j)
                    links.append({"source": j, "target": i, "value": analyze_fuel_distribution_df.loc[i, j]})
        nodes = []
        for i in list(set(node_list)):
            nodes.append({"name": i})
        return nodes, links

    def analyze_city_time_distribution(self):
        all_time_dict = {}
        for i in range(1997, 2016):
            data_now = pd.read_excel("./co2_demo/Province sectoral CO2 emissions " + str(i) + ".xlsx", sheet_name="Sum",
                                     index_col=[0])
            all_time_dict[str(i)] = dict(data_now["Total"][:-2])
        x_data = list(all_time_dict['1997'].keys())
        y_data = []
        # 时间
        for i in all_time_dict.keys():
            # 地点
            for j in all_time_dict[i].keys():
                y_data.append([i, all_time_dict[i][j], j])
        return x_data, y_data

    def analyze_city_industry_distribution(self, city):
        all_time_dict = {}
        data = pd.read_excel("./co2_demo/Province sectoral CO2 emissions 2015.xlsx", sheet_name="Hebei", index_col=[0])
        industry = list(data.index)[3:]
        for i in range(1997, 2016):
            data_now = pd.read_excel("./co2_demo/Province sectoral CO2 emissions " + str(i) + ".xlsx",
                                     sheet_name=city, index_col=[0])
            a_year_dict = {}
            for j in industry:
                a_year_dict[j] = data_now.loc[j, "Total"]
            all_time_dict[str(i)] = a_year_dict
        x_data_industry = list(all_time_dict['1997'].keys())
        y_data_industry = []
        # 时间
        for i in all_time_dict.keys():
            # 地点
            for j in all_time_dict[i].keys():
                y_data_industry.append([i, all_time_dict[i][j], j])
        return x_data_industry, y_data_industry

class Visualization:
    def __init__(self, data):
        self.data = data

    def plot_area(self):
        province_distribution = self.data
        province = list(province_distribution.keys())
        values = list(province_distribution.values())
        chinese_map = Map("中国地图", '中国地图', width=1200, height=600)
        chinese_map.add("", province, values, visual_range=[0, 600], maptype='china', is_visualmap=True,
                        visual_text_color='#000')
        chinese_map.render(path="指定时间指定种类的CO2区域分布.html")

    def plot_sankey(self, nodes, links):
        c = (
            Sankey()
                .add(
                "sankey",
                nodes,
                links,
                linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
                label_opts=opts.LabelOpts(position="right"),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="燃料种类和行业分布的关系"))
                .render("燃料种类和行业分布的关系.html")
        )

    def plot_themeriver(self, x_data, y_data):
        c = (
            ThemeRiver(init_opts=opts.InitOpts(width="900px", height="600px"))
                .add(
                series_name=x_data,
                data=y_data,
                singleaxis_opts=opts.SingleAxisOpts(
                    pos_top="50", pos_bottom="50", type_="time"
                ),
            )
                .set_global_opts(
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line")
            )
                .render("指定城市不同行业二氧化碳排放量随时间变化.html")
        )


class NotNumError(ValueError):
    def __init__(self, year, province, industry, fuel_type):
        self.year = year
        self.province = province
        self.industry = industry
        self.fuel_type = fuel_type
        self.message = "nan error in {}, {}, {}, {}".format(year, province, industry, fuel_type)

class Check:
    def __init__(self, year, province, industry, fuel_type):
        self.year = year
        self.province = province
        self.industry = industry
        self.fuel_type = fuel_type
    def check_nan(self):
        data = pd.read_excel("./co2_demo/Province sectoral CO2 emissions "+str(self.year)+".xlsx",
                             sheet_name=self.province, index_col=[0])
        val = data.loc[self.industry, self.fuel_type]
        if pd.isna(val):
            raise NotNumError(self.year, self.province, self.industry, self.fuel_type)

    def check_zero_sum(self):
        data = pd.read_excel("./co2_demo/Province sectoral CO2 emissions "+str(self.year)+".xlsx",
                             sheet_name=self.province, index_col=[0])
        total = data.loc[self.industry, "Total"]
        if total == 0:
            raise ZeroDivisionError

if __name__ == "__main__":
    a = Analytics()
    x_data, y_data = a.analyze_city_time_distribution()
    print("x_data:",x_data)
    print("y_data:",y_data)
import datetime

from django.core.management.base import BaseCommand
import xlwings as xw
import os
import shutil
import pandas as pd
from cost.models import ShopDay
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        sycm_dir = "D:\运营\数据源\生意参谋"
        sycm_filelist = os.listdir(sycm_dir)
        app = xw.App(visible=False, add_book=False)
        app.display_alerts = False
        app.screen_updating = False
        for sycm_file in sycm_filelist:
            use_excel = "{file_dir}\{file_name}".format(file_dir=sycm_dir, file_name=sycm_file)
            print(sycm_file)
            wb = app.books.open(use_excel)
            sheet1 = wb.sheets[0]
            # 获取 sheet 行数
            info = sheet1.used_range
            rows = info.last_cell.row
            rows_value = sheet1.range('A6:AH{i}'.format(i=rows)).value
            for item in rows_value:
                try:
                    ShopDay.objects.create(shop_date=item[0], shop_id=item[1], shop_name=item[2], sales=float(item[19].replace(',', '')))
                except IntegrityError:
                    print('{date} {shop_id}has exist'.format(date=item[0], shop_id=item[1]))
            wb.close()
            shutil.move("{file_dir}\{file_name}".format(file_dir=sycm_dir, file_name=sycm_file),
                        "D:\运营\回收站\{file_name}".format(file_name=sycm_file))
        app.quit()

        # 直通车数据
        print("直通车数据统计开始")
        train_dir = "D:\运营\数据源\直通车"
        train_filelist = os.listdir(train_dir)
        for train_file in train_filelist:
            use_excel = "{file_dir}\{file_name}".format(file_dir=train_dir, file_name=train_file)
            print(train_file)
            data_frame = pd.read_csv(use_excel)
            group = data_frame.groupby(["日期", "商品id"])
            new_data = (group.agg('sum'))

            for index, row in new_data.iterrows():
                try:
                    shop_day = ShopDay.objects.get(shop_date=index[0], shop_id=str(index[1]))
                    shop_day.train_cost = round(row['花费'] ,2)
                    shop_day.save()
                except ShopDay.DoesNotExist:
                    print("{date} {shop_id} Object not found".format(date=index[0], shop_id=index[1]))
            shutil.move(use_excel, "D:\运营\回收站\{file_name}".format(file_name=train_file))

        # 超级推荐
        print("超级推荐数据统计开始")
        tuijian_dir = "D:\运营\数据源\超级推荐"
        tuijian_list = os.listdir(tuijian_dir)
        for tuijian_file in tuijian_list:
            use_excel = "{file_dir}\{file_name}".format(file_dir=tuijian_dir, file_name=tuijian_file)
            print(tuijian_file)
            data_frame = pd.read_excel(use_excel, sheet_name="报表数据")

            for index, row in data_frame.iterrows():
                try:
                    shop_day = ShopDay.objects.get(shop_date=row['日期'], shop_id=str(row['商品id']))
                    shop_day.tuijian_cost = row['消耗']
                    shop_day.save()
                except ShopDay.DoesNotExist:
                    print("{date} {shop_id} Object not found".format(date=row['日期'], shop_id=row['商品id']))

            shutil.move("{file_dir}\{file_name}".format(file_dir=tuijian_dir, file_name=tuijian_file),
                        "D:\运营\回收站\{file_name}".format(file_name=tuijian_file))

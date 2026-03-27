import os
import datetime


def get_dates(l_year, l_month):
    # 获取当前时间并格式化
    dates = []
    # l_year年l_month月1日
    start_date = datetime.date(l_year, l_month, 1)
    # l_year年l_month+1月1日
    start_date2 = datetime.date(l_year, l_month + 1, 1)
    # print(start_date2)
    # l_year年l_month月最后一日
    end_date = start_date2 - datetime.timedelta(days=1)

    # 逐日生成日期
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%Y%m%d"))
        current_date += datetime.timedelta(days=1)
    return dates


def create_folder(folder_path):
    """
    创建指定路径的文件夹
    如果文件夹已存在，则不进行操作
    """
    try:
        # 使用 os.makedirs 创建文件夹，exist_ok=True 表示如果文件夹已存在则不抛出异常
        os.makedirs(folder_path, exist_ok=True)
        print(f"文件夹 '{folder_path}' 创建成功")
    except Exception as e:
        print(f"创建文件夹时发生错误: {e}")


if __name__ == "__main__":
    l_year = 2026
    l_month = 5
    dates = get_dates(l_year, l_month)
    print(dates)
    for date in dates:
        if date >= datetime.date.today().strftime("%Y%m%d"):
            folder_name = date
            folder_path = 'E:\\GoKin\\0-DtDay work\\'+str(l_year)+'\\'+str(l_year)+str(l_month).zfill(2)+'\\'+folder_name
            # print(folder_path)
            create_folder(folder_path)

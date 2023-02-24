import argparse
from parse_strings import parse_file
from parse_excel import *
from find_lproj import get_lproj_folders

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", help="Path to search for lproj folders")
    parser.add_argument("lang_excel_path", help="path to parse excel data")
    args = parser.parse_args()
    lproj_folders = get_lproj_folders(args.project_path)
    excel_path = args.lang_excel_path

    en_info_path = list(filter(lambda x: x.endswith("InfoPlist.strings"), lproj_folders["en"]))[0]
    en_info_result = list(map(lambda x: list(x.keys())[0], parse_file(en_info_path)))

    # 读取 Excel 数据
    data = read_excel_file(excel_path)

    # 处理数据并写入文件
    output_file_path = './output'

    process_data_and_write_file_with_other_files(data, output_file_path, "App", [{"InfoPlist": en_info_result}])
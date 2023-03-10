import os
import shutil
import yaml
from typing import Dict
from utils.logger import configure_logging

logger = configure_logging(__name__)


def ensure_folder(folder: str) -> None:
    """
    創建資料夾，如果已存在就刪除重新創建

    :param folder: str 要創建的資料夾路徑
    """

    if not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)
    else:
        logger.info(f"路徑: {folder} 已存在, 將其移除！")
        shutil.rmtree(folder, ignore_errors=True)
        os.makedirs(folder, exist_ok=True)

    logger.info(f"{folder} 輸出路徑創建完成\n")


def gen_folder(yaml_data: dict) -> Dict[str, str]:
    """
    根據給定的 YAML 資料，動態生成影像輸出路徑並返回路徑字典。

    :param yaml_data: 包含 YAML 資料的字典，需要包含 'output_dir_name' 和 'output_dir' 兩個鍵。
    :return: 包含各種影像輸出路徑的字典。
    """
    directory_path = {}

    # 動態生成格式化字符串的佔位符
    fmt = "/{}" * len(yaml_data['output_dir_name'])
    # 儲存各種影像輸出路徑
    for path, dir_format in yaml_data["output_dir"].items():
        if dir_format != "":
            # 取得影像輸出路徑的各個資料夾名稱，用來填充格式化字串的佔位符
            values = list(yaml_data['output_dir_name'].values())
            # 將格式化字串的佔位符填充完畢，得到最終的影像輸出路徑
            output = dir_format.replace("{}", fmt)
            output = output.format(*values)
            norm_path = os.path.normpath(output)
            # 確保目錄存在
            ensure_folder(norm_path)
            # 將影像輸出路徑加入 directory_path 字典中
            directory_path[path] = norm_path
        else:
            continue
    return directory_path


def load_yaml_config(file_path):
    """
    讀取 yaml 配置檔
    :param file_path: yaml 配置檔路徑
    :return: 讀取到的 yaml 配置資料
    """

    # 檢查檔案是否存在
    assert os.path.isfile(file_path), "Yaml File Not Exist!!"
    # 使用 logger 記錄器，記錄 YAML 檔案位置
    logger.info("Yaml 檔案存在: {} \n".format(file_path))
    # 讀取 yaml 檔案
    with open(file_path, "r") as stream:
        yaml_data = yaml.full_load(stream)
    return yaml_data

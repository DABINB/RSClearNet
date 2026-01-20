import os
import shutil
# re-upload

def make_dataset(hazy_path, GT_path, new_GT_path):
    os.makedirs(new_GT_path, exist_ok=True)
    hazy_files = os.listdir(hazy_path)
    for file in hazy_files:
        index = file.split('_')[0]
        origin_name = index + '.png'
        change_name = file
        origin_path = os.path.join(GT_path, origin_name)
        change_path = os.path.join(new_GT_path, change_name)
        # ==== 复制并重命名 ====
        if os.path.exists(origin_path):
            shutil.copy2(origin_path, change_path)
            print(f"[OK] {origin_name} -> {change_path}")
        else:
            print(f"[MISS] GT not found: {origin_path}")
    print("处理完成！")



if __name__ == '__main__':
    GT_path = 'D:\Graduation\Dataset\RSHaze_new\GT'
    hazy_path = 'D:\Graduation\Dataset\RSHaze_new\Hazy'
    new_GT_path = 'D:\Graduation\Dataset\RSHaze_new\\new_GT'
    make_dataset(hazy_path, GT_path, new_GT_path)

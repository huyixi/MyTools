import os

folder_path = './posts'
output_file = 'all_posts.txt'

with open(output_file, 'w', encoding='utf-8') as f_out:
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f_in:
                f_out.write(f'### {filename}\n\n')  # 标题
                f_out.write(f_in.read())  # 文件内容
                f_out.write('\n\n')  # 空行

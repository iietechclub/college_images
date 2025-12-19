import os

count = 0


def delete_ts_files(root_dir):
    global count
    for root, dirs, files in os.walk(root_dir):
        if "(" in root and (dirs.__len__() == 0) and files.__len__() == 1:
            print(root)

        # for dir in dirs:
        #     dir_path = os.path.join(root, dir)
        #     file_path = os.path.join(dir_path, ".gitkeep")
        #     if "(" in dir_path and not os.path.exists(file_path):
        #         open(file_path, "w").close()

        #         # with open(file_path, "w") as f:
        #         #     f.write("")

        #         print(f"Created: {file_path}")

        # for file in files:
        #     if file.endswith((".ts", ".tsx")):
        #         file_path = os.path.join(root, file)
        #         # os.remove(file_path)
        #         count += 1
        #         print(f"Deleted: {file_path}")


if __name__ == "__main__":
    target_directory = "C:/Code/Projects/Collage/collage-site/college_images"
    delete_ts_files(target_directory)
    # print(f"Deleted {count} files.")

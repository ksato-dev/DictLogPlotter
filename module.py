import numpy as np
import matplotlib.pyplot as plt
import argparse

class DictLogPlotter():
    def __init__(self):
        self.y_dict = {}
        self.extract_keys = []
        self.range_x = []
        self.range_y = []
        self.use_same_window = False
        self.file_name = ""

    def read_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--extract_keys", nargs="*", default="", type=str, help="")
        parser.add_argument("--range_x", default="", type=str, help="")
        parser.add_argument("--range_y", default="", type=str, help="")
        parser.add_argument("--use_same_window", default=False, type=bool, help="")
        parser.add_argument("--file_name", default="", type=str, help="")

        args = parser.parse_args()
        self.extract_keys = args.extract_keys
        self.use_same_window = args.use_same_window
        self.file_name = args.file_name

        if (args.range_x != ""):
            self.range_x = args.range_x.split(":")
        if (args.range_y != ""):
            self.range_y = args.range_y.split(":")

        ## Initialize elems in dict.
        if (self.extract_keys != ""):
            for key_name in self.extract_keys:
                self.y_dict[key_name] = []

        return parser.parse_args()

    def __split_line(self, str_line):
        key_and_val_list = str_line.split(",")
        # print(key_and_val_list)
        for elem in key_and_val_list:
            elem = elem.strip()
            key, value = None, None
            if (elem != "" and ":" in elem):
                key, value = elem.split(":")
            # print("key:", key, ", value:", value)

            if (0 < self.extract_keys.count(key)):
                self.y_dict[key].append(float(value))

    def __scan_file(self, file_obj):
        for str_line in file_obj:
            temp_str = str_line[:-1] 
            self.__split_line(temp_str)

    def parse_file(self):
        with open(self.file_name, "r") as fobj:
            self.__scan_file(fobj)

    def plot(self):
        fig, ax = plt.subplots()

        ax.set_xlabel('t')  # x軸ラベル
        ax.set_ylabel('value')  # y軸ラベル
        # ax.set_title(r'$\sin(x)$ and $\cos(x)$') # グラフタイトル
        for key in self.y_dict.keys():
            value_array = self.y_dict[key]
            x = np.arange(0, len(value_array))
            y = np.array(value_array)
            # plt.figure(figsize=(12, 8), dpi=200)
            ax.plot(x, y, linewidth=0.3, marker=".", markersize=0.8, label=key)
            # plt.title(key)
            # plt.xlabel("id")
            # plt.ylabel("value")
            # plt.grid()

        ax.grid()
        ax.legend(loc=0)    # 凡例
        fig.tight_layout()  # レイアウトの設定

        plt.show()


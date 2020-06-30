from module import DictLogPlotter

if __name__ == "__main__":
    hoge = DictLogPlotter()
    # print(hoge.read_args())
    hoge.read_args()

    # print(hoge.range_x)
    hoge.parse_file()

    # print()
    # print(hoge.y_dict)
    hoge.plot()

    


from module import DictLogPlotter

if __name__ == "__main__":
    hoge = DictLogPlotter()
    # print(hoge.read_args())
    cl_args = hoge.read_args()

    # print(hoge.range_x)
    hoge.parse_file()

    # print()
    # print(hoge.y_dict)

    if (cl_args.overlap_on is False):
        hoge.plot()
    else:
        hoge.plot_overlapping()


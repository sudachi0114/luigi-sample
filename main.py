import luigi
import requests
import pandas
from sklearn import svm
import pickle

from Dataset import Dataset

# iris data をダウンロードして、CSV ファイルに出力するタスク
class Download2CSV(luigi.Task):
    task_namespace = 'iris_tasks'

    # luigi.cfg ファイルから設定を取得してくる
    SOURCE_URL = luigi.Parameter()
    MID_ORIGINAL_PATH = luigi.Parameter()

    def run(self):
        with self.output().open('w') as f:
            responce = requests.get(self.SOURCE_URL)
            f.write(responce.text)

    def output(self):
        return luigi.LocalTarget(self.MID_ORIGINAL_PATH)


class CreateDataset(luigi.Task):
    task_namespace = 'iris_tasks'

    DATASET_PATH = luigi.Parameter()

    def requires(self):
        return Download2CSV()

    def output(self):
        return luigi.LocalTarget(self.DATASET_PATH, format=luigi.format.Nop)  # pickle で output する場合はこの format を指定する

    def run(self):
        data = pandas.read_csv(self.input().path, header=None)
        # print(data)

        x = data.iloc[:, [0, 1, 2, 3]]
        y = data.iloc[:, 4].replace({
            'Iris-setosa': 0,
            'Iris-versicolor': 1,
            'Iris-virginica': 2
        })

        # print(len(x), len(y))

        # train / test に分ける
        train_x, train_y = x[:120], y[:120]
        test_x, test_y = x[120:], y[120:]

        print("----- train -----\n", train_x, len(train_x))
        print("----- test  -----\n", test_x, len(test_x))

        iris_dataset = Dataset()

        iris_dataset.train_x = train_x
        iris_dataset.train_y = train_y

        iris_dataset.test_x = test_x
        iris_dataset.test_y = test_y

        with self.output().open('w') as p:
            p.write( pickle.dumps(iris_dataset, protocol=pickle.HIGHEST_PROTOCOL) )
            # output はファイルを介して行わなければいけないのか...??
            #    データをそのまま次のタスクに投げ渡したい... (return 的なことがしたい)

        # self.output = iris_dataset
        # print(self.output(), type(self.output()) )
        #    output() という関数を書かないと、空のlist [] を返すだけっぽい..??


class CreateModel(luigi.Task):
    task_namespace = 'iris_tasks'

    SAVE_MODEL_PATH = luigi.Parameter()  # TODO: 変数名変えたほうがいい (luigi.cfg も変えないといけないの、めんどうだなあ...)
    # パラメータの設定も class (Task) 毎だし...
    # 透明性とかもちょっと怪しい感じする (self.input() とか、データ・中間生成物の受け渡しがちょっとわかりにくい, 可読性低いような気が...しないでもない...)

    def requires(self):
        return CreateDataset()

    def run(self):
        with self.input().open('r') as infile:
            iris_dataset = pickle.load(infile)

            print(iris_dataset)
            print(iris_dataset.train_x)

            model = svm.SVC()  # なんだこれ..??
            model.fit(
                iris_dataset.train_x,
                iris_dataset.train_y
            )

            # 正解率の算出
            print(f"[train accuracy] {model.score(iris_dataset.train_x, iris_dataset.train_y)}")
            print(f"[test accuracy] {model.score(iris_dataset.test_x, iris_dataset.test_y)}")
            # TODO: ここも、テストとして、別タスクに切り出したい

            with self.output().open('w') as pf:
                pickle.dump(model, pf)

    def output(self):
        # バイナリファイルを出力する場合には format に luigi.format.NopFormat を指定するらしい
        # return luigi.LocalTarget(self.DATASET_PATH, format=luigi.format.Nop)
        #   Nop でもいいっぽい??
        return luigi.LocalTarget(self.SAVE_MODEL_PATH, format=luigi.format.NopFormat)


if __name__ == '__main__':
    # luigi.cfg という決まった名前 (?) なら、path の設定はいらないかも..??
    # luigi.configuration.LuigiConfigParser.add_config_path('./luigi.cfg')

    """
    luigi.run([
        # 'iris_tasks.Download2CSV',
        'iris_tasks.CreateModel',
        '--local-scheduler'
    ])
    """
    luigi.run()

import luigi
import requests
import pandas
from sklearn import svm
import pickle

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


class CreateModel(luigi.Task):
    task_namespace = 'iris_tasks'

    SAVE_MODEL_PATH = luigi.Parameter()  # TODO: 変数名変えたほうがいい (luigi.cfg も変えないといけないの、めんどうだなあ...)
    # パラメータの設定も class (Task) 毎だし...
    # 透明性とかもちょっと怪しい感じする (self.input() とか、データ・中間生成物の受け渡しがちょっとわかりにくい, 可読性低いような気が...しないでもない...)

    def requires(self):
        return Download2CSV()


    def run(self):
        with open(self.output().path, 'wb') as fb:
            data = pandas.read_csv(self.input().path, header=None)
            # print(data)

            # TODO: この辺を前処理として、別タスクに切り出したい..
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

            # print(train_x, len(train_x))
            # print(test_x, len(test_x))


            model = svm.SVC()  # なんだこれ..??
            model.fit(train_x, train_y)


            # 正解率の算出
            print(f"[train accuracy] {model.score(train_x, train_y)}")
            print(f"[test accuracy] {model.score(test_x, test_y)}")
            # TODO: ここも、テストとして、別タスクに切り出したい

            pickle.dump(model, fb)


    def output(self):
        # バイナリファイルを出力する場合には format に luigi.format.NopFormat を指定するらしい
        return luigi.LocalTarget(self.SAVE_MODEL_PATH, format=luigi.format.NopFormat)


if __name__ == '__main__':
    # luigi.cfg という決まった名前 (?) なら、path の設定はいらないかも..??
    # luigi.configuration.LuigiConfigParser.add_config_path('./luigi.cfg')

    luigi.run([
        # 'iris_tasks.Download2CSV',
        'iris_tasks.CreateModel',
        '--local-scheduler'
    ])

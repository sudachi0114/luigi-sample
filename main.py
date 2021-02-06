import luigi
import requests

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


if __name__ == '__main__':
    # luigi.cfg という決まった名前 (?) なら、path の設定はいらないかも..??
    # luigi.configuration.LuigiConfigParser.add_config_path('./luigi.cfg')

    luigi.run([
        'iris_tasks.Download2CSV',
        '--local-scheduler'
    ])

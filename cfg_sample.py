import luigi

class GetParameterCFGfile(luigi.Task):
    param = luigi.Parameter()  # ここのパラメータの中身が変わっても
    
    def requires(self):
        pass

    def output(self):
        return luigi.LocalTarget("./output/output_cfg.txt")  # この成果物が存在する以上は、タスクを重複して実行することはしないらしい。

    def run(self):
        with self.output().open('w') as f:
            f.write(f"{self.param} World.\n")

if __name__ == "__main__":
    luigi.configuration.LuigiConfigParser.add_config_path('./sample.cfg')

    """ ここで run に list で渡しているパラメータは、実行時にコマンドラインで渡すこともできる
        like: $ python source.py GetParameterCFGfile --local-scheduler
        luigi.run([]) で渡しておくと、 $ python source.py するだけで実行可能.
    """
    luigi.run([
        'GetParameterCFGfile',
        '--local-scheduler'
    ])

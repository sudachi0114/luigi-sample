# sklearn.pipeline.Pipeline
sklean の持つパイプライン機能 `sklean.pipeline.Pipeline` を試してみる。

スクリプトは全て、プロジェクトルートから実行する。

## Python 仮想環境 アクティベート

```sh
python -m venv venv
source venv/bin/activate
```

### library update && install

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

## main 処理

TODO: これから書きます

<!-- 

```sh
python main.py
```

-->

<!--

## Luigi Task 定義 Tips 📝 :

* `Luigi` では「入力 ➡️  処理 ➡️  出力」という一連の処理をひとまとまりとして扱う。
  - この一連の処理は、`luigi.Task` (or それを継承したクラス) を継承することで定義する。
    - `luigi.Task` クラスでは、`requires`, `run`, `output` の3つのメソッドを主に実装することで、一連の処理を表現することができる。
	  - `requires` : これから実行しようとしている処理が依存している処理を定義する。(タスクの依存関係を定義)
	  - `output` : 「出力先」を定義する。( Local の他にも AWS/S3 や GCP/BigQuery などが選択できるらしい...)
	  - `run` : 出力を生成する処理を記述する。( output で指定したものが存在しないときのみ、run メソッドが走る )

-->

### Execution help:

<!-- 

#### Main:

* How to execute `src/luigi/main.py` ?

```shell
python src/luigi/main.py
```

-->

#### `src/sklearn/tutorial`:

[sklean 公式ドキュメントの `pipeline` 部分](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)にある公式の例

* How to execute `src/sklearn/tutorial/sample.py` ?

```shell
python src/sklearn/tutorial/sample.py
```

内容 (なにを学習してるのか?) に関してはちょっとよくわかってない...ごめん (´･ω･`)


## Links

* [sklearn.pipeline.Pipeline - official document](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)

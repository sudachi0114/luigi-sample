# Luigi トライアル
python で pipeline 処理を実現するためのライブラリ `Luigi` を試してみる。

> パイプライン → 配管工 → ルイージ と読むらしい。

## Python 仮想環境 アクティベート

```sh
python -m venv venv
source ./venv/bin/activate
```

### library update && install

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

## main 処理

```sh
python main.py
```

* **CAUTION:** もし `output/models/model.pkl` がないと言われたら""

```sh
mkdir output/models
```


## Luigi Task 定義 Tips 📝 :

* `Luigi` では「入力 ➡️  処理 ➡️  出力」という一連の処理をひとまとまりとして扱う。
  - この一連の処理は、`luigi.Task` (or それを継承したクラス) を継承することで定義する。
    - `luigi.Task` クラスでは、`requires`, `run`, `output` の3つのメソッドを主に実装することで、一連の処理を表現することができる。
	  - `requires` : これから実行しようとしている処理が依存している処理を定義する。(タスクの依存関係を定義)
	  - `output` : 「出力先」を定義する。( Local の他にも AWS/S3 や GCP/BigQuery などが選択できるらしい...)
	  - `run` : 出力を生成する処理を記述する。( output で指定したものが存在しないときのみ、run メソッドが走る )



### Execution help:

* How to execute `task_example.py` ?

```shell
python src/luigi/task_example.py
```

then create `mid/task1.txt` & `output/task2.txt`.


## Links
* [Python: Luigiでデータパイプラインを作る (基本参考サイト)](https://ohke.hateblo.jp/entry/2018/04/07/230000)
* [Luigi リポジトリ](https://github.com/spotify/luigi)
* [機械学習で便利なluigiフレームワークの紹介](https://www.m3tech.blog/entry/2018/10/17/105115)

* [Pythonでパイプライン処理をする](https://qiita.com/yujikawa/items/208049ed2469f8e3fdd1)

* [luigiを使ってみた](https://www.nogawanogawa.com/entry/luigi_intro)
* [Python, LuigiでPipeline管理の基本を学ぶ](https://qiita.com/yuusei/items/6ba669a781b9f8ec7f63)

* [Luigi逆引きリファレンス](https://qiita.com/hagino3000/items/b9a7761dad1f352ec723#pandas%E3%81%AEdataframe%E3%82%92output%E3%81%AB%E3%81%97%E3%81%9F%E3%81%84)

* [scikit-learn基本の予測モデル](https://qiita.com/ground0state/items/25d2db49589b52d65396)

* [【Python】自作のクラスを読み込むとTypeError: 'module' object is not callableとでる件](https://chat-rate.com/it/3969/)

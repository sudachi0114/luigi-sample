# Luigi トライアル
python で pipeline 処理を実現するためのライブラリ `Luigi` を試してみる

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
	  - `run` : 出力を生成する処理を記述する。
	  - `output` : 「出力先」を定義する。( Local の他にも AWS/S3 や GCP/BigQuery などが選択できるらしい...)


## Links
* [参考サイト](https://ohke.hateblo.jp/entry/2018/04/07/230000)
* [Luigi リポジトリ](https://github.com/spotify/luigi)
* [機械学習で便利なluigiフレームワークの紹介](https://www.m3tech.blog/entry/2018/10/17/105115)

# To-Do リストカレンダー

このプロジェクトは、カレンダーとTo-Doリストを統合したアプリケーションです。ユーザーは特定の日に紐づけてTo-Do項目を追加、編集、削除することができ、選択した日付に関連するタスクを簡単に管理できます。

## 特徴

- 日付選択が簡単なカレンダー
- 各日に関連するTo-Doリストを表示
- To-Do項目の追加、削除、色の変更が可能
- To-DoリストはJSON形式で保存され、アプリケーションを再起動してもデータが保持されます

## 必要な環境

- Python 3.x
- PySide6

## インストール手順

1. リポジトリをクローンまたはダウンロードします。
2. 必要なパッケージをインストールします。

```
pip install PySide6
```
3. アプリケーションが起動したら、カレンダーの日付をクリックして、その日にタスクを追加することができます。

## 使用方法
カレンダーの日付をクリックして、タスクを追加したい日を選択します。
下の入力ボックスにTo-Do項目を入力し、「追加」ボタンをクリックします。
リストに表示されるTo-Do項目は右クリックすることで、色変更や削除が可能です。

## データの保存
To-Doリストは、アプリケーションのルートディレクトリに todos.json という名前で保存されます。このファイルには、日付ごとのタスクがJSON形式で保存されます。


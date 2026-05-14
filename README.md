# ai-news-jp

AI最新情報の日本語SEOブログ。Claude CLI で毎日3記事自動生成し、GitHub Pagesに自動デプロイ。Amazon/A8/Adsterra広告スロット組み込み済み。

## 仕組み

```
Reddit/HN/RSS → fetch_sources.py → data/trends.json
                                          ↓
                              generate_articles.py (claude -p)
                                          ↓
                              content/posts/*.md (frontmatter+md)
                                          ↓
                                   build_site.py
                                          ↓
                                       site/ (HTML+sitemap+rss)
                                          ↓
                              GitHub Actions → GitHub Pages公開
```

## ワンタイム手動セットアップ（30分）

### 1. GitHubリポジトリ作成
```
gh repo create ai-news-jp --public --source . --remote origin --push
```
※ `gh` がなければ https://github.com/new で `ai-news-jp` を public で作成 → `git remote add origin git@github.com:USER/ai-news-jp.git && git push -u origin main`

### 2. GitHub Pages有効化
リポジトリ Settings → Pages → Source: **GitHub Actions** に設定

### 3. Secret登録
Settings → Secrets and variables → Actions → New repository secret
- `ANTHROPIC_API_KEY`: Anthropicコンソールで発行したAPIキー
- `INDEXNOW_KEY` (任意): BingのIndexNow用キー (https://www.bing.com/indexnow で発行)

### 4. config.json 更新
- `site.base_url` を実際の公開URLに（例: `https://nayo126.github.io/ai-news-jp`）
- `deploy.github_user` を自分のGitHubユーザー名に

### 5. マネタイズ（親協力アクション）
親に頼んで承認を取った後、config.json の `monetization` を更新:
- `amazon_associate_id`: Amazonアソシエイト承認後にタグID（例: `nayo126-22`）
- `adsterra_publisher_id`: Adsterra承認後の publisher ID
- `a8_sid`: A8.netのsid
- `rakuten_id`: 楽天アフィID

更新後、次のcron実行で自動的に広告タグが全記事に反映される（再ビルド不要）。

### 6. Google Search Console登録
1. https://search.google.com/search-console
2. プロパティ追加: `https://nayo126.github.io/ai-news-jp/` を URL prefix で
3. 所有権確認: HTMLファイル方式かHTMLタグ方式
4. sitemap.xml を送信

## ローカルでテスト

```
python3 scripts/fetch_sources.py        # 元ネタ取得
python3 scripts/generate_articles.py    # 記事自動生成
python3 scripts/build_site.py           # 静的サイトビルド
open site/index.html                    # ブラウザ確認
```

## スケジュール

GitHub Actions cron:
- 毎日 UTC 22:00 (JST 07:00) — 朝のニュース
- 毎日 UTC 10:00 (JST 19:00) — 夕方のニュース

手動: Actions タブから `Run workflow` で即時実行可能

## マネタイズの見込み

3〜6ヶ月でSEOで月間PV 1万〜が現実的射程。CPC型広告で月¥3,000〜¥30,000、Amazonアフィ込みで月¥10,000〜¥100,000を想定。

## トラブルシュート

- **generator が rc=2** → 「新しい元ネタがなかった」だけ。問題なし
- **claude CLI が rate limit** → 数時間後の次のcronで自動再試行
- **記事の数字や固有名詞が古い** → 元RSSが古い。anthropic_news のRSSは404のため除外推奨

## 次のステップ（自動化拡張アイデア）

- 多言語化（英語版を別ブランチで生成）
- 関連記事レコメンド機能
- ユーザー検索ログのSEO反映

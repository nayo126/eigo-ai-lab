#!/bin/zsh
# 3日収益化スプリント: 1晩で15-20記事を一気に生成して SEO 種まき
set -e
cd "$(dirname "$0")/.."
LOG=logs/burst.log
mkdir -p logs
echo "[$(date -Iseconds)] === burst start ===" | tee -a "$LOG"

PY=/opt/homebrew/bin/python3
ROUNDS=${1:-5}     # rounds × articles_per_run = total articles

for i in $(seq 1 $ROUNDS); do
  echo "[$(date -Iseconds)] -- round $i/$ROUNDS --" | tee -a "$LOG"
  $PY scripts/fetch_sources.py 2>&1 | tail -3 | tee -a "$LOG"
  $PY scripts/generate_articles.py 2>&1 | tail -5 | tee -a "$LOG" || echo "  (gen rc=$?)" | tee -a "$LOG"
  sleep 5
done

echo "[$(date -Iseconds)] -- build --" | tee -a "$LOG"
$PY scripts/build_site.py 2>&1 | tail -3 | tee -a "$LOG"

echo "[$(date -Iseconds)] -- commit --" | tee -a "$LOG"
git add -A
git -c user.email=bot@local -c user.name="auto-builder" commit -m "burst: $(date +%F-%H%M)" --allow-empty 2>&1 | tail -3 | tee -a "$LOG" || true

echo "[$(date -Iseconds)] === burst done ===" | tee -a "$LOG"

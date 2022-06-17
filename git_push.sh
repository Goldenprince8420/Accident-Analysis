echo "# Accident-Analysis" >> README.md
git init
git add README.md git_push.sh main.py driver.csv spatiotemporal.csv
git commit -m "Main Push"
git remote add origin https://github.com/Goldenprince8420/Accident-Analysis.git
git remote -v
git push origin main
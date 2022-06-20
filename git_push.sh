echo "# Accident-Analysis" >> README.md
git init
git add README.md                            data_encoded_p.csv     feature_normalizer.py  lin_reg_p.csv       missing_handling.py  point_biserial_p.csv  spatiotemporal.csv  weighted_tau_p.csv                    driver.csv             git_push.sh            lin_reg_r.csv       modules.sh           point_biserial_r.csv  spearman_p.csv      weighted_tau_r.csv advanced_analysis_driver.py          driver_exploration.py  kendal_tau_p.csv       lin_reg_slope.csv   pearson_p.csv        processing.r          spearman_r.csv advanced_analysis_spatiotemporal.py  driver_processed.csv   kendal_tau_r.csv       lin_reg_stderr.csv  pearson_r.csv        read_data.py          temp_analysis.py categorical_encoder.py               driver_readied.csv     lin_reg_inter.csv      main.py             plots                requirements.txt
git commit -m "Main Push"
git remote add origin https://github.com/Goldenprince8420/Accident-Analysis.git
git remote -v
git push origin main
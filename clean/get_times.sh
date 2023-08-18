
find . -maxdepth 2 -name "MEBuilder-*.log" | xargs head -1 > builder_time1.txt
find . -maxdepth 2 -name "MEBuilder-*.log" | xargs tail -n 1 > builder_time2.txt

find . -maxdepth 2 -name "MEReconstruction-*.log" | xargs head -1 > recon_time1.txt
find . -maxdepth 2 -name "MEReconstruction-*.log" | xargs tail -n 1 > recon_time2.txt

find . -maxdepth 2 -name "METroubleshooter-*.log" | xargs head -1 > ts_time1.txt
find . -maxdepth 2 -name "METroubleshooter-*.log" | xargs tail -n 1 > ts_time2.txt
# overall_merit
DMD execises
# dependency
Python 2.7.9
numpy

# preparation
virtualenv --no-site-packages  local_python
source local_python/bin/activate
pip install numpy

#execise1 有杭州,昆明,拉萨三个旅游地供选择,假如选择的标准和依据有:景色,费用,饮食,居住和旅途，哪一个为最佳旅游地点 .
python ex1.py > result1
gvim result1

#execise2 3 某儿童医院2004～2008年7项指标的实际值，比较该医院这5年的医疗质量。
python ex2.py > result2
gvim result2





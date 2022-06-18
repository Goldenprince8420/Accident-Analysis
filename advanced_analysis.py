from scipy.stats import chisquare
from scipy.stats import ttest_ind


class AdvancedAnalyser:
    def __init__(self, data):
        super(AdvancedAnalyser, self).__init__()
        self.frame = data
        self.chi_stat = None
        self.chi_p_values = None
        self.t_stat = None
        self.t_p_values = None

    def do_chi_square(self):
        self.chi_stat, self.chi_p_values = chisquare(self.frame)

    def get_chi_stats(self):
        self.do_chi_square()
        return self.chi_stat, self.chi_p_values

    def do_t_test(self, col_a, col_b):
        a = self.frame[col_a].values
        b = self.frame[col_b].values
        self.t_stat, self.t_p_values = ttest_ind(a, b)

    def get_t_stats(self, col_a, col_b):
        self.do_t_test(col_a, col_b)
        return self.t_stat, self.t_p_values

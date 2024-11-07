import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_dept_score(threat_scores, importance):
    return np.mean(threat_scores) * importance

def calculate_aggregated_score(dept_scores, importance_weights):
    total_weight = sum(importance_weights)
    weighted_scores = [score * weight for score, weight in zip(dept_scores, importance_weights)]
    return sum(weighted_scores) / total_weight

class TestAggregatedThreatScore(unittest.TestCase):

    def test_case_1(self):
        num_dept = 5
        importance = [1, 1, 1, 1, 1]
        user_counts = [20, 20, 20, 20, 20]
        mean = 30
        variance = 10
        threat_scores = [generate_random_data(mean, variance, count) for count in user_counts]
        dept_scores = [calculate_dept_score(scores, imp) for scores, imp in zip(threat_scores, importance)]
        aggregated_score = calculate_aggregated_score(dept_scores, importance)
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

    def test_high_variance(self):
        # Different dept means, high var in scores
        mean_variances = [10, 20, 30, 70, 80]
        variances = [5, 10, 15, 10, 5]
        importance = [1, 1, 1, 1, 1]
        user_counts = [50, 50, 50, 50, 50]
        threat_scores = [generate_random_data(mean, variance, count) for mean, variance, count in zip(mean_variances, variances, user_counts)]
        department_scores = [calculate_dept_score(scores, imp) for scores, imp in zip(threat_scores, importance)]
        aggregated_score = calculate_aggregated_score(department_scores, importance)
        self.assertGreaterEqual(aggregated_score, 0)
        self.assertLessEqual(aggregated_score, 90)

if __name__ == '__main__':
    unittest.main()

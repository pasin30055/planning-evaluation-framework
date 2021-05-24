# Copyright 2021 The Private Cardinality Estimation Framework Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for privacy_tracker.py."""

from absl.testing import absltest

from wfa_planning_evaluation_framework.simulator import privacy_tracker


class PrivacyTrackerTest(absltest.TestCase):
    def test_empty_object(self):
        tracker = privacy_tracker.PrivacyTracker()
        self.assertEqual(tracker.privacy_consumption.epsilon, 0)
        self.assertEqual(tracker.privacy_consumption.delta, 0)
        self.assertEqual(tracker.mechanisms, [])

    def test_single_event(self):
        tracker = privacy_tracker.PrivacyTracker()
        tracker.append(
            privacy_tracker.NoisingEvent(
                privacy_tracker.PrivacyBudget(0.1, 0.01),
                privacy_tracker.DP_NOISE_MECHANISM_LAPLACE,
                {"sensitivity": 1},
            )
        )
        self.assertEqual(tracker.privacy_consumption.epsilon, 0.1)
        self.assertEqual(tracker.privacy_consumption.delta, 0.01)
        self.assertEqual(
            tracker.mechanisms, [privacy_tracker.DP_NOISE_MECHANISM_LAPLACE]
        )

    def test_two_events(self):
        tracker = privacy_tracker.PrivacyTracker()
        tracker.append(
            privacy_tracker.NoisingEvent(
                privacy_tracker.PrivacyBudget(0.1, 0.01),
                privacy_tracker.DP_NOISE_MECHANISM_LAPLACE,
                {"sensitivity": 1},
            )
        )
        tracker.append(
            privacy_tracker.NoisingEvent(
                privacy_tracker.PrivacyBudget(0.2, 0.015),
                privacy_tracker.DP_NOISE_MECHANISM_GAUSSIAN,
                {},
            )
        )
        self.assertAlmostEqual(tracker.privacy_consumption.epsilon, 0.3)
        self.assertAlmostEqual(tracker.privacy_consumption.delta, 0.025)
        self.assertEqual(
            tracker.mechanisms,
            [
                privacy_tracker.DP_NOISE_MECHANISM_LAPLACE,
                privacy_tracker.DP_NOISE_MECHANISM_GAUSSIAN,
            ],
        )


if __name__ == "__main__":
    absltest.main()

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
"""Associate random pricing information to impression data."""

from typing import List
from typing import Tuple


class PricingGenerator:
    """Associates random pricing information to impression data.

    This class, along with ImpressionGenerator, assists in the generation of
    random PublisherDataFiles.  The PricingGenerator will associate random
    prices to the impressions generated by the ImpressionGenerator.
    """

    def __init__(self):
        """Constructor for the PricingGenerator.

        This would typically be overridden with a method whose signature
        would specify the various parameters of the pricing distribution
        to be generated.
        """
        pass

    def __call__(self, impressions: List[int]) -> List[Tuple[int, float]]:
        """Generate a random sequence of prices.

        Args:
          impressions:  A list of user id's, with multiplicities, to which
            pricing data is to be associated.
        Returns:
          A list of pairs (user_id, total_spend).  The length of the list would
          be the same as the list of impressions, and user_id's would be in 1-1
          correspondences with those in the list of impressions.  Associated to
          each user_id is the total spend amount at which the impression would be
          included in those shown by the advertiser.
        """
        pass

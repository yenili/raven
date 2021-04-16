# Copyright 2017 Battelle Energy Alliance, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
  The Models module for building, running, and simulating things in RAVEN.

  Created on May 9, 2017
  @author: maljdp
"""
from .PostProcessorInterface import PostProcessorInterface
from .FTImporter import FTImporter
from .BasicStatistics import BasicStatistics
from .LimitSurface import LimitSurface
from .Metric import Metric
from .ETImporter import ETImporter
from .DataMining import DataMining
from .SafestPoint import SafestPoint
from .ValueDuration import ValueDuration
from .SampleSelector import SampleSelector
from .ImportanceRank import ImportanceRank
from .CrossValidation import CrossValidation
from .LimitSurfaceIntegral import LimitSurfaceIntegral
from .FastFourierTransform import FastFourierTransform
from .ExternalPostProcessor import ExternalPostProcessor
from .InterfacedPostProcessor import InterfacedPostProcessor
from .TopologicalDecomposition import TopologicalDecomposition
from .DataClassifier import DataClassifier
from .ComparisonStatisticsModule import ComparisonStatistics
from .RealizationAverager import RealizationAverager
from .ParetoFrontierPostProcessor import ParetoFrontier
from .MCSimporter import MCSImporter
from .EconomicRatio import EconomicRatio
from .RiskMeasuresDiscrete import RiskMeasuresDiscrete
## These utilize the optional prequisite library PySide, so don't error if they
## do not import appropriately.
additionalModules = []
try:
  from .TopologicalDecomposition import QTopologicalDecomposition
  from .DataMining import QDataMining
  additionalModules.append(QTopologicalDecomposition)
  additionalModules.append(QDataMining)
except ImportError:
  pass
## [ Add new class here ]

from .Factory import factory

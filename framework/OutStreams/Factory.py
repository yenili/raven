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
  Created on April 1, 2021

  @author: talbpaul
  historically designed and architected by @alfoa
"""

from EntityFactoryBase import EntityFactory

# Entities
from .OutStreamEntity import OutStreamEntity
from .PlotEntity import Plot
from .PrintEntity import Print

factory = EntityFactory('OutStreams')
factory.registerType('Print', Print)
factory.registerType('Plot', Plot)

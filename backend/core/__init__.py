# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from utils import CustomJSONEncoder

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# Import Blueprints
from .blueprints.retailers import retailers
from .blueprints.coop_configurations import coop_configurations
from .blueprints.logs import logs
from .blueprints.scheduler import scheduler

app.register_blueprint(retailers)
app.register_blueprint(coop_configurations)
app.register_blueprint(logs)
app.register_blueprint(scheduler)
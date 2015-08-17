from .common import *

from .dockerenv import *

INSTALLED_APPS += ["taiga_contrib_gogs","taiga_contrib_letschat"]
PROJECT_MODULES_CONFIGURATORS["gogs"] = "taiga_contrib_gogs.services.get_or_generate_config"

# THROTTLING
#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec"
#}

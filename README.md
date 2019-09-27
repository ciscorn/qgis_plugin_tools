## QGIS Plugin core tools

### How to use it

The module is helping you with:
* fetching resources in `resources` folder
* fetching compiled UI file in `resources/ui` folder
* fetching compiled translation file in `resources/i18n` folder
* translate using the `i18n.tr` function.

To use the logging system:
```python
import logging
from .qgis_plugin_tools.resources import plugin_name

# Top of the file
LOGGER = logging.getLogger(plugin_name())

# Later in the code
LOGGER.error('Log an error here')
LOGGER.warning('Log a warning here')
LOGGER.critical('Log a critical error here')
LOGGER.info('Log some info here')
```

Use the Makefile in your plugin root folder:

```bash
make i18n_help
make i18n_1_prepare
make i18n_2_push
make i18n_3_pull
make i18n_4_compile

make deploy_help
make deploy_zip
make deploy_upload
```

### How to install it in an existing plugin

* Go to the root folder of your plugin
* `git submodule add git@github.com:3liz/qgis_plugin_tools.git`
* `pip3 install -r requirements_dev.txt`
* Update the makefile to use `git-archive-all`

For setting up the logging:
```python
from .qgis_plugin_tools.resources import plugin_name
from .qgis_plugin_tools.custom_logging import setup_logger

setup_logger(plugin_name())
```

Setting the Makefile:
* Copy the Makefile.parent content to your plugin's Makefile.

## Plugin tree example

Plugin `Foo` root folder:
* `qgis_plugins_tools/` submodule
* `resources/`
  * `i18n/`
  * `ui/`
* `test/`
* `.gitattributes`
* `.gitmodules`
* `.gitignore`
* `__init__.py`
* `foo.py`
* `Makefile`
* `metadata.txt`

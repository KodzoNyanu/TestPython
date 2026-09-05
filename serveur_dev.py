import os
import importlib.util, sys

spec = importlib.util.spec_from_file_location("app_mentions", os.path.join(os.path.dirname(__file__), "test.py"))
m = importlib.util.module_from_spec(spec); sys.modules["app_mentions"] = m; spec.loader.exec_module(m)
m.app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=False)

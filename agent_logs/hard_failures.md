## ❌ Error at 2025-06-21 08:34:19 UTC
**Context:** Unhandled exception during agent run

**Error Message:**
```
[Errno 2] No such file or directory: 'tasks/logi.yaml'

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 13, in run_agent
    login_tasks = load_task_list_from_yaml("tasks/logi.yaml")
  File "/Users/apple/browser-use/agents/loaders.py", line 4, in load_task_list_from_yaml
    with open(path, "r", encoding="utf-8") as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'tasks/logi.yaml'

```

## ❌ Error at 2025-06-21 08:40:30 UTC
**Context:** Unhandled exception during agent run

**Error Message:**
```
'list' object has no attribute 'get'

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 15, in run_agent
    login_tasks = login_data.get("tests", [])
                  ^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get'

```

## ❌ Error at 2025-06-21 08:42:51 UTC
**Context:** Unhandled exception during agent run

**Error Message:**
```
YAML files must contain a 'tests' key with a list of steps.

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 20, in run_agent
    raise ValueError("YAML files must contain a 'tests' key with a list of steps.")
ValueError: YAML files must contain a 'tests' key with a list of steps.

```

## ❌ Error at 2025-06-21 08:45:36 UTC
**Context:** Unhandled exception during agent run

**Error Message:**
```
YAML files must contain a 'tests' key with a list of steps.

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 20, in run_agent
    raise ValueError("YAML files must contain a 'tests' key with a list of steps.")
ValueError: YAML files must contain a 'tests' key with a list of steps.

```

## ❌ Error at 2025-06-24 11:20:16 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
[Errno 2] No such file or directory: 'tasks/logi.yaml'

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 12, in run_agent
    login_data = load_task_list_from_yaml("tasks/logi.yaml")
  File "/Users/apple/browser-use/agents/loaders.py", line 4, in load_task_list_from_yaml
    with open(path, "r", encoding="utf-8") as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'tasks/logi.yaml'

```

## ❌ Error at 2025-06-26 09:43:44 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
[Errno 2] No such file or directory: 'tasks/logi.yaml'

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 11, in run_agent
    login_data = load_task_list_from_yaml("tasks/logi.yaml")
  File "/Users/apple/browser-use/agents/loaders.py", line 4, in load_task_list_from_yaml
    with open(path, "r", encoding="utf-8") as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'tasks/logi.yaml'

```

## ❌ Error at 2025-06-26 09:45:05 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
login.yaml must contain a 'tests' key with a list of steps.

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/login_agent.py", line 15, in run_agent
    raise ValueError("login.yaml must contain a 'tests' key with a list of steps.")
ValueError: login.yaml must contain a 'tests' key with a list of steps.

```

## ❌ Error at 2025-07-30 12:32:21 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
auto_routes.yaml must contain a 'tests' key with a list of steps.

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/auto_routes.py", line 17, in run_agent
    raise ValueError("auto_routes.yaml must contain a 'tests' key with a list of steps.")
ValueError: auto_routes.yaml must contain a 'tests' key with a list of steps.

```

## ❌ Error at 2025-07-30 12:33:33 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
auto_routes.yaml must contain a 'tests' key with a list of steps.

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/auto_routes.py", line 17, in run_agent
    raise ValueError("auto_routes.yaml must contain a 'tests' key with a list of steps.")
ValueError: auto_routes.yaml must contain a 'tests' key with a list of steps.

```

## ❌ Error at 2025-07-30 12:35:12 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
auto_routes.yaml must contain a 'tests' key with a list of steps.

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/auto_routes.py", line 17, in run_agent
    raise ValueError("auto_routes.yaml must contain a 'tests' key with a list of steps.")
ValueError: auto_routes.yaml must contain a 'tests' key with a list of steps.

```

## ❌ Error at 2025-07-30 13:09:00 UTC
**Context:** 💥 Unhandled exception during agent run

**Error Message:**
```
mapping values are not allowed here
  in "tasks/PSM/auto_routes.yaml", line 39, column 23

Traceback:
Traceback (most recent call last):
  File "/Users/apple/browser-use/agents/auto_routes.py", line 14, in run_agent
    auto_routes = load_task_list_from_yaml("tasks/PSM/auto_routes.yaml")
  File "/Users/apple/browser-use/helpers/loaders.py", line 5, in load_task_list_from_yaml
    data = yaml.safe_load(f)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 111, in compose_sequence_node
    node.value.append(self.compose_node(node, index))
                      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/composer.py", line 127, in compose_mapping_node
    while not self.check_event(MappingEndEvent):
              ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/parser.py", line 98, in check_event
    self.current_event = self.state()
                         ~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/parser.py", line 428, in parse_block_mapping_key
    if self.check_token(KeyToken):
       ~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/scanner.py", line 116, in check_token
    self.fetch_more_tokens()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/scanner.py", line 223, in fetch_more_tokens
    return self.fetch_value()
           ~~~~~~~~~~~~~~~~^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/yaml/scanner.py", line 577, in fetch_value
    raise ScannerError(None, None,
            "mapping values are not allowed here",
            self.get_mark())
yaml.scanner.ScannerError: mapping values are not allowed here
  in "tasks/PSM/auto_routes.yaml", line 39, column 23

```

